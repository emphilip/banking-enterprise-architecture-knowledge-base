---
id: fraud-scoring-models
title: Fraud Scoring Models
type: business-capability
domain: Risk Management
level: L4
aliases: ["Fraud Risk Scoring", "Fraud Model Development"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm"]
---

# Fraud Scoring Models

**Definition.** Fraud Scoring Models develop, deploy and monitor machine-learning and rules-based models that score fraud risk on events, realised through the BIAN Fraud Model service domain and governed under model risk management.
**Also known as:** Fraud Risk Scoring, Fraud Model Development.

## Relationships
- Fraud Scoring Models is defined in the Risk Management domain.
- Fraud Scoring Models is derived from Fraud Monitoring.
- Fraud Scoring Models depends on the Machine Learning Platform capability.
- Fraud Scoring Models depends on the Fraud Analytics capability.

## Details
Fraud Scoring Models engineer features from transaction, device, behavioural-biometric and graph-link data and train supervised classifiers (gradient-boosted trees, neural networks) plus anomaly-detection models to output a real-time fraud probability. As decisioning models they fall under SR 11-7 model risk governance: documented conceptual soundness, independent validation, ongoing monitoring of score distributions, false-positive and detection rates, and population stability. Champion-challenger deployment and feedback loops from confirmed fraud retrain the models against drift.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Federal Reserve SR 11-7](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm)
