---
id: order-ticket
title: Order Ticket
type: artifact
domain: Wealth & Investments
aliases: ["Trade Order", "Deal Ticket"]
status: draft
sources: ["https://www.ssctech.com/solutions/trade-order-management", "https://www.horizontrading.io/what-is-an-order-management-system-oms/"]
---

# Order Ticket

**Definition.** Order Ticket is the instruction to buy or sell a security, specifying instrument, side, quantity and constraints, that is captured into trade order management to start the trade lifecycle in the wealth flow.

**Also known as:** Trade Order, Deal Ticket.

## Relationships
- Order Ticket is related to the Wealth & Investments domain.
- Order Ticket mentions Trade Order Management.
- Order Ticket mentions Capture Order.

## Details
Order Ticket specifies the instrument identifier (e.g. ticker, ISIN/CUSIP), the side (buy/sell), the quantity or notional, the order type (market, limit, stop) and price, the time-in-force, the account or block reference and any handling or compliance constraints. Order Ticket can originate from a trader directly or be raised from an approved rebalance plan by a portfolio manager. Once captured into the OMS, Order Ticket is validated and pre-trade compliance-checked against mandate, limits and restricted lists before routing and execution. Order Ticket is the front-end record from which fills, the Trade Confirmation, allocations and the settled position are derived and audited.

## References
- https://www.ssctech.com/solutions/trade-order-management
- https://www.horizontrading.io/what-is-an-order-management-system-oms/
