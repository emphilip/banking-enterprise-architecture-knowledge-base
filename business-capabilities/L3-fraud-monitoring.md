---
id: fraud-monitoring
title: Fraud Monitoring
type: business-capability
domain: Risk Management
level: L3
aliases: ["Fraud Surveillance", "Fraud Screening Capability"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.fincen.gov/resources/statutes-regulations"]
---

# Fraud Monitoring

**Definition.** Fraud Monitoring screens transactions and behaviour in real time and batch to score and flag suspected fraud for action, supported by the BIAN Fraud Model service domain.
**Also known as:** Fraud Surveillance, Fraud Screening Capability.

## Relationships
- Fraud Monitoring is defined in the Risk Management domain.
- Fraud Monitoring is derived from Fraud Management.
- Fraud Monitoring depends on the Fraud Analytics capability.
- Fraud Monitoring depends on the Machine Learning Platform capability.

## Details
Fraud Monitoring evaluates events at sub-second latency in the authorisation path and in near-real-time behavioural streams, combining deterministic rules, velocity checks, device and behavioural-biometric signals and machine-learning scores to assign a fraud score and decision (approve, challenge, decline, hold). Confirmed fraud meeting reporting thresholds drives Suspicious Activity Report filing to FinCEN under the BSA. Feedback from confirmed outcomes retrains scoring models and tunes rule thresholds to balance loss avoidance against customer friction.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [FinCEN Statutes and Regulations (BSA)](https://www.fincen.gov/resources/statutes-regulations)
