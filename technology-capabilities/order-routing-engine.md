---
id: order-routing-engine
title: Order Routing Engine
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Order Routing Service", "Smart Order Routing", "FIX Routing Engine"]
status: draft
sources: ["https://www.limina.com/blog/order-management-system-oms", "https://professional.bloomberg.com/solutions/buy-side/trade-execution/", "https://www.crd.com/solutions/charles-river-ims/"]
---

# Order Routing Engine

**Definition.** Order Routing Engine is the technology capability that generates, enriches and routes orders to brokers, trading venues and execution providers, applying smart-routing and connectivity so orders reach the right destination for execution.
**Also known as:** Order Routing Service, Smart Order Routing, FIX Routing Engine.

## Relationships
- Order Routing Engine is defined in the Core Processing domain.
- Order Routing Engine is derived from Order Management System.
- Order Routing Engine depends on Pre-Trade Compliance Engine.
- Order Routing Engine is related to Brokerage & Trading.

## Details
Order Routing Engine enriches and routes orders from the OMS to brokers, venues and execution providers, almost universally over the FIX protocol, applying smart-order-routing (SOR) logic to select venues that support best execution. It evaluates each order against Pre-Trade Compliance Engine rules before release and tracks acknowledgements and fills back from the destination. Platforms such as Charles River IMS, Bloomberg trade execution and Limina realize broker/venue connectivity, FIX session management and routing across multi-asset liquidity pools.

## References
- [Limina OMS](https://www.limina.com/blog/order-management-system-oms)
- [Bloomberg Trade Execution](https://professional.bloomberg.com/solutions/buy-side/trade-execution/)
- [Charles River IMS](https://www.crd.com/solutions/charles-river-ims/)
