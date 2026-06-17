---
id: render-loan-decision
title: Render Loan Decision
type: process-step
process: Loan Origination Workflow
order: 5
aliases: ["Decide Loan", "Loan Adjudication Step"]
status: draft
sources: ["https://www.fundingo.com/loan-origination-the-seven-stages/", "https://www.decisivedge.com/blog/7-stages-in-loan-origination/"]
---

# Render Loan Decision

**Definition.** Render Loan Decision applies policy and scoring to approve, decline or refer the application.
**Also known as:** Decide Loan, Loan Adjudication Step.

## Relationships
- Render Loan Decision is defined in the Loan Origination Workflow process.
- Render Loan Decision causes Issue Loan Offer.
- Render Loan Decision depends on the Credit Decisioning Engine capability.
- Render Loan Decision mentions Loan Officer.
- Render Loan Decision mentions Credit Decision.

## Details
The Loan Officer renders the decision. Inputs are the verified loan file; outputs are a Credit Decision. Controls include credit policy and delegated authority. The decision branches on approve, decline or refer, and emits a Credit Decision Issued Event.

## References
- [Fundingo: the seven stages of loan origination](https://www.fundingo.com/loan-origination-the-seven-stages/)
- [DecisiveEdge: 7 stages in loan origination](https://www.decisivedge.com/blog/7-stages-in-loan-origination/)
