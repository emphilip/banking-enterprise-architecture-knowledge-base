---
id: service-maintenance-request
title: Service Maintenance Request
type: artifact
domain: Deposits & Accounts
aliases: ["Account Maintenance Request", "Servicing Request"]
status: draft
sources: ["https://www.associatedbank.com/forms-and-disclosures/disclosures/deposit-account-agreement", "https://openonline.53.com/product/service/apply/document/depositAccountRules"]
---

# Service Maintenance Request

**Definition.** Service Maintenance Request is the request to change account static data, mandate, stop payment or standing instruction on an open deposit account. Service Maintenance Request is the input artifact that initiates the account-maintenance flow.

**Also known as:** Account Maintenance Request, Servicing Request.

## Relationships
- Service Maintenance Request is related to the Deposits & Accounts domain.
- Service Maintenance Request mentions Receive Maintenance Request.
- Service Maintenance Request mentions Maintenance Intake & Verification.

## Details
Service Maintenance Request captures the account identifier, the requested change such as address update, mandate or signatory amendment, stop payment, or standing-instruction setup, and the requester's identity. Service Maintenance Request is logged and the requester's signatory authority is verified against the Signature Card before execution. Changes that move account terms require a Reg DD change-in-terms notice, and static-data changes are applied under dual control.

## References
- https://www.associatedbank.com/forms-and-disclosures/disclosures/deposit-account-agreement
- https://openonline.53.com/product/service/apply/document/depositAccountRules
