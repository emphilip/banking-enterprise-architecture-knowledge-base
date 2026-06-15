---
id: card-operations-analyst
title: Card Operations Analyst
type: role
domain: Cards
aliases: ["Card Auth Analyst", "Authorization Operations Analyst"]
status: draft
sources: ["https://www.aciworldwide.com/emv-payments-transactions", "https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html"]
---

# Card Operations Analyst

**Definition.** Card Operations Analyst is the role that runs real-time card authorization decisioning at the issuer, validating the cryptogram and PIN, checking limits, funds and fraud rules, and managing the authorization response, hold and downstream clearing and posting. Card Operations Analyst keeps the authorization path approving genuine transactions while declining risky ones within scheme timing.

**Also known as:** Card Auth Analyst, Authorization Operations Analyst.

## Relationships
- Card Operations Analyst is related to the Cards domain.
- Card Operations Analyst mentions Card Transaction Authorization.
- Card Operations Analyst mentions Receive Authorization Request.
- Card Operations Analyst mentions Authorize Transaction.
- Card Operations Analyst mentions Return Authorization Response.

## Details
Card Operations Analyst receives the Authorization Request routed from the acquirer via the scheme, validates the EMV ARQC and PIN/CVM, and checks the available credit limit or funds against the requested amount. The role applies velocity and fraud-scoring rules, decides approve or decline, places the authorization hold, and generates the ARPC response returned to the acquirer, including stand-in (STIP) handling when the issuer is unavailable. Card Operations Analyst later matches the cleared presentment to the hold and posts the transaction, monitoring interchange and posting accuracy.

## References
- https://www.aciworldwide.com/emv-payments-transactions
- https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html
