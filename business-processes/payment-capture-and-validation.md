---
id: payment-capture-and-validation
title: Payment Capture & Validation
type: business-process
domain: Payments
aliases: ["Payment Intake", "Capture & Validation"]
status: draft
sources: ["https://achdevguide.nacha.org/how-ach-works", "https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/"]
---

# Payment Capture & Validation

**Definition.** Payment Capture & Validation receives, enriches and validates inbound payment instructions before they enter execution.
**Also known as:** Payment Intake, Capture & Validation.

## Relationships
- Payment Capture & Validation is derived from Payment Processing.
- Payment Capture & Validation is defined in the Payments domain.
- Payment Capture & Validation depends on the Payment Orchestration capability.

## Details
The sub-process is performed by the Payment Operations Analyst. Inputs are the inbound Payment Instruction; outputs are a validated payment order ready for authorization. Controls include schema/format validation and duplicate checking to prevent erroneous or repeated payments entering the flow.

## References
- [Nacha ACH Dev Guide](https://achdevguide.nacha.org/how-ach-works)
- [ISO 20022 pain messages](https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/)
