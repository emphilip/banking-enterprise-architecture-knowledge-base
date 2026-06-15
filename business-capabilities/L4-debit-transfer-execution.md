---
id: debit-transfer-execution
title: Debit Transfer Execution
type: business-capability
domain: Payments
level: L4
aliases: ["ACH Debit", "Pull Payment"]
status: draft
sources: ["https://achdevguide.nacha.org/how-ach-works", "https://www.southstatebank.com/commercial/treasury-management/payables/ach-payments/ach-details"]
---

# Debit Transfer Execution

**Definition.** Debit Transfer Execution performs domestic pull debit transfers such as Nacha ACH debits (WEB, PPD, CCD) initiated by the receiver-authorised originator, within the BIAN Payment Execution service domain.
**Also known as:** ACH Debit, Pull Payment.

## Relationships
- Debit Transfer Execution is defined in the Payments domain.
- Debit Transfer Execution is derived from Domestic Payments.
- Debit Transfer Execution depends on the Payment Orchestration capability.

## Details
Debit Transfer Execution grounds in the BIAN Payment Execution service domain. It performs domestic pull debit transfers such as Nacha ACH debits across WEB, PPD and CCD entry types, initiated by the receiver-authorised originator. It assembles and submits the debit entries to the domestic rail.

## References
- [Nacha ACH Developer Guide](https://achdevguide.nacha.org/how-ach-works)
- [ACH Details](https://www.southstatebank.com/commercial/treasury-management/payables/ach-payments/ach-details)
