---
id: backtesting-and-pandl-attribution
title: Backtesting & P&L Attribution
type: business-capability
domain: Risk Management
level: L4
aliases: ["PLA Test", "VaR Backtesting", "Model Performance Testing"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d457.htm"]
---

# Backtesting & P&L Attribution

**Definition.** Backtesting & P&L Attribution compares model risk forecasts against realised P&L and runs the FRTB PLA test to confirm internal-model eligibility per trading desk, defined by the Basel FRTB standard.
**Also known as:** PLA Test, VaR Backtesting, Model Performance Testing.

## Relationships
- Backtesting & P&L Attribution is defined in the Risk Management domain.
- Backtesting & P&L Attribution is derived from Value-at-Risk Calculation.
- Backtesting & P&L Attribution depends on the Risk Analytics Engine capability.
- Backtesting & P&L Attribution depends on the Analytics Platform capability.

## Details
Backtesting & P&L Attribution implements the two FRTB (d457) desk-level eligibility tests. Backtesting counts exceptions where one-day loss exceeds the 97.5% and 99% VaR over 250 days, scoring against the green/amber/red traffic-light zones. The P&L Attribution test compares the desk's risk-theoretical P&L against hypothetical P&L using the Spearman correlation and Kolmogorov-Smirnov metrics. Desks failing either test lose Internal Models Approach status and revert to the Standardised Approach, with reporting feeding model risk governance.

## References
- [Basel FRTB — Minimum Capital Requirements for Market Risk (d457)](https://www.bis.org/bcbs/publ/d457.htm)
