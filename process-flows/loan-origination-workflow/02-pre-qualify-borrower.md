---
id: pre-qualify-borrower
title: Pre-Qualify Borrower
type: process-step
process: Loan Origination Workflow
order: 2
aliases: ["Soft Eligibility Check", "Prequal Step"]
status: draft
sources: ["https://www.cflowapps.com/loan-origination-system-workflow/", "https://www.decisivedge.com/blog/7-stages-in-loan-origination/"]
---

# Pre-Qualify Borrower

**Definition.** Pre-Qualify Borrower runs a soft eligibility check against minimum criteria to confirm the borrower can proceed.
**Also known as:** Soft Eligibility Check, Prequal Step.

## Relationships
- Pre-Qualify Borrower is defined in the Loan Origination Workflow process.
- Pre-Qualify Borrower causes Collect Supporting Documents.
- Pre-Qualify Borrower depends on the Credit Decisioning Engine capability.
- Pre-Qualify Borrower mentions Loan Officer.

## Details
The Loan Officer runs the soft check. Inputs are the captured loan file; outputs are a pre-qualified application. Controls include soft-pull policy, eligibility thresholds and an adverse-action note where declined. This step branches to exit when minimum criteria are not met.

## References
- [Cflow: loan origination system workflow](https://www.cflowapps.com/loan-origination-system-workflow/)
- [DecisiveEdge: 7 stages in loan origination](https://www.decisivedge.com/blog/7-stages-in-loan-origination/)
