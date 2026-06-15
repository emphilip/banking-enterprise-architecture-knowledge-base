---
id: verify-cardholder-activity
title: Verify Cardholder Activity
type: process-step
process: Card Fraud Handling
order: 2
status: draft
sources: ["https://www.sardine.ai/issuing-fraud"]
---

# Verify Cardholder Activity

**Definition.** Verify Cardholder Activity contacts/verifies the cardholder to confirm whether flagged transactions are genuine.

## Relationships
- Verify Cardholder Activity is defined in the Card Fraud Handling process.
- Verify Cardholder Activity causes Block Compromised Card.
- Verify Cardholder Activity depends on the Notification Services capability.
- Verify Cardholder Activity mentions Fraud Alert.
- Verify Cardholder Activity mentions Card Fraud Analyst.

## Details
Verify Cardholder Activity reaches out to the cardholder via outreach controls to confirm whether the flagged transactions are genuine before containment.

## References
- [Issuing fraud](https://www.sardine.ai/issuing-fraud)
