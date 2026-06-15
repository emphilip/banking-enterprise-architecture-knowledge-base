---
id: deposit-account-opening
title: Deposit Account Opening
type: business-process
domain: Deposits & Accounts
aliases: ["New Account Process"]
status: draft
---

# Deposit Account Opening

**Definition.** Deposit Account Opening is the process of establishing a new deposit account for a customer, including product selection, terms agreement, account provisioning, and initial funding.
**Also known as:** New Account Process.

## Relationships
- Deposit Account Opening is defined in the Deposits & Accounts domain.
- Deposit Account Opening depends on the Account Opening capability.

## Details
Deposit Account Opening captures the product choice, applies eligibility and terms, creates the account record in the core banking system, and enables initial deposits and channel access. Actors include the customer, branch or digital channel operators, and account operations staff. The process integrates with the core ledger, notification services, and statement setup.

## Flow
- Capture Account Application causes Collect CIP Information.
- Collect CIP Information causes Verify Account Applicant.
- Verify Account Applicant causes Capture Signature Card.
- Capture Signature Card causes Disclose Account Terms.
- Disclose Account Terms causes Establish Deposit Account.
- Establish Deposit Account causes Fund New Account.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
