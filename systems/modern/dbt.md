---
id: dbt
title: dbt
type: modern-system
domain: Data & Analytics
maturity: standard
aliases: ["dbt Core", "dbt Cloud", "data build tool"]
status: draft
sources: ["https://www.getdbt.com/"]
---

# dbt

**Definition.** dbt is a SQL-based transformation framework from dbt Labs for the modern ELT stack, performing in-warehouse transformations with version control, testing, and lineage.
**Also known as:** dbt Core, dbt Cloud, data build tool.

## Relationships
- Data Warehousing depends on dbt.
- dbt supersedes Informatica PowerCenter.

## Details
dbt implements the transform ("T") step of ELT by running modular SQL models directly inside the cloud data warehouse, with dependency-aware orchestration, automated tests, and generated documentation and lineage. dbt Core is the open-source engine and dbt Cloud adds a managed development and scheduling environment. This replaces dedicated mid-tier ETL transform engines with in-warehouse, version-controlled SQL.

## References
- [dbt](https://www.getdbt.com/)
