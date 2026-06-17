---
id: risk-data-mart
title: Risk Data Mart
type: technology-capability
domain: Data & Analytics
level: L3
aliases: ["Risk Subject-Area Mart", "Risk Reporting Mart"]
status: draft
sources: ["https://erstudio.com/blog/enterprise-data-warehouse-architecture/", "https://www.databricks.com/blog/enterprise-data-governance-complete-modern-framework"]
---

# Risk Data Mart

**Definition.** Risk Data Mart publishes subject-area risk datasets curated from the risk data warehouse for risk analytics and reporting.
**Also known as:** Risk Subject-Area Mart, Risk Reporting Mart.

## Relationships
- Risk Data Mart is defined in the Data & Analytics domain.
- Risk Data Mart is derived from Risk Data Warehouse.
- Risk Data Mart is related to Exposure Aggregation Service.

## Details
Risk Data Mart provides the presentation layer of the risk data architecture: focused, conformed datasets scoped to credit, market, liquidity, or operational risk and optimised for risk analytics, capital calculation, and reporting. Built downstream of the integrated risk data warehouse, marts apply consistent dimensions (counterparty, instrument, book, time) so exposures, limits, and losses can be sliced reliably for regulatory and management views. Aligning to BCBS 239 principles, the mart carries lineage back to the warehouse and source systems so reported risk figures are accurate, complete, and traceable. Subject-area scoping lets credit and market risk teams consume and govern their reporting datasets independently.

## References
- [erwin: Enterprise data warehouse architecture](https://erstudio.com/blog/enterprise-data-warehouse-architecture/)
- [Databricks: Enterprise data governance framework](https://www.databricks.com/blog/enterprise-data-governance-complete-modern-framework)
