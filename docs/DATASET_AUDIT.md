# Dataset Audit: Dataset_small.csv

## 1. Scope

This audit describes the file `Dataset_small.csv` uploaded for the TCN electricity-theft research repository on 19 November 2026. The filename matches the path referenced in the author's pasted Colab code. This filename match alone does not prove that this exact file version generated the published IEEE results.

The CSV contains customer identifiers. The raw file is therefore not committed to this public repository. Do not publish customer-level identifiers or confidential consumption records.

## 2. Structural summary

| Check | Observed value |
|---|---:|
| Raw CSV dimensions | 141 rows × 30 columns |
| Rows with a customer ID and FLAG | 140 |
| Unique customer IDs among those rows | 140 |
| Consumption columns | 28 |
| Date coverage represented by headers | 1–28 January 2015 |
| Distinct non-missing FLAG values | 1 |
| FLAG value counts | 140 records labelled 1 |

The first CSV data row has missing `CONS_NO` and `FLAG`, while its 28 consumption cells contain the sequence 1 through 28. It does not look like a valid labelled customer record and was excluded from the customer/label summary. Its origin should be checked against the source export before any permanent cleaning rule is adopted.

The first 12 date headers use slash-separated dates (for example, `1/1/2015`), while the remaining 16 use hyphenated two-digit-year dates (for example, `13-01-15`). They can be interpreted as consecutive dates from 1 January through 28 January 2015, but a cleaning script should parse and sort them explicitly rather than depend on their text format.

## 3. Target-label limitation

Among the 140 rows with a customer ID and a non-missing target:

- `FLAG = 1`: 140 customers
- `FLAG = 0`: 0 customers

**This file contains only one target class. It cannot support supervised binary training or a valid two-class evaluation of electricity-theft detection by itself.**

In particular:

- A classifier cannot learn the distinction between normal and theft-labelled customers from a single class.
- Stratified two-class cross-validation cannot be formed from this file alone.
- SMOTE cannot create a missing original class; it is an oversampling method for an existing minority class.
- Binary ROC-AUC and a two-class confusion matrix cannot be meaningfully computed from a one-class test set.

Do not duplicate, relabel or synthetically invent normal-customer records to force a binary experiment.

## 4. Missing and unusual consumption values

After excluding the row with missing customer ID and target, the 140 × 28 consumption matrix has:

| Check | Observed value |
|---|---:|
| Consumption cells | 3,920 |
| Missing consumption cells | 1,275 |
| Missing proportion | 32.53% |
| Customers with at least one missing reading | 48 |
| Minimum observed value | -0.01 |
| Maximum observed value | 138.19 |
| Negative observed readings | 1 |

A missingness rate of 32.53% is material and requires an explicit treatment plan. The single value of -0.01 should be checked against the source/measurement conventions; it must not be silently clipped or converted without justification.

The earlier exploratory code uses `fillna(0)`. That may conflate missing readings with genuine zero consumption. We should not adopt this treatment automatically. Missingness indicators and fold-safe imputation should be evaluated and documented.

## 5. Difference from a saved notebook's reported input dimensions

One saved notebook copy displays a dataset with 9,957 rows and 367 columns, including `CONS_NO`, `FLAG` and 365 consumption columns. The uploaded `Dataset_small.csv` has 140 labelled customer rows and 28 consumption columns after excluding the malformed first row.

These dimensions differ substantially. The uploaded file may be a small subset or a different development extract, but its relationship to the dataset used in the published experiment has not been established.

## 6. Decision

**No supervised TCN retraining has been performed with this file.** This is a deliberate methodological decision, not a technical failure.

The file is useful for schema inspection and exploratory data-quality analysis. It is not sufficient for the paper's binary electricity-theft classification experiment because it contains only FLAG=1 records and has substantial missing data.

## 7. Requirements before a defensible rerun

1. Locate the corresponding normal-consumption records (`FLAG=0`) from the same dataset source and collection period.
2. Confirm whether this 28-day file is a subset of the original data or a separate extract.
3. Verify the first malformed row and the meaning of the single negative reading.
4. Establish the official date/consumption schema and the meaning of `FLAG`.
5. Document missing-data handling without leaking validation/test information.
6. Keep customer identifiers out of model inputs and public repository files.
7. Preserve the IEEE paper's historical results separately from any new rerun.

Until these requirements are satisfied, this file must not be used to claim reproduction of the paper's reported 97% accuracy or 0.98 ROC-AUC.
