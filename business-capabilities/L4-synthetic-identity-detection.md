---
id: synthetic-identity-detection
title: Synthetic Identity Detection
type: business-capability
domain: Risk Management
level: L4
aliases: ["Synthetic Fraud Detection", "Identity Fraud Detection"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.federalreserve.gov/publications/files/synthetic-identity-fraud-mitigation-toolkit.pdf"]
---

# Synthetic Identity Detection

**Definition.** Synthetic Identity Detection identifies fabricated and manipulated identities used to open accounts and obtain credit, linking identity, device and behaviour signals, supporting the BIAN Fraud Model service domain.
**Also known as:** Synthetic Fraud Detection, Identity Fraud Detection.

## Relationships
- Synthetic Identity Detection is defined in the Risk Management domain.
- Synthetic Identity Detection is derived from Fraud Risk Assessment.
- Synthetic Identity Detection depends on the Fraud Analytics capability.
- Synthetic Identity Detection depends on the Machine Learning Platform capability.

## Details
Synthetic Identity Detection targets the fastest-growing US fraud type described in the Federal Reserve Synthetic Identity Fraud Mitigation Toolkit, where fraudsters combine real and fictitious data (often a valid but unused SSN such as a child's) to build a credit profile, then "bust out". Detection correlates SSN issuance dates against claimed age, runs SSA eCBSV validation, applies device and velocity links, and uses graph analytics to surface identity clusters sharing addresses, phones or devices, scoring the likelihood of fabrication at onboarding.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Federal Reserve Synthetic Identity Fraud Mitigation Toolkit](https://www.federalreserve.gov/publications/files/synthetic-identity-fraud-mitigation-toolkit.pdf)
