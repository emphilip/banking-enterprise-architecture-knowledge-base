---
id: funds-transfer-self-service
title: Funds Transfer Self-Service
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["Self-Service Transfers", "Move Money"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.oracle.com/financial-services/banking/digital-experience/"]
---

# Funds Transfer Self-Service

**Definition.** Funds Transfer Self-Service is the Channels & Engagement capability that lets customers initiate transfers, payees and scheduled payments through self-directed digital channels, fronting payment initiation from the BIAN Customer Workbench service domain.
**Also known as:** Self-Service Transfers, Move Money.

## Relationships
- Funds Transfer Self-Service is defined in the Channels & Engagement domain.
- Funds Transfer Self-Service is derived from Digital Self-Service.
- Funds Transfer Self-Service depends on the Digital Channel Platform capability.

## Details
Funds Transfer Self-Service surfaces BIAN Customer Workbench actions to initiate internal transfers, external payees and standing orders, handing the instruction to the Payment Initiation capability. Every payment requires PSD2 Strong Customer Authentication with dynamic linking of amount and payee, while transaction risk analysis can exempt low-risk trusted-beneficiary transfers. Confirmation of Payee / payee-name verification reduces misdirected-payment and authorised-push-payment fraud before the customer confirms. Limits, beneficiary cooling-off periods and step-up on new payees are the front-line fraud controls, with ISO 20022 used for the underlying channel-to-rail message.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [EBA PSD2 Strong Customer Authentication](https://www.eba.europa.eu/regulation-and-policy/payment-services-and-electronic-money)
- [Oracle Banking Digital Experience](https://www.oracle.com/financial-services/banking/digital-experience/)
