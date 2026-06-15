---
id: receive-credit-application
title: Receive Credit Application
type: process-step
process: Trade Finance Processing
order: 1
aliases: ["Take LC Request", "Credit Application Step"]
status: draft
sources: ["https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-members/letter-of-credit-import-process-issuance-trade-finance/ba-p/13494066", "https://incodocs.com/blog/letter-credit-lc/"]
---

# Receive Credit Application

**Definition.** Receive Credit Application receives the applicant's documentary or standby credit request and the underlying contract terms.
**Also known as:** Take LC Request, Credit Application Step.

## Relationships
- Receive Credit Application is defined in the Trade Finance Processing process.
- Receive Credit Application causes Assess Trade Limit.
- Receive Credit Application depends on the Workflow Orchestration capability.
- Receive Credit Application mentions Trade Finance Officer.

## Details
The Trade Finance Officer receives the request. Inputs are the Letter Of Credit application; outputs are a captured LC request. Controls include mandate capture, UCP 600 / ISP98 rule selection and KYC of the applicant.

## References
- [SAP: letter of credit import issuance](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-members/letter-of-credit-import-process-issuance-trade-finance/ba-p/13494066)
- [IncoDocs: letter of credit](https://incodocs.com/blog/letter-credit-lc/)
