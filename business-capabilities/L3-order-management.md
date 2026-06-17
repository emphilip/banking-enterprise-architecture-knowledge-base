---
id: order-management
title: Order Management
type: business-capability
domain: Wealth & Investments
level: L3
aliases: ["Order Lifecycle Management", "OMS Capability"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.dtcc.com/-/media/Files/PDFs/T2/Accelerating-the-US-Securities-Settlement-Cycle-to-T1-December-1-2021.pdf"]
---

# Order Management

**Definition.** Order Management captures, validates, routes, and tracks client and discretionary investment orders through their lifecycle; it is realised through the BIAN Trade Order service domain.
**Also known as:** Order Lifecycle Management, OMS Capability.

## Relationships
- Order Management is defined in the Wealth & Investments domain.
- Order Management is derived from Brokerage & Trading.
- Order Management depends on the Order Management System capability.
- Order Management depends on the Core Banking Processing capability.

## Details
The BIAN Trade Order service domain manages an order from creation to completion. Concretely, Order Management applies pre-trade compliance and limit checks, aggregates client orders into blocks, tracks state transitions (new, partially filled, filled, cancelled), and times the workflow to support same-day allocation and affirmation needed for the US T+1 settlement cycle.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [DTCC — Accelerating the US Securities Settlement Cycle to T+1](https://www.dtcc.com/-/media/Files/PDFs/T2/Accelerating-the-US-Securities-Settlement-Cycle-to-T1-December-1-2021.pdf)
