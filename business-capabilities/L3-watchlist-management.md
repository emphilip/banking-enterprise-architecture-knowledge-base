---
id: watchlist-management
title: Watchlist Management
type: business-capability
domain: Compliance & Financial Crime
level: L3
aliases: ["List Management", "Sanctions List Management"]
status: draft
sources: ["https://ofac.treasury.gov/media/16331/download?inline", "https://ofac.treasury.gov/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists"]
---

# Watchlist Management

**Definition.** Watchlist Management ingests, curates and maintains sanctions, PEP and internal watchlists that feed screening, per the OFAC 2019 Framework for Compliance Commitments internal-controls component.
**Also known as:** List Management, Sanctions List Management.

## Relationships
- Watchlist Management is defined in the Compliance & Financial Crime domain.
- Watchlist Management is derived from AML Monitoring.
- Watchlist Management depends on the Data Governance capability.
- Watchlist Management depends on the Transaction Monitoring Platform capability.

## Details
The OFAC Framework's internal-controls component expects institutions to maintain current sanctions reference data so screening reflects the latest designations. OFAC's 50% Rule means any entity owned 50% or more, directly or indirectly, by one or more blocked persons is itself blocked even if not separately listed, so watchlists must support derived/ownership-based entries beyond the published SDN list. Watchlist Management governs ingestion of OFAC SDN, EU and UN consolidated lists, deduplication, and version control feeding Sanctions Screening.

## References
- [OFAC Framework for Compliance Commitments](https://ofac.treasury.gov/media/16331/download?inline)
- [OFAC SDN list](https://ofac.treasury.gov/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists)
