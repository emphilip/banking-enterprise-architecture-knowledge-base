---
id: push-notification-service
title: Push Notification Service
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Mobile Push Service", "APNs/FCM Gateway", "Push Dispatch Service"]
status: draft
sources: ["https://dev.to/matt_frank_usa/building-a-scalable-notification-system-push-email-and-sms-2ga6", "https://www.systemdesignhandbook.com/guides/design-a-notification-system/"]
---

# Push Notification Service

**Definition.** Push Notification Service delivers mobile and web push messages through platform gateways (APNs, FCM), managing device tokens, topics, and platform-specific payload formatting.
**Also known as:** Mobile Push Service, APNs/FCM Gateway, Push Dispatch Service.

## Relationships
- Push Notification Service is defined in the Integration & APIs domain.
- Push Notification Service is derived from Notification Services.
- Push Notification Service depends on Notification Template Manager.

## Details
Push Notification Service sends payloads to Apple Push Notification service (APNs) over HTTP/2 with token-based (JWT) authentication and to Firebase Cloud Messaging (FCM) for Android and web push, formatting platform-specific envelopes (aps alert/badge/sound versus FCM notification/data). It registers and refreshes device tokens, prunes invalid tokens on rejection, and supports topic-based fan-out. In banking it powers mobile-app alerts and step-up authentication prompts; token hygiene and per-platform priority flags keep time-sensitive security pushes reliably delivered.

## References
- [Building a scalable notification system](https://dev.to/matt_frank_usa/building-a-scalable-notification-system-push-email-and-sms-2ga6)
- [Design a notification system](https://www.systemdesignhandbook.com/guides/design-a-notification-system/)
