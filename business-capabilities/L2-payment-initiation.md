---
id: payment-initiation
title: Payment Initiation
type: business-capability
domain: Payments
level: L2
aliases: ["Payment Origination"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Payment Initiation

**Definition.** Payment Initiation is the L2 business capability for capturing, validating, and authorising payment instructions from customers and channels, including Open Banking payment initiation, before they enter execution.
**Also known as:** Payment Origination.

## Relationships
- Payment Initiation is defined in the Payments domain.
- Payment Initiation is derived from Payment Services.
- Payment Initiation depends on the Payment Orchestration capability.
- Payment Initiation depends on the API Management capability.

## Details
Payment Initiation aligns to the BIAN Payment Order service domain. Typical sub-functions include instruction capture across channels, beneficiary validation, duplicate and limit checks, authorisation and authentication, and Open Banking PISP integration. It feeds validated orders into Payment Execution. API management platforms expose payment initiation APIs under Open Banking and PSD2-style mandates.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
