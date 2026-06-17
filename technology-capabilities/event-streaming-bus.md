---
id: event-streaming-bus
title: Event Streaming Bus
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Streaming Backbone", "Kafka Bus", "Event Log"]
status: draft
sources: ["https://docs.confluent.io/cloud/current/client-apps/architecture.html", "https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about"]
---

# Event Streaming Bus

**Definition.** Event Streaming Bus is the durable, partitioned, publish-subscribe log that transports event streams between producers and consumers at scale.
**Also known as:** Streaming Backbone, Kafka Bus, Event Log.

## Relationships
- Event Streaming Bus is defined in the Data & Analytics domain.
- Event Streaming Bus is derived from Data Streaming.
- Event Streaming Bus is related to Streaming Connector Framework.
- Event Streaming Bus is related to Event Schema Registry.

## Details
Event Streaming Bus, realised by platforms such as Apache Kafka and Azure Event Hubs, persists events as an append-only commit log organised into topics. Each topic is split into partitions that are distributed across brokers, providing horizontal scalability and ordered delivery within a partition. Producers append records to topic partitions and consumers track their own offset, so many independent consumer groups can read the same stream at their own pace with replay from any retained offset. Replication across brokers gives durability and fault tolerance. The partitioned log model decouples producers from consumers and is the backbone for stream processing, change-data-capture, and event-driven integration.

## References
- [Confluent: Kafka client application architecture](https://docs.confluent.io/cloud/current/client-apps/architecture.html)
- [Microsoft: About Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about)
