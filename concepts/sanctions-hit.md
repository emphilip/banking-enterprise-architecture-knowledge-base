---
id: sanctions-hit
title: Sanctions Hit
type: artifact
domain: Compliance & Financial Crime
aliases: ["Watchlist Match", "Sanctions Match Alert"]
status: draft
sources: ["https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/customer-screening/8.1.2.10.0/csoug/alert-decision.html"]
---

# Sanctions Hit

**Definition.** Sanctions Hit is the alert artifact raised when party or transaction data matches a sanctions or watchlist entry, requiring triage and resolution. Sanctions Hit holds the evidence used to confirm a true match versus a false positive and to drive blocking and reporting.
**Also known as:** Watchlist Match, Sanctions Match Alert.

## Relationships
- Sanctions Hit is related to the Compliance & Financial Crime domain.
- Sanctions Hit mentions Match Against Watchlist.
- Sanctions Hit mentions Resolve Sanctions Hit.

## Details
Sanctions Hit records the screened party or transaction, the matched list entry and source (e.g. an OFAC SDN or consolidated-list record, UN or EU list), the matched attributes (name, date of birth, address, identifiers), the fuzzy match score, the alert priority and the screening timestamp. During resolution it accumulates the triage decision, the analyst notes, the true-match/false-positive disposition reached on the preponderance standard, and the four-eyes approval. A confirmed hit drives blocking of the transaction or relationship and reporting to OFAC within 10 business days, with the full record retained for audit.

## References
- [OFAC SDN and sanctions lists](https://ofac.treasury.gov/sanctions-programs-and-country-information)
- [OFAC compliance guidance](https://ofac.treasury.gov/)
