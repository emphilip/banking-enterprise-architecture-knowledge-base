---
id: trade-allocation-engine
title: Trade Allocation Engine
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Allocation Service", "Block Allocation Engine", "Average Price Allocation"]
status: draft
sources: ["https://www.limina.com/blog/order-management-system-oms", "https://www.ssctech.com/solutions/trade-order-management", "https://www.crd.com/solutions/charles-river-ims/"]
---

# Trade Allocation Engine

**Definition.** Trade Allocation Engine is the technology capability that splits executed block trades across underlying accounts and sleeves, applies allocation rules such as pro-rata and average price, and produces allocated legs back to the portfolio book-of-record for confirmation.
**Also known as:** Allocation Service, Block Allocation Engine, Average Price Allocation.

## Relationships
- Trade Allocation Engine is defined in the Core Processing domain.
- Trade Allocation Engine is derived from Order Management System.
- Trade Allocation Engine is related to Portfolio Accounting Engine.
- Trade Allocation Engine is related to Brokerage & Trading.

## Details
Trade Allocation Engine takes aggregated block executions and distributes fills across participating accounts and sleeves using fair allocation methods such as pro-rata, average price and rule-based weighting, ensuring no account is favoured. Allocated legs flow back to the Portfolio Accounting Engine for booking and to confirmation/affirmation workflows. Platforms such as SS&C trade order management, Charles River IMS and Limina realize block-and-allocate handling, a step that grows time-critical under T+1 where same-day allocation and affirmation are required.

## References
- [Limina OMS](https://www.limina.com/blog/order-management-system-oms)
- [SS&C Trade Order Management](https://www.ssctech.com/solutions/trade-order-management)
- [Charles River IMS](https://www.crd.com/solutions/charles-river-ims/)
