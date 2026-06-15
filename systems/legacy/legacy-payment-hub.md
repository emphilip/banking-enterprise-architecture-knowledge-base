---
id: legacy-payment-hub
title: Legacy Payment Hub
type: legacy-system
domain: Core Processing
maturity: legacy
aliases: ["On-Prem Payment Hub"]
status: draft
sources: ["https://en.wikipedia.org/wiki/Payment_hub"]
---

# Legacy Payment Hub

**Definition.** Legacy Payment Hub refers to the category of older, on-premises payment hub systems that centralize the routing, processing, and orchestration of payments across multiple rails and channels within a bank.
**Also known as:** On-Prem Payment Hub.

## Relationships
- Payment Orchestration depends on Legacy Payment Hub.
- Legacy Payment Hub mentions Adyen.
- Legacy Payment Hub is related to ACI BASE24.

## Details
Legacy Payment Hub systems consolidate payment initiation, validation, routing, and settlement that were previously handled by siloed applications per rail. They are commonly deployed on-premises with batch and message-based integration, and often predate ISO 20022 standardization. Limited real-time capability and rigid integration make them frequent candidates for replacement by cloud-native payment platforms.

## References
- [Payment hub (Wikipedia)](https://en.wikipedia.org/wiki/Payment_hub)
