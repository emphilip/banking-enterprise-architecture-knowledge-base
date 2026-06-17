---
id: risk-capital-calculation
title: Risk Capital Calculation
type: business-capability
domain: Risk Management
level: L3
aliases: ["RWA Calculation", "Capital Charge Computation", "Capital Charge Engine"]
status: draft
sources: ["https://www.bis.org/basel_framework/", "https://www.bis.org/bcbs/basel3.htm"]
---

# Risk Capital Calculation

**Definition.** Risk Capital Calculation computes risk-weighted assets and capital charges across credit, market and operational risk using standardised and internal approaches, defined by the BCBS Basel III/IV consolidated capital framework.
**Also known as:** RWA Calculation, Capital Charge Computation, Capital Charge Engine.

## Relationships
- Risk Capital Calculation is defined in the Risk Management domain.
- Risk Capital Calculation is derived from Regulatory Capital Adequacy.
- Risk Capital Calculation depends on the Risk Analytics Engine capability.
- Risk Capital Calculation depends on the Risk Data Aggregation capability.

## Details
Risk Capital Calculation applies the Basel Framework calculation engines: credit RWA via the standardised approach (CRE20) or IRB (CRE30+) using PD/LGD/EAD, market risk under FRTB, and operational risk under the Standardised Approach (Business Indicator Component times the Internal Loss Multiplier). It enforces the Basel III/IV output floor (72.5% of standardised RWA) capping internal-model benefits, and produces the RWA denominator feeding CET1 and total capital ratios.

## References
- [Consolidated Basel Framework](https://www.bis.org/basel_framework/)
- [Basel III Framework](https://www.bis.org/bcbs/basel3.htm)
