---
id: payment-message-transformer
title: Payment Message Transformer
type: technology-capability
domain: Core Processing
level: L2
aliases: ["Message Transformation", "ISO 20022 Translation", "Payment Message Transformation"]
status: draft
sources: ["https://www.bottomline.com/uk/payments-connectivity-compliance-financial-institutions/message-transformation-and-enrichment", "https://www.volantetech.com/iso-20022-services/", "https://www.swift.com/standards/iso-20022"]
---

# Payment Message Transformer

**Definition.** Payment Message Transformer is the technology capability that performs canonical normalization, format transformation and data enrichment of payment messages across standards such as ISO 20022 MX, ISO 8583, SWIFT MT and NACHA, including MT/MX coexistence and truncation handling.
**Also known as:** Message Transformation, ISO 20022 Translation, Payment Message Transformation.

## Relationships
- Payment Message Transformer is defined in the Core Processing domain.
- Payment Message Transformer is derived from Payment Orchestration.
- Payment Message Transformer is related to Payment Validation Engine.
- Payment Message Transformer mentions ISO 20022.

## Details
Payment Message Transformer normalizes inbound and outbound payment messages to a canonical internal model and transforms them to the formats required by each scheme, enriching data as needed. It handles MT/MX coexistence and field truncation during the ISO 20022 migration, drawing on capabilities such as Bottomline message transformation and Volante ISO 20022 services.

## References
- [Bottomline Message Transformation and Enrichment](https://www.bottomline.com/uk/payments-connectivity-compliance-financial-institutions/message-transformation-and-enrichment)
- [Volante ISO 20022 Services](https://www.volantetech.com/iso-20022-services/)
- [SWIFT ISO 20022](https://www.swift.com/standards/iso-20022)
