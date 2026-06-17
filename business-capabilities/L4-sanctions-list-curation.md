---
id: sanctions-list-curation
title: Sanctions List Curation
type: business-capability
domain: Compliance & Financial Crime
level: L4
aliases: ["List Quality Management", "Whitelist Management"]
status: draft
sources: ["https://ofac.treasury.gov/media/16331/download?inline", "https://ofac.treasury.gov/faqs"]
---

# Sanctions List Curation

**Definition.** Sanctions List Curation maintains internal good-guy lists, whitelists and list quality to control screening false positives, per the OFAC 2019 Framework internal-controls component.
**Also known as:** List Quality Management, Whitelist Management.

## Relationships
- Sanctions List Curation is defined in the Compliance & Financial Crime domain.
- Sanctions List Curation is derived from Watchlist Management.
- Sanctions List Curation depends on the Data Governance capability.
- Sanctions List Curation depends on the Transaction Monitoring Platform capability.

## Details
The OFAC Framework expects internal controls that keep screening effective and auditable. Curation governs good-guy lists (previously cleared true matches) and whitelists so recurring false positives are not re-alerted, while ensuring no genuinely sanctioned party is suppressed. It must account for the OFAC 50% Rule — entities owned 50% or more by blocked persons are themselves blocked even if unlisted — by maintaining derived entries. Every whitelist decision is documented and periodically re-reviewed against fresh list loads to avoid masking a new designation.

## References
- [OFAC Framework for Compliance Commitments](https://ofac.treasury.gov/media/16331/download?inline)
- [OFAC FAQs](https://ofac.treasury.gov/faqs)
