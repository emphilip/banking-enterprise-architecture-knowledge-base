---
id: streaming-connector-framework
title: Streaming Connector Framework
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Streaming Connectors", "Kafka Connect", "Connector Hub"]
status: draft
sources: ["https://opsiocloud.com/in/apache-kafka-event-streaming/", "https://oceanobe.com/news/using-kafka-to-stream-change-data-capture-data-between-databases/984"]
---

# Streaming Connector Framework

**Definition.** Streaming Connector Framework provides pre-built source and sink connectors that integrate external systems with the streaming platform without bespoke code.
**Also known as:** Streaming Connectors, Kafka Connect, Connector Hub.

## Relationships
- Streaming Connector Framework is defined in the Data & Analytics domain.
- Streaming Connector Framework is derived from Data Streaming.
- Streaming Connector Framework depends on Event Streaming Bus.
- Streaming Connector Framework is related to Change Data Capture Service.

## Details
Streaming Connector Framework, embodied by Kafka Connect, runs a fleet of worker processes that host configurable connectors: source connectors pull data from databases, files, and SaaS systems into topics, while sink connectors push topic data out to warehouses, search, and object stores. Connectors are declared as JSON configuration rather than code, with the framework handling parallelism through tasks, offset tracking, retries, and at-least-once or exactly-once delivery. Single Message Transforms reshape records in flight. This connector model is the standard integration tier for streaming architectures and is how log-based change-data-capture sources commonly publish into the bus.

## References
- [Opsio: Apache Kafka event streaming](https://opsiocloud.com/in/apache-kafka-event-streaming/)
- [Oceanobe: Using Kafka to stream CDC data between databases](https://oceanobe.com/news/using-kafka-to-stream-change-data-capture-data-between-databases/984)
