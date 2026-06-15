---
id: real-time-payments
title: Real-Time Payments
type: business-capability
domain: Payments
level: L3
aliases: ["RTP", "Instant Payments"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Real-Time Payments

**Definition.** Real-Time Payments is the L3 business capability for executing instant, irrevocable transfers with immediate clearing and confirmation, over rails such as RTP, FedNow, and SEPA Instant.
**Also known as:** RTP, Instant Payments.

## Relationships
- Real-Time Payments is defined in the Payments domain.
- Real-Time Payments is derived from Payment Execution.
- Real-Time Payments depends on the Data Streaming capability.
- Real-Time Payments depends on the Payment Orchestration capability.

## Details
Real-Time Payments aligns to BIAN Payment Execution and Payment Order service domains operating under 24x7 instant scheme rules. Typical sub-functions include sub-second authorisation, liquidity checks, instant confirmation, and request-to-pay handling. It relies on event-streaming infrastructure for low-latency processing and on payment orchestration for scheme routing. ISO 20022 is the native message standard for instant rails.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
