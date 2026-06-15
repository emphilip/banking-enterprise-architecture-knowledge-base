---
id: card-authorization-engine
title: Card Authorization Engine
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Authorization Decisioning Engine", "Issuer Auth Engine", "Dynamic Authorization"]
status: draft
sources: ["https://www.marqeta.com/platform/card-processing", "https://www.marqeta.com/docs/developer-guides/about-transactions"]
---

# Card Authorization Engine

**Definition.** Card Authorization Engine is the technology capability providing real-time issuer authorization decisioning that evaluates each inbound card transaction against account status, available balance or credit, spend controls, velocity and risk rules and returns an approve or decline within scheme timeouts.
**Also known as:** Authorization Decisioning Engine, Issuer Auth Engine, Dynamic Authorization.

## Relationships
- Card Authorization Engine is defined in the Core Processing domain.
- Card Authorization Engine is derived from Card Processing.
- Card Authorization Engine depends on Card Transaction Switch.
- Card Authorization Engine is related to Card Authorization.

## Details
Card Authorization Engine receives ISO 8583 authorization requests from the scheme switch and applies issuer rules to authorize within network response-time windows. Marqeta's dynamic authorization model invokes program logic per transaction to apply just-in-time funding, spend controls and velocity limits before returning an approval or decline. It writes authorization holds to the cardholder account and integrates real-time fraud scoring for card-not-present risk.

## References
- [Marqeta Card Processing](https://www.marqeta.com/platform/card-processing)
- [Marqeta About Transactions](https://www.marqeta.com/docs/developer-guides/about-transactions)
