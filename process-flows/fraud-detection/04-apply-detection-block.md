---
id: apply-detection-block
title: Apply Detection Block
type: process-step
process: Fraud Detection
order: 4
aliases: ["Block Or Allow", "Detection Block Step"]
status: draft
sources: ["https://www.getfocal.ai/blog/bank-fraud-investigation"]
---

# Apply Detection Block

**Definition.** Apply Detection Block is the decision point that auto-blocks or holds high-risk activity or allows it to proceed.
**Also known as:** Block Or Allow, Detection Block Step.

## Relationships
- Apply Detection Block is defined in the Fraud Detection process.
- Apply Detection Block causes Route Fraud Alert.
- Apply Detection Block depends on the Fraud Analytics capability.
- Apply Detection Block mentions Fraud Alert.

## Details
This decision point reads the Fraud Alert and risk score and branches on the score band to a block/allow decision. Controls include block policy, branching on the score band and an audit trail of every block or release.

## References
- [Focal — Bank Fraud Investigation](https://www.getfocal.ai/blog/bank-fraud-investigation)
