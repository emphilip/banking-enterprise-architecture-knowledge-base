---
id: enterprise-service-bus
title: Enterprise Service Bus
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["ESB", "Service Bus", "Integration Bus"]
status: draft
sources: ["https://www.jitterbit.com/blog/what-is-esb/", "https://www.ibm.com/think/topics/enterprise-application-integration"]
---

# Enterprise Service Bus

**Definition.** Enterprise Service Bus provides a centralized messaging backbone that routes, mediates, and orchestrates synchronous and asynchronous service interactions between heterogeneous enterprise applications.
**Also known as:** ESB, Service Bus, Integration Bus.

## Relationships
- Enterprise Service Bus is defined in the Integration & APIs domain.
- Enterprise Service Bus is derived from Integration Platform.
- Enterprise Service Bus is related to Integration Message Broker.

## Details
Enterprise Service Bus implements mediation flows that decouple producers from consumers: content-based and itinerary routing, protocol bridging (JMS, SOAP, HTTP, MQ), message transformation, and service orchestration along a common bus rather than point-to-point links. Products such as IBM Integration Bus and MuleSoft expose mediation primitives and adapters so a single canonical message can fan out to many systems. The bus centralizes cross-cutting concerns (logging, security, error handling) but can become a bottleneck, which is why event brokers often complement it.

## References
- [What is an ESB?](https://www.jitterbit.com/blog/what-is-esb/)
- [IBM: Enterprise application integration](https://www.ibm.com/think/topics/enterprise-application-integration)
