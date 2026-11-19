# Results from the Original Research

## Published comparison

The IEEE paper reports the following comparison between an imbalanced dataset without SMOTE and a balanced dataset using SMOTE.

| Metric | Imbalanced (without SMOTE) | Balanced (with SMOTE) |
|---|---:|---:|
| Accuracy | 89% | 97% |
| Precision | 88% | 96% |
| Recall | 91% | 97% |
| F1-score | 89% | 97% |
| ROC-AUC | 0.92 | 0.98 |

The paper also reports a separate noise-augmentation comparison:
- Without noise augmentation: 96% accuracy and 96% F1-score.
- With noise augmentation: 97% accuracy and 97% F1-score.

## Interpretation limited to the paper's claims

The publication reports improved classification metrics after SMOTE balancing and a one-percentage-point increase in accuracy and F1-score with noise augmentation.

## Research provenance and GitHub status

The author confirms that the reported values were obtained through the original research experiments and were reported in the IEEE paper.

The complete original experiment has not yet been recovered, cleaned, packaged and rerun end-to-end from this repository. The current `src/train_tcn.py` script is a separate baseline and did not generate the paper's result table.

The saved notebook copies currently available for review include working-stage code and execution issues, and do not all contain a complete successful run that can be directly matched to the paper's result tables. This is a limitation of the available saved copies and repository packaging; it does not imply that the author did not conduct the experiments reported in the paper.

## Interpreting future retraining results

A rerun may produce metrics that differ from those in the paper. This can happen when the input dataset, preprocessing, split, random seed, TCN initialization, noise augmentation, SMOTE sampling, software versions or execution environment differ.

The published values in this document are historical results from the IEEE paper. They must remain separate from any future rerun. New results should be recorded with their own dataset description, configuration, run date, fold-level metrics and saved outputs. A rerun must not overwrite or silently replace the published table.

See [the retraining protocol](RETRAINING_PROTOCOL.md) for the notebook audit, current data limitation and planned validation procedure.
