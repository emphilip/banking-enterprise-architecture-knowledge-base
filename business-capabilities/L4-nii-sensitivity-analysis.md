---
id: nii-sensitivity-analysis
title: NII Sensitivity Analysis
type: business-capability
domain: Finance & Treasury
level: L4
aliases: ["Net Interest Income Sensitivity", "Earnings-at-Risk", "NII Simulation"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d368.htm", "https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/analytical-applications-infrastructure/812/almug/interest-rate-risk-banking-book-irrbb.html"]
---

# NII Sensitivity Analysis

**Definition.** NII Sensitivity Analysis projects the change in net interest income under rate-shock and repricing scenarios as the earnings-based limb of IRRBB measurement.
**Also known as:** Net Interest Income Sensitivity, Earnings-at-Risk, NII Simulation.

## Relationships
- NII Sensitivity Analysis is defined in the Finance & Treasury domain.
- NII Sensitivity Analysis is derived from Interest Rate Risk In The Banking Book.
- NII Sensitivity Analysis depends on the Asset Liability Management Engine capability.

## Details
NII Sensitivity Analysis simulates net interest income over a forward horizon (typically 1-3 years) under rate shocks and yield-curve scenarios, capturing repricing timing, balance assumptions and reinvestment, to quantify earnings-at-risk. It complements the value-based EVE measure required under BCBS d368 with the short-run earnings view ALCO uses to set the banking-book rate-risk position, and it is computed on both a constant and a dynamic (new-business) balance-sheet basis.

## References
- [Interest rate risk in the banking book (BCBS d368)](https://www.bis.org/bcbs/publ/d368.htm)
- [Oracle ALM - IRRBB](https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/analytical-applications-infrastructure/812/almug/interest-rate-risk-banking-book-irrbb.html)
