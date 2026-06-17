---
id: account-closure-request
title: Account Closure Request
type: artifact
domain: Deposits & Accounts
aliases: ["Closure Request", "Close Account Application"]
status: draft
sources: ["https://www.sofi.com/learn/content/bank-letter-to-close-account/", "https://legalclarity.org/what-happens-when-you-close-a-bank-account/"]
---

# Account Closure Request

**Definition.** Account Closure Request is the signed instruction to close a deposit account, including how residual funds should be disbursed. Account Closure Request is the input artifact that initiates the account-closure flow.

**Also known as:** Closure Request, Close Account Application.

## Relationships
- Account Closure Request is related to the Deposits & Accounts domain.
- Account Closure Request mentions Receive Closure Request.
- Account Closure Request mentions Closure Request Handling.

## Details
Account Closure Request states the account identifier, the closing instruction and the disbursement method for the residual balance, such as transfer to another account, cashier's draft or cash. Account Closure Request is validated for signatory authority and checked against holds, pending items and linked services before the balance is settled to zero. A dormancy or escheatment trigger can stand in for a customer-signed Account Closure Request when the account is abandoned.

## References
- https://www.sofi.com/learn/content/bank-letter-to-close-account/
- https://legalclarity.org/what-happens-when-you-close-a-bank-account/
