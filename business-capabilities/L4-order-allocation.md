---
id: order-allocation
title: Order Allocation
type: business-capability
domain: Wealth & Investments
level: L4
aliases: ["Block Allocation", "Fill Allocation"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://securities.cib.bnpparibas/us-t1-trade-affirmation-settlement/"]
---

# Order Allocation

**Definition.** Order Allocation splits block-order fills fairly across client accounts and confirms allocations; it supports the BIAN Trade Order service domain.
**Also known as:** Block Allocation, Fill Allocation.

## Relationships
- Order Allocation is defined in the Wealth & Investments domain.
- Order Allocation is derived from Order Management.
- Order Allocation depends on the Order Management System capability.
- Order Allocation depends on the Core Banking Processing capability.

## Details
When multiple client orders are aggregated into a single block trade, Order Allocation distributes the resulting fills back to accounts using a fair, pre-disclosed method (typically pro-rata at the average execution price) so no account is favoured. Under the US T+1 cycle, allocations must be completed and communicated on trade date to allow affirmation by the 9:00 p.m. ET cut-off, supporting the BIAN Trade Order service domain.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [BNP Paribas — US T+1 Trade Affirmation and Settlement](https://securities.cib.bnpparibas/us-t1-trade-affirmation-settlement/)
