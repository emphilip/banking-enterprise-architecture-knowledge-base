---
id: legacy-notification-gateway
title: Legacy Notification Gateway
type: legacy-system
domain: Integration & APIs
maturity: legacy
aliases: ["On-Prem SMS Gateway", "SMPP Gateway", "Legacy SMS Gateway"]
status: draft
sources: ["https://en.wikipedia.org/wiki/SMS_gateway"]
---

# Legacy Notification Gateway

**Definition.** Legacy Notification Gateway is a generic on-premises or carrier-connected multi-channel notification gateway (SMS and email) representing pre-cloud outbound customer messaging based on SMPP and SMTP for alerting, OTP, and statement notices.
**Also known as:** On-Prem SMS Gateway, SMPP Gateway, Legacy SMS Gateway.

## Relationships
- Notification Services depends on Legacy Notification Gateway.
- Legacy Notification Gateway is related to Legacy Online Banking.

## Details
A Legacy Notification Gateway category describes self-hosted messaging infrastructure that connects to mobile carriers over the SMPP protocol and to mail servers over SMTP to deliver outbound notifications. Banks historically used such gateways for transaction alerts, one-time passwords, and statement notices. Cloud communications and engagement platforms increasingly replace these fixed-capacity, carrier-bound deployments.

## References
- [SMS gateway (Wikipedia)](https://en.wikipedia.org/wiki/SMS_gateway)
- [Short Message Peer-to-Peer (Wikipedia)](https://en.wikipedia.org/wiki/Short_Message_Peer-to-Peer)
