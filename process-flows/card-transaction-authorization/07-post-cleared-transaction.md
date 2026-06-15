---
id: post-cleared-transaction
title: Post Cleared Transaction
type: process-step
process: Card Transaction Authorization
order: 7
status: draft
sources: ["https://www.marqeta.com/blog/card-program-clearing-and-settlement-how-issuer-processors-manage-fund-flow"]
---

# Post Cleared Transaction

**Definition.** Post Cleared Transaction matches the cleared presentment to the hold and posts the transaction to the cardholder account.

## Relationships
- Post Cleared Transaction is defined in the Card Transaction Authorization process.
- Post Cleared Transaction depends on the Core Banking Processing capability.
- Post Cleared Transaction mentions Card Operations Analyst.

## Details
Post Cleared Transaction matches the cleared presentment to the original authorization hold, applies interchange and posts the transaction with auth-to-clearing matching and posting accuracy controls. This is the final step of Card Transaction Authorization.

## References
- [Clearing and settlement fund flow](https://www.marqeta.com/blog/card-program-clearing-and-settlement-how-issuer-processors-manage-fund-flow)
