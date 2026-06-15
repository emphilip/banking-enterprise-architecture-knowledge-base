---
id: payment-authorization-and-routing
title: Payment Authorization & Routing
type: business-process
domain: Payments
aliases: ["Authorization & Routing", "Payment Routing"]
status: draft
sources: ["https://www.iso20022payments.com/cbpr/pacs-008-serial-method/", "https://fedwireservice.org/"]
---

# Payment Authorization & Routing

**Definition.** Payment Authorization & Routing screens, authorizes and routes each payment to the correct clearing rail.
**Also known as:** Authorization & Routing, Payment Routing.

## Relationships
- Payment Authorization & Routing is derived from Payment Processing.
- Payment Authorization & Routing is defined in the Payments domain.
- Payment Authorization & Routing depends on the Payment Orchestration capability.

## Details
The sub-process is performed by the Payment Operations Analyst. Inputs are the validated payment order; outputs are a routed payment ready for clearing. Controls include sanctions screening, fraud checks and limit checks before the rail decision is made.

## References
- [CBPR+ pacs.008 serial method](https://www.iso20022payments.com/cbpr/pacs-008-serial-method/)
- [Fedwire Funds Service](https://fedwireservice.org/)
