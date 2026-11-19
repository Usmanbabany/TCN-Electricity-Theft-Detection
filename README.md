# Temporal Convolutional Networks for Electricity Theft Detection With Limited Data

**Researcher and paper author:** Usman Haruna  
**Research area:** Computer Science, temporal deep learning, electricity-theft detection

## Overview

This repository documents the research presented in the IEEE INDIACom 2025 paper *Temporal Convolutional Networks for Electricity Theft Detection with Limited Data*. The study investigates a Temporal Convolutional Network (TCN) approach for identifying suspicious electricity-consumption patterns under limited, noisy and imbalanced-data conditions.

The repository distinguishes the results of the author's original research experiments from the current state of the code packaged here.

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

## Results from the original research

The following results are reported in the IEEE paper and come from the author's original research experiments.

| Metric | Imbalanced (without SMOTE) | Balanced (with SMOTE) |
|---|---:|---:|
| Accuracy | 89% | 97% |
| Precision | 88% | 96% |
| Recall | 91% | 97% |
| F1-score | 89% | 97% |
| ROC-AUC | 0.92 | 0.98 |

The paper also reports a separate noise-augmentation comparison: 96% accuracy and 96% F1-score without noise augmentation, compared with 97% accuracy and 97% F1-score with noise augmentation. See [reported results and experiment status](docs/REPORTED_RESULTS.md).

## Original experiment notebooks

The author has supplied the Colab notebooks used during the research for review and repository preparation. These notebooks are being checked and organized before any are presented as a clean, reproducible release. The saved copies currently available for review include working-stage code and execution issues that need to be reconciled with the final experiment record.

## Repository structure

- `src/` — implementation code under development.
- `docs/` — paper-based methodology, results and documentation.
- `publications/` — publication information.
- `future_research/` — possible extensions beyond the published study.

## Data and reproducibility

The original research dataset is not included. Do not commit confidential, licensed or identifiable customer-level electricity data. The paper does not provide enough dataset provenance, preprocessing detail, split information or full training configuration to reconstruct the experiment from the publication alone. The original notebooks and experiment configuration must be reconciled before the complete workflow can be packaged for independent execution.

The current `src/train_tcn.py` file is a separate baseline implementation. It is **not** the original experiment implementation and does not implement the paper's complete Gaussian-noise, SMOTE, stratified 10-fold and Grid Search pipeline. Therefore, the results above must not be described as outputs of this current baseline script.

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
