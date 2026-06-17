---
id: deposit-account-management
title: Deposit Account Management
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Account Master Service", "Deposit Account Service", "Account System of Record"]
status: draft
sources: ["https://www.thoughtmachine.net/vault-core", "https://help.sap.com/docs/SAP_FOR_BANKING/b0c17eb728054c5e92d73923f704edd7/53ffbdb976794b099a360da5b4ec88b6.html"]
---

# Deposit Account Management

**Definition.** Deposit Account Management is the technology capability that maintains the system-of-record for deposit accounts (current, savings, term/fixed deposits), holding account master data, balances, holds, multi-currency positions and account-level configuration as the authoritative core record.
**Also known as:** Account Master Service, Deposit Account Service, Account System of Record.

## Relationships
- Deposit Account Management is defined in the Core Processing domain.
- Deposit Account Management is derived from Core Banking Processing.
- Deposit Account Management is related to Account Servicing.

## Details
Deposit Account Management holds the authoritative record for current, savings and term/fixed-deposit accounts, including balances, holds and multi-currency positions. Thought Machine Vault Core models accounts as the system of record driven by configurable smart-contract products, and SAP Deposits Management maintains deposit account contracts and their configuration as the core deposit record, so downstream posting, interest and statement processing all reference this single account master.

## References
- [Thought Machine Vault Core](https://www.thoughtmachine.net/vault-core)
- [SAP Deposits Management](https://help.sap.com/docs/SAP_FOR_BANKING/b0c17eb728054c5e92d73923f704edd7/53ffbdb976794b099a360da5b4ec88b6.html)
