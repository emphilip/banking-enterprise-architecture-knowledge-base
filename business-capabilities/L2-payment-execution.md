---
id: payment-execution
title: Payment Execution
type: business-capability
domain: Payments
level: L2
aliases: ["Payment Processing Capability"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Payment Execution

**Definition.** Payment Execution is the L2 business capability for processing validated payment instructions through to the relevant scheme or rail, including routing, format transformation, and status management, aligned to the BIAN Payment Execution service domain.
**Also known as:** Payment Processing Capability.

## Relationships
- Payment Execution is defined in the Payments domain.
- Payment Execution is derived from Payments.
- Payment Execution depends on the Payment Orchestration capability.
- Payment Execution is related to Payment Clearing & Settlement.

## Details
Payment Execution maps to BIAN Payment Execution and Payment Order service domains. It is the parent of Domestic Payments, Cross-Border Payments, and Real-Time Payments, and underpins the Payment Processing business process. Typical sub-functions include instruction validation, scheme routing, ISO 20022 transformation, and execution status tracking. Payment orchestration hubs such as cloud-native payment platforms realize this capability.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
