---
id: ledger-account-mapping
title: Ledger Account Mapping
type: business-capability
domain: Finance & Treasury
level: L4
aliases: ["Account Mapping", "GL Mapping Rules", "Sub-Ledger Mapping"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf"]
---

# Ledger Account Mapping

**Definition.** Ledger Account Mapping maintains the mappings between source-system accounts, sub-ledgers and the group chart of accounts so that transactions are classified consistently across the bank.
**Also known as:** Account Mapping, GL Mapping Rules, Sub-Ledger Mapping.

## Relationships
- Ledger Account Mapping is defined in the Finance & Treasury domain.
- Ledger Account Mapping is derived from Chart Of Accounts Management.
- Ledger Account Mapping depends on the General Ledger Engine capability.

## Details
Ledger Account Mapping translates product- and source-system codes (core banking, cards, treasury, payroll) into the correct group GL account, cost centre and reporting dimensions, and maps local statutory accounts to the group consolidation chart. Accurate mapping rules are the prerequisite for clean consolidation and multi-GAAP reporting; broken or stale mappings push transactions to suspense and inflate close effort. The capability versions mapping rules, validates completeness, and routes unmapped items for exception handling.

## References
- [APQC PCF 9.0 Manage Financial Resources](https://www.apqc.org/resource-library/resource-listing/90-manage-financial-resources-definitions-and-key-measures-pcf)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
