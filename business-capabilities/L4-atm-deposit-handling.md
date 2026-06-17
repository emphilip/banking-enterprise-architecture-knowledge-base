---
id: atm-deposit-handling
title: ATM Deposit Handling
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["ATM Cash Deposit", "Deposit Automation"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://us.brinks.com/branch-services"]
---

# ATM Deposit Handling

**Definition.** ATM Deposit Handling is the Channels & Engagement capability that processes cash and cheque deposits at deposit-automation ATMs, including provisional credit and verification, supporting the BIAN ATM Network Operations service domain.
**Also known as:** ATM Cash Deposit, Deposit Automation.

## Relationships
- ATM Deposit Handling is defined in the Channels & Engagement domain.
- ATM Deposit Handling is derived from ATM Transaction Processing.
- ATM Deposit Handling depends on the Core Banking Processing capability.

## Details
ATM Deposit Handling supports BIAN ATM Network Operations for intelligent-deposit terminals: validating and authenticating notes, imaging cheques (MICR plus image), and posting a provisional credit to the core before back-office verification. US funds-availability is governed by Reg CC, so the ATM applies and discloses next-day or extended holds at deposit time. Cash deposits over thresholds feed Bank Secrecy Act monitoring and counterfeit detection rejects suspect notes. Cheque images route to clearing under Check 21, and discrepancies between declared and counted amounts are reconciled with chargeback on returned items. Deposit automation reduces envelope fraud and CIT collection of deposited cash.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [CFPB Regulation CC (Funds Availability)](https://www.consumerfinance.gov/rules-policy/regulations/229/)
- [Brinks Branch Services](https://us.brinks.com/branch-services)
