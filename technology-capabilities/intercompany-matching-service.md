---
id: intercompany-matching-service
title: Intercompany Matching Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["IC Matching Service", "Intercompany Reconciliation (Consolidation)", "Group Matching Service"]
status: draft
sources: ["https://www.onestream.com/", "https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/index.html"]
---

# Intercompany Matching Service

**Definition.** Intercompany Matching Service matches and reconciles intercompany balances and transactions across group entities to identify mismatches ahead of elimination during consolidation.
**Also known as:** IC Matching Service, Intercompany Reconciliation (Consolidation), Group Matching Service.

## Relationships
- Intercompany Matching Service is defined in the Core Processing domain.
- Intercompany Matching Service is derived from Consolidation Engine.
- Intercompany Matching Service is related to Intercompany Accounting Service.

## Details
Intercompany Matching Service pairs the two sides of each intra-group relationship — the receivable booked by one entity against the payable booked by its counterparty — and flags differences in amount, currency or timing before group elimination. It applies matching tolerances and reason codes, produces an out-of-balance report by entity pair, and routes disputed differences for resolution so the consolidation does not carry unreconciled intercompany positions. EPM consolidation platforms such as OneStream and Oracle run this matching prior to posting the elimination entries. The matched data complements postings produced by Intercompany Accounting Service.

## References
- [OneStream platform](https://www.onestream.com/)
- [Oracle EPM consolidation documentation](https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/index.html)
