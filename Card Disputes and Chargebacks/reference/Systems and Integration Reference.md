---
title: Systems and Integration Reference
type: reference
domain: banking-and-payments
tags: [reference, systems, integration, genericisation, disputes, chargebacks, card-platform, retail-banking]
aliases: [Systems Reference, Disputes Systems, Genericisation Map, System Roles]
---

# Systems and Integration Reference

The process flows in this library are **generalized** from a real Canadian card-issuer disputes & chargebacks program. Brand- and vendor-specific system names from the source deck's *Disputes – Systems* page have been abstracted to **generic system roles** so the content applies to an average Canadian retail card issuer. This note records those roles and the genericisation mapping.

## Generic System Roles

| Generic role | What it does in these flows | Capability home |
|---|---|---|
| **Disputes & chargeback management platform** | The claims/chargeback platform of record: logs disputes, holds claim cases, drives work-baskets and the chargeback lifecycle. Built on a workflow/BPM platform. Connected to the card-network APIs. | [[Case Management]] / [[Transaction Processing]] |
| **Card processing platform** | The transaction system of record: generates account and card numbers, holds transactions, processes chargebacks and reversals, manages loyalty, and calculates insurance premiums. | [[Transaction Processing]] / [[Servicing - Monetary]] |
| **Card-network dispute-management application** | The card network's application for managing inflight disputes between issuer and acquirer (first chargeback, second presentment, pre-compliance). | [[Transaction Processing]] |
| **Client servicing platform** | The main web-based client servicing platform; contact-centre UI with web services for IVR/digital; real-time updates/inquiries against the card platform; profile changes, lost/stolen, product changes. | Servicing / Channels |
| **Fraud management system** | Fraud management, detection, and case management; receives real-time notification and a monthly file from the customer information file for cardholders. | [[Fraud Management]] |
| **Workflow / BPM platform** | The case-management engine underlying the disputes platform (source: SmartDispute on PEGA PRPC). | Operations — Workflow & Rules |
| **Merchant-collaboration network** | A third-party network that lets issuers and merchants resolve disputes/credits before formal chargeback processing (source: Ethoca). | [[Settlement]] / [[Transaction Processing]] |
| **Customer information file (MDM)** | Enterprise customer master data feeding the fraud system (source: eCIF). | Enterprise Support — Books of Record |
| **Card network** | The payment network (source: Visa / MasterCard) whose rules govern chargeback rights, timeframes, fraud (SAFE) reporting, fee collection, and arbitration. | [[Transaction Processing]] / [[Settlement]] |
| **Fraud document repository** | Storage for fraud write-off approval forms (source: Fraud SharePoint). | Operations — Case Mgmt. |

## Genericisation Mapping (source → generic)

| Source name (CIBC / Capco deck) | Generalized to |
|---|---|
| CIBC | The bank / a generic Canadian retail card issuer |
| CRS (Claims Resolution System) | Disputes & chargeback management platform |
| SmartDispute / PEGA PRPC | Workflow / BPM platform (underlying CRS) |
| PRM | Fraud management system |
| PSP (Payment Servicing Platform) | Client servicing platform |
| MCOM / MasterCom | Card-network dispute-management application |
| TSYS / TS2 (Total System Services) | Card processing platform (transaction system of record) |
| Ethoca | Merchant-collaboration network |
| eCIF | Customer information file (MDM) |
| Visa / MasterCard / MC | Card network |
| SAFE | Network fraud reporting (SAFE) |
| ITR (inbound) | Fraud investigations team |
| RCS (Dispute Analyst) | Disputes operations team / dispute analyst |
| ESD | Escalations / specialist disputes team |
| DCC / COMPAS | Contact centre / servicing application |
| PA (Performance Auditor) | Performance Auditor (write-off/arbitration approver) |
| FO | Fraud Operations (approver) |
| Fraud SharePoint | Fraud document repository |
| MC Acquirer Basket | Network acquirer (work) basket |
| Global_Account_Support@mastercard.com | Card-network support mailbox |
| Client Care | Client care / complaints team |

## Integration Patterns Observed

- **Dual-system chargebacks.** A chargeback exists in both the **card processing platform** (issuer system of record) and the **card-network dispute-management application** (inflight issuer–acquirer tool); the disputes platform orchestrates both.
- **Status as a contract.** Chargeback status transitions (pending → rejected / processed) in the network application drive the next step; the disputes platform mirrors case status.
- **Provisional credit then reversal.** The cardholder is provisionally credited at dispute initiation; if a merchant credit later arrives (collaboration network), the provisional credit is reversed to avoid a double credit.
- **Authority-gated write-offs.** Write-offs are gated by dispute-analyst authority and, above a value threshold, by Performance-Auditor and Fraud-Operations approval evidenced in the fraud document repository.
- **Network-rule-driven.** Chargeback rights, timeframes (e.g., the 45-day question), SAFE reporting, fee collection, and arbitration are all governed by card-network rules — see [[Canadian Regulatory Context]].

## Related

[[Generic Multi-Functional Bank Capability Model]] · [[Glossary]] · [[Process-to-Capability Mapping Matrix]] · [[Canadian Regulatory Context]]
