---
id: intercompany-elimination
title: Intercompany Elimination
type: business-capability
domain: Finance & Treasury
level: L4
aliases: ["IC Elimination", "Intra-Group Elimination", "Reciprocal Elimination"]
status: draft
sources: ["https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/", "https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf"]
---

# Intercompany Elimination

**Definition.** Intercompany Elimination removes reciprocal intra-group balances and unrealised profit during the consolidation run, directly supporting IFRS 10 group accounts.
**Also known as:** IC Elimination, Intra-Group Elimination, Reciprocal Elimination.

## Relationships
- Intercompany Elimination is defined in the Finance & Treasury domain.
- Intercompany Elimination is derived from Intercompany Accounting.
- Intercompany Elimination depends on the General Ledger Engine capability.

## Details
Intercompany Elimination cancels matched intra-group receivables/payables, intra-group revenue/expense and unrealised profit on intra-group inventory or asset transfers, as IFRS 10 requires these be eliminated in full so that consolidated statements present the group as a single economic entity. The capability identifies elimination pairs from the matched intercompany ledger, books elimination journals at the consolidation layer, and reports residual mismatches (timing or FX differences) for resolution before group results are finalised.

## References
- [IFRS 10 Consolidated Financial Statements](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-10-consolidated-financial-statements/)
- [APQC PCF 9.0 Manage Financial Resources](https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf)
