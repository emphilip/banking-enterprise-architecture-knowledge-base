---
id: mortgage-origination
title: Mortgage Origination
type: business-process
domain: Lending & Credit
aliases: ["Mortgage Process"]
status: draft
---

# Mortgage Origination

**Definition.** Mortgage Origination is the process of originating a secured home loan, encompassing application, property valuation, collateral assessment, underwriting, and completion.
**Also known as:** Mortgage Process.

## Relationships
- Mortgage Origination is defined in the Lending & Credit domain.
- Mortgage Origination depends on the Loan Origination capability.
- Mortgage Origination depends on the Collateral Management capability.
- Mortgage Origination causes Credit Underwriting.

## Details
Mortgage Origination captures the borrower application, orders property valuation, perfects collateral and security, and progresses through underwriting to offer and completion. Actors include applicants, mortgage advisors, valuers, and underwriters. Systems involved include a loan origination platform, collateral and valuation services, and document processing.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)

## Flow
- Take Mortgage Application causes Issue Loan Estimate.
- Issue Loan Estimate causes Order Property Appraisal.
- Order Property Appraisal causes Review Title And Liens.
- Review Title And Liens causes Clear To Close.
- Clear To Close causes Deliver Closing Disclosure.
- Deliver Closing Disclosure causes Fund Mortgage Loan.
