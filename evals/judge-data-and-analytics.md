# LLM-Judge Report — Data & Analytics (TECHNOLOGY-only run)

Scope: 22-file sample (16 technology sub-capabilities + 6 systems) from the decomposition of
Data Warehousing, Data Streaming, Analytics Platform, and Document Management.
Judge run date: 2026-06-17. All 22 paths exist; none skipped.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|------|----------|----------|-----|--------|------|-------|
| technology-capabilities/data-lakehouse-platform.md | 5 | 5 | 5 | 5 | 5 | Accurate ACID/open-table-format/time-travel definition matches Databricks reference; derived_from Data Warehousing (L1) sensible; related-to Cloud DW & Distributed Query Engine correct grain. |
| technology-capabilities/cloud-data-warehouse.md | 5 | 4 | 5 | 5 | 5 | MPP/columnar/separated compute-storage correct; Snowflake/BigQuery/Redshift named — well-known but only generically sourced (AWS+erwin blogs), defensible. derived_from Data Warehousing sound. |
| technology-capabilities/elt-pipeline-engine.md | 5 | 5 | 5 | 5 | 4 | ELT vs ETL inversion accurate to cited AWS/Azure design-pattern sources; depends_on Cloud Data Warehouse correct direction; slight scope overlap with Data Transformation Framework but related-to is appropriate. |
| technology-capabilities/semantic-layer-service.md | 5 | 4 | 5 | 5 | 5 | Governed-metrics/single-definition framing matches IBM source; AtScale "universal semantic layer" plausible but AtScale homepage is thin support. derived_from Data Warehousing sensible. |
| technology-capabilities/event-streaming-bus.md | 5 | 5 | 5 | 5 | 5 | Partitioned append-only log, offsets, consumer groups, replication all match Confluent/Event Hubs docs; derived_from Data Streaming; related-to Connector Framework & Schema Registry apt. |
| technology-capabilities/stream-processing-engine.md | 5 | 5 | 5 | 5 | 5 | Topology/event-time/watermarks/exactly-once accurate to Kafka Streams arch; depends_on Event Streaming Bus correct direction; related-to Stateful Stream Processor correct. |
| technology-capabilities/change-data-capture-service.md | 5 | 4 | 5 | 5 | 5 | Log-based vs query-based CDC, before/after images, Debezium accurate; sources are reputable-but-secondary (Estuary blog, dev.to) — claims are standard CDC facts, acceptable. depends_on Event Streaming Bus right. |
| technology-capabilities/bi-and-reporting-service.md | 5 | 4 | 5 | 5 | 4 | Consumption-tier/pushdown/RLS framing correct; derived_from Analytics Platform sound; depends_on Semantic Layer Service correct. Some overlap with Dashboarding Service, handled via related-to. |
| technology-capabilities/olap-cube-engine.md | 5 | 4 | 5 | 5 | 5 | MDX/SSAS/pre-aggregation and "logical OLAP" pushdown accurate; AtScale homepage thin but claim standard. derived_from Analytics Platform; related-to Semantic Layer & BI sensible. |
| technology-capabilities/content-repository.md | 5 | 4 | 5 | 5 | 5 | Metadata-driven ECM store, versioning, check-in/out, audit accurate to M-Files/Box; derived_from Document Management; related-to Archival & Records correct. |
| technology-capabilities/records-management-service.md | 5 | 5 | 5 | 5 | 5 | DoD 5015.2, ISO 15489, SEC 17a-4 all verified accurate; depends_on Content Repository correct direction; hands preservation to Archival & Retention — clean boundary. |
| technology-capabilities/reference-data-management.md | 5 | 5 | 5 | 5 | 5 | ISO 4217/3166, slowly-changing code sets, effective dating, stewardship accurate; derived_from Master Data Management is a sensible parent (reference data is an MDM sub-domain). |
| technology-capabilities/medallion-storage-layer.md | 5 | 5 | 5 | 5 | 5 | Bronze/silver/gold curation accurate to Databricks + arXiv survey; L3 derived_from Data Lakehouse Platform (L2) correct hierarchy; atomic curation-pattern grain fits L3. |
| technology-capabilities/stateful-stream-processor.md | 5 | 5 | 5 | 5 | 5 | Keyed state stores, changelog-backed exactly-once, tumbling/hopping/session windows accurate to Kafka Streams docs; L3 derived_from Stream Processing Engine (L2) correct. |
| technology-capabilities/natural-language-query-service.md | 5 | 4 | 5 | 5 | 5 | NL->query, ThoughtSpot pioneer, LLM-on-semantic-layer grounding accurate; sources are BI-roundup blogs (generic) but claims sound. L3 derived_from Self-Service Analytics (L2); depends_on Semantic Layer correct. |
| technology-capabilities/intelligent-document-recognition.md | 5 | 4 | 5 | 5 | 5 | OCR + ML classification/field extraction, confidence routing to human review accurate (IDP); sources Newgen/TechTarget acceptable. L3 derived_from Content Capture Service (L2); depends_on Content Repository correct. |
| systems/legacy/sap-businessobjects.md | 5 | 4 | 4 | 5 | 5 | BOBJ universe/WebIntelligence/Crystal Reports accurate; single SAP source. No supersedes/superseded_by present (Tableau declares the reverse), so the legacy note relies on the modern note for the pairing — acceptable, slightly thin relationships. |
| systems/legacy/informatica-powercenter.md | 5 | 4 | 4 | 5 | 5 | Mid-tier mapping-based ETL accurate; single Informatica source. No superseded_by edge (dbt declares supersedes from the modern side); relationships terse but correct. |
| systems/modern/tableau.md | 5 | 5 | 5 | 5 | 5 | Salesforce ownership and long-running Gartner Leader status verified; supersedes SAP BusinessObjects is same-capability (enterprise BI) — correct. |
| systems/modern/collibra.md | 5 | 4 | 5 | 5 | 5 | Catalog/glossary/lineage/DQ/governance + BCBS 239/CCAR/FRTB plausible; vendor page 403 (not fetchable) but claims standard. supersedes Informatica Axon is same-capability (data governance); Axon is EOL/replaced by Informatica CDGC, banks migrate to Collibra — sensible. |
| systems/modern/dbt.md | 5 | 5 | 5 | 5 | 5 | SQL-in-warehouse transform, Core vs Cloud, tests/lineage accurate; supersedes Informatica PowerCenter — same-capability (the transform tier of ETL/ELT), correct framing. |
| systems/modern/microsoft-sharepoint.md | 5 | 4 | 5 | 5 | 5 | Libraries/versioning/metadata/retention-labels/workflow accurate; single MS source. supersedes IBM FileNet is same-capability (document/content management) — sensible. |

