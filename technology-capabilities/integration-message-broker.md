---
id: integration-message-broker
title: Integration Message Broker
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Message-Oriented Middleware", "MOM", "Application Message Broker"]
status: draft
sources: ["https://www.ibm.com/think/topics/enterprise-application-integration", "https://solace.com/resources/solace-event-driven-architecture-resources/ultimate-guide-evaluating-event-brokers"]
---

# Integration Message Broker

**Definition.** Integration Message Broker provides queue- and topic-based asynchronous messaging with guaranteed delivery, routing, and message exchange patterns between integrated applications.
**Also known as:** Message-Oriented Middleware, MOM, Application Message Broker.

## Relationships
- Integration Message Broker is defined in the Integration & APIs domain.
- Integration Message Broker is derived from Integration Platform.
- Integration Message Broker is related to Integration Event Mesh.

## Details
Integration Message Broker decouples senders and receivers through queues (point-to-point) and topics (publish-subscribe), offering persistence, acknowledgements, dead-letter handling, and at-least-once or exactly-once delivery. Brokers such as IBM MQ, RabbitMQ, and ActiveMQ support transactional messaging, message TTL, priority, and request-reply, and speak protocols like AMQP, MQTT, JMS, and STOMP. In banking it underpins reliable transfer of payment and posting messages where lost or duplicated messages are unacceptable, with delivery guarantees enforced per queue.

## References
- [IBM: Enterprise application integration](https://www.ibm.com/think/topics/enterprise-application-integration)
- [Ultimate guide to evaluating event brokers](https://solace.com/resources/solace-event-driven-architecture-resources/ultimate-guide-evaluating-event-brokers)
