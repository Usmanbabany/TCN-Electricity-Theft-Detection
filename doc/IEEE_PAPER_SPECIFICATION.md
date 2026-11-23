# IEEE Paper-Based Research Specification

## 1. Publication identity

**Title:** Temporal Convolutional Networks for Electricity Theft Detection with Limited Data  
**Author:** Usman Haruna  
**Venue:** 19th INDIACom / 12th International Conference on Computing for Sustainable Global Development  
**Publisher:** IEEE  
**Year:** 2025

This document summarizes the research methodology described in the published paper.

## 2. Research problem

The study investigates the use of Temporal Convolutional Networks (TCNs) to detect electricity theft, a form of non-technical loss, by identifying suspicious patterns in electricity-consumption data under limited-data conditions.

## 3. Methodology

The paper describes the following workflow:

1. Electricity-consumption dataset preparation.
2. Data preprocessing, including missing-value handling and normalization.
3. Gaussian-noise injection for data augmentation.
4. SMOTE to address class imbalance.
5. TCN architecture design and training.
6. Stratified 10-fold cross-validation.
7. Hyperparameter tuning using Grid Search.
8. Evaluation using accuracy, precision, recall, F1-score and ROC-AUC.

## 4. Dataset

The research dataset was obtained from Kaggle. The dataset is not redistributed in this repository. Users should obtain the data from its original source and comply with its applicable terms of use.

## 5. Reported hyperparameters

| Parameter | Value |
|---|---:|
| Convolutional filters | 64 |
| Kernel size | 3 |
| Dropout rate | 0.2 |
| Adam learning rate | 0.001 |

## 6. Evaluation metrics

The paper reports the use of accuracy, precision, recall, F1-score and area under the ROC curve (ROC-AUC).

## 7. Related documentation

See [Reported Results](REPORTED_RESULTS.md) for the performance values presented in the IEEE paper.
