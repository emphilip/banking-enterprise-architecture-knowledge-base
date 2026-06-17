---
id: data-classification-service
title: Data Classification Service
type: technology-capability
domain: Data & Analytics
level: L3
aliases: ["Data Tagging Service", "Sensitivity Classification", "Data Categorisation"]
status: draft
sources: ["https://www.databricks.com/blog/enterprise-data-governance-complete-modern-framework", "https://learn.microsoft.com/da-dk/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/govern-components"]
---

# Data Classification Service

**Definition.** Data Classification Service tags and categorises data assets by sensitivity and domain to drive access, protection, and retention policies.
**Also known as:** Data Tagging Service, Sensitivity Classification, Data Categorisation.

## Relationships
- Data Classification Service is defined in the Data & Analytics domain.
- Data Classification Service is derived from Metadata Catalog.
- Data Classification Service is related to Data Policy & Stewardship Service.

## Details
Data Classification Service scans and labels data assets with sensitivity tiers such as public, internal, confidential, and restricted, and with categories like PII, PCI cardholder data, or material non-public information. Classification can be rules-based, pattern-based, or machine-learning-assisted, applied at column or asset level and persisted as governed tags in the catalog. These tags then drive automated controls: masking and access policies for sensitive columns, encryption requirements, retention rules, and audit scoping. By making sensitivity machine-readable, classification lets a bank enforce least-privilege access and privacy regulation consistently at scale, and it provides the input that policy and stewardship workflows act upon.

## References
- [Databricks: Enterprise data governance framework](https://www.databricks.com/blog/enterprise-data-governance-complete-modern-framework)
- [Microsoft: Govern components for cloud-scale analytics](https://learn.microsoft.com/da-dk/azure/cloud-adoption-framework/scenarios/cloud-scale-analytics/govern-components)
