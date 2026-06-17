---
id: reward-points-redemption
title: Reward Points Redemption
type: business-capability
domain: Cards
level: L4
aliases: ["Points Redemption", "Loyalty Redemption"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Reward Points Redemption

**Definition.** Reward Points Redemption processes cardholder redemption of accumulated points against rewards, statement credits or purchases, supporting the BIAN Reward Points Account service domain.
**Also known as:** Points Redemption, Loyalty Redemption.

## Relationships
- Reward Points Redemption is defined in the Cards domain.
- Reward Points Redemption is derived from Rewards Management.
- Reward Points Redemption depends on the Core Banking Processing capability.

## Details
This capability debits the BIAN Reward Points Account at the redemption conversion rate (cents-per-point varies by redemption type — statement credit vs travel vs merchandise) and posts the offsetting value to the cardholder ledger or fulfilment partner in core banking. It enforces minimum-redemption thresholds, available-balance checks against the points sub-ledger, and reduces the outstanding reward liability when points are burned.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Frameworks](https://www.apqc.org/process-frameworks)
