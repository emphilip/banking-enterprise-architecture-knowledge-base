---
id: validate-payment
title: Validate Payment
type: process-step
process: Payment Processing
order: 2
aliases: ["Payment Validation", "Field Validation"]
status: draft
sources: ["https://www.iso20022payments.com/cbpr/pacs-008-serial-method/", "https://achdevguide.nacha.org/how-ach-works"]
---

# Validate Payment

**Definition.** Validate Payment checks format/schema, mandatory fields, account validity and duplicates, rejecting or requesting repair on failure.
**Also known as:** Payment Validation, Field Validation.

## Relationships
- Validate Payment is defined in the Payment Processing process.
- Validate Payment causes Screen Sanctions.
- Validate Payment depends on the Payment Orchestration capability.
- Validate Payment mentions Payment Operations Analyst.

## Details
The Payment Operations Analyst validates the raw payment order. Inputs are the raw payment order; outputs are a validated payment order. Controls include schema validation and duplicate/dedupe checks. The decision branch rejects invalid payments versus accepting valid ones for downstream screening.

## References
- [CBPR+ pacs.008 serial method](https://www.iso20022payments.com/cbpr/pacs-008-serial-method/)
- [Nacha ACH Dev Guide](https://achdevguide.nacha.org/how-ach-works)
