---
id: submit-to-clearing
title: Submit To Clearing
type: process-step
process: Payment Processing
order: 7
aliases: ["Dispatch To Operator", "Rail Submission Step"]
status: draft
sources: ["https://achdevguide.nacha.org/how-ach-works", "https://fedwireservice.org/"]
---

# Submit To Clearing

**Definition.** Submit To Clearing transmits the clearing message/batch to the ACH operator, Fedwire, or RTP/FedNow within cut-off windows.
**Also known as:** Dispatch To Operator, Rail Submission Step.

## Relationships
- Submit To Clearing is defined in the Payment Processing process.
- Submit To Clearing causes Capture Clearing Response.
- Submit To Clearing depends on the Payment Orchestration capability.
- Submit To Clearing mentions Clearing Operations Specialist.
- Submit To Clearing mentions Cut-Off Reached Event.

## Details
The Clearing Operations Specialist transmits the Clearing Message to the operator. Inputs are the Clearing Message; outputs are a submitted clearing batch. The Cut-Off Reached Event gates submission. Controls include cut-off enforcement and transmission acknowledgement.

## References
- [Nacha ACH Dev Guide](https://achdevguide.nacha.org/how-ach-works)
- [Fedwire Funds Service](https://fedwireservice.org/)
