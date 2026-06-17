---
id: mark-to-market-valuation
title: Mark-to-Market Valuation
type: business-capability
domain: Risk Management
level: L4
aliases: ["Independent Price Verification", "Position Revaluation", "IPV"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.bis.org/bcbs/publ/d457.htm"]
---

# Mark-to-Market Valuation

**Definition.** Mark-to-Market Valuation revalues positions to current market and model prices and feeds independent price verification for risk and capital, supporting the BIAN Market Risk Models service domain.
**Also known as:** Independent Price Verification, Position Revaluation, IPV.

## Relationships
- Mark-to-Market Valuation is defined in the Risk Management domain.
- Mark-to-Market Valuation is derived from Market Risk Measurement.
- Mark-to-Market Valuation depends on the Risk Analytics Engine capability.
- Mark-to-Market Valuation depends on the Analytics Platform capability.

## Details
Mark-to-Market Valuation revalues trading positions daily using observable market prices where available (mark-to-market) and calibrated models for illiquid instruments (mark-to-model). It runs Independent Price Verification by sourcing prices independently of the front office and computes Prudent Valuation Adjustments (additional valuation adjustments for close-out cost, model risk and concentrated positions) consistent with the FRTB prudent-valuation expectations under BCBS d457, feeding both fair-value P&L and risk-factor levels.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Basel FRTB — Minimum Capital Requirements for Market Risk (d457)](https://www.bis.org/bcbs/publ/d457.htm)
