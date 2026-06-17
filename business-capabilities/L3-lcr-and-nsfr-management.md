---
id: lcr-and-nsfr-management
title: LCR & NSFR Management
type: business-capability
domain: Risk Management
level: L3
aliases: ["Liquidity Ratio Management", "HQLA Management"]
status: draft
sources: ["https://www.bis.org/publ/bcbs238.htm", "https://www.bis.org/publ/bcbs295.htm"]
---

# LCR & NSFR Management

**Definition.** LCR & NSFR Management calculates and steers the Liquidity Coverage Ratio and Net Stable Funding Ratio, managing HQLA and stable-funding composition, defined by the Basel III liquidity standards.
**Also known as:** Liquidity Ratio Management, HQLA Management.

## Relationships
- LCR & NSFR Management is defined in the Risk Management domain.
- LCR & NSFR Management is derived from Liquidity Risk Management.
- LCR & NSFR Management depends on the Risk Analytics Engine capability.
- LCR & NSFR Management depends on the Risk Data Aggregation capability.

## Details
LCR & NSFR Management computes the Basel LCR (BCBS d238) — stock of HQLA divided by total net cash outflows over a 30-day stress, required to be at least 100% — applying Level 1, Level 2A and Level 2B asset haircuts and the 40%/15% caps. It also computes the NSFR (BCBS d295) as available stable funding over required stable funding, also floored at 100% over a one-year horizon. The capability manages buffer composition, run-off and inflow assumptions, and intraday steering of the ratios.

## References
- [BCBS Liquidity Coverage Ratio (bcbs238)](https://www.bis.org/publ/bcbs238.htm)
- [BCBS Net Stable Funding Ratio (bcbs295)](https://www.bis.org/publ/bcbs295.htm)
