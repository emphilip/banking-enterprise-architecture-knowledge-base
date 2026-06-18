---
id: api-lifecycle-manager
title: API Lifecycle Manager
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["API Lifecycle Governance", "API Versioning & Publishing", "API Product Manager"]
status: draft
sources: ["https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts", "https://api7.ai/blog/api-management-pillars-guide"]
---

# API Lifecycle Manager

**Definition.** API Lifecycle Manager governs how APIs are designed, imported, versioned, packaged, published, deprecated, and retired across environments with promotion and governance controls.
**Also known as:** API Lifecycle Governance, API Versioning & Publishing, API Product Manager.

## Relationships
- API Lifecycle Manager is defined in the Integration & APIs domain.
- API Lifecycle Manager is derived from API Management.
- API Lifecycle Manager is related to Developer Portal.

## Details
API Lifecycle Manager moves an API design through stages: import from OpenAPI, assign a version and revision, bundle operations into API products, promote across dev/test/prod environments, and mark older versions deprecated before retirement. Azure API Management models versions and revisions so non-breaking changes ship as revisions while breaking changes become new versions. Governance gates (linting, approval, change logs) enforce naming and security standards before an API is published to consumers through the portal.

## References
- [Azure API Management key concepts](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts)
- [API management pillars guide](https://api7.ai/blog/api-management-pillars-guide)
