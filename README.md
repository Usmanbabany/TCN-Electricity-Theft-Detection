# Temporal Convolutional Networks for Electricity Theft Detection With Limited Data

**Researcher:** Usman Haruna  
**Research area:** Computer Science, temporal deep learning, electricity-theft detection

## Overview

This repository documents the research presented in the IEEE INDIACom 2025 paper *Temporal Convolutional Networks for Electricity Theft Detection with Limited Data*. The study investigates a Temporal Convolutional Network (TCN) approach for identifying suspicious electricity-consumption patterns under limited, noisy and imbalanced-data conditions.

The repository is organised around the published paper. It distinguishes information reported in the publication from code or experiments that have been independently reproduced.

## Published methodology

The paper describes the following workflow:

1. Electricity-consumption data collection.
2. Preprocessing, including missing-value handling and normalization.
3. Gaussian-noise injection for training-data augmentation.
4. SMOTE to address class imbalance.
5. TCN architecture design and training.
6. Stratified 10-fold cross-validation.
7. Hyperparameter tuning using Grid Search.
8. Evaluation using accuracy, precision, recall, F1-score and ROC-AUC.

The best hyperparameter values reported in the paper are 64 convolutional filters, kernel size 3, dropout rate 0.2 and Adam learning rate 0.001. See [the paper-based research specification](docs/IEEE_PAPER_SPECIFICATION.md).

## Results reported in the paper

| Metric | Imbalanced (without SMOTE) | Balanced (with SMOTE) |
|---|---:|---:|
| Accuracy | 89% | 97% |
| Precision | 88% | 96% |
| Recall | 91% | 97% |
| F1-score | 89% | 97% |
| ROC-AUC | 0.92 | 0.98 |

These are **values reported in the published paper**, not results independently reproduced by the current repository code. See [reported results and validation notes](docs/REPORTED_RESULTS.md).

## Repository structure

- `src/` — implementation code under development.
- `docs/` — paper-based methodology, results and documentation.
- `docs/figures/` — figure inventory and planned figure assets.
- `publications/` — publication information.
- `future_research/` — possible extensions beyond the published study.

## Data and reproducibility

The original research dataset is not included. Do not commit confidential, licensed or identifiable customer-level electricity data. The paper does not provide enough dataset provenance, preprocessing detail, split information or full training configuration to guarantee exact reproduction from the publication alone. Those details must be confirmed from the original experiment files before any reproduction claim is made.

The current `src/train_tcn.py` file is a separate baseline implementation and **is not represented as an exact reproduction** of the paper's complete Gaussian-noise, SMOTE, stratified 10-fold and Grid Search pipeline.

## Publication

*Temporal Convolutional Networks for Electricity Theft Detection with Limited Data.* 19th INDIACom / 12th International Conference on Computing for Sustainable Global Development, IEEE, 2025.

## Research interests

- Temporal deep learning
- Data-efficient machine learning
- Electricity theft and non-technical loss detection
- Smart-grid analytics
- Anomaly detection

---
This repository is an accompanying research and documentation resource. Please consult the published paper for the formal scholarly record.
