---
id: payment-instruction
title: Payment Instruction
type: artifact
domain: Payments
aliases: ["Payment Order Request", "Pain.001 Message"]
status: draft
sources: ["https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/"]
---

# Payment Instruction

**Definition.** Payment Instruction is the customer or channel request to move funds, such as an ISO 20022 pain.001 message, a file or an API payload. Payment Instruction is the input artifact that opens the payment processing flow.

**Also known as:** Payment Order Request, Pain.001 Message.

## Relationships
- Payment Instruction is related to the Payments domain.
- Payment Instruction mentions Receive Payment Instruction.
- Payment Instruction mentions Payment Processing.
- Payment Instruction is related to Payment Initiation.
- Payment Instruction is related to ISO 20022.

## Details
Payment Instruction carries the debtor, creditor, amount, currency and remittance data needed to initiate a payment. It is captured and validated at the start of the Payment Processing flow, where format, mandatory fields, account validity and duplicates are checked before the instruction is enriched into a payment order for authorization and routing.

## References
- https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/
