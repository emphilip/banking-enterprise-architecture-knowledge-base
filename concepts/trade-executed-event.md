---
id: trade-executed-event
title: Trade Executed Event
type: event
domain: Wealth & Investments
aliases: ["Order Filled Event", "Execution Event"]
status: draft
sources: ["https://www.magmio.com/news/160-trade-execution", "https://www.crd.com/solutions/charles-river-trader"]
---

# Trade Executed Event

**Definition.** Trade Executed Event is the business event signalling that an order has been executed and fills captured, marking the transition from execution to post-trade processing in the wealth flow.

**Also known as:** Order Filled Event, Execution Event.

## Relationships
- Trade Executed Event is related to the Wealth & Investments domain.
- Trade Executed Event mentions Trade Order Management.
- Trade Executed Event causes Confirm Trade.

## Details
Trade Executed Event fires when a routed order is filled, in full or in part, at one or more venues, capturing the execution price, executed quantity, venue, execution time and any remaining open quantity. Trade Executed Event is kept distinct from Trade Settlement Event used in trade finance, as it marks execution rather than settlement. Trade Executed Event initiates confirmation of the fills with the counterparty or broker and issuance of the Trade Confirmation, followed by allocation across accounts and T+1 settlement. Best-execution and fill-accuracy controls record the event so execution quality can be monitored and reported.

## References
- https://www.magmio.com/news/160-trade-execution
- https://www.crd.com/solutions/charles-river-trader
