---
id: detect-insufficient-funds
title: Detect Insufficient Funds
type: process-step
process: Overdraft Servicing
order: 1
aliases: ["Identify Shortfall", "Insufficient Funds Detection Step"]
status: draft
sources: ["https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html"]
---

# Detect Insufficient Funds

**Definition.** Detect Insufficient Funds detects a presented debit item exceeding available balance.
**Also known as:** Identify Shortfall, Insufficient Funds Detection Step.

## Relationships
- Detect Insufficient Funds is defined in the Overdraft Servicing process.
- Detect Insufficient Funds causes Check Overdraft Opt-In.
- Detect Insufficient Funds depends on the Core Banking Processing capability.
- Detect Insufficient Funds mentions Overdraft Operations Analyst.
- Detect Insufficient Funds mentions Overdraft Triggered Event.

## Details
The Overdraft Operations Analyst detects the shortfall when a debit item exceeds available balance. Controls include available-balance accuracy; the Overdraft Triggered Event is raised on detection.

## References
- [HelpWithMyBank NSF and overdraft](https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html)
