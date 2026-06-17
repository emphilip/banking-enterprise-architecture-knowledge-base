---
id: order-placed-event
title: Order Placed Event
type: event
domain: Wealth & Investments
aliases: ["Order Raised Event", "Order Submitted Event"]
status: draft
sources: ["https://www.horizontrading.io/what-is-an-order-management-system-oms/", "https://www.ssctech.com/solutions/trade-order-management"]
---

# Order Placed Event

**Definition.** Order Placed Event is the business event signalling that an order has been captured or raised into trade order management, starting the front-to-back trade lifecycle in the wealth flow.

**Also known as:** Order Raised Event, Order Submitted Event.

## Relationships
- Order Placed Event is related to the Wealth & Investments domain.
- Order Placed Event mentions Trade Order Management.
- Order Placed Event causes Capture Order.

## Details
Order Placed Event fires when an Order Ticket is submitted into the OMS, either directly by a trader or raised from a rebalance plan by portfolio management. Order Placed Event carries the instrument identifier, side, quantity, order type and constraints, the account or block reference, the mandate reference and the placement timestamp. Order Placed Event initiates capture and validation of the order, after which pre-trade compliance runs against mandate, limits and restricted lists. The event provides the audit anchor for the order's lifecycle from capture through routing, execution, confirmation, allocation and settlement.

## References
- https://www.horizontrading.io/what-is-an-order-management-system-oms/
- https://www.ssctech.com/solutions/trade-order-management
