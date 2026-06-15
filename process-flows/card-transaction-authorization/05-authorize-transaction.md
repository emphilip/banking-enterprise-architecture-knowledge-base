---
id: authorize-transaction
title: Authorize Transaction
type: process-step
process: Card Transaction Authorization
order: 5
status: draft
sources: ["https://www.aciworldwide.com/emv-payments-transactions"]
---

# Authorize Transaction

**Definition.** Authorize Transaction decides approve or decline and places the authorization hold on the card account.

## Relationships
- Authorize Transaction is defined in the Card Transaction Authorization process.
- Authorize Transaction causes Return Authorization Response.
- Authorize Transaction depends on the Card Authorization capability.
- Authorize Transaction mentions Card Operations Analyst.

## Details
Authorize Transaction applies approve/decline policy to the risk score and limit decision, places the authorization hold with hold accuracy, and invokes scheme stand-in (STIP) when the issuer host is unavailable.

## References
- [EMV payments transactions](https://www.aciworldwide.com/emv-payments-transactions)
