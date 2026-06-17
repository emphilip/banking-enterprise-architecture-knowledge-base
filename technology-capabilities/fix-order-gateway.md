---
id: fix-order-gateway
title: FIX Order Gateway
type: technology-capability
domain: Core Processing
level: L3
aliases: ["FIX Connectivity Gateway", "FIX Session Manager", "Execution FIX Gateway"]
status: draft
sources: ["https://tradingtechnologies.com/trading/oms/", "https://flextrade.com/products/oms-platform/"]
---

# FIX Order Gateway

**Definition.** FIX Order Gateway provides managed FIX connectivity that transmits orders, amendments and execution reports between the trading desk and external venues, brokers and liquidity pools.
**Also known as:** FIX Connectivity Gateway, FIX Session Manager, Execution FIX Gateway.

## Relationships
- FIX Order Gateway is defined in the Core Processing domain.
- FIX Order Gateway is derived from Execution Management Service.
- FIX Order Gateway is related to Order Routing Engine.

## Details
FIX Order Gateway speaks the Financial Information eXchange protocol to brokers, exchanges and liquidity venues. It manages FIX sessions (Logon, Heartbeat, sequence-number recovery and ResendRequest), sends NewOrderSingle (MsgType=D) and OrderCancelReplaceRequest (MsgType=G) messages, and consumes ExecutionReport (MsgType=8) messages carrying OrdStatus and fill detail. Order management platforms such as Trading Technologies and FlexTrade route orders out and reconcile fills back through this gateway, so it is the wire-level link between Order Routing Engine decisions and external execution destinations.

## References
- [Trading Technologies OMS](https://tradingtechnologies.com/trading/oms/)
- [FlexTrade OMS platform](https://flextrade.com/products/oms-platform/)
