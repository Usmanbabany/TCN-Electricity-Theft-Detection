# Methodology

This document describes the intended workflow. Mark individual steps as completed only after their code, execution, and outputs have been checked.

## Core workflow
1. **Dataset inspection:** identify the target label, customer identifier, time columns, consumption variables, missing values, and class distribution.
2. **Preprocessing:** clean invalid values and prepare a consistent temporal representation.
3. **Data partitioning:** split observations to prevent information leakage between training and evaluation data.
4. **Scaling:** fit transformations on training data only, then apply them to validation and test data.
5. **Sequence construction:** form time-ordered windows and align each window with its correct target.
6. **Model definition:** specify the TCN architecture, input dimensions, optimizer, loss, and regularization.
7. **Training:** train on training data and use validation data for model selection.
8. **Evaluation:** report metrics on a held-out test set not used for model selection.

## Techniques requiring verification
Draft research notebooks have considered Gaussian-noise augmentation, SMOTE, K-fold validation, and hyperparameter search. Include these in the final experimental description only when their implementation and results are reproducible.

For each technique, record its purpose, pipeline position, data used, parameters, random seed, evaluation protocol, and resulting metrics.

## Leakage and validation safeguards
- Do not fit a scaler on the complete dataset before splitting.
- Avoid random splitting of heavily overlapping temporal windows if near-duplicate records can enter both training and test sets.
- Keep records from the same customer in one partition when customer-independent evaluation is required.
- Do not apply oversampling to validation or test data.
- Reinitialize model weights for each cross-validation fold.
- Preserve the chronological ordering required by temporal inputs.
- Verify the alignment between each input window and its target label.

## Metrics
For binary classification, report the confusion matrix and class-wise precision, recall, and F1-score. Accuracy and ROC-AUC may also be useful, especially when interpreted alongside class-wise results.

## Reproducibility record
Record dataset provenance, feature list, label definition, split strategy, random seed, model configuration, training settings, software versions, and test metrics for every final experiment.
