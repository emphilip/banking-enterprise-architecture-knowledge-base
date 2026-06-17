---
id: stream-processing-engine
title: Stream Processing Engine
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Stream Compute Engine", "Real-Time Processing Engine", "Flink Engine"]
status: draft
sources: ["https://docs.confluent.io/platform/current/streams/architecture.html", "https://axual.com/blog/what-is-enterprise-event-streaming-platform"]
---

# Stream Processing Engine

**Definition.** Stream Processing Engine performs continuous, low-latency computation over event streams using a topology of stream processors.
**Also known as:** Stream Compute Engine, Real-Time Processing Engine, Flink Engine.

## Relationships
- Stream Processing Engine is defined in the Data & Analytics domain.
- Stream Processing Engine is derived from Data Streaming.
- Stream Processing Engine depends on Event Streaming Bus.
- Stream Processing Engine is related to Stateful Stream Processor.

## Details
Stream Processing Engine technologies such as Kafka Streams and Apache Flink model a computation as a topology: a directed graph of source, processor, and sink nodes that transform records one event at a time as they arrive. Each processor reads from input topic partitions, applies map, filter, join, or aggregation logic, and writes to output topics, with tasks distributed across instances for parallelism keyed by partition. Engines provide event-time semantics, watermarks for handling late data, and exactly-once processing guarantees backed by changelog topics. This enables real-time fraud scoring, alerting, and continuous enrichment instead of batch micro-runs.

## References
- [Confluent: Kafka Streams architecture](https://docs.confluent.io/platform/current/streams/architecture.html)
- [Axual: What is an enterprise event streaming platform?](https://axual.com/blog/what-is-enterprise-event-streaming-platform)
