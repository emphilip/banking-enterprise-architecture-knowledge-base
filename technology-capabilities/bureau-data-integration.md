---
id: bureau-data-integration
title: Bureau Data Integration
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Bureau Connectivity Service", "Credit Data Aggregation"]
status: draft
sources: ["https://www.lendapi.com/blog/credit-decision-engine-unveiled-exploring-the-architecture-behind-smart-financial-decisions", "https://www.provenir.com/platform/decisioning/"]
---

# Bureau Data Integration

**Definition.** Bureau Data Integration is the technology capability that connects to credit bureaus and alternative-data providers, retrieving and normalising credit reports and attributes for use in scoring and rules.
**Also known as:** Bureau Connectivity Service, Credit Data Aggregation.

## Relationships
- Bureau Data Integration is defined in the Core Processing domain.
- Bureau Data Integration is derived from Credit Decisioning Engine.
- Bureau Data Integration depends on Integration Platform.

## Details
Bureau Data Integration manages connectivity to credit bureaus and alternative-data sources, pulling credit reports and normalising attributes into a common model for scoring and rules. Provenir and similar decision-engine architectures treat bureau access as a pluggable data layer, so that Experian, Equifax and TransUnion attributes plus alternative data are aggregated and made available to the decision flow.

## References
- [Credit decision engine architecture](https://www.lendapi.com/blog/credit-decision-engine-unveiled-exploring-the-architecture-behind-smart-financial-decisions)
- [Provenir Decisioning platform](https://www.provenir.com/platform/decisioning/)
