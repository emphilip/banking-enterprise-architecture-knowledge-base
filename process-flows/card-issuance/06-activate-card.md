---
id: activate-card
title: Activate Card
type: process-step
process: Card Issuance
order: 6
status: draft
sources: ["https://dashdevs.com/blog/card-issuing/"]
---

# Activate Card

**Definition.** Activate Card authenticates the cardholder and activates the card for use, emitting the Card Issued Event.

## Relationships
- Activate Card is defined in the Card Issuance process.
- Activate Card causes Provision Wallet Token.
- Activate Card depends on the Card Processing capability.
- Activate Card mentions Card Issued Event.
- Activate Card mentions Card Issuance Officer.

## Details
Activate Card authenticates the cardholder via activation controls and enables the delivered card for transactions, raising the Card Issued Event.

## References
- [Card issuing overview](https://dashdevs.com/blog/card-issuing/)
