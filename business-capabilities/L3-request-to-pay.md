---
id: request-to-pay
title: Request To Pay
type: business-capability
domain: Payments
level: L3
aliases: ["Request for Payment", "RfP", "RTP Request"]
status: draft
sources: ["https://www.iso20022.org/catalogue-messages/iso-20022-messages-archive?search=pain.013", "https://www.aciworldwide.com/fednow"]
---

# Request To Pay

**Definition.** Request To Pay enables a payee to send a structured request for payment to a payer who can accept or decline it, supporting ISO 20022 pain.013/pain.014 and the request-for-payment overlays on RTP and FedNow.
**Also known as:** Request for Payment, RfP, RTP Request.

## Relationships
- Request To Pay is defined in the Payments domain.
- Request To Pay is derived from Payment Initiation.
- Request To Pay depends on the API Management capability.

## Details
Request To Pay grounds in the BIAN Payment Order service domain and the request-for-payment overlays on instant rails. It supports ISO 20022 pain.013 and pain.014 messaging, letting payees solicit payments that payers can accept or decline. It underpins overlays on RTP and FedNow.

## References
- [ISO 20022 pain.013/pain.014 (Request to Pay)](https://www.iso20022.org/catalogue-messages/iso-20022-messages-archive?search=pain.013)
- [ACI FedNow](https://www.aciworldwide.com/fednow)
