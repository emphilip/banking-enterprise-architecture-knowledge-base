---
id: reference-data-management
title: Reference Data Management
type: technology-capability
domain: Data & Analytics
level: L2
aliases: ["Reference Data Service", "Code Table Management", "RDM"]
status: draft
sources: ["https://www.informatica.com/resources/articles/master-data-governance-framework.html", "https://www.sap.com/products/data-cloud/master-data-governance.html"]
---

# Reference Data Management

**Definition.** Reference Data Management governs the controlled lifecycle of code tables, taxonomies, hierarchies, and standard reference data shared across master data domains.
**Also known as:** Reference Data Service, Code Table Management, RDM.

## Relationships
- Reference Data Management is defined in the Data & Analytics domain.
- Reference Data Management is derived from Master Data Management.
- Reference Data Management is related to Metadata Catalog.

## Details
Reference Data Management curates the controlled vocabularies that other data depends on: currency and country codes, product and account types, industry classifications, and internal and external code mappings. Unlike transactional master data about specific parties or accounts, reference data is a relatively small, slowly changing set of permitted values, often sourced from standards bodies (ISO 4217, ISO 3166) and mapped between internal and external schemes. RDM versions these value sets, manages effective dating, governs change through stewardship and approval, and distributes consistent codes to consuming systems. In banking this ensures regulatory reports, payments, and risk aggregation all classify data against the same authoritative code sets.

## References
- [Informatica: Master data governance framework](https://www.informatica.com/resources/articles/master-data-governance-framework.html)
- [SAP: Master data governance](https://www.sap.com/products/data-cloud/master-data-governance.html)
