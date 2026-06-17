---
id: repricing-gap-engine
title: Repricing Gap Engine
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Gap Analysis Engine", "Repricing Bucket Engine", "Maturity Gap Service"]
status: draft
sources: ["https://www.afme.eu/media/t5tehhpr/afmeirrbbfinal.pdf", "https://www.fermacrisk.com/alm-structural-risk"]
---

# Repricing Gap Engine

**Definition.** Repricing Gap Engine buckets assets and liabilities by maturity or repricing date across defined tenors to compute static and dynamic repricing gaps for interest-rate risk measurement.
**Also known as:** Gap Analysis Engine, Repricing Bucket Engine, Maturity Gap Service.

## Relationships
- Repricing Gap Engine is defined in the Core Processing domain.
- Repricing Gap Engine is derived from IRRBB Analytics Engine.

## Details
Repricing Gap Engine slots every banking-book position into time bands by the date it next reprices — contractual maturity for fixed-rate items, the next reset date for floating-rate items, and modelled repricing dates for non-maturity deposits and prepaying assets. For each band it nets rate-sensitive assets against rate-sensitive liabilities to give the period gap and the cumulative gap, the basis for earnings-at-risk under a parallel rate shock. AFME's IRRBB guidance and ALM practice treat the repricing gap as the foundational measure that feeds NII sensitivity, with behavioural assumptions determining how non-maturity and optional positions are bucketed.

## References
- [AFME IRRBB guidance](https://www.afme.eu/media/t5tehhpr/afmeirrbbfinal.pdf)
- [ALM and structural interest rate risk (Ferma Risk)](https://www.fermacrisk.com/alm-structural-risk)
