---
id: bank-statement-message
title: Bank Statement Message
type: artifact
domain: Payments
aliases: ["Camt.053 Statement", "Account Statement"]
status: draft
sources: ["https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html"]
---

# Bank Statement Message

**Definition.** Bank Statement Message is the account statement or reporting message used for reconciliation and positioning, such as ISO 20022 camt.053, camt.052 or MT940. Bank Statement Message is the artifact ingested across reconciliation and settlement and cash management.

**Also known as:** Camt.053 Statement, Account Statement.

## Relationships
- Bank Statement Message is related to the Payments domain.
- Bank Statement Message mentions Ingest Bank Statement.
- Bank Statement Message mentions Aggregate Balances.
- Bank Statement Message is related to Account Reconciliation.
- Bank Statement Message is related to ISO 20022.

## Details
Bank Statement Message reports booked and intraday entries on nostro and clearing accounts. It is loaded during the Ingest Bank Statement step, where completeness and sequence are checked, then matched against internal records. In treasury, the same artifact feeds balance aggregation and cash positioning across accounts and currencies.

## References
- https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html
