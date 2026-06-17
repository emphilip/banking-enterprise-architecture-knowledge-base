---
id: atm-authorization-handling
title: ATM Authorization Handling
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["ATM Auth Handling", "Terminal Authorization"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://en.wikipedia.org/wiki/ISO_8583"]
---

# ATM Authorization Handling

**Definition.** ATM Authorization Handling is the Channels & Engagement capability that validates PIN, balances and limits for ATM transactions and applies stand-in rules, fronting the BIAN Card Terminal Operations service domain and the issuer authorization flow.
**Also known as:** ATM Auth Handling, Terminal Authorization.

## Relationships
- ATM Authorization Handling is defined in the Channels & Engagement domain.
- ATM Authorization Handling is derived from ATM Transaction Processing.
- ATM Authorization Handling depends on the Card Processing capability.

## Details
ATM Authorization Handling fronts BIAN Card Terminal Operations and the issuer authorization flow: it verifies the EMV cryptogram and encrypted PIN block, formats an ISO 8583 authorization request, routes on-us or via interchange (Visa/Plus, Mastercard/Cirrus), and applies daily/per-transaction limit checks. PCI PIN security governs the encrypted PIN block and key hierarchy; EMV at the ATM validates the chip cryptogram to defeat counterfeit cards. When the issuer host is unreachable, stand-in (STIP) rules approve within risk limits to preserve availability, with later reconciliation. Declines and fraud holds are returned to the terminal with appropriate response codes.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [ISO 8583 Authorization Messaging](https://en.wikipedia.org/wiki/ISO_8583)
- [EMVCo Specifications](https://www.emvco.com/specifications/)
