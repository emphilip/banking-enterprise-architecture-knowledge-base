---
id: channel-preference-router
title: Channel Preference Router
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Notification Routing Engine", "Preference-Based Router", "Channel Fan-Out Service"]
status: draft
sources: ["https://www.systemdesignhandbook.com/guides/design-a-notification-system/", "https://codelit.io/blog/notification-system-architecture"]
---

# Channel Preference Router

**Definition.** Channel Preference Router fans out notification events to the right channels based on subscriber preferences, consent, and priority, applying fallback strategies when a channel fails.
**Also known as:** Notification Routing Engine, Preference-Based Router, Channel Fan-Out Service.

## Relationships
- Channel Preference Router is defined in the Integration & APIs domain.
- Channel Preference Router is derived from Notification Services.
- Channel Preference Router depends on Notification Template Manager.

## Details
Channel Preference Router receives a logical notification event and resolves which channels to use by reading per-subscriber preferences, consent and opt-out state, quiet hours, and message priority, then dispatches to the SMS, email, and push delivery services. It supports escalation and fallback chains (for example, send push first, fall back to SMS if undelivered within a window) and deduplicates across channels. In banking it enforces consent and contactability rules so marketing respects opt-outs while critical security alerts still reach the customer through an available channel.

## References
- [Design a notification system](https://www.systemdesignhandbook.com/guides/design-a-notification-system/)
- [Notification system architecture](https://codelit.io/blog/notification-system-architecture)
