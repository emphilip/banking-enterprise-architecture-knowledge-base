---
id: credit-transfer-execution
title: Credit Transfer Execution
type: business-capability
domain: Payments
level: L4
aliases: ["ACH Credit", "Direct Credit", "Push Payment"]
status: draft
sources: ["https://achdevguide.nacha.org/how-ach-works", "https://www.modulrfinance.com/blog-insights/what-is-bacs"]
---

# Credit Transfer Execution

**Definition.** Credit Transfer Execution performs domestic push credit transfers such as Nacha ACH credits and Bacs Direct Credit through to rail submission, realising the credit-transfer mechanics of the BIAN Payment Execution service domain.
**Also known as:** ACH Credit, Direct Credit, Push Payment.

## Relationships
- Credit Transfer Execution is defined in the Payments domain.
- Credit Transfer Execution is derived from Domestic Payments.
- Credit Transfer Execution depends on the Payment Orchestration capability.

## Details
Credit Transfer Execution grounds in the credit-transfer mechanics of the BIAN Payment Execution service domain. It performs domestic push credit transfers such as Nacha ACH credits and Bacs Direct Credit through to rail submission. It assembles, formats and dispatches the credit entries to the appropriate domestic rail.

## References
- [Nacha ACH Developer Guide](https://achdevguide.nacha.org/how-ach-works)
- [What is Bacs](https://www.modulrfinance.com/blog-insights/what-is-bacs)
