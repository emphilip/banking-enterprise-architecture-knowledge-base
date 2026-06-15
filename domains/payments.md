---
id: payments-domain
title: Payments
type: domain
aliases: ["Payments Domain"]
status: draft
---

# Payments

**Definition.** Payments is the business value-stream domain covering the initiation, execution, clearing, and settlement of funds transfers across domestic, cross-border, and real-time payment rails.
**Also known as:** Payments Domain.

## Relationships
- Payments is defined in the Payments domain.
- Payment Execution is defined in the Payments domain.
- Payment Clearing & Settlement is defined in the Payments domain.
- Payment Initiation is defined in the Payments domain.
- Direct Debit Management is defined in the Payments domain.
- Payments is related to the Core Processing domain.

## Details
The Payments domain handles domestic schemes (ACH, Faster Payments), cross-border SWIFT flows, and real-time/instant rails, plus clearing, settlement, and direct debits. It maps closely to BIAN payment order and payment execution service domains and increasingly adopts ISO 20022 messaging for richer, standardized payment data.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
