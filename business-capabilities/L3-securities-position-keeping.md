---
id: securities-position-keeping
title: Securities Position Keeping
type: business-capability
domain: Wealth & Investments
level: L3
aliases: ["Position Management (Securities)", "Holdings Keeping"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.dtcc.com/-/media/Files/PDFs/T2/Accelerating-the-US-Securities-Settlement-Cycle-to-T1-December-1-2021.pdf"]
---

# Securities Position Keeping

**Definition.** Securities Position Keeping maintains real-time and end-of-day securities positions, holdings, and movements across accounts; it is realised through the BIAN Securities Position Management service domain.
**Also known as:** Position Management (Securities), Holdings Keeping.

## Relationships
- Securities Position Keeping is defined in the Wealth & Investments domain.
- Securities Position Keeping is derived from Brokerage & Trading.
- Securities Position Keeping depends on the Order Management System capability.
- Securities Position Keeping depends on the Core Banking Processing capability.

## Details
The BIAN Securities Position Management service domain tracks holdings and movements per account. Securities Position Keeping maintains positions on both a trade-date and settlement-date basis, applies executions and corporate-action adjustments intraday, and supplies the netting input DTCC's NSCC needs. Under the US T+1 cycle, positions must be accurate within one business day of trade date to support timely settlement and margining.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [DTCC — Accelerating the US Securities Settlement Cycle to T+1](https://www.dtcc.com/-/media/Files/PDFs/T2/Accelerating-the-US-Securities-Settlement-Cycle-to-T1-December-1-2021.pdf)
