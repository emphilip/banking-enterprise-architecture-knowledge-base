---
id: settlement-confirmation
title: Settlement Confirmation
type: business-process
domain: Payments
aliases: ["Settlement Capture"]
status: draft
sources: ["https://fedwireservice.org/", "https://www.swift.com/sites/default/files/files/pmpg-interbank-statement-creation-market-practice-final-version.pdf"]
---

# Settlement Confirmation

**Definition.** Settlement Confirmation captures settlement advices and confirms interbank money movement.
**Also known as:** Settlement Capture.

## Relationships
- Settlement Confirmation is derived from Reconciliation & Settlement.
- Settlement Confirmation is defined in the Payments domain.
- Settlement Confirmation depends on the Payment Orchestration capability.

## Details
The sub-process is performed by the Settlement Officer. Inputs are the Settlement File; outputs are confirmed settlement records. Controls include a settlement finality check and dual control over confirmation.

## References
- [Fedwire Funds Service](https://fedwireservice.org/)
- [SWIFT PMPG interbank statement market practice](https://www.swift.com/sites/default/files/files/pmpg-interbank-statement-creation-market-practice-final-version.pdf)
