---
id: change-data-capture-service
title: Change Data Capture Service
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["CDC Service", "Debezium Connector", "Log-Based CDC"]
status: draft
sources: ["https://estuary.dev/blog/change-data-capture-kafka/", "https://dev.to/joy_akinyi_115689d7dff92f/change-data-capture-cdc-in-data-engineering-concepts-tools-and-real-world-implementation-22bm"]
---

# Change Data Capture Service

**Definition.** Change Data Capture Service detects and streams row-level changes from operational databases in real time to keep downstream stores synchronised.
**Also known as:** CDC Service, Debezium Connector, Log-Based CDC.

## Relationships
- Change Data Capture Service is defined in the Data & Analytics domain.
- Change Data Capture Service is derived from Data Streaming.
- Change Data Capture Service depends on Event Streaming Bus.
- Change Data Capture Service is related to Streaming Connector Framework.

## Details
Change Data Capture Service, typified by Debezium, reads a database's transaction log (the write-ahead log or binlog) rather than polling tables, so every insert, update, and delete is captured in commit order with minimal load on the source. Log-based CDC emits a change event per row, including before and after images, onto streaming topics where consumers materialise the change downstream. Compared with query-based CDC, the log-based approach captures deletes, avoids missed intermediate states, and adds negligible overhead to the operational database. In banking this keeps analytical stores, search indexes, and caches continuously in sync with cores without nightly batch extracts.

## References
- [Estuary: Change data capture with Kafka](https://estuary.dev/blog/change-data-capture-kafka/)
- [Change data capture (CDC) in data engineering](https://dev.to/joy_akinyi_115689d7dff92f/change-data-capture-cdc-in-data-engineering-concepts-tools-and-real-world-implementation-22bm)
