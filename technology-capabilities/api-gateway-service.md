---
id: api-gateway-service
title: API Gateway Service
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["API Runtime Gateway", "Data Plane Gateway", "Edge API Gateway"]
status: draft
sources: ["https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts", "https://aws.amazon.com/blogs/architecture/build-an-enterprise-api-management-solution-using-amazon-api-gateway/"]
---

# API Gateway Service

**Definition.** API Gateway Service is the runtime data plane that receives client API calls and applies routing, protocol mediation, caching, and observability before forwarding requests to backend services.
**Also known as:** API Runtime Gateway, Data Plane Gateway, Edge API Gateway.

## Relationships
- API Gateway Service is defined in the Integration & APIs domain.
- API Gateway Service is derived from API Management.
- API Gateway Service is related to Integration Message Broker.

## Details
API Gateway Service is the data plane of an API platform: it terminates inbound HTTP/HTTPS and gRPC calls, matches them to API operations, and executes a policy pipeline (request/response transformation, header rewriting, response caching, retries, and circuit breaking) before proxying to upstream services. Azure API Management splits a control plane from a gateway data plane, and Amazon API Gateway fronts REST, HTTP, and WebSocket APIs with stage-based deployment and CloudWatch metrics. The gateway emits latency, error-rate, and throughput telemetry per route for downstream observability.

## References
- [Azure API Management key concepts](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts)
- [Enterprise API management with Amazon API Gateway](https://aws.amazon.com/blogs/architecture/build-an-enterprise-api-management-solution-using-amazon-api-gateway/)
