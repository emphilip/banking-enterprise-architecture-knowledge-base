---
id: authenticate-requester
title: Authenticate Requester
type: process-step
process: Service Request Handling
order: 2
aliases: ["Verify Requester", "Requester Authentication Step"]
status: draft
sources: ["https://www.bland.ai/blog/customer-request-triage", "https://www.checkfile.ai/en-US/blog/bank-customer-onboarding-kyc-verification"]
---

# Authenticate Requester

**Definition.** Authenticate Requester verifies the requester's identity and entitlement to act on the account before any change is actioned.
**Also known as:** Verify Requester, Requester Authentication Step.

## Relationships
- Authenticate Requester is defined in the Service Request Handling process.
- Authenticate Requester causes Categorize Request.
- Authenticate Requester depends on the Identity Access Management capability.
- Authenticate Requester mentions Service Advisor.
- Authenticate Requester mentions Service Request Ticket.

## Details
The Service Advisor verifies the requester on the Service Request Ticket. Inputs are the logged request; outputs are a verified requester. The requester authentication and entitlement check branches across verified, step-up and reject.

## References
- [Bland customer request triage](https://www.bland.ai/blog/customer-request-triage)
- [Checkfile KYC verification](https://www.checkfile.ai/en-US/blog/bank-customer-onboarding-kyc-verification)
