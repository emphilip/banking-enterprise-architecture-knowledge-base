---
id: raise-chargeback
title: Raise Chargeback
type: process-step
process: Chargeback Processing
order: 2
status: draft
sources: ["https://www.chargeflow.io/chargebacks-101/chargeback-rules"]
---

# Raise Chargeback

**Definition.** Raise Chargeback submits the chargeback (first-presentment dispute) to the acquirer via the scheme.

## Relationships
- Raise Chargeback is defined in the Chargeback Processing process.
- Raise Chargeback causes Receive Representment.
- Raise Chargeback depends on the Card Processing capability.
- Raise Chargeback mentions Chargeback Raised Event.
- Raise Chargeback mentions Dispute Resolution Specialist.

## Details
Raise Chargeback submits the first-presentment dispute to the acquirer through the scheme within the 120-day filing limit and emits the Chargeback Raised Event with required evidence.

## References
- [Chargeback rules](https://www.chargeflow.io/chargebacks-101/chargeback-rules)
