---
id: card-closure
title: Card Closure
type: business-capability
domain: Cards
level: L3
aliases: ["Card Cancellation", "Card Account Closure"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Card Closure

**Definition.** Card Closure terminates a card account, settles outstanding balances and decommissions devices and tokens within the BIAN Issued Device Administration service domain.
**Also known as:** Card Cancellation, Card Account Closure.

## Relationships
- Card Closure is defined in the Cards domain.
- Card Closure is derived from Card Lifecycle Management.
- Card Closure depends on the Core Banking Processing capability.

## Details
The BIAN Issued Device Administration service domain retires the device and the card account: the final balance, accrued interest and fees are settled in core banking, all network tokens (DPANs) are deactivated through the Token Service Provider, and recurring card-on-file mandates are terminated. For credit cards the closure is reported to credit bureaus and any remaining balance continues to accrue interest under the original Reg Z agreement until paid off.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Frameworks](https://www.apqc.org/process-frameworks)
