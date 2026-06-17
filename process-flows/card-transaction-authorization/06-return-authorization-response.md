---
id: return-authorization-response
title: Return Authorization Response
type: process-step
process: Card Transaction Authorization
order: 6
status: draft
sources: ["https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html"]
---

# Return Authorization Response

**Definition.** Return Authorization Response generates the ARPC and returns the decision to the acquirer via the scheme, emitting the Authorization Approved Event.

## Relationships
- Return Authorization Response is defined in the Card Transaction Authorization process.
- Return Authorization Response causes Post Cleared Transaction.
- Return Authorization Response depends on the Card Processing capability.
- Return Authorization Response mentions Authorization Approved Event.
- Return Authorization Response mentions Card Operations Analyst.

## Details
Return Authorization Response generates the ARPC cryptogram, routes the decision back to the acquirer through the scheme within response-timing limits, and raises the Authorization Approved Event on approval.

## References
- [ARQC validation for issuers](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/use-cases-issuers.generalfunctions.arqc.html)
