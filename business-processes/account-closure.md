---
id: account-closure
title: Account Closure
type: business-process
domain: Deposits & Accounts
aliases: ["Account Offboarding", "Deposit Account Closure"]
status: draft
sources: ["https://legalclarity.org/what-happens-when-you-close-a-bank-account/", "https://www.incharge.org/blog/what-happens-to-dormant-bank-accounts/"]
---

# Account Closure

**Definition.** Account Closure is the end-to-end closure of a deposit account, including closure request capture, balance settlement to zero, final statement and account deactivation, and covering dormancy-driven and escheatment closures.
**Also known as:** Account Offboarding, Deposit Account Closure.

## Relationships
- Account Closure is defined in the Deposits & Accounts domain.
- Account Closure depends on the Account Servicing capability.

## Details
Account Closure captures an Account Closure Request, confirms eligibility against holds and pending items, settles the residual balance to zero, produces a final statement, and deactivates the account. Dormancy-driven closures issue a Dormancy Notice and escheat unclaimed funds to the state. Actors include the Deposit Operations Clerk and the Unclaimed Property Officer. Controls include signatory verification, zero-balance confirmation, dormancy rules, escheatment, and five-year record retention.

## Flow
- Receive Closure Request causes Validate Closure Eligibility.
- Validate Closure Eligibility causes Settle Residual Balance.
- Settle Residual Balance causes Issue Final Statement.
- Issue Final Statement causes Deactivate Account.
- Deactivate Account causes Escheat Dormant Account.
- Issue Dormancy Notice causes Escheat Dormant Account.

## References
- [What happens when you close a bank account](https://legalclarity.org/what-happens-when-you-close-a-bank-account/)
- [What happens to dormant bank accounts](https://www.incharge.org/blog/what-happens-to-dormant-bank-accounts/)
