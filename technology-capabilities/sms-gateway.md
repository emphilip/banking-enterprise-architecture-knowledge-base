---
id: sms-gateway
title: SMS Gateway
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Text Messaging Gateway", "SMS Provider Adapter", "Mobile Messaging Gateway"]
status: draft
sources: ["https://www.courier.com/blog/what-is-the-twilio-messaging-api", "https://codelit.io/blog/notification-system-architecture"]
---

# SMS Gateway

**Definition.** SMS Gateway integrates with telecom carriers and aggregators (e.g. Twilio) to send and receive text messages, handling number provisioning, encoding, and carrier delivery semantics.
**Also known as:** Text Messaging Gateway, SMS Provider Adapter, Mobile Messaging Gateway.

## Relationships
- SMS Gateway is defined in the Integration & APIs domain.
- SMS Gateway is derived from Notification Services.
- SMS Gateway depends on Notification Template Manager.

## Details
SMS Gateway abstracts carrier and aggregator connectivity behind a common send API, mapping to SMPP or provider REST APIs such as Twilio Messaging. It manages sender identities (long codes, short codes, alphanumeric sender IDs), GSM-7 versus UCS-2 encoding and multipart concatenation for long messages, and processes delivery-receipt (DLR) callbacks. In banking it sends one-time passcodes and transaction alerts where low latency and high deliverability matter, applying per-country routing and opt-out handling for regulatory compliance.

## References
- [Twilio Messaging API explained](https://www.courier.com/blog/what-is-the-twilio-messaging-api)
- [Notification system architecture](https://codelit.io/blog/notification-system-architecture)
