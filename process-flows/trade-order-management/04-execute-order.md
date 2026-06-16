---
id: execute-order
title: Execute Order
type: process-step
process: Trade Order Management
order: 4
aliases: ["Order Execution Step", "Fill Capture Step"]
status: draft
sources: ["https://www.magmio.com/news/160-trade-execution"]
---

# Execute Order

**Definition.** Execute Order executes the order and captures fills, full or partial, monitoring execution quality.
**Also known as:** Order Execution Step, Fill Capture Step.

## Relationships
- Execute Order is defined in the Trade Order Management process.
- Execute Order causes Confirm Trade.
- Execute Order depends on the Brokerage & Trading capability.
- Execute Order mentions Trader.
- Execute Order mentions Trade Executed Event.

## Details
The Trader executes the routed order and captures fills, branching full or partial fill and raising the Trade Executed Event. Controls include best execution monitoring and fill accuracy.

## References
- [Trade execution](https://www.magmio.com/news/160-trade-execution)
