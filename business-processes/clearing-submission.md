---
id: clearing-submission
title: Clearing Submission
type: business-process
domain: Payments
aliases: ["Rail Submission", "Clearing Dispatch"]
status: draft
sources: ["https://achdevguide.nacha.org/how-ach-works", "https://www.frbservices.org/financial-services/ach"]
---

# Clearing Submission

**Definition.** Clearing Submission formats and transmits cleared payments to the ACH operator, Fedwire, or RTP/FedNow.
**Also known as:** Rail Submission, Clearing Dispatch.

## Relationships
- Clearing Submission is derived from Payment Processing.
- Clearing Submission is defined in the Payments domain.
- Clearing Submission depends on the Payment Orchestration capability.

## Details
The sub-process is performed by the Clearing Operations Specialist. Inputs are the routed payment; outputs are the transmitted clearing message. Controls include cut-off enforcement and message integrity checks to ensure timely and correct delivery to the operator.

## References
- [Nacha ACH Dev Guide](https://achdevguide.nacha.org/how-ach-works)
- [Federal Reserve ACH services](https://www.frbservices.org/financial-services/ach)
