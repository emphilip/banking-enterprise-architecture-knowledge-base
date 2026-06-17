---
id: cloud-data-warehouse
title: Cloud Data Warehouse
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Cloud DW", "MPP Warehouse", "Analytical Data Store"]
status: draft
sources: ["https://aws.amazon.com/blogs/big-data/etl-and-elt-design-patterns-for-lake-house-architecture-using-amazon-redshift-part-1/", "https://erstudio.com/blog/enterprise-data-warehouse-architecture/"]
---

# Cloud Data Warehouse

**Definition.** Cloud Data Warehouse is a managed columnar, massively-parallel analytical store providing elastic compute and storage for structured analytics and reporting.
**Also known as:** Cloud DW, MPP Warehouse, Analytical Data Store.

## Relationships
- Cloud Data Warehouse is defined in the Data & Analytics domain.
- Cloud Data Warehouse is derived from Data Warehousing.
- Cloud Data Warehouse is related to Distributed Query Engine.
- Cloud Data Warehouse is related to Data Lakehouse Platform.

## Details
Cloud Data Warehouse implementations such as Snowflake, Google BigQuery, and Amazon Redshift store data in compressed columnar formats and execute queries across massively-parallel-processing (MPP) compute nodes. Compute and storage scale independently, so analytical clusters can be sized or paused without moving the underlying data. The warehouse is the target of ELT load patterns, where raw data lands first and transformation is pushed down to warehouse SQL compute. Enterprise architectures layer staging, integration, and presentation schemas inside the warehouse to serve governed reporting, dashboards, and subject-area marts.

## References
- [AWS: ETL and ELT design patterns for lakehouse architecture](https://aws.amazon.com/blogs/big-data/etl-and-elt-design-patterns-for-lake-house-architecture-using-amazon-redshift-part-1/)
- [erwin: Enterprise data warehouse architecture](https://erstudio.com/blog/enterprise-data-warehouse-architecture/)
