---
id: provisional-credit-management
title: Provisional Credit Management
type: business-capability
domain: Cards
level: L4
aliases: ["Temporary Credit Handling", "Dispute Credit"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.ecfr.gov/current/title-12/chapter-X/part-1005"]
---

# Provisional Credit Management

**Definition.** Provisional Credit Management posts and recovers temporary cardholder credits during an open dispute, supporting the BIAN Card Case service domain.
**Also known as:** Temporary Credit Handling, Dispute Credit.

## Relationships
- Provisional Credit Management is defined in the Cards domain.
- Provisional Credit Management is derived from Chargeback Handling.
- Provisional Credit Management depends on the Core Banking Processing capability.

## Details
For debit-card error claims, Reg E (12 CFR 1005.11) requires the issuer to provide provisional credit within 10 business days if the investigation is not complete; this capability posts that credit to the cardholder ledger via core banking and reverses it if the dispute is resolved against the cardholder. It tracks the regulatory clocks (10/45/90-day windows) and links the credit to the BIAN Card Case so the financial position nets correctly on chargeback outcome.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [eCFR Regulation E, 12 CFR Part 1005](https://www.ecfr.gov/current/title-12/chapter-X/part-1005)
