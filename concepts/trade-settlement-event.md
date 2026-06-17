---
id: trade-settlement-event
title: Trade Settlement Event
type: event
domain: Lending & Credit
aliases: ["LC Settled Event", "Presentation Honored Event"]
status: draft
sources: ["https://www.dripcapital.com/resources/blog/letter-of-credit-lc", "https://academy.iccwbo.org/trade-finance/article/an-overview-of-ucp-600-and-isp98/"]
---

# Trade Settlement Event

**Definition.** Trade Settlement Event is the business trigger marking honor and settlement, or refusal, of a documentary-credit presentation. Trade Settlement Event records the outcome of document examination under the credit.

**Also known as:** LC Settled Event, Presentation Honored Event.

## Relationships
- Trade Settlement Event is related to the Lending & Credit domain.
- Trade Settlement Event causes Settle Trade Payment.
- Trade Settlement Event mentions Trade Finance Processing.
- Trade Settlement Event mentions Presentation & Settlement.

## Details
Trade Settlement Event fires when the Trade Finance Officer reaches the honor or refuse decision after examining presented documents against the credit terms, carrying the presentation reference, examination result and settlement amount or refusal notice. The event is raised at Settle Trade Payment in the Trade Finance Processing flow under four-eyes on payment and AML controls on settlement. On honor it triggers payment to the beneficiary; on discrepancy it triggers a refusal notice within the UCP 600 timeline.

## References
- https://www.dripcapital.com/resources/blog/letter-of-credit-lc
- https://academy.iccwbo.org/trade-finance/article/an-overview-of-ucp-600-and-isp98/
