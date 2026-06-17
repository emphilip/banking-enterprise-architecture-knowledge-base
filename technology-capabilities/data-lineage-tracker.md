---
id: data-lineage-tracker
title: Data Lineage Tracker
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Lineage Service", "Data Lineage Engine", "Provenance Tracker", "End-to-End Lineage"]
status: draft
sources: ["https://www.bis.org/publ/bcbs239.htm", "https://www.collibra.com/"]
---

# Data Lineage Tracker

**Definition.** Data Lineage Tracker is the technology sub-capability that captures and visualises end-to-end data lineage across systems, reports and transformations to support impact analysis and regulatory traceability.
**Also known as:** Lineage Service, Data Lineage Engine, Provenance Tracker, End-to-End Lineage.

## Relationships
- Data Lineage Tracker is defined in the Data & Analytics domain.
- Data Lineage Tracker is derived from Data Governance.
- Data Lineage Tracker depends on Metadata Catalog.
- Data Lineage Tracker is related to Risk Data Lineage.

## Details
Data Lineage Tracker harvests lineage from ETL/ELT tools, databases, BI layers and code to build a column-level, transformation-aware map from source systems to final reports and dashboards. Interactive lineage diagrams support upstream/downstream impact analysis when a field changes and provide the complete-lineage evidence BCBS 239 expects, letting a reported figure be traced to its origin. It draws asset definitions from the metadata catalogue and is the enterprise counterpart to the risk-specific lineage capability.

## References
- [BCBS 239 — Principles for effective risk data aggregation](https://www.bis.org/publ/bcbs239.htm)
- [Collibra (data lineage)](https://www.collibra.com/)
