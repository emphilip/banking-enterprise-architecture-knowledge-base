---
id: account-opened-event
title: Account Opened Event
type: event
domain: Deposits & Accounts
aliases: ["Account Established Event", "New Account Opened"]
status: draft
sources: ["https://www.alogent.com/banking-definitions/customer-identification-program-cip", "https://openonline.53.com/product/service/apply/document/depositAccountRules"]
---

# Account Opened Event

**Definition.** Account Opened Event is the business event signalling that a new deposit account has been created on the core ledger and funded. Account Opened Event marks the completion of the account-opening flow and the handover to ongoing servicing.

**Also known as:** Account Established Event, New Account Opened.

## Relationships
- Account Opened Event is related to the Deposits & Accounts domain.
- Account Opened Event mentions Deposit Account Opening.
- Account Opened Event causes Fund New Account.

## Details
Account Opened Event fires at the end of Fund New Account once the initial deposit is applied and the account is activated, carrying the account identifier, product code, opening date and funding reference. Account Opened Event triggers welcome servicing, statement-cycle enrolment and downstream notification, and signals compliance that CIP verification completed before activation. Operational systems consume Account Opened Event to begin interest accrual and to start the account lifecycle clock used by dormancy monitoring.

## References
- https://www.alogent.com/banking-definitions/customer-identification-program-cip
- https://openonline.53.com/product/service/apply/document/depositAccountRules
