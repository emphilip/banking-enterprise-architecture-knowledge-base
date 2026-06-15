---
id: api-management
title: API Management
type: technology-capability
domain: Integration & APIs
aliases: ["API Gateway"]
status: draft
---

# API Management

**Definition.** API Management is the technology capability that publishes, secures, throttles, versions, and monitors APIs, exposing bank services to internal consumers, partners, and Open Banking ecosystems.
**Also known as:** API Gateway.

## Relationships
- API Management is defined in the Integration & APIs domain.
- API Management depends on the Identity Access Management capability.
- API Management mentions CA API Gateway.
- API Management mentions Kong.
- API Management mentions Apigee.
- API Management is related to Integration Platform.

## Details
API Management provides the gateway, developer portal, and policy enforcement layer for Open Banking, partner, and channel APIs. Legacy gateways such as CA API Gateway are appliance-based, while modern platforms like Kong and Apigee are cloud-native, container-friendly, and support fine-grained rate limiting and OAuth. It enforces security via the Identity Access Management capability and fronts the Integration Platform.

## References
- [Open Banking Standards](https://www.openbanking.org.uk/)
- [Kong Gateway](https://konghq.com/)
