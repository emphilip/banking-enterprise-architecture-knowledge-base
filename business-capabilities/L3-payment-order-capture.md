---
id: payment-order-capture
title: Payment Order Capture
type: business-capability
domain: Payments
level: L3
aliases: ["Payment Order Management", "Order Capture"]
status: draft
sources: ["https://bian.org/servicelandscape-9-0/object_12.html?object=30969", "https://deepwiki.com/bian-official/public/5.1-payment-operations"]
---

# Payment Order Capture

**Definition.** Payment Order Capture creates, validates and authorises a customer's funds-transfer instruction prior to execution, mapping to the BIAN Payment Order service domain which performs internal bank and compliance checks before the mechanics of transfer.
**Also known as:** Payment Order Management, Order Capture.

## Relationships
- Payment Order Capture is defined in the Payments domain.
- Payment Order Capture is derived from Payment Initiation.
- Payment Order Capture depends on the Payment Orchestration capability.

## Details
Payment Order Capture grounds in the BIAN Payment Order service domain. It records the customer instruction, applies internal validation and compliance gating, and prepares the order for downstream execution. It is the entry point of the initiation flow, distinct from the rail-facing execution mechanics.

## References
- [BIAN Payment Order Service Domain](https://bian.org/servicelandscape-9-0/object_12.html?object=30969)
- [BIAN Payment Operations](https://deepwiki.com/bian-official/public/5.1-payment-operations)
