---
id: api-security-and-throttling
title: API Security & Throttling
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["API Rate Limiting", "API Threat Protection", "API Policy Enforcement"]
status: draft
sources: ["https://api7.ai/blog/api-management-pillars-guide", "https://traefik.io/glossary/api-gateway-101"]
---

# API Security & Throttling

**Definition.** API Security & Throttling enforces authentication, authorization, rate limiting, quotas, and threat protection at the gateway to safeguard backend services from abuse and overload.
**Also known as:** API Rate Limiting, API Threat Protection, API Policy Enforcement.

## Relationships
- API Security & Throttling is defined in the Integration & APIs domain.
- API Security & Throttling is derived from API Management.
- API Security & Throttling depends on API Gateway Service.

## Details
API Security & Throttling applies inbound policies such as API-key and OAuth/JWT validation, IP allow-lists, mutual TLS, schema and payload validation, and WAF-style threat rules to block injection and oversized requests. Rate-limit policies cap calls per second or per consumer key, while quota policies cap volume per subscription over a billing window, returning HTTP 429 with retry-after headers when exceeded. These controls execute in the gateway data plane so abusive or anomalous traffic is rejected before reaching backend services.

## References
- [API management pillars guide](https://api7.ai/blog/api-management-pillars-guide)
- [Traefik API Gateway 101](https://traefik.io/glossary/api-gateway-101)
