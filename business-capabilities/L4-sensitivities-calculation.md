---
id: sensitivities-calculation
title: Sensitivities Calculation
type: business-capability
domain: Risk Management
level: L4
aliases: ["Greeks Calculation", "SBM Sensitivities", "Risk Factor Sensitivities"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d457.htm"]
---

# Sensitivities Calculation

**Definition.** Sensitivities Calculation derives delta, vega and curvature risk sensitivities by risk class for the FRTB sensitivities-based method, defined by the Basel minimum capital requirements for market risk.
**Also known as:** Greeks Calculation, SBM Sensitivities, Risk Factor Sensitivities.

## Relationships
- Sensitivities Calculation is defined in the Risk Management domain.
- Sensitivities Calculation is derived from Market Risk Measurement.
- Sensitivities Calculation depends on the Risk Analytics Engine capability.
- Sensitivities Calculation depends on the Analytics Platform capability.

## Details
Sensitivities Calculation computes the delta, vega and curvature sensitivities prescribed by the FRTB Sensitivities-Based Method (BCBS d457) to defined risk factors and tenor buckets across the seven risk classes. Curvature captures non-linear option risk via prescribed up/down shocks. The sensitivities are multiplied by regulatory risk weights and aggregated within and across buckets using prescribed correlations under low, medium and high correlation scenarios to produce the standardised market-risk capital charge.

## References
- [Basel FRTB — Minimum Capital Requirements for Market Risk (d457)](https://www.bis.org/bcbs/publ/d457.htm)
