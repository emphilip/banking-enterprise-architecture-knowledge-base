---
id: same-day-ach-processing
title: Same Day ACH Processing
type: business-capability
domain: Payments
level: L4
aliases: ["SDA", "Same-Day ACH"]
status: draft
sources: ["https://www.usbank.com/corporate-and-commercial-banking/treasury-payment-solutions/treasury-management/same-day-ach.html", "https://achdevguide.nacha.org/how-ach-works"]
---

# Same Day ACH Processing

**Definition.** Same Day ACH Processing handles expedited intraday ACH settlement windows under Nacha rules (per-entry limits and submission cut-offs), a specialisation of domestic execution in the BIAN Payment Execution service domain.
**Also known as:** SDA, Same-Day ACH.

## Relationships
- Same Day ACH Processing is defined in the Payments domain.
- Same Day ACH Processing is derived from Domestic Payments.
- Same Day ACH Processing depends on the Payment Orchestration capability.

## Details
Same Day ACH Processing grounds in the BIAN Payment Execution service domain as a specialisation of domestic execution. It handles expedited intraday ACH settlement windows under Nacha rules, enforcing per-entry limits and submission cut-offs. It schedules entries to the correct same-day window.

## References
- [Same Day ACH](https://www.usbank.com/corporate-and-commercial-banking/treasury-payment-solutions/treasury-management/same-day-ach.html)
- [Nacha ACH Developer Guide](https://achdevguide.nacha.org/how-ach-works)
