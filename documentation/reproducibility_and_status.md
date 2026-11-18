# Implementation Status and Reproducibility

## Current status
This repository is being organized as a research record. Draft notebooks have been reviewed for completeness and reproducibility. Some notebook cells require correction or further execution before they can support final performance claims.

## Items to verify
- Confirm the meaning of each dataset column, especially customer identifiers versus consumption features.
- Ensure demonstration or toy-data cells do not overwrite the research dataset.
- Confirm date parsing and chronological ordering.
- Fit preprocessing transformations on training data only.
- Confirm sequence-to-label alignment.
- Use a leakage-aware train/validation/test or cross-validation design.
- Create a fresh model for each cross-validation fold.
- Ensure training produces finite loss values.
- Generate a confusion matrix for a valid held-out evaluation containing the relevant classes.
- Save metrics and plots from the final held-out evaluation.

## Reporting rule
Do not report a performance figure as validated unless it can be traced to a specific notebook or script, dataset split, model configuration, and saved evaluation output. Previously discussed figures remain provisional until this evidence is available.

## Experiment record template
| Field | Record |
|---|---|
| Experiment ID | |
| Dataset provenance/version | |
| Target label definition | |
| Input feature list | |
| Sequence/window length | |
| Split strategy | |
| Random seed | |
| Preprocessing | |
| Model configuration | |
| Training settings | |
| Validation method | |
| Test accuracy | |
| Precision / recall / F1 | |
| ROC-AUC (if used) | |
| Confusion matrix | |
| Notebook or script | |
