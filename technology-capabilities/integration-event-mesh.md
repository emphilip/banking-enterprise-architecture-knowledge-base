---
id: integration-event-mesh
title: Integration Event Mesh
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Event Mesh", "Event Broker Network", "Dynamic Event Routing Fabric"]
status: draft
sources: ["https://docs.solace.com/Cloud/Event-Mesh/about_event_meshes.htm", "https://solace.com/blog/event-mesh-service-mesh-for-microservices/"]
---

# Integration Event Mesh

**Definition.** Integration Event Mesh is a dynamic, interconnected network of event brokers that routes events across hybrid and multi-cloud environments to decouple event producers and consumers.
**Also known as:** Event Mesh, Event Broker Network, Dynamic Event Routing Fabric.

## Relationships
- Integration Event Mesh is defined in the Integration & APIs domain.
- Integration Event Mesh is derived from Integration Platform.
- Integration Event Mesh is related to Event Streaming Bus.

## Details
Integration Event Mesh links multiple event brokers into a single logical fabric so an event published in one region or cloud is dynamically routed to interested subscribers anywhere, without producers knowing consumer locations. Solace PubSub+ implements this with broker-to-broker bridging and subscription propagation, supporting topic hierarchies and wildcard subscriptions for fine-grained filtering. The mesh enables event-driven architecture at enterprise scale across on-prem and multi-cloud estates, complementing log-based streaming with smart, filtered event distribution.

## References
- [About event meshes (Solace)](https://docs.solace.com/Cloud/Event-Mesh/about_event_meshes.htm)
- [Event mesh: service mesh for microservices](https://solace.com/blog/event-mesh-service-mesh-for-microservices/)
