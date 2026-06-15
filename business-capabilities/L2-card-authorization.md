---
id: card-authorization
title: Card Authorization
type: business-capability
domain: Cards
level: L2
aliases: ["Authorization"]
status: draft
---

# Card Authorization

**Definition.** Card Authorization is the business capability that evaluates and approves or declines card transactions in real time by checking funds, limits, and risk rules against the cardholder account. It corresponds to the BIAN Card Authorization service domain.
**Also known as:** Authorization.

## Relationships
- Card Authorization is defined in the Cards domain.
- Card Authorization is derived from Cards Management.
- Card Authorization depends on the Card Processing capability.

## Details
Card Authorization processes ISO 8583 and emerging ISO 20022 authorization messages from acquirers and networks within sub-second SLAs, applying balance checks, velocity rules, and real-time fraud scoring. Stand-in processing and configurable authorization rule engines are central, with cloud processors enabling programmable controls and just-in-time funding for fintech and embedded-finance programs.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Frameworks](https://www.apqc.org/process-frameworks)
