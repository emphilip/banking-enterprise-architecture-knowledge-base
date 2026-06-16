---
id: credit-risk-rating
title: Credit Risk Rating
type: business-capability
domain: Risk Management
level: L3
aliases: ["Internal Ratings", "Rating Model Management", "IRB Rating"]
status: draft
sources: ["https://www.bis.org/basel_framework/chapter/CRE/30.htm", "https://bian.org/servicelandscape/"]
---

# Credit Risk Rating

**Definition.** Credit Risk Rating assigns and maintains internal obligor and facility ratings on a master scale calibrated to PD, LGD and EAD, underpinning the Basel IRB approach and the BIAN Credit Risk Models service domain.
**Also known as:** Internal Ratings, Rating Model Management, IRB Rating.

## Relationships
- Credit Risk Rating is defined in the Risk Management domain.
- Credit Risk Rating is derived from Credit Risk Management.
- Credit Risk Rating depends on the Machine Learning Platform capability.
- Credit Risk Rating depends on the Model Risk Management Platform capability.

## Details
Credit Risk Rating operates a master rating scale where each grade maps to a calibrated probability of default, meeting the Basel CRE30 requirements: a minimum of seven non-default obligor grades plus one default grade, meaningful distribution without excessive concentration, and a one-year PD floor of 0.03% for most exposures. Ratings are reviewed at least annually, override governance is logged, and rating system performance is monitored through discriminatory-power and stability metrics that feed model validation.

## References
- [Basel Framework CRE30 (IRB approach)](https://www.bis.org/basel_framework/chapter/CRE/30.htm)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
