---
id: semantic-layer-service
title: Semantic Layer Service
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Semantic Layer", "Metrics Layer", "Universal Semantic Model"]
status: draft
sources: ["https://www.ibm.com/think/topics/semantic-layer", "https://www.atscale.com/"]
---

# Semantic Layer Service

**Definition.** Semantic Layer Service exposes governed, reusable business metrics and dimensions over the warehouse so consumers query consistent definitions independent of physical schema.
**Also known as:** Semantic Layer, Metrics Layer, Universal Semantic Model.

## Relationships
- Semantic Layer Service is defined in the Data & Analytics domain.
- Semantic Layer Service is derived from Data Warehousing.
- Semantic Layer Service is related to OLAP Cube Engine.
- Semantic Layer Service is related to Cloud Data Warehouse.

## Details
Semantic Layer Service sits between physical storage and consumption tools, mapping raw tables and columns to business-friendly entities, dimensions, and centrally defined metrics. A single definition of measures such as "net revenue" or "active customer" is authored once and reused across dashboards, notebooks, and natural-language tools, eliminating the conflicting metric definitions that arise when each report re-implements calculations. Modern universal semantic layers (for example AtScale) translate these governed models into the native query of the underlying warehouse at run time, often serving multidimensional and BI clients alike while enforcing row- and column-level security.

## References
- [IBM: What is a semantic layer?](https://www.ibm.com/think/topics/semantic-layer)
- [AtScale semantic layer platform](https://www.atscale.com/)
