---
id: delivery-tracking-service
title: Delivery Tracking Service
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Notification Status Tracking", "Delivery Receipt Service", "Notification Lifecycle Tracker"]
status: draft
sources: ["https://codelit.io/blog/notification-system-architecture", "https://www.courier.com/blog/how-to-build-a-notification-center-for-web-and-mobile-apps"]
---

# Delivery Tracking Service

**Definition.** Delivery Tracking Service tracks each notification through its lifecycle (created, queued, sent, delivered, read), capturing receipts, opens, and failures, and driving retry handling.
**Also known as:** Notification Status Tracking, Delivery Receipt Service, Notification Lifecycle Tracker.

## Relationships
- Delivery Tracking Service is defined in the Integration & APIs domain.
- Delivery Tracking Service is derived from Notification Services.
- Delivery Tracking Service depends on Channel Preference Router.

## Details
Delivery Tracking Service maintains a per-message state machine and ingests asynchronous signals from each channel: SMS delivery receipts (DLRs), email bounce/open/click events, and push receipt callbacks, correlating them back to the originating notification by ID. It exposes status queries and webhooks, drives retry and fallback on transient failures, and writes an audit trail for compliance and customer-service lookups. In banking it proves whether a regulatory or security notification was delivered, and feeds analytics on channel reliability and engagement.

## References
- [Notification system architecture](https://codelit.io/blog/notification-system-architecture)
- [How to build a notification center](https://www.courier.com/blog/how-to-build-a-notification-center-for-web-and-mobile-apps)
