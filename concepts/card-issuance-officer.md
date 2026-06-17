---
id: card-issuance-officer
title: Card Issuance Officer
type: role
domain: Cards
aliases: ["Card Issuing Officer", "Card Operations Officer"]
status: draft
sources: ["https://dashdevs.com/blog/card-issuing/", "https://www.korahq.com/blog/build-a-card-issuing-program"]
---

# Card Issuance Officer

**Definition.** Card Issuance Officer is the operations role that owns the issuing journey for a payment card, from application decisioning and credit-limit assignment through credential generation, personalisation, fulfilment, activation and wallet provisioning. Card Issuance Officer is accountable for delivering an active, usable card to the cardholder under PCI DSS controls.

**Also known as:** Card Issuing Officer, Card Operations Officer.

## Relationships
- Card Issuance Officer is related to the Cards domain.
- Card Issuance Officer mentions Card Issuance.
- Card Issuance Officer mentions Capture Card Application.
- Card Issuance Officer mentions Activate Card.

## Details
Card Issuance Officer captures the Card Account Application, runs KYC and credit/eligibility decisioning, and assigns the credit limit before instructing production. The role oversees PAN/credential generation, EMV personalisation and secure fulfilment (physical mail or virtual/token delivery), then authenticates the cardholder at activation and provisions the card into digital wallets via network tokenisation. Card Issuance Officer applies card-scheme and PCI DSS PAN-protection controls throughout and confirms the Card Issued Event so downstream servicing, statementing and authorization can begin.

## References
- https://dashdevs.com/blog/card-issuing/
- https://www.korahq.com/blog/build-a-card-issuing-program
