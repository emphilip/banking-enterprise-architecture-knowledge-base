---
id: loan-account-maintenance
title: Loan Account Maintenance
type: business-capability
domain: Lending & Credit
level: L3
aliases: ["Loan Account Administration", "Facility Maintenance"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.consumerfinance.gov/rules-policy/regulations/1026/"]
---

# Loan Account Maintenance

**Definition.** Loan Account Maintenance is the capability that manages ongoing changes to active loan accounts such as rate resets, redraws and interest accrual, mapping to the BIAN Consumer Loan and Corporate Loan service domains.
**Also known as:** Loan Account Administration, Facility Maintenance.

## Relationships
- Loan Account Maintenance is defined in the Lending & Credit domain.
- Loan Account Maintenance is derived from Loan Servicing.
- Loan Account Maintenance depends on the Core Banking Processing capability.

## Details
The BIAN Consumer Loan and Corporate Loan service domains hold the live loan account whose static and dynamic data Loan Account Maintenance updates. A concrete banking specific: an adjustable-rate mortgage (ARM) requires a scheduled rate reset against its index plus margin, and the servicer must issue an ARM interest-rate-adjustment notice to the borrower under Regulation Z ahead of the change taking effect.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Truth in Lending Act (Regulation Z)](https://www.consumerfinance.gov/rules-policy/regulations/1026/)
