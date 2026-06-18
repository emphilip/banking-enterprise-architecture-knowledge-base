---
id: data-mapping-and-transformation
title: Data Mapping & Transformation
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Message Mapping", "Payload Mapping", "Schema Mapping Engine"]
status: draft
sources: ["https://solace.com/blog/evolution-event-driven-integration-new-micro-integrations/", "https://www.ibm.com/think/topics/enterprise-application-integration"]
---

# Data Mapping & Transformation

**Definition.** Data Mapping & Transformation converts message payloads between formats and schemas (e.g. XML, JSON, EDI, ISO 20022) through visual or rule-based field mapping and enrichment.
**Also known as:** Message Mapping, Payload Mapping, Schema Mapping Engine.

## Relationships
- Data Mapping & Transformation is defined in the Integration & APIs domain.
- Data Mapping & Transformation is derived from Integration Platform.
- Data Mapping & Transformation depends on Enterprise Service Bus.

## Details
Data Mapping & Transformation performs structural and semantic conversion: parsing a source payload, mapping fields to a target schema, applying type coercion, lookups, conditional logic, and enrichment from reference data. In banking it converts legacy SWIFT MT to ISO 20022 MX (CBPR+), flat files to JSON, and EDI segments to canonical XML. Tooling ranges from graphical mappers (XSLT, DataWeave, Mapping Studio) to code-based transforms, and mappings are versioned so format migrations stay auditable and repeatable across integration flows.

## References
- [Evolution of event-driven integration](https://solace.com/blog/evolution-event-driven-integration-new-micro-integrations/)
- [IBM: Enterprise application integration](https://www.ibm.com/think/topics/enterprise-application-integration)
