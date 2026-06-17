---
id: period-close-manager
title: Period Close Manager
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Financial Close Cockpit", "Close Orchestration Service", "GL Close Manager"]
status: draft
sources: ["https://sapinsider.org/topic/sap-finance/sap-general-ledger/", "https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana"]
---

# Period Close Manager

**Definition.** Period Close Manager is the technology capability that orchestrates the period-end close: scheduling and sequencing of close tasks, accruals and reclassifications, foreign-currency revaluation, balance carryforward and close certification across entities and ledgers.
**Also known as:** Financial Close Cockpit, Close Orchestration Service, GL Close Manager.

## Relationships
- Period Close Manager is defined in the Core Processing domain.
- Period Close Manager is derived from General Ledger Engine.
- Period Close Manager is related to Consolidation Engine.

## Details
Period Close Manager (the SAP Financial Closing Cockpit pattern) defines a templated close calendar with dependencies, owners and status tracking across local and group entities. It runs foreign-currency valuation of open items and balances, posts accruals and reclassifications, opens and closes posting periods, and carries balances forward, before certifying that subledgers and the GL tie out and the entity is ready for consolidation.

## References
- [SAP General Ledger (SAPinsider)](https://sapinsider.org/topic/sap-finance/sap-general-ledger/)
- [SAP S/4HANA General Ledger Features](https://blog.sap-press.com/11-features-of-general-ledger-accounting-in-sap-s4hana)
