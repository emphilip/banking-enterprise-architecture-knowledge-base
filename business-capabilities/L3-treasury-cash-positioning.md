---
id: treasury-cash-positioning
title: Treasury Cash Positioning
type: business-capability
domain: Finance & Treasury
level: L3
aliases: ["Cash Position Keeping", "Nostro Positioning"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.bis.org/bcbs/publ/d248.htm"]
---

# Treasury Cash Positioning

**Definition.** Treasury Cash Positioning establishes and monitors the consolidated cash and nostro position across accounts and currencies, aligning to the BIAN Treasury and Position Keeping service domains.
**Also known as:** Cash Position Keeping, Nostro Positioning.

## Relationships
- Treasury Cash Positioning is defined in the Finance & Treasury domain.
- Treasury Cash Positioning is derived from Liquidity Management.
- Treasury Cash Positioning depends on the Analytics Platform capability.

## Details
Treasury Cash Positioning aggregates opening balances, intraday MT940/MT942 statements and expected flows into a real-time, multi-currency view of the bank's nostro and central-bank account positions so that treasury can sweep surpluses and cover shortfalls before cut-off. Accurate positioning is the basis for managing the BCBS intraday-liquidity monitoring tools (daily maximum liquidity usage, available intraday liquidity) and avoids costly overdraft or failed-settlement exposure on correspondent accounts.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [BCBS Monitoring tools for intraday liquidity management (d248)](https://www.bis.org/bcbs/publ/d248.htm)
