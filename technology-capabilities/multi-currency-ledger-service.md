---
id: multi-currency-ledger-service
title: Multi-Currency Ledger Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Currency Translation Service", "FX Revaluation Service", "Multi-Currency Posting"]
status: draft
sources: ["https://blog.sap-press.com/what-is-saps-universal-journal", "https://docs.oracle.com/en/cloud/saas/financials/"]
---

# Multi-Currency Ledger Service

**Definition.** Multi-Currency Ledger Service is the technology capability that maintains transaction, local and group currencies on every posting and performs foreign-currency valuation and translation, supporting multi-ledger parallel accounting.
**Also known as:** Currency Translation Service, FX Revaluation Service, Multi-Currency Posting.

## Relationships
- Multi-Currency Ledger Service is defined in the Core Processing domain.
- Multi-Currency Ledger Service is derived from Journal Processing Engine.
- Multi-Currency Ledger Service is related to Chart Of Accounts Service.

## Details
Multi-Currency Ledger Service stores each journal line in up to three or more parallel currencies (transaction, company-code/local and group/global) so that consolidation and management reporting need no downstream re-translation. The SAP Universal Journal records these currency amounts natively. At period end the service revalues open foreign-currency items and balances at closing rates, posting unrealised gains/losses, and translates to the group currency.

## References
- [SAP Universal Journal](https://blog.sap-press.com/what-is-saps-universal-journal)
- [Oracle Fusion Financials](https://docs.oracle.com/en/cloud/saas/financials/)
