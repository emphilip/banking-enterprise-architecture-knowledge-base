---
id: ftp-rate-curve-management
title: FTP Rate Curve Management
type: business-capability
domain: Finance & Treasury
level: L4
aliases: ["Transfer Curve Management", "FTP Curve Construction", "Liquidity Premium Curves"]
status: draft
sources: ["https://www.fermacrisk.com/alm-structural-risk", "https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/analytical-applications-infrastructure/812/almug/interest-rate-risk-banking-book-irrbb.html"]
---

# FTP Rate Curve Management

**Definition.** FTP Rate Curve Management constructs and maintains the transfer-pricing yield curves and liquidity premiums used to charge and credit funds across the bank.
**Also known as:** Transfer Curve Management, FTP Curve Construction, Liquidity Premium Curves.

## Relationships
- FTP Rate Curve Management is defined in the Finance & Treasury domain.
- FTP Rate Curve Management is derived from Funds Transfer Pricing Management.
- FTP Rate Curve Management depends on the Asset Liability Management Engine capability.

## Details
FTP Rate Curve Management builds the base transfer curve from market reference rates and the bank's own funding curve, then adds tenor-based liquidity premiums and contingent-liquidity/optionality add-ons so each transaction is priced at its matched-maturity transfer rate. Curve construction is the mechanism that moves interest-rate and funding-liquidity risk from the business lines to the treasury book; the capability governs curve methodology, term points, premium calibration and the daily publication of curves that feed every FTP charge and credit.

## References
- [ALM and structural risk (Ferma)](https://www.fermacrisk.com/alm-structural-risk)
- [Oracle ALM - IRRBB and transfer pricing](https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/analytical-applications-infrastructure/812/almug/interest-rate-risk-banking-book-irrbb.html)
