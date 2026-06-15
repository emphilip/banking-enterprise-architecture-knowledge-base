---
id: direct-debit-returns
title: Direct Debit Returns
type: business-capability
domain: Payments
level: L3
aliases: ["DD Returns", "Unpaids", "Indemnity Claims"]
status: draft
sources: ["https://gocardless.com/en-us/guides/posts/bacs-payments", "https://www.dwolla.com/updates/understanding-ach-return-process"]
---

# Direct Debit Returns

**Definition.** Direct Debit Returns processes unpaid items, rejections, refunds and indemnity claims arising after collection (e.g. Bacs ADDACS/ARUDD, SEPA returns), supporting the post-collection lifecycle of the BIAN Direct Debit service domain.
**Also known as:** DD Returns, Unpaids, Indemnity Claims.

## Relationships
- Direct Debit Returns is defined in the Payments domain.
- Direct Debit Returns is derived from Direct Debit Management.
- Direct Debit Returns depends on the Workflow Orchestration capability.

## Details
Direct Debit Returns grounds in the post-collection lifecycle of the BIAN Direct Debit service domain. It processes unpaid items, rejections, refunds and indemnity claims, including Bacs ADDACS/ARUDD and SEPA returns. Workflow handles the reason-code routing, customer notification and ledger adjustments.

## References
- [GoCardless Bacs Payments Guide](https://gocardless.com/en-us/guides/posts/bacs-payments)
- [Understanding the ACH Return Process](https://www.dwolla.com/updates/understanding-ach-return-process)
