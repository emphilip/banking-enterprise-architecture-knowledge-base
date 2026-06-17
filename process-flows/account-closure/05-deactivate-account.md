---
id: deactivate-account
title: Deactivate Account
type: process-step
process: Account Closure
order: 5
aliases: ["Close Account Record", "Account Deactivation Step"]
status: draft
sources: ["https://legalclarity.org/what-happens-when-you-close-a-bank-account/"]
---

# Deactivate Account

**Definition.** Deactivate Account closes the account on the core ledger and emits the Account Closed Event.
**Also known as:** Close Account Record, Account Deactivation Step.

## Relationships
- Deactivate Account is defined in the Account Closure process.
- Deactivate Account causes Escheat Dormant Account.
- Deactivate Account depends on the Core Banking Processing capability.
- Deactivate Account mentions Deposit Operations Clerk.
- Deactivate Account mentions Account Closed Event.

## Details
The Deposit Operations Clerk closes the account record on the core ledger from the final statement. Controls include five-year record retention and closure confirmation; the Account Closed Event is emitted on completion.

## References
- [What happens when you close a bank account](https://legalclarity.org/what-happens-when-you-close-a-bank-account/)
