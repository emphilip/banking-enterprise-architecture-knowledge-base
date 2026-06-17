---
id: chargeback-case
title: Chargeback Case
type: artifact
domain: Cards
aliases: ["Dispute Case", "Chargeback Record"]
status: draft
sources: ["https://chargebacks911.com/chargeback-life-cycle/", "https://www.chargeflow.io/chargebacks-101/chargeback-rules"]
---

# Chargeback Case

**Definition.** Chargeback Case is the case record tracking a cardholder dispute through chargeback, representment and resolution. Chargeback Case is the artifact that carries the dispute state across the chargeback-processing and dispute-resolution flows.

**Also known as:** Dispute Case, Chargeback Record.

## Relationships
- Chargeback Case is related to the Cards domain.
- Chargeback Case mentions Chargeback Processing.
- Chargeback Case mentions Register Dispute Claim.
- Chargeback Case mentions Assign Reason Code.

## Details
Chargeback Case records the disputed transaction reference, the cardholder claim and category, the assigned scheme reason code (e.g. Visa 10-13, Mastercard 4837/4853), the disputed amount, provisional-credit status, the evidence package, and the representment and arbitration history with phase deadlines. It is opened when the dispute claim is registered, tracks the Reg Z 60-day billing-error and Reg E error-resolution timelines, and drives chargeback filing within the 120-day limit. Chargeback Case captures the final outcome and credit/debit, providing the audit trail for regulatory and scheme compliance.

## References
- https://chargebacks911.com/chargeback-life-cycle/
- https://www.chargeflow.io/chargebacks-101/chargeback-rules
