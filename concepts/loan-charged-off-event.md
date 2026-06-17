---
id: loan-charged-off-event
title: Loan Charged Off Event
type: event
domain: Lending & Credit
aliases: ["Charge-Off Event", "Write-Off Event"]
status: draft
sources: ["https://en.wikipedia.org/wiki/Charge-off", "https://www.debt.org/credit/collection-agencies/debt-collectors/"]
---

# Loan Charged Off Event

**Definition.** Loan Charged Off Event is the business event recording the write-off of an uncollectable loan to recovery. Loan Charged Off Event marks the accounting recognition that a debt is unlikely to be collected.

**Also known as:** Charge-Off Event, Write-Off Event.

## Relationships
- Loan Charged Off Event is related to the Lending & Credit domain.
- Loan Charged Off Event causes Charge Off Debt.
- Loan Charged Off Event mentions Loan Collections.
- Loan Charged Off Event mentions Late-Stage Recovery.

## Details
Loan Charged Off Event fires when the Recovery Officer writes the debt off as uncollectable, typically after the account is around 180 days past due, carrying the outstanding balance, charge-off date and reason. The event is raised at Charge Off Debt in the Loan Collections flow under charge-off policy and accounting controls. It moves the account to internal recovery or external agency placement and is reported for provisioning and regulatory purposes while collection efforts may continue.

## References
- https://en.wikipedia.org/wiki/Charge-off
- https://www.debt.org/credit/collection-agencies/debt-collectors/
