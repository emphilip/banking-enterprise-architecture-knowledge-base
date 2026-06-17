---
id: cross-reference-registry
title: Cross-Reference Registry
type: technology-capability
domain: Data & Analytics
level: L3
aliases: ["Cross-Reference Service", "Key Mapping Registry", "XREF Registry"]
status: draft
sources: ["https://www.informatica.com/resources/articles/master-data-governance-framework.html", "https://www.sap.com/products/data-cloud/master-data-governance.html"]
---

# Cross-Reference Registry

**Definition.** Cross-Reference Registry maintains the mappings between source-system record identifiers and the surviving golden-record key to support lookup and downstream propagation.
**Also known as:** Cross-Reference Service, Key Mapping Registry, XREF Registry.

## Relationships
- Cross-Reference Registry is defined in the Data & Analytics domain.
- Cross-Reference Registry is derived from Golden Record Management.
- Cross-Reference Registry is related to Survivorship Rule Engine.

## Details
Cross-Reference Registry stores the many-to-one mapping from each contributing source system's local key to the master golden-record key created when duplicates are merged. This cross-reference (XREF) is what lets the MDM hub answer "which golden record does this source record belong to" and "which source keys make up this golden record," enabling bidirectional lookup and consistent propagation of the mastered identifier back to operating systems. It preserves the lineage of a merge so survivorship decisions can be traced and, if a match is later found to be wrong, an unmerge can restore the original source associations. The registry is essential for downstream systems to resolve their local identifiers to the single party view.

## References
- [Informatica: Master data governance framework](https://www.informatica.com/resources/articles/master-data-governance-framework.html)
- [SAP: Master data governance](https://www.sap.com/products/data-cloud/master-data-governance.html)
