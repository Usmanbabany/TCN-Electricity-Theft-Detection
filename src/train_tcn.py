"""Reproducible baseline for TCN electricity-theft classification.

Expected CSV structure:
- FLAG: binary target (0/1)
- CONS_NO: customer identifier (excluded from model features)
- Remaining columns: ordered daily consumption measurements

Set DATASET_PATH to the authorized local dataset. Raw customer data is not
included in this repository.
"""
from __future__ import annotations

import argparse
import json
import os
import random
from pathlib import Path

import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Model
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.layers import Input, Conv1D, Dense, Dropout, GlobalAveragePooling1D
from tensorflow.keras.optimizers import Adam


SEED = 42
TARGET = "FLAG"
IDENTIFIER = "CONS_NO"


def set_seeds(seed: int = SEED) -> None:
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    tf.keras.utils.set_random_seed(seed)


def load_dataset(path: Path) -> tuple[pd.DataFrame, pd.Series]:
    if not path.is_file():
        raise FileNotFoundError(
            f"Dataset not found: {path}. Supply an authorized local CSV file."
        )

    frame = pd.read_csv(path)
    if TARGET not in frame.columns:
        raise ValueError(f"Required target column '{TARGET}' is missing.")

    # Exclude rows without labels; do not forward-fill labels or identifiers.
    frame = frame.loc[frame[TARGET].notna()].copy()
    y_numeric = pd.to_numeric(frame[TARGET], errors="coerce")
    valid = y_numeric.notna()
    frame = frame.loc[valid].copy()
    y_numeric = y_numeric.loc[valid]

    labels = set(y_numeric.unique().tolist())
    if not labels.issubset({0, 1}):
        raise ValueError(
            f"Expected binary FLAG values 0 and 1; found {sorted(labels)}."
        )
    y = y_numeric.astype("int32")

    excluded = [TARGET]
    if IDENTIFIER in frame.columns:
        excluded.append(IDENTIFIER)
    X = frame.drop(columns=excluded).apply(pd.to_numeric, errors="coerce")

    # Remove columns that contain no usable numeric observations.
    X = X.dropna(axis=1, how="all")
    if X.shape[1] < 1:
        raise ValueError("No numeric consumption feature columns were found.")

    # Preserve the CSV column order: it represents the temporal sequence.
    if y.nunique() != 2:
        raise ValueError(
            f"Both target classes are required; found {y.value_counts().to_dict()}."
        )
    if y.value_counts().min() < 2:
        raise ValueError("Each class needs at least two records for stratified splitting.")

    return X, y


def build_model(input_shape: tuple[int, int]) -> Model:
    inputs = Input(shape=input_shape, name="daily_consumption_sequence")
    x = inputs
    for dilation in (1, 2, 4, 8):
        x = Conv1D(
            filters=64,
            kernel_size=3,
            padding="causal",
            dilation_rate=dilation,
            activation="relu",
            name=f"causal_conv_d{dilation}",
        )(x)
        x = Dropout(0.2, name=f"dropout_d{dilation}")(x)

    x = GlobalAveragePooling1D()(x)
    x = Dense(32, activation="relu")(x)
    outputs = Dense(1, activation="sigmoid", name="theft_probability")(x)

    model = Model(inputs, outputs, name="electricity_theft_tcn")
    model.compile(
        optimizer=Adam(learning_rate=1e-3),
        loss="binary_crossentropy",
        metrics=[
            tf.keras.metrics.BinaryAccuracy(name="accuracy"),
            tf.keras.metrics.Precision(name="precision"),
            tf.keras.metrics.Recall(name="recall"),
            tf.keras.metrics.AUC(name="auc"),
        ],
    )
    return model


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to authorized CSV dataset")
    parser.add_argument("--output", default="outputs/baseline", help="Output directory")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch-size", type=int, default=32)
    args = parser.parse_args()

    set_seeds()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    X, y = load_dataset(Path(args.data))
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=SEED, stratify=y
    )

    # Fit imputing and scaling transformations on training data only.
    imputer = SimpleImputer(strategy="median")
    scaler = StandardScaler()
    X_train = scaler.fit_transform(imputer.fit_transform(X_train))
    X_test = scaler.transform(imputer.transform(X_test))

    # Each customer record is treated as one sequence over ordered daily columns.
    X_train = X_train.astype("float32")[..., np.newaxis]
    X_test = X_test.astype("float32")[..., np.newaxis]

    if not np.isfinite(X_train).all() or not np.isfinite(X_test).all():
        raise ValueError("Non-finite values remain after preprocessing.")

    model = build_model((X_train.shape[1], X_train.shape[2]))
    callbacks = [
        EarlyStopping(monitor="val_loss", patience=7, restore_best_weights=True),
        ReduceLROnPlateau(monitor="val_loss", patience=3, factor=0.5, min_lr=1e-6),
    ]

    history = model.fit(
        X_train,
        y_train.to_numpy(),
        validation_split=0.20,
        epochs=args.epochs,
        batch_size=args.batch_size,
        callbacks=callbacks,
        verbose=1,
    )

    probabilities = model.predict(X_test, verbose=0).ravel()
    predictions = (probabilities >= 0.5).astype("int32")
    cm = confusion_matrix(y_test, predictions, labels=[0, 1])
    report = classification_report(
        y_test, predictions, labels=[0, 1], output_dict=True, zero_division=0
    )

    metrics = {
        "test_accuracy": float(accuracy_score(y_test, predictions)),
        "confusion_matrix_labels_0_1": cm.tolist(),
        "classification_report": report,
        "test_roc_auc": (
            float(roc_auc_score(y_test, probabilities))
            if y_test.nunique() == 2
            else None
        ),
        "training_rows": int(len(y_train)),
        "test_rows": int(len(y_test)),
        "feature_count": int(X_train.shape[1]),
        "sequence_length": int(X_train.shape[1]),
        "seed": SEED,
        "threshold": 0.5,
    }

    model.save(output_dir / "tcn_baseline.keras")
    with (output_dir / "metrics.json").open("w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)
    pd.DataFrame(history.history).to_csv(output_dir / "training_history.csv", index=False)

    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
