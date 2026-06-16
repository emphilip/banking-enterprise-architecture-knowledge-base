---
id: trading-book-risk
title: Trading Book Risk
type: business-capability
domain: Risk Management
level: L3
aliases: ["Trading Book Capital", "FRTB Boundary Management"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d457.htm", "https://bian.org/servicelandscape/"]
---

# Trading Book Risk

**Definition.** Trading Book Risk manages the boundary, risk factors and capital of trading-book positions, including the sensitivities-based method and default risk charge, defined by the Basel FRTB framework and the BIAN Position Keeping service domain.
**Also known as:** Trading Book Capital, FRTB Boundary Management.

## Relationships
- Trading Book Risk is defined in the Risk Management domain.
- Trading Book Risk is derived from Market Risk Management.
- Trading Book Risk depends on the Risk Analytics Engine capability.
- Trading Book Risk depends on the Risk Data Aggregation capability.

## Details
Trading Book Risk enforces the FRTB (d457) trading-book/banking-book boundary, restricting reclassification between books and imposing capital charges on internal risk transfers. It administers desk structure for the Internal Models Approach, runs the desk-level eligibility tests (P&L attribution test and backtesting), and falls desks back to the Standardised Approach on failure. Capital combines the sensitivities-based method, default risk charge and residual risk add-on, with capital surcharges for non-modellable risk factors.

## References
- [Basel FRTB — Minimum Capital Requirements for Market Risk (d457)](https://www.bis.org/bcbs/publ/d457.htm)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
