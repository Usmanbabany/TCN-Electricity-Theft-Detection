# Notebook Audit and Retraining Protocol

## 1. Purpose

This document records the review of the author-provided development notebooks and defines a safe process for preparing a future rerun of the IEEE research.

The published IEEE results remain the historical results of the author's original research. A new run is a separate computational rerun and may produce different values. It must not be used to silently overwrite the published results.

## 2. Notebook files reviewed

The following saved notebook copies were reviewed:

- `TCNK-FOLDS-MOTE.ipynb`
- `TCN (1).ipynb`
- `TCN.ipynb`, `TCN(1).ipynb` and `TCN(2).ipynb`
- `tcn2.ipynb`
- The PyTorch TCN code pasted by the author during repository preparation

The files `TCN.ipynb`, `TCN(1).ipynb`, `TCN(2).ipynb` and `TCN (1).ipynb` are byte-identical copies in the currently available file set.

## 3. Findings by notebook

### 3.1 TCNK-FOLDS-MOTE.ipynb

This notebook is the closest saved copy to the paper's class-balancing and cross-validation workflow. It contains code for SMOTE, a TCN layer and stratified fold splitting.

However, the saved code has important gaps:

- It sets `n_splits=5`, whereas the published methodology specifies stratified 10-fold cross-validation.
- It imports `KFold` but uses `StratifiedKFold` without importing it.
- It creates `X` by dropping only `FLAG`, leaving `CONS_NO` among the model inputs. Customer identifiers should not be treated as consumption measurements.
- It applies forward filling before the folds are created, rather than documenting a fold-safe preprocessing procedure.
- The saved cell performs SMOTE on a flattened training-fold matrix and reshapes the data, but does not complete the model training, fold evaluation and aggregation procedure.
- The saved execution output records an `AttributeError: 'tuple' object has no attribute 'as_list'` during the TCN/model setup path.
- The saved code does not implement the paper's Gaussian-noise augmentation or Grid Search procedure.

**Assessment:** useful evidence of a development stage, but not a complete executable record of the published experiment.

### 3.2 TCN (1).ipynb and identical copies

The notebook output shows a dataset with 9,957 rows and 367 columns, including `CONS_NO`, `FLAG` and 365 consumption-date columns.

Issues in the saved version include:

- `StandardScaler` is fitted before the train/test split, which allows information from the test set to influence preprocessing.
- The scaler emits invalid-value warnings.
- The K-fold section uses two folds and ordinary `KFold`, not stratified 10-fold.
- The fold-training cell refers to `X_train_reshaped` before that variable is defined in the notebook's saved cell order.
- The saved training output records `NaN` loss throughout the displayed epochs.
- The saved classification report contains only one class with support of 28, and the confusion matrix is `[[28]]`. That is not a valid two-class evaluation of electricity theft detection.
- The saved workflow does not show completed SMOTE, Gaussian-noise augmentation or Grid Search stages.

The model-construction cell uses causal Conv1D layers with 64 filters, kernel size 3 and dilation rates 1, 2, 4 and 8. These are code settings in this notebook version; they do not by themselves establish that this exact version generated the published result table.

**Assessment:** a useful development artifact, but its saved execution outputs cannot be used as evidence of the final reported performance.

### 3.3 tcn2.ipynb

The saved prototype mixes PyTorch imports with TensorFlow/Keras model construction. It also uses `CONS_NO` as the numeric signal for sequence construction, rather than building each customer's sequence from the daily consumption columns.

Additional issues:

- The sequence construction slides over customer rows, so a sequence can combine different customers.
- The label selection is not aligned clearly to the constructed sequences.
- A later plotting cell replaces the `data` variable with a small illustrative dictionary, overwriting the previously loaded dataset variable.
- No completed training/evaluation output is saved in this notebook copy.

**Assessment:** an early prototype, not a valid record of the published experiment.

### 3.4 PyTorch code pasted during repository preparation

The pasted code imports `keras-tcn` and attempts to use its TCN class as a PyTorch `nn.Module`. Keras layers and PyTorch modules are not interchangeable.

The sequence helper also slides across rows of the customer table, rather than treating each customer's chronological consumption readings as one sequence. This would mix records from different customers. The snippet does not implement the paper's full 10-fold, Gaussian-noise, SMOTE and Grid Search workflow.

**Assessment:** development code requiring correction; it must not be described as the final published implementation.

## 4. Dataset availability and audit

