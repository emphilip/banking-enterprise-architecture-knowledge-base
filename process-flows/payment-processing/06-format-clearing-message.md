---
id: format-clearing-message
title: Format Clearing Message
type: process-step
process: Payment Processing
order: 6
aliases: ["Build Clearing Message", "Message Formatting"]
status: draft
sources: ["https://www.iso20022payments.com/cbpr/pacs-008-serial-method/", "https://achdevguide.nacha.org/how-ach-works"]
---

# Format Clearing Message

**Definition.** Format Clearing Message transforms the routed payment into the rail-specific message (Nacha entry, pacs.008, Fedwire format).
**Also known as:** Build Clearing Message, Message Formatting.

## Relationships
- Format Clearing Message is defined in the Payment Processing process.
- Format Clearing Message causes Submit To Clearing.
- Format Clearing Message depends on the Payment Orchestration capability.
- Format Clearing Message mentions Clearing Operations Specialist.
- Format Clearing Message mentions Clearing Message.

## Details
The Clearing Operations Specialist transforms the routed payment into the rail message. Inputs are the routed payment; outputs are the Clearing Message. Controls include message integrity and format validation against the scheme specification.

## References
- [CBPR+ pacs.008 serial method](https://www.iso20022payments.com/cbpr/pacs-008-serial-method/)
- [Nacha ACH Dev Guide](https://achdevguide.nacha.org/how-ach-works)
