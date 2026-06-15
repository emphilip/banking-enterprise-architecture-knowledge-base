---
id: account-statement-generator
title: Account Statement Generator
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Statement Engine", "Statement Production Service", "Statement Generator"]
status: draft
sources: ["https://www.iso20022.org/iso-20022-message-definitions", "https://www.alogent.com/banking-definitions/core-banking-systems"]
---

# Account Statement Generator

**Definition.** Account Statement Generator is the technology capability that produces periodic and on-demand account statements and transaction histories, including ISO 20022 camt.05x messages, assembling balances, postings, interest and fees for delivery to channels and document services.
**Also known as:** Statement Engine, Statement Production Service, Statement Generator.

## Relationships
- Account Statement Generator is defined in the Core Processing domain.
- Account Statement Generator is derived from Core Banking Processing.
- Account Statement Generator depends on Document Management.
- Account Statement Generator is related to Statement Generation.

## Details
Account Statement Generator assembles balances, postings, interest and fees into periodic and on-demand statements and transaction histories. ISO 20022 defines the camt.05x bank-to-customer statement messages that standardise this output, and core-banking component models treat statement production as a core service, with rendered statements handed to document and content services for storage and delivery to channels.

## References
- [ISO 20022 message definitions](https://www.iso20022.org/iso-20022-message-definitions)
- [Alogent core banking systems definitions](https://www.alogent.com/banking-definitions/core-banking-systems)
