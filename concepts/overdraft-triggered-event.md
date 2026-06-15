---
id: overdraft-triggered-event
title: Overdraft Triggered Event
type: event
domain: Deposits & Accounts
aliases: ["Insufficient Funds Event", "NSF Triggered Event"]
status: draft
sources: ["https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html", "https://www.consumerfinance.gov/about-us/blog/new-insights-on-bank-overdraft-fees-and-4-ways-to-avoid-them/"]
---

# Overdraft Triggered Event

**Definition.** Overdraft Triggered Event is the business event raised when a presented debit item exceeds the available balance on a deposit account. Overdraft Triggered Event begins overdraft and NSF decisioning in account servicing.

**Also known as:** Insufficient Funds Event, NSF Triggered Event.

## Relationships
- Overdraft Triggered Event is related to the Deposits & Accounts domain.
- Overdraft Triggered Event mentions Overdraft Servicing.
- Overdraft Triggered Event causes Detect Insufficient Funds.

## Details
Overdraft Triggered Event fires when posting evaluates a debit item against available balance and finds a shortfall, carrying the account identifier, item amount, item type and shortfall value. Overdraft Triggered Event drives the Reg E opt-in check for one-time debit and ATM items, the coverage-limit evaluation, and the pay-or-return decision. When the item is paid into overdraft, the event leads to assessment of the disclosed Overdraft Fee and a customer notice.

## References
- https://www.helpwithmybank.gov/help-topics/bank-accounts/nsf-fees-overdraft-protection/index-nsf-fees-overdraft-protection.html
- https://www.consumerfinance.gov/about-us/blog/new-insights-on-bank-overdraft-fees-and-4-ways-to-avoid-them/
