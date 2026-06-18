---
id: api-monetisation-service
title: API Monetisation Service
type: technology-capability
domain: Integration & APIs
level: L3
aliases: ["API Monetization", "API Billing & Metering", "API Plan Management"]
status: draft
sources: ["https://tyk.io/api-monetization/", "https://www.digitalapi.ai/blogs/what-is-api-monetization"]
---

# API Monetisation Service

**Definition.** API Monetisation Service manages subscription plans, tiered pricing, metering, and billing integration so APIs can be packaged and sold as revenue-generating products.
**Also known as:** API Monetization, API Billing & Metering, API Plan Management.

## Relationships
- API Monetisation Service is defined in the Integration & APIs domain.
- API Monetisation Service is derived from API Lifecycle Manager.
- API Monetisation Service depends on API Analytics Service.

## Details
API Monetisation Service defines rate plans (free, pay-as-you-go, tiered, and freemium with quota caps), maps API products to those plans, meters consumption per consumer key, and pushes usage records to billing systems such as Stripe for invoicing. Tyk and similar platforms support quota-based and per-call billing tied to subscription policies, while overage and tier-upgrade rules govern paywall behaviour. Accurate metering depends on usage telemetry so each billable call is attributed to the correct consumer and plan.

## References
- [Tyk API monetization](https://tyk.io/api-monetization/)
- [What is API monetization?](https://www.digitalapi.ai/blogs/what-is-api-monetization)
