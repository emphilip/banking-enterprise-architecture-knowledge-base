---
id: direct-debit-collection
title: Direct Debit Collection
type: business-capability
domain: Payments
level: L3
aliases: ["Direct Debit Processing", "Creditor Collection"]
status: draft
sources: ["https://developer.huntington.com/enterprisepayments/docs/iso-pain008", "https://deepwiki.com/bian-official/public/5.1-payment-operations"]
---

# Direct Debit Collection

**Definition.** Direct Debit Collection submits creditor-side collection batches against valid mandates and initiates the pull payments (ISO 20022 pain.008, SEPA SDD, Bacs Direct Debit), realising the collection processing of the BIAN Direct Debit service domain.
**Also known as:** Direct Debit Processing, Creditor Collection.

## Relationships
- Direct Debit Collection is defined in the Payments domain.
- Direct Debit Collection is derived from Direct Debit Management.
- Direct Debit Collection depends on the Payment Orchestration capability.

## Details
Direct Debit Collection grounds in the collection processing of the BIAN Direct Debit service domain. It submits creditor-side collection batches against valid mandates and initiates the pull payments using ISO 20022 pain.008 across SEPA SDD and Bacs Direct Debit. It produces the collection instructions dispatched to the scheme.

## References
- [ISO pain.008 Reference](https://developer.huntington.com/enterprisepayments/docs/iso-pain008)
- [BIAN Payment Operations](https://deepwiki.com/bian-official/public/5.1-payment-operations)
