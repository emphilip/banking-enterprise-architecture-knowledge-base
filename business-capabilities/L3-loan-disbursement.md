---
id: loan-disbursement
title: Loan Disbursement
type: business-capability
domain: Lending & Credit
level: L3
aliases: ["Fund Disbursement", "Loan Drawdown"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/tila-respa-integrated-disclosures/"]
---

# Loan Disbursement

**Definition.** Loan Disbursement is the capability that releases approved funds to the borrower or third parties and activates the loan facility, mapping to the BIAN Disbursement service domain.
**Also known as:** Fund Disbursement, Loan Drawdown.

## Relationships
- Loan Disbursement is defined in the Lending & Credit domain.
- Loan Disbursement is derived from Loan Origination.
- Loan Disbursement depends on the Core Banking Processing capability.
- Loan Disbursement depends on the Workflow Orchestration capability.

## Details
The BIAN Disbursement service domain handles the controlled release of funds against an approved facility, recording drawdown amounts and value dates. A concrete banking specific: mortgage disbursement is staged against satisfied conditions precedent and, in the US, cannot fund until the TILA-RESPA Integrated Disclosure (TRID) three-business-day waiting period after the Closing Disclosure has elapsed.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [CFPB TILA-RESPA Integrated Disclosure (TRID) rule](https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/tila-respa-integrated-disclosures/)
