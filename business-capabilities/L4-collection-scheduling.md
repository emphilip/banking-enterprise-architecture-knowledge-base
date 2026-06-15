---
id: collection-scheduling
title: Collection Scheduling
type: business-capability
domain: Payments
level: L4
aliases: ["DD Scheduling", "Collection Runs"]
status: draft
sources: ["https://www.modulrfinance.com/blog-insights/what-is-bacs", "https://developer.huntington.com/enterprisepayments/docs/iso-pain008"]
---

# Collection Scheduling

**Definition.** Collection Scheduling sequences and submits direct debit collection batches to scheme cut-offs (e.g. Bacs three-day cycle, SEPA pre-notification), supporting the collection processing of the BIAN Direct Debit service domain.
**Also known as:** DD Scheduling, Collection Runs.

## Relationships
- Collection Scheduling is defined in the Payments domain.
- Collection Scheduling is derived from Direct Debit Collection.
- Collection Scheduling depends on the Payment Orchestration capability.

## Details
Collection Scheduling grounds in the collection processing of the BIAN Direct Debit service domain. It sequences and submits direct debit collection batches to scheme cut-offs, including the Bacs three-day cycle and SEPA pre-notification windows. It plans collection runs to meet scheme timing rules.

## References
- [What is Bacs](https://www.modulrfinance.com/blog-insights/what-is-bacs)
- [ISO pain.008 Reference](https://developer.huntington.com/enterprisepayments/docs/iso-pain008)
