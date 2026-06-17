---
id: route-order
title: Route Order
type: process-step
process: Trade Order Management
order: 3
aliases: ["Order Routing Step", "Venue Selection Step"]
status: draft
sources: ["https://iongroup.com/blog/markets/stepping-into-the-trading-future-with-order-management-systems/"]
---

# Route Order

**Definition.** Route Order routes the validated order to the chosen venue or broker for best execution.
**Also known as:** Order Routing Step, Venue Selection Step.

## Relationships
- Route Order is defined in the Trade Order Management process.
- Route Order causes Execute Order.
- Route Order depends on the Brokerage & Trading capability.
- Route Order mentions Trader.
- Route Order mentions Order Placed Event.

## Details
The Trader routes the validated order to the selected venue using market data, raising the Order Placed Event. Controls include best execution and venue selection.

## References
- [Stepping into the trading future with OMS](https://iongroup.com/blog/markets/stepping-into-the-trading-future-with-order-management-systems/)
