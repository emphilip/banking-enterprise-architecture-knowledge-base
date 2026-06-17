---
id: trade-execution
title: Trade Execution
type: business-capability
domain: Wealth & Investments
level: L3
aliases: ["Execution Management", "Best Execution"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://securities.cib.bnpparibas/us-t1-trade-affirmation-settlement/"]
---

# Trade Execution

**Definition.** Trade Execution sends orders to venues or counterparties, achieves best execution, and captures fills; it supports the BIAN Securities Fulfillment service domain.
**Also known as:** Execution Management, Best Execution.

## Relationships
- Trade Execution is defined in the Wealth & Investments domain.
- Trade Execution is derived from Brokerage & Trading.
- Trade Execution depends on the Order Management System capability.
- Trade Execution depends on the Core Banking Processing capability.

## Details
The BIAN Securities Fulfillment service domain executes the order against the market. Under MiFID II best-execution rules, the firm must take all sufficient steps to obtain the best result for the client across price, cost, speed, and likelihood of settlement, and evidence it. Trade Execution selects venues and algorithms, captures executions, and time-stamps fills so that settlement can complete within the T+1 cycle.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [BNP Paribas — US T+1 Trade Affirmation and Settlement](https://securities.cib.bnpparibas/us-t1-trade-affirmation-settlement/)
