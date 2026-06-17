---
id: event-schema-registry
title: Event Schema Registry
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Schema Registry", "Stream Schema Service", "Message Contract Registry"]
status: draft
sources: ["https://docs.confluent.io/cloud/current/client-apps/architecture.html", "https://axual.com/blog/what-is-enterprise-event-streaming-platform"]
---

# Event Schema Registry

**Definition.** Event Schema Registry centrally manages and versions message schemas and enforces compatibility rules for schema evolution across streaming applications.
**Also known as:** Schema Registry, Stream Schema Service, Message Contract Registry.

## Relationships
- Event Schema Registry is defined in the Data & Analytics domain.
- Event Schema Registry is derived from Data Streaming.
- Event Schema Registry is related to Event Streaming Bus.
- Event Schema Registry is related to Stream Processing Engine.

## Details
Event Schema Registry stores Avro, JSON Schema, and Protobuf definitions for the records flowing through topics, assigning each a global ID and version. Producers and consumers serialise and deserialise against the registered schema, embedding only the schema ID in the payload to keep messages compact. The registry enforces a configurable compatibility mode (backward, forward, or full) so a new schema version cannot be registered if it would break existing readers, making the schema the explicit contract between independently deployed services. This governs safe schema evolution and prevents poison messages in event-driven banking pipelines.

## References
- [Confluent: Client application architecture and Schema Registry](https://docs.confluent.io/cloud/current/client-apps/architecture.html)
- [Axual: What is an enterprise event streaming platform?](https://axual.com/blog/what-is-enterprise-event-streaming-platform)
