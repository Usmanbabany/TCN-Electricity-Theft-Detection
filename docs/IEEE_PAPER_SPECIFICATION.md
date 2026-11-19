# IEEE Paper-Based Research Specification

## 1. Publication identity

**Title:** Temporal Convolutional Networks for Electricity Theft Detection with Limited Data  
**Lead author:** Usman Haruna  
**Venue:** 19th INDIACom / 12th International Conference on Computing for Sustainable Global Development  
**Publisher:** IEEE  
**Year:** 2025

This document records the methodology and claims as described in the published paper. It does not add unreported experimental details.

## 2. Research problem and motivation

The paper addresses electricity theft as a form of non-technical loss and investigates whether temporal deep learning can identify suspicious consumption patterns when data is limited, noisy, incomplete or imbalanced.

## 3. Research objectives

The paper's stated objectives include:
- Developing a TCN-based approach for electricity-theft detection under limited-data conditions.
- Using data-enhancement techniques, including noise injection, to increase training-data diversity.
- Applying SMOTE to reduce class imbalance.
- Evaluating classification performance using precision, recall, F1-score and AUC, alongside accuracy.

## 4. Dataset description as published

The paper refers in its abstract and introduction to an EU benchmark described as a 4.2-million-meter dataset. It also mentions a 2023 São Paulo pilot and outcomes involving 41,000 households.

**Important documentation limitation:** The paper does not provide a sufficiently detailed dataset citation, access link, exact sample counts for the model experiment, feature schema, label definition, time span, train/test split or data-preparation procedure to independently identify and reconstruct the precise experimental dataset from the paper alone. A separate CSV shared during repository preparation has not been verified as the dataset used for the IEEE experiment and is not treated as that dataset here.

The dataset statements above are transcribed as claims made in the publication; they should not be interpreted as independently verified by this repository.

## 5. Methodology reported

The paper describes a multi-stage process:

1. **Data collection:** electricity-consumption records are supplied to the workflow.
2. **Preprocessing:** handle missing values and normalize data.
3. **Noise augmentation:** inject Gaussian noise into training data to simulate volatility and improve generalization.
4. **Class balancing:** use Synthetic Minority Over-sampling Technique (SMOTE) to address minority-class under-representation.
5. **TCN design:** use temporal convolutional modelling to analyse sequential electricity-consumption patterns.
6. **Training and validation:** use stratified 10-fold cross-validation.
7. **Hyperparameter tuning:** use Grid Search with cross-validation.
8. **Evaluation:** calculate accuracy, precision, recall, F1-score and ROC-AUC.
9. **Prediction workflow:** classify suspicious activity for further investigation or log normal consumption, as represented in the paper.

The publication does not specify all implementation-level choices required for exact reproduction (for example, the precise noise distribution parameters, SMOTE settings, fold-level preprocessing order, full TCN layer-by-layer configuration, search grid, random seeds and software versions). These must not be invented.

## 6. Hyperparameters reported

| Parameter | Value reported |
|---|---:|
| Convolutional filters | 64 |
| Kernel size | 3 |
| Dropout rate | 0.2 |
| Adam learning rate | 0.001 |

The paper discusses tuning convolutional filters, kernel size, dilation rates, dropout and learning rate. The table above lists the best values explicitly stated in the paper.

## 7. Evaluation metrics

The paper reports using:
- Accuracy
- Precision
- Recall
- F1-score
- Area under the ROC curve (ROC-AUC)

## 8. Author-provided experiment notebooks

The author has supplied Colab notebooks identified as the notebooks used during the research. They are being reviewed as original project artifacts before inclusion in the public repository.

The saved copies currently available for review contain working-stage code and do not all show a complete successful end-to-end run matching the reported result tables. They must therefore be reconciled with the final executed experiment notebook(s), saved outputs and configuration before being released as a verified reproduction package. This qualification concerns the current saved notebook copies and repository packaging; it does not change the author's account that the reported results came from the original research experiments.

## 9. Reproduction status

**Research result provenance:** The author confirms that the results reported in the IEEE paper were obtained through the original research experiments.

**GitHub release status:** The complete experiment has not yet been cleaned, packaged and rerun end-to-end from this repository. The current `src/train_tcn.py` file is a separate baseline, not the original full experiment implementation.

A reproducible release requires reconciling the original notebooks, confirming the dataset and preprocessing used for the published experiments, recovering the final configuration and preserving the relevant execution outputs. Missing implementation details must not be guessed.

## 10. Known reporting ambiguities to resolve

- The paper's dataset description is not sufficiently detailed to identify and independently reconstruct the exact experiment dataset.
- The paper's abstract includes large-scale benchmark and pilot-impact statements that are not accompanied by enough methodological detail in the paper to reproduce those claims.
- The ROC figure should be checked against the numerical AUC values stated in the results text (0.92 and 0.98) before any future reproduction or comparison.
- The text refers to a later ROC figure number that does not match the four-figure sequence shown in the paper.

These points are recorded transparently rather than silently corrected or presented as verified facts.
