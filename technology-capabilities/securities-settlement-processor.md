---
id: securities-settlement-processor
title: Securities Settlement Processor
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Securities Settlement Engine", "Post-Trade Processor", "SSI & Confirmation Service"]
status: draft
sources: ["https://www.limina.com/blog/order-management-system-oms", "https://www.advent.com/geneva/", "https://www.crd.com/solutions/charles-river-ims/"]
---

# Securities Settlement Processor

**Definition.** Securities Settlement Processor is the technology capability that manages post-trade processing for securities: trade confirmation, affirmation and matching, standing settlement instruction generation, custodian and CSD messaging, and settlement status tracking through to settled positions.
**Also known as:** Securities Settlement Engine, Post-Trade Processor, SSI & Confirmation Service.

## Relationships
- Securities Settlement Processor is defined in the Core Processing domain.
- Securities Settlement Processor is derived from Order Management System.
- Securities Settlement Processor depends on Trade Allocation Engine.
- Securities Settlement Processor is related to Brokerage & Trading.

## Details
Securities Settlement Processor handles the post-trade leg: it confirms, affirms and matches trades, derives standing settlement instructions (SSIs), and messages custodians and central securities depositories (CSDs) to settle delivery-versus-payment. It tracks settlement status, flags fails and drives exception handling. Allocated legs arrive from the Trade Allocation Engine. The move to T+1 settlement compresses the affirmation and SSI window to trade date, pushing platforms such as SS&C Advent Geneva and Charles River IMS toward same-day, straight-through post-trade automation.

## References
- [Limina OMS](https://www.limina.com/blog/order-management-system-oms)
- [SS&C Advent Geneva](https://www.advent.com/geneva/)
- [Charles River IMS](https://www.crd.com/solutions/charles-river-ims/)