## Per-dimension means (n=22)

| dimension | mean |
|-----------|------|
| Definitional accuracy | 5.00 |
| Groundedness | 4.36 |
| Relationship sensibility | 4.86 |
| Canonical-naming fidelity | 5.00 |
| Granularity fit | 4.91 |

## Verdict

**PASS.**

- Every dimension mean is >= 4.0 (lowest is Groundedness at 4.36).
- No individual note scores < 3 on Groundedness or Relationship sensibility (minimum on either dimension is 4).
- All derived_from parents are sensible L1/L2 ancestors; all four supersedes edges (Tableau->BusinessObjects, dbt->PowerCenter, Collibra->Axon, SharePoint->FileNet) are same-capability and the targets exist in the legacy registry.
- All relationship objects use exact canonical registry names.

## Required fixes

None are gate-blocking. Optional quality improvements (not required for `done`):

- Groundedness hygiene: several vendor/product claims (Snowflake/BigQuery/Redshift in cloud-data-warehouse; AtScale "universal semantic layer" in semantic-layer-service and olap-cube-engine; ThoughtSpot in natural-language-query-service) lean on generic roundup blogs or thin vendor homepages. Add one primary vendor-doc citation each to lift Groundedness above 4.
- collibra.md cites a page that returns HTTP 403 to the fetcher; consider a stable, fetchable Collibra/regulatory source for the BCBS 239/CCAR/FRTB claim.
- Legacy systems sap-businessobjects.md and informatica-powercenter.md carry no explicit superseded_by edge; the supersession is only declared from the modern side. Consider adding the reciprocal edge for symmetry (cosmetic; relationship is still correct and traceable).
- Minor registry-wide note (outside this sample's scoring): data-warehousing.md lists alias "Lakehouse" while data-lakehouse-platform.md is a distinct L2 capability — potential alias collision worth deduping.
