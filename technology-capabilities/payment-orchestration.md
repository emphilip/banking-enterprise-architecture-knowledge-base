---
id: payment-orchestration
title: Payment Orchestration
type: technology-capability
domain: Core Processing
aliases: ["Payment Hub"]
status: draft
---

# Payment Orchestration

**Definition.** Payment Orchestration is the technology capability that routes, validates, enriches, and executes payment instructions across rails such as ACH, wires, card networks, and real-time schemes, acting as the bank's central payment hub.
**Also known as:** Payment Hub.

## Relationships
- Payment Orchestration is defined in the Core Processing domain.
- Payment Orchestration depends on the Core Banking Processing capability.
- Payment Orchestration depends on the Data Streaming capability.
- Payment Orchestration mentions ACI BASE24.
- Payment Orchestration mentions Legacy Payment Hub.
- Payment Orchestration mentions Stripe.
- Payment Orchestration mentions Adyen.

## Details
Payment Orchestration normalizes inbound and outbound flows to ISO 20022 and applies routing, sanctions, and fraud checks before settlement. Legacy hubs such as ACI BASE24 run on premise with batch ACH cycles, while modern providers like Stripe, Adyen, Modern Treasury, and Volante Payments deliver API-first, cloud-native orchestration with real-time rail support. It is a hub-and-spoke layer that decouples channels from clearing and settlement utilities.

## References
- [ISO 20022 Standard](https://www.iso20022.org/)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
