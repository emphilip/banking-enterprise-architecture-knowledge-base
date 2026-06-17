---
id: authorization-response-and-hold
title: Authorization Response & Hold
type: business-process
level: sub-process
domain: Cards
aliases: ["Auth Response", "Hold Management"]
status: draft
sources: ["https://www.aciworldwide.com/emv-payments-transactions"]
---

# Authorization Response & Hold

**Definition.** Authorization Response & Hold generates the ARPC response, places/releases the authorization hold and routes the decision back to the acquirer (including stand-in).
**Also known as:** Auth Response, Hold Management.

## Relationships
- Authorization Response & Hold is derived from Card Transaction Authorization.
- Authorization Response & Hold is defined in the Cards domain.
- Authorization Response & Hold depends on the Card Authorization capability.

## Details
Authorization Response & Hold generates the ARPC cryptogram response, places or releases the authorization hold on the card account, and routes the decision back to the acquirer through the scheme, including scheme stand-in (STIP) when the issuer host is unavailable. Actors include the Card Operations Analyst.

## References
- [EMV payments transactions](https://www.aciworldwide.com/emv-payments-transactions)
