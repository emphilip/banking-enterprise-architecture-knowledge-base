---
id: feed-detection-models
title: Feed Detection Models
type: process-step
process: Fraud Investigation
order: 6
aliases: ["Tune Detection Models", "Feedback Loop Step"]
status: draft
sources: ["https://www.getfocal.ai/blog/bank-fraud-investigation"]
---

# Feed Detection Models

**Definition.** Feed Detection Models feeds confirmed outcomes back to tune detection rules and models and emits the Fraud Case Closed Event.
**Also known as:** Tune Detection Models, Feedback Loop Step.

## Relationships
- Feed Detection Models is defined in the Fraud Investigation process.
- Feed Detection Models depends on the Machine Learning Platform capability.
- Feed Detection Models mentions Fraud Investigator.
- Feed Detection Models mentions Fraud Case Closed Event.

## Details
The Fraud Investigator feeds the fraud disposition back as model feedback and closes the case, emitting the Fraud Case Closed Event. Controls include the model feedback loop, label quality and change governance. This is the final step of Fraud Investigation.

## References
- [Focal — Bank Fraud Investigation](https://www.getfocal.ai/blog/bank-fraud-investigation)
