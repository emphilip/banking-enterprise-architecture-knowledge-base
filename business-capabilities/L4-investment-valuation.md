---
id: investment-valuation
title: Investment Valuation
type: business-capability
domain: Wealth & Investments
level: L4
aliases: ["Pricing & Valuation (Investments)", "NAV Calculation"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.dtcc.com/-/media/Files/PDFs/T2/Accelerating-the-US-Securities-Settlement-Cycle-to-T1-December-1-2021.pdf"]
---

# Investment Valuation

**Definition.** Investment Valuation prices holdings using market and model inputs and strikes portfolio NAV and unit prices; it supports the BIAN Securities Position Management service domain.
**Also known as:** Pricing & Valuation (Investments), NAV Calculation.

## Relationships
- Investment Valuation is defined in the Wealth & Investments domain.
- Investment Valuation is derived from Portfolio Accounting.
- Investment Valuation depends on the Portfolio Management System capability.
- Investment Valuation depends on the Analytics Platform capability.

## Details
Investment Valuation applies a fair-value hierarchy: Level 1 quoted market prices for liquid securities, Level 2 observable inputs for thinly traded instruments, and Level 3 model-based marks for illiquid assets. It strikes daily net asset value (NAV) per the standard formula — assets minus liabilities divided by units outstanding — and feeds priced positions to the BIAN Securities Position Management service domain for performance and reporting.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [DTCC — Accelerating the US Securities Settlement Cycle to T+1](https://www.dtcc.com/-/media/Files/PDFs/T2/Accelerating-the-US-Securities-Settlement-Cycle-to-T1-December-1-2021.pdf)
