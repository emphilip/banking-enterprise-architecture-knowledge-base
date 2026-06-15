---
id: authorization-controls
title: Authorization Controls
type: business-capability
domain: Cards
level: L3
aliases: ["Spending Controls", "Velocity Controls", "Card Controls"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.iso.org/standard/31628.html"]
---

# Authorization Controls

**Definition.** Authorization Controls applies velocity, merchant-category, geographic and limit rules to permit or block card transactions, supporting the BIAN Card Authorization service domain.
**Also known as:** Spending Controls, Velocity Controls, Card Controls.

## Relationships
- Authorization Controls is defined in the Cards domain.
- Authorization Controls is derived from Card Authorization.
- Authorization Controls depends on the Card Processing capability.

## Details
This capability enforces configurable rules against the BIAN Card Authorization decision: per-transaction and daily limits, velocity counts, allowed/blocked MCCs (ISO 18245 merchant category codes), country and channel (card-present vs e-commerce) restrictions, and ATM vs POS toggles. Increasingly exposed to cardholders as self-service controls in mobile apps, the rules are evaluated on each ISO 8583 authorization message and can decline before the funds check runs.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [ISO 8583 Financial transaction card messaging](https://www.iso.org/standard/31628.html)
