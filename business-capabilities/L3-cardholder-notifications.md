---
id: cardholder-notifications
title: Cardholder Notifications
type: business-capability
domain: Cards
level: L3
aliases: ["Card Alerts", "Transaction Alerts"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Cardholder Notifications

**Definition.** Cardholder Notifications delivers transaction alerts, statement-ready and security notices to cardholders across channels, supporting the BIAN Issued Device Administration and Card Billing and Payments service domains.
**Also known as:** Card Alerts, Transaction Alerts.

## Relationships
- Cardholder Notifications is defined in the Cards domain.
- Cardholder Notifications is derived from Card Lifecycle Management.
- Cardholder Notifications depends on the Notification Services capability.

## Details
This capability pushes real-time alerts off the authorization and clearing streams of the BIAN Card Billing and Payments and Issued Device Administration service domains: purchase alerts, declined-transaction and suspected-fraud notices, payment-due and minimum-payment reminders, and statement-ready notifications. Fraud alerts often request cardholder confirmation (one-time reply) to release or block an authorization, and delivery respects the cardholder's consented channels and E-SIGN electronic-disclosure preferences.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Frameworks](https://www.apqc.org/process-frameworks)
