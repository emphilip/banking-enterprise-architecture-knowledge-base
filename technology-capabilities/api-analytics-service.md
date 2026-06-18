---
id: api-analytics-service
title: API Analytics Service
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["API Usage Analytics", "API Reporting & Insights", "API Telemetry"]
status: draft
sources: ["https://www.ibm.com/think/topics/api-management", "https://api7.ai/blog/api-management-pillars-guide"]
---

# API Analytics Service

**Definition.** API Analytics Service collects, aggregates, and visualizes API usage, performance, latency, and consumer-behaviour metrics to drive operational health and adoption insight.
**Also known as:** API Usage Analytics, API Reporting & Insights, API Telemetry.

## Relationships
- API Analytics Service is defined in the Integration & APIs domain.
- API Analytics Service is derived from API Management.
- API Analytics Service depends on API Gateway Service.

## Details
API Analytics Service ingests per-call telemetry emitted by the gateway (request count, response code distribution, p50/p95/p99 latency, bandwidth, and consumer identity) and rolls it into dashboards and reports by API, product, operation, and subscriber. IBM API Connect and similar platforms surface adoption trends, top consumers, and error hotspots, and export events to external observability and SIEM tooling. The metering it produces also feeds chargeback and capacity-planning decisions across the API estate.

## References
- [IBM: What is API management?](https://www.ibm.com/think/topics/api-management)
- [API management pillars guide](https://api7.ai/blog/api-management-pillars-guide)
