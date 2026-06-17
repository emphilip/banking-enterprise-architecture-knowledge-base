---
id: distributed-query-engine
title: Distributed Query Engine
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Query Engine", "Federated Query Engine", "MPP Query Engine"]
status: draft
sources: ["https://trino.io/episodes/21.html", "https://github.com/starburstdata/dbt-trino"]
---

# Distributed Query Engine

**Definition.** Distributed Query Engine executes federated, massively-parallel SQL over lake and warehouse storage for interactive analytical queries.
**Also known as:** Query Engine, Federated Query Engine, MPP Query Engine.

## Relationships
- Distributed Query Engine is defined in the Data & Analytics domain.
- Distributed Query Engine is derived from Data Warehousing.
- Distributed Query Engine is related to Data Lakehouse Platform.
- Distributed Query Engine is related to Cloud Data Warehouse.

## Details
Distributed Query Engine technologies such as Trino, Presto, Spark SQL, and Photon decompose a SQL statement into a distributed plan executed across worker nodes that read data in parallel from object storage and relational sources. A coordinator parses and optimises the query while workers stream and aggregate partitions, enabling interactive analytics over open table formats without first loading data into a single proprietary warehouse. Connectors let one query federate across the lakehouse, cloud warehouse, and operational databases. This separation of a pluggable compute engine from storage is central to lakehouse architectures and is targetable by transformation tools via adapters such as dbt-trino.

## References
- [Trino: How Trino executes queries](https://trino.io/episodes/21.html)
- [Starburst: dbt-trino adapter](https://github.com/starburstdata/dbt-trino)
