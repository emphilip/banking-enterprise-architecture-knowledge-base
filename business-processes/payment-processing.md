---
id: payment-processing
title: Payment Processing
type: business-process
domain: Payments
aliases: ["Payment Run"]
status: draft
---

# Payment Processing

**Definition.** Payment Processing is the process of validating, authorizing, routing, and executing customer and bank payment instructions across domestic, real-time, and cross-border rails.
**Also known as:** Payment Run.

## Relationships
- Payment Processing is defined in the Payments domain.
- Payment Processing depends on the Payment Execution capability.
- Payment Processing depends on the Payment Orchestration capability.
- Payment Processing causes Reconciliation & Settlement.

## Details
Payment Processing receives an instruction, performs validation and fraud and sanctions checks, applies routing to the appropriate scheme, and executes the debit and credit legs. Actors include customers, payment operations staff, and scheme operators. Systems involved include a payment orchestration hub, the core banking ledger, and clearing connectivity.

## Flow
- Receive Payment Instruction causes Validate Payment.
- Validate Payment causes Screen Sanctions.
- Screen Sanctions causes Authorize Payment.
- Authorize Payment causes Route Payment.
- Route Payment causes Format Clearing Message.
- Format Clearing Message causes Submit To Clearing.
- Submit To Clearing causes Capture Clearing Response.
- Capture Clearing Response causes Confirm Settlement.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
