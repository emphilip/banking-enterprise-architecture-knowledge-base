---
id: apply-velocity-rules
title: Apply Velocity Rules
type: process-step
process: Card Transaction Authorization
order: 4
status: draft
sources: ["https://www.checkout.com/blog/velocity-check"]
---

# Apply Velocity Rules

**Definition.** Apply Velocity Rules applies velocity and fraud-scoring rules to the in-flight transaction.

## Relationships
- Apply Velocity Rules is defined in the Card Transaction Authorization process.
- Apply Velocity Rules causes Authorize Transaction.
- Apply Velocity Rules depends on the Fraud Analytics capability.
- Apply Velocity Rules mentions Card Operations Analyst.

## Details
Apply Velocity Rules runs velocity counters and real-time fraud scoring against the in-flight transaction to produce a risk score for the authorization decision.

## References
- [Velocity checks](https://www.checkout.com/blog/velocity-check)
