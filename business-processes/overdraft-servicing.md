---
id: overdraft-servicing
title: Overdraft Servicing
type: business-process
domain: Deposits & Accounts
aliases: ["Overdraft Handling", "NSF Processing"]
status: draft
sources: ["https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html", "https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-12.html"]
---

# Overdraft Servicing

**Definition.** Overdraft Servicing is the handling of debit items that exceed available balance, covering opt-in capture, overdraft-versus-NSF decisioning, limit checks, the pay-or-return decision and fee application under Reg E.
**Also known as:** Overdraft Handling, NSF Processing.

## Relationships
- Overdraft Servicing is defined in the Deposits & Accounts domain.
- Overdraft Servicing depends on the Overdraft Management capability.
- Overdraft Servicing depends on the Account Servicing capability.

## Details
Overdraft Servicing detects insufficient funds, checks the Reg E Opt-In Record for one-time debit and ATM items, evaluates the overdraft coverage limit, decides pay or return, applies the applicable Overdraft Fee, and notifies the customer. Actors include the Overdraft Operations Analyst. Controls include Reg E opt-in, overdraft coverage limits, fee disclosure, and fair-access underwriting.

## Flow
- Detect Insufficient Funds causes Check Overdraft Opt-In.
- Check Overdraft Opt-In causes Evaluate Overdraft Limit.
- Evaluate Overdraft Limit causes Decide Pay Or Return.
- Decide Pay Or Return causes Apply Overdraft Fee.
- Apply Overdraft Fee causes Notify Overdraft Outcome.

## References
- [HelpWithMyBank NSF and overdraft](https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html)
- [OCC Bulletin 2023-12](https://www.occ.gov/news-issuances/bulletins/2023/bulletin-2023-12.html)
