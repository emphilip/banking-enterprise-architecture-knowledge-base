---
id: assign-reason-code
title: Assign Reason Code
type: process-step
process: Chargeback Processing
order: 1
status: draft
sources: ["https://rivero.tech/guide-chargeback-reason-codes"]
---

# Assign Reason Code

**Definition.** Assign Reason Code selects the correct scheme chargeback reason code for the dispute.

## Relationships
- Assign Reason Code is defined in the Chargeback Processing process.
- Assign Reason Code causes Raise Chargeback.
- Assign Reason Code depends on the Card Processing capability.
- Assign Reason Code mentions Chargeback Case.
- Assign Reason Code mentions Dispute Resolution Specialist.

## Details
Assign Reason Code selects the correct scheme reason code (Visa 10-13, Mastercard 4837/4853) for the Chargeback Case, observing the 120-day filing limit.

## References
- [Guide to chargeback reason codes](https://rivero.tech/guide-chargeback-reason-codes)
