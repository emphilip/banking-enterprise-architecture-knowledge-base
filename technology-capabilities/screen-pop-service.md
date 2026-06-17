---
id: screen-pop-service
title: Screen Pop Service
type: technology-capability
domain: Channels & Engagement
level: L3
aliases: ["Screen Pop", "Contextual Pop"]
status: draft
sources: ["https://www.genesys.com/capabilities", "https://aws.amazon.com/connect/features/"]
---

# Screen Pop Service

**Definition.** Screen Pop Service is the technology sub-capability providing event-driven presentation of caller identity and context to the agent desktop on contact arrival.
**Also known as:** Screen Pop, Contextual Pop.

## Relationships
- Screen Pop Service is defined in the Channels & Engagement domain.
- Screen Pop Service is derived from Computer Telephony Integration.
- Screen Pop Service is related to Agent Desktop.

## Details
Screen Pop Service listens for the connect event and attached call data (ANI/DNIS, IVR-collected account number, authentication state), looks up the matching customer and case, and pushes that record to the agent's workspace the instant the interaction routes, eliminating manual search and re-authentication. It can deep-link to a specific case or task and pre-fill disposition. Built on the CTI event and data layer, Genesys and Amazon Connect deliver screen pop into embedded CRM and agent desktops.

## References
- [Genesys capabilities](https://www.genesys.com/capabilities)
- [Amazon Connect features](https://aws.amazon.com/connect/features/)
