---
id: payment-initiated-event
title: Payment Initiated Event
type: event
domain: Payments
aliases: ["Payment Received Event", "Instruction Received"]
status: draft
sources: ["https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/"]
---

# Payment Initiated Event

**Definition.** Payment Initiated Event is the trigger event raised when a payment instruction is received and accepted for processing. Payment Initiated Event starts the payment processing flow.

**Also known as:** Payment Received Event, Instruction Received.

## Relationships
- Payment Initiated Event is related to the Payments domain.
- Payment Initiated Event causes Receive Payment Instruction.
- Payment Initiated Event mentions Payment Processing.
- Payment Initiated Event is related to Payment Instruction.

## Details
Payment Initiated Event marks the arrival of a customer or channel request to move funds, whether as an ISO 20022 pain.001 message, a file or an API payload. The event signals payment operations to capture and validate the instruction, and is the entry point that downstream authorization, routing and clearing steps depend upon.

## References
- https://www.cashbook.com/understanding-iso-20022-and-pain-messages-a-complete-guide/
