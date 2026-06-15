---
id: disburse-loan-funds
title: Disburse Loan Funds
type: process-step
process: Loan Origination Workflow
order: 7
aliases: ["Fund Loan", "Disbursement Step"]
status: draft
sources: ["https://www.fundingo.com/loan-origination-the-seven-stages/", "https://nortridge.com/blog/loan-processing-workflow/"]
---

# Disburse Loan Funds

**Definition.** Disburse Loan Funds executes the loan agreement and releases funds, booking the loan to the core ledger.
**Also known as:** Fund Loan, Disbursement Step.

## Relationships
- Disburse Loan Funds is defined in the Loan Origination Workflow process.
- Disburse Loan Funds depends on the Core Banking Processing capability.
- Disburse Loan Funds mentions Loan Officer.
- Disburse Loan Funds mentions Loan Agreement.

## Details
The Loan Officer executes funding. Inputs are the Loan Agreement; outputs are a disbursed loan. Controls include four-eyes on disbursement, agreement execution and funding reconciliation. This terminal step emits the Loan Funded Event.

## References
- [Fundingo: the seven stages of loan origination](https://www.fundingo.com/loan-origination-the-seven-stages/)
- [Nortridge: loan processing workflow](https://nortridge.com/blog/loan-processing-workflow/)
