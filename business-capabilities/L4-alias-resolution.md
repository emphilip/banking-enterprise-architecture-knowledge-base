---
id: alias-resolution
title: Alias Resolution
type: business-capability
domain: Payments
level: L4
aliases: ["Proxy Lookup", "Directory Resolution"]
status: draft
sources: ["https://www.crossriver.com/insights/comparing-rtp-and-fednow", "https://www.aciworldwide.com/fednow"]
---

# Alias Resolution

**Definition.** Alias Resolution maps proxy identifiers (phone, email or handle) to the underlying account for instant payments, supporting addressing for real-time rails within the BIAN Payment Initiation and Payment Execution service domains.
**Also known as:** Proxy Lookup, Directory Resolution.

## Relationships
- Alias Resolution is defined in the Payments domain.
- Alias Resolution is derived from Real-Time Payments.
- Alias Resolution depends on the API Management capability.

## Details
Alias Resolution grounds in the BIAN Payment Initiation and Payment Execution service domains. It maps proxy identifiers such as phone, email or handle to the underlying account for instant payments. Directory lookups are typically exposed and consumed through APIs to resolve addressing before execution.

## References
- [Comparing RTP and FedNow](https://www.crossriver.com/insights/comparing-rtp-and-fednow)
- [ACI FedNow](https://www.aciworldwide.com/fednow)
