---
id: ingest-bank-statement
title: Ingest Bank Statement
type: process-step
process: Reconciliation & Settlement
order: 2
aliases: ["Load Statement", "Statement Ingestion"]
status: draft
sources: ["https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html", "https://validatefin.com/en/blog/camt053-bank-statement"]
---

# Ingest Bank Statement

**Definition.** Ingest Bank Statement loads end-of-day and intraday statements (camt.053, camt.052, MT940) from nostro and clearing accounts.
**Also known as:** Load Statement, Statement Ingestion.

## Relationships
- Ingest Bank Statement is defined in the Reconciliation & Settlement process.
- Ingest Bank Statement causes Match Transactions.
- Ingest Bank Statement depends on the Integration Platform capability.
- Ingest Bank Statement mentions Reconciliation Analyst.
- Ingest Bank Statement mentions Bank Statement Message.

## Details
The Reconciliation Analyst loads statements into reconciliation. Inputs are the Bank Statement Message; outputs are loaded statement data. Controls include completeness and sequence checks across statement messages.

## References
- [camt.053/camt.052 statements](https://corporates.dzbank.com/content/firmenkunden/en/homepage/products/transaction-banking/national-international_payments/iso-20022/camt-053-52.html)
- [camt.053 bank statement](https://validatefin.com/en/blog/camt053-bank-statement)
