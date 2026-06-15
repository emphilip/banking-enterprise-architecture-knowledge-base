---
id: clearing-message
title: Clearing Message
type: artifact
domain: Payments
aliases: ["Pacs.008 Message", "ACH Entry"]
status: draft
sources: ["https://www.iso20022payments.com/cbpr/pacs-008-serial-method/"]
---

# Clearing Message

**Definition.** Clearing Message is the rail-specific interbank payment message, such as a Nacha entry, an ISO 20022 pacs.008 or a Fedwire-format message. Clearing Message is the artifact produced for transmission to a clearing operator in payment processing.

**Also known as:** Pacs.008 Message, ACH Entry.

## Relationships
- Clearing Message is related to the Payments domain.
- Clearing Message mentions Format Clearing Message.
- Clearing Message mentions Submit To Clearing.
- Clearing Message is related to Clearing Submission.
- Clearing Message is related to ISO 20022.

## Details
Clearing Message is built when a routed payment is transformed into the format required by the selected rail. The artifact is then transmitted, within cut-off windows, to the ACH operator, Fedwire or instant-payment network, with message integrity controls ensuring the interbank message is well-formed and complete.

## References
- https://www.iso20022payments.com/cbpr/pacs-008-serial-method/
