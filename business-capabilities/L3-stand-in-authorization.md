---
id: stand-in-authorization
title: Stand-In Authorization
type: business-capability
domain: Cards
level: L3
aliases: ["STIP", "Stand-In Processing", "Fallback Authorization"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.emvco.com/specifications/"]
---

# Stand-In Authorization

**Definition.** Stand-In Authorization decisions transactions on the issuer's behalf when the host is unavailable, using EMV offline parameters and scheme stand-in within the BIAN Card Authorization service domain.
**Also known as:** STIP, Stand-In Processing, Fallback Authorization.

## Relationships
- Stand-In Authorization is defined in the Cards domain.
- Stand-In Authorization is derived from Card Authorization.
- Stand-In Authorization depends on the Card Processing capability.

## Details
When the issuer host times out or is offline, scheme stand-in processing (Visa STIP, Mastercard X-Code) applies issuer-supplied parameters — floor limits, velocity caps, hot-card lists and EMV offline data authentication (ODA/CDA) — to approve or decline against the BIAN Card Authorization service domain. Offline-approved transactions are queued and reconciled with the host on recovery, exposing the issuer to limited stand-in credit risk.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [EMVCo Specifications](https://www.emvco.com/specifications/)
