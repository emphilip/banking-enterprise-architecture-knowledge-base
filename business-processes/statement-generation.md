---
id: statement-generation
title: Statement Generation
type: business-process
domain: Deposits & Accounts
aliases: ["Statement Production"]
status: draft
---

# Statement Generation

**Definition.** Statement Generation is the process of producing periodic account statements, including transaction aggregation, formatting, and delivery across paper and digital channels.
**Also known as:** Statement Production.

## Relationships
- Statement Generation is defined in the Deposits & Accounts domain.
- Statement Generation depends on the Account Servicing capability.

## Details
Statement Generation gathers period transactions and balances, applies templates and disclosures, renders documents, and delivers them via the customer's preferred channel. Actors include account operations staff and customers. Systems involved include the core banking ledger, document and content services, and notification services.

## Flow
- Determine Statement Cycle causes Extract Account Activity.
- Extract Account Activity causes Reconcile Statement Data.
- Reconcile Statement Data causes Assemble Statement Document.
- Assemble Statement Document causes Render Statement Output.
- Render Statement Output causes Deliver Statement.
- Deliver Statement causes Archive Statement.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
