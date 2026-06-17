---
id: chargeback-processing
title: Chargeback Processing
type: business-process
domain: Cards
aliases: ["Chargeback Lifecycle", "Dispute Chargeback"]
status: draft
sources: ["https://www.chargeflow.io/chargebacks-101/chargeback-rules", "https://chargebacks911.com/chargeback-life-cycle/", "https://rivero.tech/guide-chargeback-reason-codes"]
---

# Chargeback Processing

**Definition.** Chargeback Processing is the lifecycle of an issuer-raised chargeback against the acquirer/merchant: select scheme reason code, raise the chargeback (first-presentment dispute), handle merchant representment, and escalate to pre-arbitration/arbitration, applying provisional and final credit under Reg Z / Reg E.
**Also known as:** Chargeback Lifecycle, Dispute Chargeback.

## Relationships
- Chargeback Processing is defined in the Cards domain.
- Chargeback Processing depends on the Dispute Management capability.

## Details
Chargeback Processing assigns the correct scheme chargeback reason code (e.g. Visa 10-13, Mastercard 4837/4853), raises the chargeback to the acquirer through the scheme within the 120-day filing limit, and receives and reviews merchant representment within the 30-day phase response window. Contested cases escalate to pre-arbitration and arbitration. Provisional credit is granted under Reg Z 60-day billing-error and Reg E error-resolution rules, and final credit/debit is applied at settlement. Actors include the Dispute Resolution Specialist working a Chargeback Case.

## Flow
- Assign Reason Code causes Raise Chargeback.
- Raise Chargeback causes Receive Representment.
- Receive Representment causes Review Representment Evidence.
- Review Representment Evidence causes Escalate To Arbitration.
- Escalate To Arbitration causes Settle Chargeback.

## References
- [Chargeback rules](https://www.chargeflow.io/chargebacks-101/chargeback-rules)
- [Chargeback life cycle](https://chargebacks911.com/chargeback-life-cycle/)
- [Guide to chargeback reason codes](https://rivero.tech/guide-chargeback-reason-codes)
