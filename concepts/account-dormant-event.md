---
id: account-dormant-event
title: Account Dormant Event
type: event
domain: Deposits & Accounts
aliases: ["Dormancy Triggered Event", "Inactivity Detected Event"]
status: draft
sources: ["https://www.incharge.org/blog/what-happens-to-dormant-bank-accounts/", "https://www.mtb.com/personal/checking-accounts/tips-on-managing-your-account/abandoned-funds"]
---

# Account Dormant Event

**Definition.** Account Dormant Event is the business event raised when a deposit account exceeds its dormancy period without customer-initiated activity. Account Dormant Event begins the dormancy and escheatment branch of the account lifecycle.

**Also known as:** Dormancy Triggered Event, Inactivity Detected Event.

## Relationships
- Account Dormant Event is related to the Deposits & Accounts domain.
- Account Dormant Event mentions Dormancy Management.
- Account Dormant Event causes Issue Dormancy Notice.

## Details
Account Dormant Event fires when inactivity detection finds no customer-initiated transactions for the statutory dormancy interval, carrying the account identifier, last-activity date and balance. Account Dormant Event flags the account as dormant, suppresses certain fees, and triggers Issue Dormancy Notice so the Unclaimed Property Officer can attempt contact before escheatment. Failure to reactivate within the abandonment window leads to escheatment of the unclaimed balance to the state.

## References
- https://www.incharge.org/blog/what-happens-to-dormant-bank-accounts/
- https://www.mtb.com/personal/checking-accounts/tips-on-managing-your-account/abandoned-funds
