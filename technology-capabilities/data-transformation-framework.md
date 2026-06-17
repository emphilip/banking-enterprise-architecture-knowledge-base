---
id: data-transformation-framework
title: Data Transformation Framework
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["dbt Framework", "In-Warehouse Transformation", "Analytics Engineering Framework"]
status: draft
sources: ["https://www.getdbt.com/blog/data-transformation-in-data-warehouse", "https://datacoves.com/dbt-libs"]
---

# Data Transformation Framework

**Definition.** Data Transformation Framework provides version-controlled, SQL-centric in-warehouse modelling with testing and documentation to build curated, business-ready data models.
**Also known as:** dbt Framework, In-Warehouse Transformation, Analytics Engineering Framework.

## Relationships
- Data Transformation Framework is defined in the Data & Analytics domain.
- Data Transformation Framework is derived from Data Warehousing.
- Data Transformation Framework depends on ELT Pipeline Engine.
- Data Transformation Framework is related to Data Mart Service.

## Details
Data Transformation Framework, exemplified by dbt (data build tool), treats analytics transformations as software: models are SQL SELECT statements under version control, compiled into a directed acyclic graph of dependencies and materialised as tables or views in the warehouse. It adds data tests (uniqueness, not-null, referential integrity), auto-generated lineage and documentation, and reusable macros so analytics engineers build modular, tested layers from staging through to marts. By running transformation inside the warehouse it completes the "T" of the ELT pattern, replacing bespoke transformation code with declarative, peer-reviewable models.

## References
- [dbt: Data transformation in the data warehouse](https://www.getdbt.com/blog/data-transformation-in-data-warehouse)
- [Datacoves: dbt packages and libraries](https://datacoves.com/dbt-libs)
