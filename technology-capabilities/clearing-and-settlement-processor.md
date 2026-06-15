---
id: clearing-and-settlement-processor
title: Clearing & Settlement Processor
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Card Clearing Engine", "Interchange & Settlement Processor", "Presentment Processor"]
status: draft
sources: ["https://docs.fiserv.dev/private/docs/omnipay-boarding-intro", "https://medium.com/@umutt.akbulut/card-network-settlement-a-comprehensive-architectural-operational-and-distributed-systems-2de92a158b37"]
---

# Clearing & Settlement Processor

**Definition.** Clearing & Settlement Processor is the technology capability that processes incoming and outgoing scheme clearing files, matches presentments to prior authorizations, calculates interchange and scheme fees, and computes net settlement positions and funding with the card networks.
**Also known as:** Card Clearing Engine, Interchange & Settlement Processor, Presentment Processor.

## Relationships
- Clearing & Settlement Processor is defined in the Core Processing domain.
- Clearing & Settlement Processor is derived from Card Processing.
- Clearing & Settlement Processor depends on Card Account Ledger.
- Clearing & Settlement Processor is related to Card Authorization.

## Details
Clearing & Settlement Processor ingests Visa and Mastercard clearing files, matches each presentment to its earlier ISO 8583 authorization, and applies interchange and scheme fee qualification. It nets debits and credits into settlement positions, drives funding movements with the networks, and posts cleared amounts to the cardholder ledger. Fiserv OmniPay provides this clearing, settlement, billing and funding for acquirers and sponsor banks.

## References
- [Fiserv OmniPay Boarding Introduction](https://docs.fiserv.dev/private/docs/omnipay-boarding-intro)
- [Card Network Settlement Architecture](https://medium.com/@umutt.akbulut/card-network-settlement-a-comprehensive-architectural-operational-and-distributed-systems-2de92a158b37)
