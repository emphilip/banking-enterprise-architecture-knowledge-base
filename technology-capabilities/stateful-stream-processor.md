---
id: stateful-stream-processor
title: Stateful Stream Processor
type: technology-capability
domain: Data & Analytics
level: L3
aliases: ["Windowed Aggregation Service", "Keyed State Processor", "Stream Join Engine"]
status: draft
sources: ["https://docs.confluent.io/platform/current/streams/architecture.html", "https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about"]
---

# Stateful Stream Processor

**Definition.** Stateful Stream Processor maintains keyed state, windows, and aggregations across event streams to support joins, sessionisation, and exactly-once computation.
**Also known as:** Windowed Aggregation Service, Keyed State Processor, Stream Join Engine.

## Relationships
- Stateful Stream Processor is defined in the Data & Analytics domain.
- Stateful Stream Processor is derived from Stream Processing Engine.
- Stateful Stream Processor depends on Event Streaming Bus.

## Details
Stateful Stream Processor keeps local state stores keyed by record key, so operations like counts, running aggregates, and stream-table joins can be computed continuously without an external database lookup per event. State is partitioned to match the input topic partitions and backed by changelog topics, allowing fault-tolerant recovery and exactly-once semantics after failure. Windowing groups events by tumbling, hopping, or session windows over event time, with watermarks bounding how long to wait for late records. These primitives enable real-time enrichment, sessionised customer-behaviour analytics, and velocity-based fraud features within a single keyed processing topology.

## References
- [Confluent: Kafka Streams architecture and state](https://docs.confluent.io/platform/current/streams/architecture.html)
- [Microsoft: About Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about)
