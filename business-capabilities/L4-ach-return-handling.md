---
id: ach-return-handling
title: ACH Return Handling
type: business-capability
domain: Payments
level: L4
aliases: ["ACH Returns", "Return Codes", "R-codes"]
status: draft
sources: ["https://www.dwolla.com/updates/understanding-ach-return-process", "https://achdevguide.nacha.org/how-ach-works"]
---

# ACH Return Handling

**Definition.** ACH Return Handling processes returned and reversed ACH entries within Nacha return time-frames (including extended consumer unauthorised windows) and posts adjustments, within the BIAN Payment Execution service domain.
**Also known as:** ACH Returns, Return Codes, R-codes.

## Relationships
- ACH Return Handling is defined in the Payments domain.
- ACH Return Handling is derived from Domestic Payments.
- ACH Return Handling depends on the Payment Orchestration capability.

## Details
ACH Return Handling grounds in the BIAN Payment Execution service domain. It processes returned and reversed ACH entries within Nacha return time-frames, including the extended consumer unauthorised windows, and posts the corresponding adjustments. It interprets R-codes and routes items for reprocessing or notification.

## References
- [Understanding the ACH Return Process](https://www.dwolla.com/updates/understanding-ach-return-process)
- [Nacha ACH Developer Guide](https://achdevguide.nacha.org/how-ach-works)
