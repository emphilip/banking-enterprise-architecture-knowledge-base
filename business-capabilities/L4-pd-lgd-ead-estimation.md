---
id: pd-lgd-ead-estimation
title: PD LGD EAD Estimation
type: business-capability
domain: Risk Management
level: L4
aliases: ["Risk Parameter Estimation", "Default Parameter Modelling"]
status: draft
sources: ["https://www.bis.org/basel_framework/chapter/CRE/36.htm", "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/"]
---

# PD LGD EAD Estimation

**Definition.** PD LGD EAD Estimation develops and calibrates the risk parameter models — probability of default, loss given default and exposure at default — feeding ratings, ECL and capital, defined by the Basel IRB framework.
**Also known as:** Risk Parameter Estimation, Default Parameter Modelling.

## Relationships
- PD LGD EAD Estimation is defined in the Risk Management domain.
- PD LGD EAD Estimation is derived from Credit Risk Rating.
- PD LGD EAD Estimation depends on the Machine Learning Platform capability.
- PD LGD EAD Estimation depends on the Model Risk Management Platform capability.

## Details
PD LGD EAD Estimation builds the three Basel IRB risk parameters per the requirements in CRE36: a long-run average one-year PD per grade (0.03% floor), downturn LGD reflecting economic-loss including discounting and collection costs, and EAD via credit-conversion factors on undrawn limits, with regulatory input floors (e.g. 5% unsecured retail LGD). The same models supply point-in-time, forward-looking parameters for IFRS 9 ECL. Calibration, segmentation and margins of conservatism are evidenced for validation and supervisory approval.

## References
- [Basel Framework CRE36 (IRB minimum requirements)](https://www.bis.org/basel_framework/chapter/CRE/36.htm)
- [IFRS 9 Financial Instruments](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/)
