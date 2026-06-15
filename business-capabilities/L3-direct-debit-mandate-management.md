---
id: direct-debit-mandate-management
title: Direct Debit Mandate Management
type: business-capability
domain: Payments
level: L3
aliases: ["Mandate Management", "DDI Setup"]
status: draft
sources: ["https://www.iso20022.org/catalogue-messages/iso-20022-messages-archive?search=pain", "https://gocardless.com/en-us/guides/posts/bacs-payments"]
---

# Direct Debit Mandate Management

**Definition.** Direct Debit Mandate Management establishes, amends and cancels creditor mandates and authorisations (ISO 20022 pain.009/010/011 for SEPA; Bacs uses the AUDDIS service), mapping to the BIAN Direct Debit Mandate service domain.
**Also known as:** Mandate Management, DDI Setup.

## Relationships
- Direct Debit Mandate Management is defined in the Payments domain.
- Direct Debit Mandate Management is derived from Direct Debit Management.
- Direct Debit Mandate Management depends on the Document Management capability.

## Details
Direct Debit Mandate Management grounds in the BIAN Direct Debit Mandate service domain. It establishes, amends and cancels creditor mandates and authorisations using ISO 20022 pain.009/010/011 for SEPA mandates, while Bacs mandates are handled through the AUDDIS service. Mandate documents and audit trails are retained for the lifetime of the authorisation.

## References
- [ISO 20022 pain messages](https://www.iso20022.org/catalogue-messages/iso-20022-messages-archive?search=pain)
- [GoCardless Bacs Payments Guide](https://gocardless.com/en-us/guides/posts/bacs-payments)
