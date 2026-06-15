---
id: route-payment
title: Route Payment
type: process-step
process: Payment Processing
order: 5
aliases: ["Rail Selection", "Payment Routing Step"]
status: draft
sources: ["https://fedwireservice.org/", "https://www.moderntreasury.com/journal/interoperability-between-rtp-and-fednow"]
---

# Route Payment

**Definition.** Route Payment selects the clearing rail (ACH, Fedwire, RTP/FedNow, SWIFT) based on amount, speed and destination.
**Also known as:** Rail Selection, Payment Routing Step.

## Relationships
- Route Payment is defined in the Payment Processing process.
- Route Payment causes Format Clearing Message.
- Route Payment depends on the Payment Orchestration capability.
- Route Payment mentions Payment Operations Analyst.

## Details
The Payment Operations Analyst selects the rail for the authorized payment. Inputs are the authorized payment; outputs are a routed payment. Controls are rail eligibility rules, branching across ACH versus wire versus instant rails.

## References
- [Fedwire Funds Service](https://fedwireservice.org/)
- [RTP and FedNow interoperability](https://www.moderntreasury.com/journal/interoperability-between-rtp-and-fednow)
