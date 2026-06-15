---
id: receive-payment-instruction
title: Receive Payment Instruction
type: process-step
process: Payment Processing
order: 1
aliases: ["Capture Instruction", "Intake Payment"]
status: draft
sources: ["https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/", "https://achdevguide.nacha.org/how-ach-works"]
---

# Receive Payment Instruction

**Definition.** Receive Payment Instruction captures an inbound payment instruction from a channel or corporate.
**Also known as:** Capture Instruction, Intake Payment.

## Relationships
- Receive Payment Instruction is defined in the Payment Processing process.
- Receive Payment Instruction causes Validate Payment.
- Receive Payment Instruction depends on the Payment Orchestration capability.
- Receive Payment Instruction mentions Payment Operations Analyst.
- Receive Payment Instruction mentions Payment Instruction.

## Details
The Payment Operations Analyst captures an inbound payment instruction (e.g. ISO 20022 pain.001, file, or API call). Inputs are the Payment Instruction; outputs are a raw payment order. The Payment Initiated Event is raised on acceptance. Controls include channel authentication and intake logging.

## References
- [ISO 20022 pain messages](https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/)
- [Nacha ACH Dev Guide](https://achdevguide.nacha.org/how-ach-works)
