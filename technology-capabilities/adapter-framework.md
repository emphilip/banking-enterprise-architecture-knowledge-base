---
id: adapter-framework
title: Adapter Framework
type: technology-capability
domain: Integration & APIs
level: L3
aliases: ["Connector SDK", "Adapter Runtime", "Integration Adapter Toolkit"]
status: draft
sources: ["https://www.celigo.com/articles/what-is-ipaas-integration-platform-as-a-service/", "https://www.jitterbit.com/blog/what-is-esb/"]
---

# Adapter Framework

**Definition.** Adapter Framework is the extensible runtime and SDK for building, configuring, and managing protocol and application adapters that connect the integration platform to endpoints.
**Also known as:** Connector SDK, Adapter Runtime, Integration Adapter Toolkit.

## Relationships
- Adapter Framework is defined in the Integration & APIs domain.
- Adapter Framework is derived from iPaaS Connector Hub.
- Adapter Framework is related to Data Mapping & Transformation.

## Details
Adapter Framework defines a common adapter contract (connect, authenticate, read, write, poll, and handle errors) plus an SDK so developers build reusable connectors for protocols (JMS, JDBC, file, HTTP) and applications (SAP, Salesforce, mainframe). Each adapter externalizes endpoint metadata, credentials, and operation definitions, and the framework runtime manages lifecycle, connection pooling, retry, and back-pressure. By standardizing how endpoints are wired in, the framework lets the connector hub expand its catalog without bespoke code per integration.

## References
- [What is iPaaS?](https://www.celigo.com/articles/what-is-ipaas-integration-platform-as-a-service/)
- [What is an ESB?](https://www.jitterbit.com/blog/what-is-esb/)
