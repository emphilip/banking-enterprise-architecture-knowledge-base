---
id: card-collections
title: Card Collections
type: business-capability
domain: Cards
level: L3
aliases: ["Card Dunning", "Card Arrears Management"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.ecfr.gov/current/title-12/chapter-X/part-1026"]
---

# Card Collections

**Definition.** Card Collections manages delinquent card balances, dunning and recovery activity, realising the BIAN Card Collections service domain.
**Also known as:** Card Dunning, Card Arrears Management.

## Relationships
- Card Collections is defined in the Cards domain.
- Card Collections is derived from Card Lifecycle Management.
- Card Collections depends on the Notification Services capability.

## Details
The BIAN Card Collections service domain (Cards-specific, distinct from Lending's Collections & Recovery) manages accounts that miss the minimum payment, stepping through delinquency buckets (30/60/90+ days past due), late-fee assessment within CARD Act / Reg Z limits, penalty-APR application, and charge-off at 180 days per FFIEC uniform retail credit classification. Dunning notices and payment reminders are issued through notification channels, and bureau reporting reflects the delinquency status.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [eCFR Regulation Z, 12 CFR Part 1026](https://www.ecfr.gov/current/title-12/chapter-X/part-1026)
