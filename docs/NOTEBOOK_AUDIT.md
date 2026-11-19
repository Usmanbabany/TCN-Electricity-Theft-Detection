# Audit of Author-Provided TCN Notebooks

## Purpose

This document records a technical review of the Colab notebooks supplied by the paper's author, Usman Haruna. The review is intended to identify which saved notebook copy can serve as the starting point for a clean experimental rerun.

The review does not question the author's account that the IEEE paper's reported results came from the original research. It assesses only the saved notebook copies and execution outputs currently available for repository preparation.

## Summary

**No saved notebook reviewed here provides a complete, internally consistent execution that independently verifies the paper's reported 97% result.** The original paper result should therefore remain recorded as a published research result, while any new training run should be recorded separately as a fresh evaluation.

## Notebook-by-notebook findings

### 1. `TCN.ipynb`, `TCN(1).ipynb` and `TCN(2).ipynb`

The three saved files are byte-identical copies of the same notebook (SHA-256: `fa2acc608aaa7499fed9121f0d8a7075152edeb3f61edbcfc4a215fea69589c3`). They are not three independent experiment runs.

The notebook includes a TensorFlow/Keras TCN with:
- Four causal Conv1D layers.
- 64 filters per layer.
- Kernel size 3.
- Dilation rates 1, 2, 4 and 8.
- A Flatten layer and sigmoid output.
- 20 training epochs and batch size 16 in the displayed training cell.

Important issues in the saved copy:
- The data-loading cell assigns the dataset to `data_cleaned` but subsequently prints `data.info()`, referring to another variable.
- The cleaning cells alternate between `data_cleaned` and `data`, so the saved notebook's execution state is not consistently traceable.
- Missing consumption values are forward-filled down the table. In a customer-by-date matrix, this can carry one customer's values into another customer's row.
- The scaler is fitted before the train/test split. This leaks information from the test partition into preprocessing.
- The saved scaler output includes invalid-value warnings, and the training log shows `loss: nan` and `val_loss: nan`.
- The saved evaluation reports only one class and a confusion matrix of `[[28]]`. The displayed 100% accuracy is therefore not a valid two-class performance assessment.
- A separate KFold cell uses two folds rather than the paper's stated stratified 10-fold validation. The fold loop also evaluates the same held-out test set repeatedly and is not a clean nested evaluation procedure.
- The custom Conv1D model shown in the notebook does not include the 0.2 dropout listed in the paper's reported best hyperparameters.

**Assessment:** This is useful as a development-history artifact and for recovering the intended convolutional structure, but its saved metrics must not be reused as valid experimental results.

### 2. `TCNK-FOLDS-MOTE.ipynb`

This notebook is the closest saved attempt at combining TCN and SMOTE, but it is incomplete.

Findings:
- It sets up `StratifiedKFold(n_splits=5)`, whereas the paper reports stratified 10-fold validation.
- It imports `KFold` but calls `StratifiedKFold`, so the shown cell is missing the required import.
- It initially includes all columns except `FLAG`, which may include the customer identifier `CONS_NO`; the identifier must not be treated as a consumption feature.
- It applies SMOTE to flattened rows, then reshapes the result for the TCN.
- The saved code reaches model definition/summary but does not show a completed model-fit and fold-level evaluation sequence.
- The saved output includes an execution error.

**Assessment:** It is the closest methodological draft for SMOTE plus TCN, but it is not a complete trained experiment and does not establish the published metrics.

### 3. `tcn2.ipynb`

This is an incomplete prototype. It mixes PyTorch imports with TensorFlow/Keras modelling code, has no saved execution outputs, and its sequence-building approach slides across rows. For a wide customer-by-date matrix, that would mix different customers into a sequence unless the data were first restructured appropriately.

**Assessment:** Retain as development history, not as the final research implementation.

## Important data and evaluation corrections for a fresh run

A new run should:
1. Confirm the exact dataset used in the published experiment before training. The notebook files refer to both `Dataset_small.csv` and `Electricity_Theft_Data.csv`; these names must not be assumed to refer to the same file.
2. Treat each customer's chronologically ordered consumption readings as one time series and use `FLAG` as that customer's label.
3. Exclude `CONS_NO` from model features.
4. Drop rows with missing customer identifiers or labels, validate that labels are binary, and inspect missing/constant consumption columns.
5. Fit imputation and scaling only on each training fold, then apply the fitted transformations to that fold's validation data.
6. Apply Gaussian-noise augmentation and SMOTE only to training-fold data. The paper's exact noise parameters and SMOTE configuration must be recovered or explicitly documented as new experimental choices.
7. Use stratified 10-fold validation, as reported in the paper.
8. Record per-fold predictions and metrics, plus the complete confusion matrix and ROC-AUC. Save random seeds, package versions, model configuration and all outputs.
9. Keep any new run separate from the historical results in the IEEE paper. Do not tune or select a model using the final test folds and then report those same folds as unbiased evaluation.

## Status and next step

- **Historical IEEE result:** preserve the metrics reported in the published paper as historical published results.
- **Saved notebook evidence:** the copies reviewed do not independently verify the result table.
- **Fresh rerun:** not yet performed. The exact source dataset is not established from the currently available files.
- **Next step:** identify the original dataset file used for the IEEE experiment, then prepare and run a clean, fold-safe implementation. Record the new metrics as a fresh rerun; do not silently replace the paper's published values.
