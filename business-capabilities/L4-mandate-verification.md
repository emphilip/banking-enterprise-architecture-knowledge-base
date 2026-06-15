---
id: mandate-verification
title: Mandate Verification
type: business-capability
domain: Payments
level: L4
aliases: ["Mandate Check", "Authorisation Check"]
status: draft
sources: ["https://developer.huntington.com/enterprisepayments/docs/iso-pain008", "https://deepwiki.com/bian-official/public/5.1-payment-operations"]
---

# Mandate Verification

**Definition.** Mandate Verification confirms that a valid, in-force mandate exists for each collection item before submission, realising the mandate-check step of the BIAN Direct Debit service domain.
**Also known as:** Mandate Check, Authorisation Check.

## Relationships
- Mandate Verification is defined in the Payments domain.
- Mandate Verification is derived from Direct Debit Collection.
- Mandate Verification depends on the Document Management capability.

## Details
Mandate Verification grounds in the mandate-check step of the BIAN Direct Debit service domain. It confirms that a valid, in-force mandate exists for each collection item before submission. It retrieves and checks mandate records and status, blocking collections without a valid authorisation.

## References
- [ISO pain.008 Reference](https://developer.huntington.com/enterprisepayments/docs/iso-pain008)
- [BIAN Payment Operations](https://deepwiki.com/bian-official/public/5.1-payment-operations)
