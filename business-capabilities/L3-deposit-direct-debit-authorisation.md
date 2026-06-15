---
id: deposit-direct-debit-authorisation
title: Deposit Direct Debit Authorisation
type: business-capability
domain: Deposits & Accounts
level: L3
aliases: ["Debtor Mandate Management", "Account DD Authorisation"]
status: draft
sources: ["https://www.openriskmanual.org/wiki/Category:BIAN_Service_Domain", "https://www.nacha.org/rules"]
---

# Deposit Direct Debit Authorisation

**Definition.** Deposit Direct Debit Authorisation maintains debtor-side direct debit mandates and authorisations held against deposit accounts, realising the BIAN Direct Debit Mandate service domain from the account-holding bank's perspective.
**Also known as:** Debtor Mandate Management, Account DD Authorisation.

## Relationships
- Deposit Direct Debit Authorisation is defined in the Deposits & Accounts domain.
- Deposit Direct Debit Authorisation is derived from Account Servicing.
- Deposit Direct Debit Authorisation depends on the Core Banking Processing capability.

## Details
The BIAN Direct Debit Mandate service domain stores debtor authorisations; under the Nacha Operating Rules and Regulation E a consumer may revoke an ACH debit authorisation and stop payment, which the account-holding bank must honour.

## References
- [BIAN Service Domain catalog (Open Risk Manual)](https://www.openriskmanual.org/wiki/Category:BIAN_Service_Domain)
- [Nacha Operating Rules](https://www.nacha.org/rules)
