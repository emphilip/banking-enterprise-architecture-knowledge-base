---
id: self-service-ivr
title: Self-Service IVR
type: business-capability
domain: Channels & Engagement
level: L3
aliases: ["Voice Self-Service", "IVR Self-Service"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.cloudtalk.io/blog/ivr-in-banking/"]
---

# Self-Service IVR

**Definition.** Self-Service IVR is the Channels & Engagement capability that resolves enquiries and authenticates callers through interactive voice menus before or instead of agent handling, fronting the BIAN Party Authentication and Servicing Issue service domains in a voice self-service context.
**Also known as:** Voice Self-Service, IVR Self-Service.

## Relationships
- Self-Service IVR is defined in the Channels & Engagement domain.
- Self-Service IVR is derived from Contact Center.
- Self-Service IVR depends on the Conversational AI capability.

## Details
Self-Service IVR fronts BIAN Party Authentication and Servicing Issue in the voice channel: callers check balances, hear recent transactions, make payments and reset PINs through DTMF or natural-language menus without an agent. Caller verification follows FFIEC authentication expectations using PIN, OTP and increasingly voice biometrics, with step-up before any money movement. Conversational AI replaces rigid menu trees with intent recognition, raising containment (calls resolved without an agent) while passing recognised intent to Channel Interaction Routing for clean escalation. PCI DSS requires payment card entry in IVR to be handled with pause-and-resume or DTMF masking.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [FFIEC Authentication Guidance](https://www.ffiec.gov/guidance.htm)
- [IVR in Banking](https://www.cloudtalk.io/blog/ivr-in-banking/)
