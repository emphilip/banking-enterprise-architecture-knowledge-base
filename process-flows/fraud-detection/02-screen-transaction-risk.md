---
id: screen-transaction-risk
title: Screen Transaction Risk
type: process-step
process: Fraud Detection
order: 2
aliases: ["Score Transaction Risk", "Risk Screening Step"]
status: draft
sources: ["https://www.getfocal.ai/blog/bank-fraud-investigation"]
---

# Screen Transaction Risk

**Definition.** Screen Transaction Risk applies rules and ML models to score transaction and event risk in real time.
**Also known as:** Score Transaction Risk, Risk Screening Step.

## Relationships
- Screen Transaction Risk is defined in the Fraud Detection process.
- Screen Transaction Risk causes Generate Fraud Alert.
- Screen Transaction Risk depends on the Fraud Analytics capability.
- Screen Transaction Risk mentions Fraud Detection Analyst.

## Details
The Fraud Detection Analyst tunes the scoring that produces a risk score from the normalized event feed. Controls include real-time scoring, model performance monitoring and rule governance to keep false positives within tolerance.

## References
- [Focal — Bank Fraud Investigation](https://www.getfocal.ai/blog/bank-fraud-investigation)
