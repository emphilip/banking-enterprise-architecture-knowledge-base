---
id: pin-management
title: PIN Management
type: business-capability
domain: Cards
level: L3
aliases: ["PIN Services", "PIN Reset", "PIN Change"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.pcisecuritystandards.org/document_library/"]
---

# PIN Management

**Definition.** PIN Management issues, changes, resets and unblocks cardholder PINs subject to PIN-try limits, supporting the BIAN Issued Device Administration service domain.
**Also known as:** PIN Services, PIN Reset, PIN Change.

## Relationships
- PIN Management is defined in the Cards domain.
- PIN Management is derived from Card Lifecycle Management.
- PIN Management depends on the Card Processing capability.

## Details
The BIAN Issued Device Administration service domain governs PIN lifecycle while the cryptographic operations follow the PCI PIN Security Requirements: PINs are enciphered in an HSM as an ISO 9564 PIN block, never stored or transmitted in the clear, and verified by PVV or offline against the EMV chip. PIN-try counters trigger lock-out (a 38/75 "allowable PIN tries exceeded" decline), and online PIN change/unblock uses scheme key-management standards (TR-31, DUKPT).

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [PCI SSC Document Library (PIN Security)](https://www.pcisecuritystandards.org/document_library/)
