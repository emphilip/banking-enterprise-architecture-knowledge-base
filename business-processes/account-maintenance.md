---
id: account-maintenance
title: Account Maintenance
type: business-process
domain: Deposits & Accounts
aliases: ["Account Servicing Process", "Account Detail Maintenance"]
status: draft
sources: ["https://www.associatedbank.com/forms-and-disclosures/disclosures/deposit-account-agreement", "https://openonline.53.com/product/service/apply/document/depositAccountRules"]
---

# Account Maintenance

**Definition.** Account Maintenance is the ongoing servicing of an open deposit account, covering change of address and details, mandate and signatory changes, stop payments, standing instructions, interest posting and fee changes.
**Also known as:** Account Servicing Process, Account Detail Maintenance.

## Relationships
- Account Maintenance is defined in the Deposits & Accounts domain.
- Account Maintenance depends on the Account Servicing capability.

## Details
Account Maintenance captures a Service Maintenance Request, verifies the requester's signatory authority, applies the change in the core system under dual control, and issues any required Reg DD change-in-terms notice. Actors include the Deposit Operations Clerk. Controls include signatory verification, authentication, dual control on static-data changes, and interest accrual accuracy.

## Flow
- Receive Maintenance Request causes Verify Account Holder.
- Verify Account Holder causes Assess Change Impact.
- Assess Change Impact causes Apply Account Change.
- Apply Account Change causes Post Account Interest.
- Post Account Interest causes Notify Account Change.

## References
- [Associated Bank deposit account agreement](https://www.associatedbank.com/forms-and-disclosures/disclosures/deposit-account-agreement)
- [Fifth Third deposit account rules](https://openonline.53.com/product/service/apply/document/depositAccountRules)
