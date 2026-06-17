---
id: loan-funded-event
title: Loan Funded Event
type: event
domain: Lending & Credit
aliases: ["Disbursement Event", "Loan Booked Event"]
status: draft
sources: ["https://nortridge.com/blog/loan-processing-workflow/", "https://www.guildmortgage.com/blog/the-mortgage-loan-process-a-checklist-for-understanding-each-step/"]
---

# Loan Funded Event

**Definition.** Loan Funded Event is the business trigger marking disbursement and booking of loan funds, ending origination. Loan Funded Event records the moment the loan moves to servicing.

**Also known as:** Disbursement Event, Loan Booked Event.

## Relationships
- Loan Funded Event is related to the Lending & Credit domain.
- Loan Funded Event causes Disburse Loan Funds.
- Loan Funded Event mentions Loan Origination Workflow.
- Loan Funded Event mentions Fund Mortgage Loan.

## Details
Loan Funded Event fires when the loan agreement is executed and funds are released and booked to the core ledger, carrying the loan identifier, disbursed amount, value date and funding reference. It is raised at the end of Disburse Loan Funds in the Loan Origination Workflow and at Fund Mortgage Loan in the Mortgage Origination flow. The event closes origination, triggers funding reconciliation under four-eyes controls and hands the account to loan servicing for repayment scheduling.

## References
- https://nortridge.com/blog/loan-processing-workflow/
- https://www.guildmortgage.com/blog/the-mortgage-loan-process-a-checklist-for-understanding-each-step/
