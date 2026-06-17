---
id: channel-orchestration-layer
title: Channel Orchestration Layer
type: technology-capability
domain: Channels & Engagement
level: L2
aliases: ["Experience Orchestration", "Backend-for-Frontend", "Journey Orchestration Mid-Tier"]
status: draft
sources: ["https://www.backbase.com/blog/digital-banking-platform", "https://www.temenos.com/products/infinity/"]
---

# Channel Orchestration Layer

**Definition.** Channel Orchestration Layer is the technology sub-capability providing the mid-tier that orchestrates data, workflows and shared customer state across mobile, web, branch and contact-centre execution surfaces.
**Also known as:** Experience Orchestration, Backend-for-Frontend, Journey Orchestration Mid-Tier.

## Relationships
- Channel Orchestration Layer is defined in the Channels & Engagement domain.
- Channel Orchestration Layer is derived from Digital Channel Platform.
- Channel Orchestration Layer depends on Integration Platform.
- Channel Orchestration Layer depends on Workflow Orchestration.

## Details
Channel Orchestration Layer implements the backend-for-frontend (BFF) pattern: it aggregates and reshapes domain APIs into channel-optimised payloads, holds session and journey state, and coordinates multi-step processes so the same logic drives every front end. It enforces consistent entitlements, caching and resilience (circuit breakers, retries) between thin clients and core systems. Engagement-banking platforms such as Backbase and Temenos Infinity position this tier as the place where reusable journeys are composed and orchestrated.

## References
- [Backbase digital banking platform](https://www.backbase.com/blog/digital-banking-platform)
- [Temenos Infinity](https://www.temenos.com/products/infinity/)