The author has now supplied a file named `Dataset_small.csv`, matching the filename referenced in the pasted development code. Its contents are summarized in [DATASET_AUDIT.md](DATASET_AUDIT.md).

The uploaded file has 141 raw rows and 30 columns. One first row has no customer ID or target label and contains the sequence 1 through 28 in the consumption cells. Excluding that malformed row leaves 140 labelled customers and 28 daily consumption columns (1–28 January 2015).

All 140 valid customer records have `FLAG=1`; there are no `FLAG=0` records. The consumption matrix also has 1,275 missing readings out of 3,920 (32.53%), with 48 customers having at least one missing reading and one observed value of -0.01.

This file cannot support supervised binary theft-versus-normal training by itself. SMOTE cannot create a missing original class, and two-class cross-validation and ROC-AUC cannot be validly evaluated on a one-class dataset. Do not duplicate or relabel samples to force a binary experiment.

The uploaded file's dimensions (140 customers × 28 daily readings after excluding the malformed row) also differ from the saved notebook's reported input (9,957 rows × 365 consumption columns plus identifiers/label). Its relationship to the final IEEE experiment data therefore remains unconfirmed.

The separate `Electricity_Theft_Data.csv` file remains set aside until its dataset provenance is established.

**Current decision: no new supervised model training has been performed.** This is intentional: training a binary classifier on the one-class extract would not be methodologically valid and would not reproduce the published experiment.

## 5. Why a new training run may produce different results

Even with the same broad model design, rerun metrics may change due to:

- A different dataset or different records/labels.
- Different missing-value handling, feature selection or normalization.
- A different train/test partition or cross-validation folds.
- Random weight initialization and batch shuffling.
- Gaussian-noise samples and SMOTE-generated observations.
- Different software versions, device kernels or floating-point execution.
- Differences between the saved development notebooks and the actual code used in the final original experiment.

A fixed random seed can reduce variation, but it cannot compensate for a different dataset or unknown preprocessing and experiment settings.

## 6. Procedure for a defensible rerun

When the exact research data and any recoverable experiment settings are available, use this procedure:

1. **Confirm provenance.** Record the dataset source, exact file/version, row and column counts, date coverage, label definition and a file checksum. Do not publish customer identifiers or confidential records.
2. **Validate the schema.** Confirm the customer ID, target label and chronological consumption columns. Exclude identifiers from numeric model inputs.
3. **Preserve customer-level temporal structure.** Build each sample from the ordered consumption measurements belonging to one customer. Do not slide a sequence across different customers.
4. **Prevent data leakage.** Split by the intended evaluation protocol first. Fit imputers and scalers only on each training fold, then apply the fitted transformations to its validation fold.
5. **Apply augmentation only to training data.** Gaussian noise and SMOTE must not use validation/test observations. Confirm the original noise parameters and SMOTE settings rather than inventing them.
6. **Implement the TCN consistently.** Use one framework throughout and document the exact architecture, input shape, optimizer and learning rate.
7. **Match the paper's evaluation protocol.** The paper reports stratified 10-fold cross-validation and Grid Search. Recover the actual search space and scoring procedure before claiming an exact reproduction.
8. **Save all evidence.** Store configuration, random seeds, per-fold scores, aggregate metrics, confusion matrices, ROC-AUC values, training history and software versions for each run.
9. **Separate results.** Keep the paper's published table unchanged. Record new numbers in a separately dated rerun report with the dataset and configuration used.

## 7. Settings that must not be guessed

The following details are not sufficiently established by the currently available saved notebooks and paper documentation:

- The exact dataset version used in the final IEEE experiment.
- The final missing-value treatment and feature/sequence construction.
- Gaussian-noise distribution parameters and where it was applied.
- SMOTE parameters and fold-level application order.
- The exact TCN layer configuration used for the final paper results.
- The Grid Search parameter ranges, scoring rule and selection procedure.
- The final random seeds and software environment.
- The exact final executed notebook and its saved outputs.

Where the original setting cannot be recovered, any new choice must be documented as a rerun design decision, not attributed to the original experiment.

## 8. Current status

- Published-paper results: retained as reported historical results.
- Author-provided notebook copies: reviewed; none of the currently available saved copies establishes the complete final run.
- Uploaded `Dataset_small.csv`: audited; 140 valid rows, all `FLAG=1`, 28 daily readings and 32.53% missing consumption cells; insufficient for supervised binary classification.
- New training run: not performed.
- Current GitHub baseline script: separate from the published experiment.
- Next technical step: obtain or identify the exact data used for the paper and then build a versioned rerun without replacing the published results.
