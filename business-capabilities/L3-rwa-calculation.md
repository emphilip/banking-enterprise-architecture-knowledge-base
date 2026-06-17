---
id: rwa-calculation
title: RWA Calculation
type: business-capability
domain: Finance & Treasury
level: L3
aliases: ["Risk-Weighted Assets Calculation", "RWA Computation", "Basel RWA"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d424.htm", "https://www.bis.org/bcbs/publ/d424_hlsummary.htm"]
---

# RWA Calculation

**Definition.** RWA Calculation computes risk-weighted assets across credit, market and operational risk under the Basel III standardised and internal-model approaches, subject to the aggregate output floor.
**Also known as:** Risk-Weighted Assets Calculation, RWA Computation, Basel RWA.

## Relationships
- RWA Calculation is defined in the Finance & Treasury domain.
- RWA Calculation is derived from Regulatory Capital Management.
- RWA Calculation depends on the Regulatory Reporting Engine capability.

## Details
RWA Calculation aggregates exposure-level risk weights into total RWA, the denominator of the Basel III capital ratios (CET1, Tier 1, total capital). The finalised Basel III framework (BCBS d424) revised the credit and operational standardised approaches, constrained IRB use, and introduced the 72.5% output floor that caps internally-modelled RWA at a share of the standardised result. This capability sources credit, market and operational components and applies the floor to produce the consolidated RWA used in capital adequacy returns.

## References
- [Basel III: Finalising post-crisis reforms (BCBS d424)](https://www.bis.org/bcbs/publ/d424.htm)
- [Basel III finalisation - high-level summary](https://www.bis.org/bcbs/publ/d424_hlsummary.htm)
