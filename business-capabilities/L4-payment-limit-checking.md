---
id: payment-limit-checking
title: Payment Limit Checking
type: business-capability
domain: Payments
level: L4
aliases: ["Limit Validation", "Threshold Checks"]
status: draft
sources: ["https://bian.org/servicelandscape-9-0/object_12.html?object=30969", "https://deepwiki.com/bian-official/public/5.1-payment-operations"]
---

# Payment Limit Checking

**Definition.** Payment Limit Checking validates an instruction against customer, channel and regulatory thresholds prior to execution, realising the limit-application responsibility of the BIAN Payment Order service domain.
**Also known as:** Limit Validation, Threshold Checks.

## Relationships
- Payment Limit Checking is defined in the Payments domain.
- Payment Limit Checking is derived from Payment Order Capture.
- Payment Limit Checking depends on the Payment Orchestration capability.

## Details
Payment Limit Checking grounds in the limit-application responsibility of the BIAN Payment Order service domain. It validates an instruction against customer, channel and regulatory thresholds prior to execution. It evaluates cumulative and per-transaction limits and blocks or escalates breaches.

## References
- [BIAN Payment Order Service Domain](https://bian.org/servicelandscape-9-0/object_12.html?object=30969)
- [BIAN Payment Operations](https://deepwiki.com/bian-official/public/5.1-payment-operations)
