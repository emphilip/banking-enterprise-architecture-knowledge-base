---
id: data-lakehouse-platform
title: Data Lakehouse Platform
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Lakehouse Platform", "Open Lakehouse", "Delta/Iceberg Lakehouse"]
status: draft
sources: ["https://docs.databricks.com/aws/en/lakehouse-architecture/reference", "https://learn.microsoft.com/en-us/azure/databricks/lakehouse-architecture/reference"]
---

# Data Lakehouse Platform

**Definition.** Data Lakehouse Platform unifies data-lake storage and data-warehouse semantics over open table formats so a single curated store serves both business intelligence and machine-learning workloads.
**Also known as:** Lakehouse Platform, Open Lakehouse, Delta/Iceberg Lakehouse.

## Relationships
- Data Lakehouse Platform is defined in the Data & Analytics domain.
- Data Lakehouse Platform is derived from Data Warehousing.
- Data Lakehouse Platform is related to Cloud Data Warehouse.
- Data Lakehouse Platform is related to Distributed Query Engine.

## Details
Data Lakehouse Platform applies ACID transactions, schema enforcement, and time travel directly on inexpensive object storage using open table formats such as Delta Lake and Apache Iceberg. This removes the historical split between a raw data lake and a separate data warehouse: the same governed tables back SQL analytics, streaming, and model training without copying data into a proprietary store. The reference lakehouse architecture organises ingestion, curation, and serving so that BI tools and ML pipelines read consistent, transactional snapshots, with open formats avoiding vendor lock-in and enabling multiple query engines to operate over one copy of the data.

## References
- [Databricks Lakehouse architecture reference](https://docs.databricks.com/aws/en/lakehouse-architecture/reference)
- [Azure Databricks lakehouse architecture reference](https://learn.microsoft.com/en-us/azure/databricks/lakehouse-architecture/reference)
