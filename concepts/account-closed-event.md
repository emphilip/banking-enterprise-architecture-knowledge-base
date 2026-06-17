---
id: account-closed-event
title: Account Closed Event
type: event
domain: Deposits & Accounts
aliases: ["Account Closure Event", "Account Terminated Event"]
status: draft
sources: ["https://legalclarity.org/what-happens-when-you-close-a-bank-account/", "https://www.sofi.com/learn/content/bank-letter-to-close-account/"]
---

# Account Closed Event

**Definition.** Account Closed Event is the business event signalling that a deposit account has been settled to zero and deactivated on the core ledger. Account Closed Event marks the end of the account lifecycle in deposit servicing.

**Also known as:** Account Closure Event, Account Terminated Event.

## Relationships
- Account Closed Event is related to the Deposits & Accounts domain.
- Account Closed Event mentions Account Closure.
- Account Closed Event causes Deactivate Account.

## Details
Account Closed Event fires at Deactivate Account after the residual balance is settled to zero and the final statement is produced, carrying the account identifier, closure date and final-disbursement reference. Account Closed Event stops interest accrual, halts statement cycles, releases linked services such as standing orders, and starts the post-closure record-retention period. Downstream systems consume Account Closed Event to update the customer relationship view and reporting.

## References
- https://legalclarity.org/what-happens-when-you-close-a-bank-account/
- https://www.sofi.com/learn/content/bank-letter-to-close-account/
