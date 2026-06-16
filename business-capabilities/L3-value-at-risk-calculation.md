---
id: value-at-risk-calculation
title: Value-at-Risk Calculation
type: business-capability
domain: Risk Management
level: L3
aliases: ["Expected Shortfall Calculation", "VaR/ES"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d457.htm", "https://www.bis.org/bcbs/publ/d352.pdf"]
---

# Value-at-Risk Calculation

**Definition.** Value-at-Risk Calculation computes VaR and expected shortfall on trading and banking-book positions over defined horizons and confidence levels, where the Basel FRTB internal models approach replaces 99% VaR with 97.5% expected shortfall.
**Also known as:** Expected Shortfall Calculation, VaR/ES.

## Relationships
- Value-at-Risk Calculation is defined in the Risk Management domain.
- Value-at-Risk Calculation is derived from Market Risk Management.
- Value-at-Risk Calculation depends on the Risk Analytics Engine capability.
- Value-at-Risk Calculation depends on the Analytics Platform capability.

## Details
Value-at-Risk Calculation runs historical, parametric and Monte-Carlo simulation to estimate potential loss. Under the FRTB Internal Models Approach (d457), the metric is a 97.5% expected shortfall calibrated to a stress period and scaled by liquidity horizons (10 to 120 days) per risk factor, with capital for non-modellable risk factors held separately. A 99%/1-day VaR is retained for regulatory backtesting against actual and hypothetical P&L. Outputs feed desk-level internal-model eligibility and limit monitoring.

## References
- [Basel FRTB — Minimum Capital Requirements for Market Risk (d457)](https://www.bis.org/bcbs/publ/d457.htm)
- [BCBS Minimum Capital Requirements for Market Risk, 2016 (d352)](https://www.bis.org/bcbs/publ/d352.pdf)
