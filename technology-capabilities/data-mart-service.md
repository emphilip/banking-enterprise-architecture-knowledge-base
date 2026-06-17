---
id: data-mart-service
title: Data Mart Service
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Data Mart Management", "Subject-Area Mart", "Marts Layer"]
status: draft
sources: ["https://www.getdbt.com/blog/data-transformation-in-data-warehouse", "https://erstudio.com/blog/enterprise-data-warehouse-architecture/"]
---

# Data Mart Service

**Definition.** Data Mart Service publishes subject-area, business-ready marts of summary and wide tables optimised for departmental analytics and downstream consumption.
**Also known as:** Data Mart Management, Subject-Area Mart, Marts Layer.

## Relationships
- Data Mart Service is defined in the Data & Analytics domain.
- Data Mart Service is derived from Data Warehousing.
- Data Mart Service depends on Data Transformation Framework.
- Data Mart Service is related to Cloud Data Warehouse.

## Details
Data Mart Service exposes the presentation layer of the warehouse: focused, denormalised datasets scoped to a single business subject such as finance, risk, or marketing. Marts are typically built as star or wide-table models with conformed dimensions so departmental users get fast, predictable queries without traversing the full integration layer. In a layered architecture they sit downstream of staging and integration models, materialised by the transformation framework as the final "gold" tables that BI tools, semantic models, and self-service consumers read. Subject-area scoping limits blast radius and lets teams own their marts independently.

## References
- [dbt: Data transformation in the data warehouse](https://www.getdbt.com/blog/data-transformation-in-data-warehouse)
- [erwin: Enterprise data warehouse architecture](https://erstudio.com/blog/enterprise-data-warehouse-architecture/)
