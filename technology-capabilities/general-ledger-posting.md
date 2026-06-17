---
id: general-ledger-posting
title: General Ledger Posting
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Sub-Ledger to GL Posting", "GL Interface Service", "Core GL Bridge"]
status: draft
sources: ["https://sdk.finance/blog/what-is-a-general-ledger-core-concepts/", "https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products"]
---

# General Ledger Posting

**Definition.** General Ledger Posting is the technology capability that aggregates core sub-ledger entries into GL postings, maintains the chart-of-accounts mapping and reconciles deposit sub-ledgers upward to the institution-wide general ledger.
**Also known as:** Sub-Ledger to GL Posting, GL Interface Service, Core GL Bridge.

## Relationships
- General Ledger Posting is defined in the Core Processing domain.
- General Ledger Posting is derived from Core Banking Processing.
- General Ledger Posting depends on General Ledger Engine.
- General Ledger Posting is related to General Ledger Accounting.

## Details
General Ledger Posting rolls deposit sub-ledger entries up to the institution-wide general ledger, applying chart-of-accounts mappings and reconciling balances between the sub-ledger and GL. General-ledger concept references distinguish detailed sub-ledgers from the summarised GL, and core-banking data-model references describe sub-ledger-to-GL reconciliation as a core function, with the consolidated postings handed to the enterprise General Ledger Engine.

## References
- [What is a general ledger - core concepts](https://sdk.finance/blog/what-is-a-general-ledger-core-concepts/)
- [Core banking data model, ledger and products](https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products)
