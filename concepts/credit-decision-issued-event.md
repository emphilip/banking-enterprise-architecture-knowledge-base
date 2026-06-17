---
id: credit-decision-issued-event
title: Credit Decision Issued Event
type: event
domain: Lending & Credit
aliases: ["Decision Rendered Event", "Adjudication Complete Event"]
status: draft
sources: ["https://www.ltfinance.com/blog/personal-loan/underwriting-meaning-process-loans", "https://www.fundingo.com/loan-origination-the-seven-stages/"]
---

# Credit Decision Issued Event

**Definition.** Credit Decision Issued Event is the business event signalling an approve, decline or refer outcome from underwriting. Credit Decision Issued Event closes adjudication and unblocks the offer stage.

**Also known as:** Decision Rendered Event, Adjudication Complete Event.

## Relationships
- Credit Decision Issued Event is related to the Lending & Credit domain.
- Credit Decision Issued Event causes Issue Loan Offer.
- Credit Decision Issued Event mentions Credit Underwriting.
- Credit Decision Issued Event mentions Adjudicate Credit.

## Details
Credit Decision Issued Event fires when the Credit Underwriter renders the approve, conditionally approve, decline or refer decision in the Credit Underwriting flow, carrying the outcome, terms, pricing and any conditions. On approval the event triggers Issue Loan Offer in the Loan Origination Workflow; on decline it triggers adverse-action notification. The event records the decision under delegated authority and four-eyes controls and is the audit anchor linking underwriting to offer issuance.

## References
- https://www.ltfinance.com/blog/personal-loan/underwriting-meaning-process-loans
- https://www.fundingo.com/loan-origination-the-seven-stages/
