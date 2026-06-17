---
id: assessment-cycle-engine
title: Assessment Cycle Engine
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Assessment & Distribution Engine", "Cost Cycle Engine", "Allocation Cycle Service"]
status: draft
sources: ["https://learn.microsoft.com/en-us/dynamics365/business-central/finance-allocate-revenue-costs", "https://blog.sap-press.com/how-to-split-cost-of-goods-sold-cogs-with-sap-s/4hana-finance"]
---

# Assessment Cycle Engine

**Definition.** Assessment Cycle Engine executes assessment and distribution cycles that reallocate pooled costs and revenues across cost objects using configured drivers, percentages and iterative rules.
**Also known as:** Assessment & Distribution Engine, Cost Cycle Engine, Allocation Cycle Service.

## Relationships
- Assessment Cycle Engine is defined in the Core Processing domain.
- Assessment Cycle Engine is derived from Allocation Engine.

## Details
Assessment Cycle Engine runs the periodic allocation cycles that move pooled costs from sender cost objects to receivers. A cycle holds segments that define senders, receivers, the allocation base (fixed percentage, fixed amount, or statistical/driver-based such as headcount or transaction volume), and an execution order; iterative cycles resolve reciprocal allocations across cost centres. Distribution preserves the original primary cost element, while assessment posts to a secondary assessment element. The result is fully allocated cost and profitability views by cost object for management reporting.

## References
- [Allocate revenue and costs (Microsoft Dynamics 365)](https://learn.microsoft.com/en-us/dynamics365/business-central/finance-allocate-revenue-costs)
- [Splitting COGS with SAP S/4HANA Finance (SAP PRESS)](https://blog.sap-press.com/how-to-split-cost-of-goods-sold-cogs-with-sap-s/4hana-finance)
