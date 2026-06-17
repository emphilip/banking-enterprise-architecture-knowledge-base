---
id: subledger-accounting
title: Subledger Accounting
type: technology-capability
domain: Core Processing
level: L2
aliases: ["SLA", "Subledger Accounting Engine", "Accounting Hub", "Subledger Service"]
status: draft
sources: ["https://docs.oracle.com/en/cloud/saas/financials/saas-subledger-accounting/", "https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana"]
---

# Subledger Accounting

**Definition.** Subledger Accounting is the technology capability that provides a centralised rules-based subledger transforming business transactions (AP, AR, assets and positions) into accounting entries and reconciling them to the general ledger, giving a detailed audit trail beneath summarised GL balances.
**Also known as:** SLA, Subledger Accounting Engine, Accounting Hub, Subledger Service.

## Relationships
- Subledger Accounting is defined in the Core Processing domain.
- Subledger Accounting is derived from General Ledger Engine.
- Subledger Accounting is related to Accounting Rules Engine.
- Subledger Accounting is related to General Ledger Posting.

## Details
Subledger Accounting receives source transactions from operational systems and applies configurable accounting methods to derive debit/credit entries, supporting multiple accounting representations (multi-GAAP) from a single business event. Oracle Fusion Subledger Accounting and an accounting-hub pattern post summarised or detailed lines to the GL while retaining full transactional lineage for audit and reconciliation, bridging core sub-ledgers to the General Ledger Posting interface.

## References
- [Oracle Subledger Accounting](https://docs.oracle.com/en/cloud/saas/financials/saas-subledger-accounting/)
- [SAP S/4HANA General Ledger Features](https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana)
