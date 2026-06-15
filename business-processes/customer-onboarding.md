---
id: customer-onboarding
title: Customer Onboarding
type: business-process
domain: Customer Management
aliases: ["Client Onboarding"]
status: draft
---

# Customer Onboarding

**Definition.** Customer Onboarding is the end-to-end process by which a prospective party is acquired, identified, screened, and established as a banking customer with active products and access credentials.
**Also known as:** Client Onboarding.

## Relationships
- Customer Onboarding is defined in the Customer Management domain.
- Customer Onboarding depends on the Customer Acquisition capability.
- Customer Onboarding depends on the Identity Verification capability.
- Customer Onboarding depends on the KYC Management capability.
- KYC Verification causes Customer Onboarding.
- Customer Onboarding causes Deposit Account Opening.

## Details
Customer Onboarding begins with application capture across digital or branch channels, proceeds through identity proofing and customer due diligence, and concludes with account provisioning and welcome servicing. Actors include the prospective customer, onboarding operations staff, and compliance reviewers. Systems involved typically include a digital channel platform, a customer identity solution, document processing, and the core banking system for account creation.

## Flow
- Receive Application causes Capture Consent.
- Capture Consent causes Collect Documents.
- Collect Documents causes Verify Identity.
- Verify Identity causes Screen Customer.
- Screen Customer causes Assess Customer Risk.
- Assess Customer Risk causes Approve Onboarding.
- Approve Onboarding causes Create Customer Record.
- Create Customer Record causes Activate Customer.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
