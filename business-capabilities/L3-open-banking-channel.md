---
id: open-banking-channel
title: Open Banking Channel
type: business-capability
domain: Channels & Engagement
level: L3
aliases: ["Third-Party Channel", "Embedded Banking Channel"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.oracle.com/financial-services/banking/digital-experience/"]
---

# Open Banking Channel

**Definition.** Open Banking Channel is the Channels & Engagement capability that exposes account and payment access to third-party providers and partner apps as a distinct engagement channel, realising the BIAN Customer Access Entitlement and Party Authentication service domains over open APIs.
**Also known as:** Third-Party Channel, Embedded Banking Channel.

## Relationships
- Open Banking Channel is defined in the Channels & Engagement domain.
- Open Banking Channel is derived from Digital Banking.
- Open Banking Channel depends on the API Management capability.
- Open Banking Channel depends on the Customer Identity capability.

## Details
Open Banking Channel implements the PSD2 access-to-account (XS2A) mandate, publishing Account Information (AISP) and Payment Initiation (PISP) APIs to licensed third parties. Standards bodies define the contract: the UK Open Banking Standard and the Berlin Group NextGenPSD2 framework specify the API shape, while payment messages align to ISO 20022. Access is gated by eIDAS QWAC/QSEAL certificates and SCA-backed customer consent, with consent dashboards mapping to BIAN Customer Access Entitlement. The channel must support redirect, decoupled and embedded SCA flows and meet PSD2 regulatory uptime and performance reporting.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [EBA PSD2 Access to Account](https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money)
- [Oracle Banking Digital Experience](https://www.oracle.com/financial-services/banking/digital-experience/)
