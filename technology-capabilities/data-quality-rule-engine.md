---
id: data-quality-rule-engine
title: Data Quality Rule Engine
type: technology-capability
domain: Data & Analytics
level: L3
aliases: ["DQ Rule Engine", "Validation Rule Service", "Quality Rule Manager"]
status: draft
sources: ["https://www.actian.com/blog/data-governance/master-data-governance/", "https://www.informatica.com/resources/articles/master-data-governance-framework.html"]
---

# Data Quality Rule Engine

**Definition.** Data Quality Rule Engine defines, validates, and monitors business data-quality rules and thresholds, raising issues when validity, accuracy, or completeness breach targets.
**Also known as:** DQ Rule Engine, Validation Rule Service, Quality Rule Manager.

## Relationships
- Data Quality Rule Engine is defined in the Data & Analytics domain.
- Data Quality Rule Engine is derived from Data Quality Engine.
- Data Quality Rule Engine is related to Metadata Catalog.

## Details
Data Quality Rule Engine is the rule-authoring and execution sub-component of data quality management. Stewards express rules across the standard dimensions, completeness, validity, accuracy, consistency, uniqueness, and timeliness, as testable conditions with thresholds, for example "IBAN must pass check-digit validation" or "customer date-of-birth must be a plausible date." The engine runs these rules against datasets on schedule or in pipeline, scores conformance, and raises exceptions or remediation tasks when thresholds are breached. Results feed dashboards and trend tracking so quality is measured over time. As a child of the broader data quality engine, it focuses specifically on the definition and evaluation of validation rules rather than profiling or remediation workflow.

## References
- [Actian: Master data governance](https://www.actian.com/blog/data-governance/master-data-governance/)
- [Informatica: Master data governance framework](https://www.informatica.com/resources/articles/master-data-governance-framework.html)
