---
id: transaction-reversal-handling
title: Transaction Reversal Handling
type: business-capability
domain: Deposits & Accounts
level: L4
aliases: ["Entry Reversal", "Posting Correction"]
status: draft
sources: ["https://www.openriskmanual.org/wiki/Category:BIAN_Service_Domain", "https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.11"]
---

# Transaction Reversal Handling

**Definition.** Transaction Reversal Handling processes corrections, returns and reversals of posted entries, supporting the adjustment behaviour of the BIAN Current Account and Account Reconciliation service domains.
**Also known as:** Entry Reversal, Posting Correction.

## Relationships
- Transaction Reversal Handling is defined in the Deposits & Accounts domain.
- Transaction Reversal Handling is derived from Transaction Posting.
- Transaction Reversal Handling depends on the Transaction Posting Engine capability.

## Details
The BIAN Current Account/Account Reconciliation adjustment behaviour books reversing entries; ACH reversals and returns must follow Nacha Operating Rules timeframes (e.g. consumer return within 60 days), and disputed EFT errors are corrected under Regulation E (12 CFR 1005.11).

## References
- [BIAN Service Domain](https://www.openriskmanual.org/wiki/Category:BIAN_Service_Domain)
- [Regulation E 12 CFR 1005.11](https://www.ecfr.gov/current/title-12/chapter-X/part-1005/section-1005.11)
