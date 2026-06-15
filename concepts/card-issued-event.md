---
id: card-issued-event
title: Card Issued Event
type: event
domain: Cards
aliases: ["Card Activated Event", "Card Provisioned Event"]
status: draft
sources: ["https://dashdevs.com/blog/card-issuing/", "https://www.zeta.tech/us/resources/blog/demystifying-tokenized-card-payments/"]
---

# Card Issued Event

**Definition.** Card Issued Event is the business event signalling that a payment card has been activated and is ready for use. Card Issued Event marks the completion of the card-issuance flow and the handover to authorization and ongoing card servicing.

**Also known as:** Card Activated Event, Card Provisioned Event.

## Relationships
- Card Issued Event is related to the Cards domain.
- Card Issued Event mentions Card Issuance.
- Card Issued Event causes Activate Card.

## Details
Card Issued Event fires when Activate Card completes cardholder authentication and enables the card, carrying the card identifier (tokenised PAN reference), product code, activation timestamp and wallet-provisioning status. Card Issued Event signals that personalisation and secure fulfilment finished and that the card may now generate Authorization Requests. Downstream systems consume Card Issued Event to enrol the card in statement cycles, start the card lifecycle clock and open the authorization profile, and it confirms to the cardholder that any provisioned wallet tokens are live.

## References
- https://dashdevs.com/blog/card-issuing/
- https://www.zeta.tech/us/resources/blog/demystifying-tokenized-card-payments/
