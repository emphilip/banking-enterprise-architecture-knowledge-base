---
id: reward-points-accrual
title: Reward Points Accrual
type: business-capability
domain: Cards
level: L4
aliases: ["Points Earning", "Loyalty Accrual"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Reward Points Accrual

**Definition.** Reward Points Accrual calculates and posts earned points or cashback from qualifying card spend, supporting the BIAN Reward Points Account service domain.
**Also known as:** Points Earning, Loyalty Accrual.

## Relationships
- Reward Points Accrual is defined in the Cards domain.
- Reward Points Accrual is derived from Rewards Management.
- Reward Points Accrual depends on the Core Banking Processing capability.

## Details
On each cleared, settled transaction this capability applies the program earn matrix to the BIAN Reward Points Account: base points per dollar plus category bonuses keyed off the transaction MCC, capped at any quarterly/annual spend caps. Reversed or refunded transactions claw back previously accrued points, and the accrued balance contributes to the issuer's reward liability accrual recorded through core banking.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Frameworks](https://www.apqc.org/process-frameworks)
