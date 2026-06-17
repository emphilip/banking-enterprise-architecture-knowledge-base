---
id: account-lifecycle-manager
title: Account Lifecycle Manager
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Account State Engine", "Deposit Lifecycle Engine", "Account Status Manager"]
status: draft
sources: ["https://docs.mambu.com/docs/profit-sharing-deposit-account-life-cycle-and-states/", "https://help.sap.com/docs/SAP_FOR_BANKING/b0c17eb728054c5e92d73923f704edd7/53ffbdb976794b099a360da5b4ec88b6.html"]
---

# Account Lifecycle Manager

**Definition.** Account Lifecycle Manager is the technology capability that drives deposit account state transitions through the lifecycle — opening, activation, dormancy, hold or freeze, maturity and rollover for term deposits, and closure — enforcing lifecycle rules in the core.
**Also known as:** Account State Engine, Deposit Lifecycle Engine, Account Status Manager.

## Relationships
- Account Lifecycle Manager is defined in the Core Processing domain.
- Account Lifecycle Manager is derived from Core Banking Processing.
- Account Lifecycle Manager is related to Account Opening.
- Account Lifecycle Manager is related to Account Servicing.

## Details
Account Lifecycle Manager governs deposit account state transitions from opening and activation through dormancy, holds, term-deposit maturity and rollover, and closure. Mambu documents an explicit deposit account life cycle and states, and SAP Deposits Management manages contract lifecycle across current, savings and fixed-term accounts, so this capability enforces the permitted state machine and lifecycle rules within the core.

## References
- [Mambu deposit account life cycle and states](https://docs.mambu.com/docs/profit-sharing-deposit-account-life-cycle-and-states/)
- [SAP Deposits Management](https://help.sap.com/docs/SAP_FOR_BANKING/b0c17eb728054c5e92d73923f704edd7/53ffbdb976794b099a360da5b4ec88b6.html)
