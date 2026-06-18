---
id: email-delivery-service
title: Email Delivery Service
type: technology-capability
domain: Integration & APIs
level: L2
aliases: ["Transactional Email Service", "Email Dispatch Service", "SMTP Delivery Service"]
status: draft
sources: ["https://dev.to/sgchris/designing-a-notification-system-push-email-and-sms-at-scale-kio", "https://codelit.io/blog/notification-system-architecture"]
---

# Email Delivery Service

**Definition.** Email Delivery Service dispatches transactional and bulk email via SMTP or provider APIs (e.g. SendGrid), managing sender reputation, bounce handling, and deliverability.
**Also known as:** Transactional Email Service, Email Dispatch Service, SMTP Delivery Service.

## Relationships
- Email Delivery Service is defined in the Integration & APIs domain.
- Email Delivery Service is derived from Notification Services.
- Email Delivery Service depends on Notification Template Manager.

## Details
Email Delivery Service relays messages over SMTP or provider REST APIs and authenticates sending domains with SPF, DKIM signing, and DMARC alignment to maximize inbox placement and prevent spoofing. It processes asynchronous bounce, complaint, and unsubscribe feedback (including feedback loops), suppresses bad addresses, and warms IP reputation for bulk sends. In banking it delivers statements, confirmations, and alerts; DKIM-signed, DMARC-aligned mail and bounce suppression protect the bank's sending reputation and reduce phishing impersonation risk.

## References
- [Designing a notification system at scale](https://dev.to/sgchris/designing-a-notification-system-push-email-and-sms-at-scale-kio)
- [Notification system architecture](https://codelit.io/blog/notification-system-architecture)
