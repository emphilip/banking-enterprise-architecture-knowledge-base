---
id: watchlist-data-management
title: Watchlist Data Management
type: technology-capability
domain: AI & Automation
level: L3
aliases: ["List Management Service", "Reference List Manager", "Sanctions List Loader", "WorldCompliance Data"]
status: draft
sources: ["https://risk.lexisnexis.com/global/en/products/worldcompliance-data", "https://risk.lexisnexis.com/global/en/financial-services/financial-crime-compliance/watchlist-screening"]
---

# Watchlist Data Management

**Definition.** Watchlist Data Management is the technology sub-capability for ingestion, normalisation, deduplication and refresh of sanctions, PEP and adverse-media reference lists used by the screening engine.
**Also known as:** List Management Service, Reference List Manager, Sanctions List Loader, WorldCompliance Data.

## Relationships
- Watchlist Data Management is defined in the AI & Automation domain.
- Watchlist Data Management is derived from Watchlist Screening Engine.
- Watchlist Data Management depends on Data Governance.

## Details
Watchlist Data Management loads and maintains the reference data behind screening — official sanctions lists (OFAC SDN, EU, UN, HMT), PEP registers and commercial datasets such as LexisNexis WorldCompliance. It normalises records to a common schema, deduplicates entries, tracks list versions and effective dates, and triggers re-screening when lists change so screening always runs against current data. Data quality, provenance and access controls draw on the enterprise data governance capability, providing audit evidence of which list version produced each hit.

## References
- [LexisNexis WorldCompliance Data](https://risk.lexisnexis.com/global/en/products/worldcompliance-data)
- [LexisNexis Watchlist Screening](https://risk.lexisnexis.com/global/en/financial-services/financial-crime-compliance/watchlist-screening)
