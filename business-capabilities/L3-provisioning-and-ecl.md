---
id: provisioning-and-ecl
title: Provisioning & ECL
type: business-capability
domain: Risk Management
level: L3
aliases: ["Expected Credit Loss", "Impairment Provisioning", "IFRS 9 Staging"]
status: draft
sources: ["https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/", "https://bian.org/servicelandscape/"]
---

# Provisioning & ECL

**Definition.** Provisioning & ECL calculates expected credit loss and impairment provisions using PD, LGD and EAD across the three IFRS 9 staging buckets, governed by the IFRS 9 standard and the BIAN Credit Risk Models service domain.
**Also known as:** Expected Credit Loss, Impairment Provisioning, IFRS 9 Staging.

## Relationships
- Provisioning & ECL is defined in the Risk Management domain.
- Provisioning & ECL is derived from Credit Risk Management.
- Provisioning & ECL depends on the Risk Analytics Engine capability.
- Provisioning & ECL depends on the Machine Learning Platform capability.

## Details
Provisioning & ECL implements the IFRS 9 three-stage impairment model: Stage 1 carries 12-month ECL, Stage 2 (significant increase in credit risk) and Stage 3 (credit-impaired) carry lifetime ECL. ECL is the probability-weighted product of point-in-time PD, LGD and EAD discounted at the effective interest rate, incorporating forward-looking macroeconomic scenarios. The capability manages staging transfer criteria, post-model adjustments and the divergence between IFRS 9 ECL and US GAAP CECL lifetime loss for cross-listed entities.

## References
- [IFRS 9 Financial Instruments](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
