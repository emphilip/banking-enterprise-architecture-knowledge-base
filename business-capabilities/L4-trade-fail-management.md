---
id: trade-fail-management
title: Trade Fail Management
type: business-capability
domain: Wealth & Investments
level: L4
aliases: ["Fails Management", "Settlement Exceptions"]
status: draft
sources: ["https://securities.cib.bnpparibas/us-t1-trade-affirmation-settlement/", "https://bian.org/servicelandscape/"]
---

# Trade Fail Management

**Definition.** Trade Fail Management detects, investigates, and resolves failed or unmatched settlements and applies buy-in or penalties; it supports the BIAN Securities Fulfillment service domain.
**Also known as:** Fails Management, Settlement Exceptions.

## Relationships
- Trade Fail Management is defined in the Wealth & Investments domain.
- Trade Fail Management is derived from Trade Settlement.
- Trade Fail Management depends on the Order Management System capability.
- Trade Fail Management depends on the Core Banking Processing capability.

## Details
A settlement fails when securities or cash are not delivered on the contractual date. Trade Fail Management identifies the fail reason (unmatched instruction, insufficient inventory, SSI error), pursues resolution, and applies remedies — buy-in of undelivered shares and, under regimes such as the EU CSDR Settlement Discipline, cash penalties accruing daily. The compressed US T+1 cycle leaves less time to cure fails, raising the value of proactive exception handling in the BIAN Securities Fulfillment service domain.

## References
- [BNP Paribas — US T+1 Trade Affirmation and Settlement](https://securities.cib.bnpparibas/us-t1-trade-affirmation-settlement/)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
