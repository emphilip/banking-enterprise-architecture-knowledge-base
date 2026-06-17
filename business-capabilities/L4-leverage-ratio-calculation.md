---
id: leverage-ratio-calculation
title: Leverage Ratio Calculation
type: business-capability
domain: Finance & Treasury
level: L4
aliases: ["Leverage Exposure Measure", "LR Calculation", "Leverage Ratio"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d424.htm", "https://www.bis.org/publ/work586.pdf"]
---

# Leverage Ratio Calculation

**Definition.** Leverage Ratio Calculation computes the Basel III non-risk-based leverage exposure measure and ratio as a backstop to the risk-weighted capital requirements.
**Also known as:** Leverage Exposure Measure, LR Calculation, Leverage Ratio.

## Relationships
- Leverage Ratio Calculation is defined in the Finance & Treasury domain.
- Leverage Ratio Calculation is derived from RWA Calculation.
- Leverage Ratio Calculation depends on the Regulatory Reporting Engine capability.

## Details
Leverage Ratio Calculation divides Tier 1 capital by the total exposure measure — on-balance-sheet assets, derivative exposures (SA-CCR), securities-financing transactions and credit-conversion-adjusted off-balance-sheet items — to a Basel III minimum of 3% (with an additional G-SIB leverage buffer). Being non-risk-based, it constrains excessive balance-sheet growth regardless of risk weights and prevents under-capitalisation where RWA understates leverage. The capability assembles the exposure components and applies the prescribed netting and add-on rules.

## References
- [Basel III: Finalising post-crisis reforms (BCBS d424)](https://www.bis.org/bcbs/publ/d424.htm)
- [BIS working paper on the leverage ratio](https://www.bis.org/publ/work586.pdf)
