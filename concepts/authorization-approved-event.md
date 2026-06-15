---
id: authorization-approved-event
title: Authorization Approved Event
type: event
domain: Cards
aliases: ["Auth Approved Event", "Authorization Granted Event"]
status: draft
sources: ["https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html", "https://www.aciworldwide.com/emv-payments-transactions"]
---

# Authorization Approved Event

**Definition.** Authorization Approved Event is the event signalling that a card authorization request has been approved and an authorization hold placed against the card account. Authorization Approved Event confirms the issuer's positive decision and triggers the response back to the acquirer and downstream clearing.

**Also known as:** Auth Approved Event, Authorization Granted Event.

## Relationships
- Authorization Approved Event is related to the Cards domain.
- Authorization Approved Event mentions Card Transaction Authorization.
- Authorization Approved Event causes Return Authorization Response.

## Details
Authorization Approved Event fires after Authorize Transaction decides approve and the hold is recorded, carrying the approval code, approved amount, hold reference, and the ARPC needed for issuer authentication of the response. Authorization Approved Event causes the ARPC to be generated and returned to the acquirer via the scheme, decrements the available limit/open-to-buy by the hold amount, and seeds the auth-to-clearing match used when the presentment later clears. Cardholder real-time notifications and spend-tracking systems also consume Authorization Approved Event.

## References
- https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html
- https://www.aciworldwide.com/emv-payments-transactions
