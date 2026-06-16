---
id: trade-order-management
title: Trade Order Management
type: business-process
domain: Wealth & Investments
aliases: ["Trade Order Lifecycle", "OMS Workflow"]
status: draft
sources: ["https://www.crd.com/solutions/charles-river-trader", "https://www.ssctech.com/solutions/trade-order-management", "https://iongroup.com/blog/markets/stepping-into-the-trading-future-with-order-management-systems/"]
---

# Trade Order Management

**Definition.** Trade Order Management is the front-to-back securities trade lifecycle: capture and validate the order, run pre-trade compliance, route and execute on best terms, confirm and allocate fills across accounts, and settle the trade on the T+1 cycle.
**Also known as:** Trade Order Lifecycle, OMS Workflow.

## Relationships
- Trade Order Management is defined in the Wealth & Investments domain.
- Trade Order Management depends on the Brokerage & Trading capability.

## Details
Trade Order Management captures an Order Ticket into the OMS, validates it against mandate and limits, routes for best execution, captures fills, confirms with the counterparty, allocates fairly across accounts, and settles on the T+1 cycle with custody reconciliation. Controls include pre-trade mandate/limit checks, best execution, allocation fairness, four-eyes, T+1 settlement, and trade-vs-custody reconciliation. Actors include the Trader and the Settlement Operations Officer.

## Flow
- Capture Order causes Validate Order.
- Validate Order causes Route Order.
- Route Order causes Execute Order.
- Execute Order causes Confirm Trade.
- Confirm Trade causes Allocate Fills.
- Allocate Fills causes Settle Trade.

## References
- [Charles River Trader (OMS/EMS)](https://www.crd.com/solutions/charles-river-trader)
- [SS&C trade order management](https://www.ssctech.com/solutions/trade-order-management)
