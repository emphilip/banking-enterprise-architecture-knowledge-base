---
id: medallion-storage-layer
title: Medallion Storage Layer
type: technology-capability
domain: Data & Analytics
level: L3
aliases: ["Medallion Architecture", "Bronze-Silver-Gold Layers", "Curated Storage Zones"]
status: draft
sources: ["https://docs.databricks.com/aws/en/lakehouse-architecture/reference", "https://arxiv.org/pdf/2310.08697"]
---

# Medallion Storage Layer

**Definition.** Medallion Storage Layer organises lakehouse data into progressively curated bronze, silver, and gold zones to manage raw, cleansed, and business-ready data.
**Also known as:** Medallion Architecture, Bronze-Silver-Gold Layers, Curated Storage Zones.

## Relationships
- Medallion Storage Layer is defined in the Data & Analytics domain.
- Medallion Storage Layer is derived from Data Lakehouse Platform.
- Medallion Storage Layer is related to Data Mart Service.

## Details
Medallion Storage Layer is the canonical curation pattern inside a lakehouse: the bronze zone holds raw ingested data exactly as received for full auditability and replay; the silver zone holds cleansed, conformed, and de-duplicated entities after validation and joins; the gold zone holds aggregated, business-ready tables optimised for reporting and machine learning. Each promotion step incrementally improves data quality and structure, so failures can be reprocessed from an earlier layer without re-ingesting source systems. Because the layers are stored in open transactional table formats, the same medallion tables serve BI, ad-hoc SQL, and model training.

## References
- [Databricks Lakehouse architecture reference](https://docs.databricks.com/aws/en/lakehouse-architecture/reference)
- [The Data Lakehouse: a survey and experimental study (arXiv)](https://arxiv.org/pdf/2310.08697)
