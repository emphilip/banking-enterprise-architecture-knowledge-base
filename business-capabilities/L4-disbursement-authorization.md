---
id: disbursement-authorization
title: Disbursement Authorization
type: business-capability
domain: Lending & Credit
level: L4
aliases: ["Drawdown Authorization", "Release Authorization"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/tila-respa-integrated-disclosures/"]
---

# Disbursement Authorization

**Definition.** Disbursement Authorization is the capability that validates and approves fund-release instructions prior to drawdown, mapping to the BIAN Disbursement service domain.
**Also known as:** Drawdown Authorization, Release Authorization.

## Relationships
- Disbursement Authorization is defined in the Lending & Credit domain.
- Disbursement Authorization is derived from Loan Disbursement.
- Disbursement Authorization depends on the Core Banking Processing capability.
- Disbursement Authorization depends on the Workflow Orchestration capability.

## Details
The BIAN Disbursement service domain controls the release of funds, and Disbursement Authorization provides the maker-checker approval gate ahead of it. A concrete banking specific: dual authorisation and four-eyes controls are applied to fund release for fraud and operational-risk reasons, and for mortgages the release is held until the TRID Closing Disclosure waiting period has expired.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [CFPB TILA-RESPA Integrated Disclosure (TRID) rule](https://www.consumerfinance.gov/compliance/compliance-resources/mortgage-resources/tila-respa-integrated-disclosures/)
