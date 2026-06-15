---
id: authorization-request
title: Authorization Request
type: artifact
domain: Cards
aliases: ["Auth Request Message", "ISO 8583 Auth Request"]
status: draft
sources: ["https://dpogroup.com/blog/a-step-by-step-guide-to-the-emv-and-online-card-transaction-journey/", "https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html"]
---

# Authorization Request

**Definition.** Authorization Request is the real-time message (carrying the EMV ARQC) requesting issuer approval of a card transaction. Authorization Request is the input artifact that triggers the card-transaction-authorization flow at the issuer.

**Also known as:** Auth Request Message, ISO 8583 Auth Request.

## Relationships
- Authorization Request is related to the Cards domain.
- Authorization Request mentions Card Transaction Authorization.
- Authorization Request mentions Receive Authorization Request.

## Details
Authorization Request is typically an ISO 8583 message (MTI 0100/0200) carrying the PAN or device token, transaction amount and currency, merchant category code (MCC), acquirer and terminal identifiers, point-of-service entry mode and the EMV ARQC cryptogram with related chip data for issuer authentication. It is routed from the acquirer through the card scheme to the issuer, where the ARQC and PIN/CVM are validated and limit, funds, velocity and fraud checks run. Authorization Request drives the approve/decline decision and the authorization hold, and is later matched to the clearing presentment during posting.

## References
- https://dpogroup.com/blog/a-step-by-step-guide-to-the-emv-and-online-card-transaction-journey/
- https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html
