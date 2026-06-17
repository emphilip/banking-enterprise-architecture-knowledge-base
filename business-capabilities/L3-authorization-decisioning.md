---
id: authorization-decisioning
title: Authorization Decisioning
type: business-capability
domain: Cards
level: L3
aliases: ["Authorization Approval", "Auth Decisioning"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.iso.org/standard/31628.html"]
---

# Authorization Decisioning

**Definition.** Authorization Decisioning approves or declines real-time card transaction requests against balance, status and risk parameters, realising the BIAN Card Authorization service domain.
**Also known as:** Authorization Approval, Auth Decisioning.

## Relationships
- Authorization Decisioning is defined in the Cards domain.
- Authorization Decisioning is derived from Card Authorization.
- Authorization Decisioning depends on the Card Processing capability.

## Details
The BIAN Card Authorization service domain receives the ISO 8583 0100/0200 authorization request from the scheme, evaluates open-to-buy, card status, EMV cryptogram (ARQC) validity and risk score, and returns a 0110 response with an action code (e.g. 00 approve, 05 do not honor, 51 insufficient funds). Decisions occur within scheme response-time windows and place a hold on available funds before clearing.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [ISO 8583 Financial transaction card messaging](https://www.iso.org/standard/31628.html)
