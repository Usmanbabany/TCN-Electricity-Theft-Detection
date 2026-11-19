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

## Research provenance and GitHub reproduction status

The author confirms that the reported values were obtained through the original research experiments and were reported in the IEEE paper. The author has also supplied the Colab notebooks used during the research for review and repository preparation.

**GitHub status: The complete original experiment has not yet been cleaned, packaged and rerun end-to-end from this repository.** The current `src/train_tcn.py` script is a separate baseline and did not generate the paper's result table.

The saved notebook copies currently available for review include working-stage code and execution issues, and do not all contain a complete successful run that can be directly matched to the paper's result tables. They are being reconciled with the final experiment record before being released as a reproducible package. This is a limitation of the currently saved copies and repository packaging; it does not imply that the author did not conduct the experiments reported in the paper.

## Figure and metric consistency

The paper's results text states ROC-AUC values of 0.92 (imbalanced) and 0.98 (balanced). Any future analysis or reproduction should compare the ROC plot with these values using original plotting data or saved experiment outputs. No synthetic ROC curve or performance plot should be created to imitate the reported values.
