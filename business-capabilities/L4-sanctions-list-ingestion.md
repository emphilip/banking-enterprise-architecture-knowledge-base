---
id: sanctions-list-ingestion
title: Sanctions List Ingestion
type: business-capability
domain: Compliance & Financial Crime
level: L4
aliases: ["List Ingestion", "SDN Loading"]
status: draft
sources: ["https://ofac.treasury.gov/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists", "https://ofac.treasury.gov/media/16331/download?inline"]
---

# Sanctions List Ingestion

**Definition.** Sanctions List Ingestion acquires, normalises and version-controls OFAC SDN, consolidated and other sanctions lists for screening, supporting the OFAC 2019 Framework internal-controls component.
**Also known as:** List Ingestion, SDN Loading.

## Relationships
- Sanctions List Ingestion is defined in the Compliance & Financial Crime domain.
- Sanctions List Ingestion is derived from Watchlist Management.
- Sanctions List Ingestion depends on the Data Governance capability.
- Sanctions List Ingestion depends on the Transaction Monitoring Platform capability.

## Details
OFAC publishes the Specially Designated Nationals (SDN) list and a separate Consolidated (non-SDN) list, updating them frequently and sometimes intraday; the EU and UN maintain parallel consolidated lists. Ingestion pulls each authority's machine-readable feed, parses entries (names, aliases, dates of birth, identifiers, programs), normalises transliterations, and version-controls the load so screening always runs against current designations. Because OFAC strict-liability penalties attach to dealings with newly listed parties, ingestion latency must be minimised and each load auditable.

## References
- [OFAC SDN list](https://ofac.treasury.gov/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists)
- [OFAC Framework for Compliance Commitments](https://ofac.treasury.gov/media/16331/download?inline)
