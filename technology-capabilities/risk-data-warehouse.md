---
id: risk-data-warehouse
title: Risk Data Warehouse
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Risk Data Store", "Risk Mart", "Risk Repository"]
status: draft
sources: ["https://atlan.com/bcbs-239-guide/", "https://www.ovaledge.com/blog/bcbs-239"]
---

# Risk Data Warehouse

**Definition.** Risk Data Warehouse is the technology capability that provides a centralized, reconciled repository (warehouse or lakehouse) of risk-relevant positions, exposures, reference and market data across business lines — the system-of-record feeding risk computation and reporting.
**Also known as:** Risk Data Store, Risk Mart, Risk Repository.

## Relationships
- Risk Data Warehouse is defined in the Data & Analytics domain.
- Risk Data Warehouse is derived from Risk Data Aggregation.
- Risk Data Warehouse depends on the Data Warehousing capability.
- Risk Data Warehouse is related to Exposure Aggregation Service.

## Details
Risk Data Warehouse consolidates positions, trades, exposures, counterparty and instrument reference data and market data into a single reconciled risk data model, applying validation and reconciliation controls so that risk metrics are accurate and complete per BCBS 239. It serves as the system-of-record over which the Risk Analytics Engine and reporting layers operate, often implemented on a lakehouse to support both batch capital runs and near-real-time exposure queries.

## References
- [Atlan BCBS 239 Guide](https://atlan.com/bcbs-239-guide/)
- [OvalEdge BCBS 239](https://www.ovaledge.com/blog/bcbs-239)
