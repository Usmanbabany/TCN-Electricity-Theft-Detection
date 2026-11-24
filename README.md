# Temporal Convolutional Networks for Electricity Theft Detection With Limited Data

**Researcher and paper author:** Usman Haruna  
**Research area:** Computer Science, temporal deep learning and electricity-theft detection

## Overview

This repository accompanies the IEEE INDIACom 2025 paper *Temporal Convolutional Networks for Electricity Theft Detection with Limited Data*. It presents the research methodology, reported findings and implementation code for applying Temporal Convolutional Networks (TCNs) to electricity-theft detection under limited-data conditions.

## Methodology

The research workflow described in the paper includes:

1. Electricity-consumption data preparation and preprocessing.
2. Gaussian-noise augmentation.
3. SMOTE for class-imbalance handling.
4. Temporal Convolutional Network modelling.
5. Stratified 10-fold cross-validation.
6. Grid Search for hyperparameter tuning.
7. Evaluation using accuracy, precision, recall, F1-score and ROC-AUC.

The reported best settings include 64 convolutional filters, kernel size 3, dropout rate 0.2 and Adam learning rate 0.001.

## Results reported in the IEEE paper

| Metric | Without SMOTE | With SMOTE |
|---|---:|---:|
| Accuracy | 89% | 97% |
| Precision | 88% | 96% |
| Recall | 91% | 97% |
| F1-score | 89% | 97% |
| ROC-AUC | 0.92 | 0.98 |

The paper also reports 96% accuracy and F1-score without Gaussian-noise augmentation, compared with 97% for both metrics with augmentation. These are the results reported in the published research. See [Reported Results](docs/REPORTED_RESULTS.md).

## Dataset

The research dataset was obtained from Kaggle. The dataset is not included in this repository; users should obtain it from its source and follow the applicable usage terms.

## Implementation

The src/train_tcn.py script provides the repository's training implementation. It accepts a CSV dataset containing a binary FLAG target, a customer identifier (CONS_NO) and ordered consumption measurements. See the script for usage and configuration details.

## Repository structure

- src/ — TCN training implementation.
- docs/ — IEEE paper specification and Reported Result.
- publications/ — publication information.
- future_research/ — potential future research directions.
- documentation/ — data privacy, methodology, reproducibility and status, research background and TCN architecture.

## Publication

*Temporal Convolutional Networks for Electricity Theft Detection with Limited Data.* 19th INDIACom / 12th International Conference on Computing for Sustainable Global Development, IEEE, 2025.

## Research interests

- Temporal deep learning
- Data-efficient machine learning
- Electricity theft and non-technical loss detection
- Smart-grid analytics
- Anomaly detection

---

This repository is an accompanying research and implementation resource for the published study. Please cite the IEEE paper when referring to the research.
