---
id: authorize-payment
title: Authorize Payment
type: process-step
process: Payment Processing
order: 4
aliases: ["Payment Authorization Step", "Approve Payment"]
status: draft
sources: ["https://achdevguide.nacha.org/how-ach-works", "https://fedwireservice.org/"]
---

# Authorize Payment

**Definition.** Authorize Payment applies fraud scoring, limit checks and funds/credit availability, then approves, holds or declines the payment.
**Also known as:** Payment Authorization Step, Approve Payment.

## Relationships
- Authorize Payment is defined in the Payment Processing process.
- Authorize Payment causes Route Payment.
- Authorize Payment depends on the Fraud Analytics capability.
- Authorize Payment mentions Payment Operations Analyst.

## Details
The Payment Operations Analyst authorizes the screened payment order. Inputs are the screened payment order; outputs are an authorized payment. Controls include fraud checks, exposure/limit checks and funds availability. The decision branches across approve, hold or decline.

## References
- [Nacha ACH Dev Guide](https://achdevguide.nacha.org/how-ach-works)
- [Fedwire Funds Service](https://fedwireservice.org/)
