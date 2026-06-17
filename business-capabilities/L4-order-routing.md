---
id: order-routing
title: Order Routing
type: business-capability
domain: Wealth & Investments
level: L4
aliases: ["Smart Order Routing", "Venue Selection"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://securities.cib.bnpparibas/us-t1-trade-affirmation-settlement/"]
---

# Order Routing

**Definition.** Order Routing selects venues, brokers, and algorithms and routes orders for best execution; it supports the BIAN Trade Order service domain.
**Also known as:** Smart Order Routing, Venue Selection.

## Relationships
- Order Routing is defined in the Wealth & Investments domain.
- Order Routing is derived from Order Management.
- Order Routing depends on the Order Management System capability.
- Order Routing depends on the Core Banking Processing capability.

## Details
The BIAN Trade Order service domain directs an order to fulfilment. Order Routing applies a smart order router to split and sequence flow across lit exchanges, dark pools, and market makers, choosing the execution algorithm (VWAP, TWAP, implementation shortfall) to minimise market impact and meet the MiFID II best-execution obligation across price, cost, speed, and likelihood of execution and settlement.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [BNP Paribas — US T+1 Trade Affirmation and Settlement](https://securities.cib.bnpparibas/us-t1-trade-affirmation-settlement/)
