---
id: elt-pipeline-engine
title: ELT Pipeline Engine
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["ETL/ELT Pipeline Engine", "Data Pipeline Orchestrator", "Ingestion & Load Engine"]
status: draft
sources: ["https://sqlofthenorth.blog/2021/03/29/elt-etl-design-patterns-with-azure-data-services/", "https://aws.amazon.com/blogs/big-data/etl-and-elt-design-patterns-for-lake-house-architecture-using-amazon-redshift-part-1/"]
---

# ELT Pipeline Engine

**Definition.** ELT Pipeline Engine ingests raw source data into the warehouse and orchestrates extract-load-transform pipelines, pushing transformation logic down to warehouse compute.
**Also known as:** ETL/ELT Pipeline Engine, Data Pipeline Orchestrator, Ingestion & Load Engine.

## Relationships
- ELT Pipeline Engine is defined in the Data & Analytics domain.
- ELT Pipeline Engine is derived from Data Warehousing.
- ELT Pipeline Engine depends on Cloud Data Warehouse.
- ELT Pipeline Engine is related to Data Transformation Framework.

## Details
ELT Pipeline Engine inverts the classic ETL order: data is extracted and loaded in raw form first, then transformed in place using the scalable SQL compute of the target store. Unlike ETL, where a separate transformation tier reshapes data before loading, the ELT pattern lets cheap elastic warehouse compute do the heavy lifting, simplifying ingestion and preserving raw history for reprocessing. The engine schedules and monitors ingestion connectors, manages incremental and full loads, and hands off to in-warehouse transformation. This pattern underpins lakehouse and cloud-warehouse architectures where storage is cheap and compute is elastic.

## References
- [SQL of the North: ELT/ETL design patterns with Azure data services](https://sqlofthenorth.blog/2021/03/29/elt-etl-design-patterns-with-azure-data-services/)
- [AWS: ETL and ELT design patterns for lakehouse architecture](https://aws.amazon.com/blogs/big-data/etl-and-elt-design-patterns-for-lake-house-architecture-using-amazon-redshift-part-1/)
