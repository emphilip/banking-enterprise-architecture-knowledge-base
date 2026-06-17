---
id: credit-risk-rwa
title: Credit Risk RWA
type: business-capability
domain: Finance & Treasury
level: L4
aliases: ["Credit RWA", "SA-CR RWA", "IRB RWA"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d424.htm", "https://www.bis.org/bcbs/publ/d424_hlsummary.htm"]
---

# Credit Risk RWA

**Definition.** Credit Risk RWA computes credit risk-weighted assets under the Basel III standardised approach and internal ratings-based approach, applying revised risk weights and the output floor.
**Also known as:** Credit RWA, SA-CR RWA, IRB RWA.

## Relationships
- Credit Risk RWA is defined in the Finance & Treasury domain.
- Credit Risk RWA is derived from RWA Calculation.
- Credit Risk RWA depends on the Regulatory Reporting Engine capability.

## Details
Credit Risk RWA applies exposure-class risk weights under the finalised Basel III standardised approach (BCBS d424) — more granular weights for corporates, banks, retail and real estate, with due-diligence requirements on external ratings — and, where approved, IRB risk weights derived from PD/LGD/EAD parameters now constrained by input floors and the removal of the advanced IRB option for certain portfolios. The 72.5% aggregate output floor caps modelled credit RWA relative to the standardised result, which this capability computes alongside both approaches.

## References
- [Basel III: Finalising post-crisis reforms (BCBS d424)](https://www.bis.org/bcbs/publ/d424.htm)
- [Basel III finalisation - high-level summary](https://www.bis.org/bcbs/publ/d424_hlsummary.htm)
