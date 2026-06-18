---
title: Case Management
type: capability
level: L1
capability-id: OPS-CAS
parent: Operations (OPS)
tags: [capability, case-management, workbasket, escalation, resolution, audit, disputes, retail-banking]
aliases: [OPS-CAS, Case Management Capability, Claims Case]
---

# Case Management (OPS-CAS)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Operations (OPS)]]

The Case Management capability group covers the **creation, routing, status, audit, escalation, and resolution** of operational cases. A dispute *is* a case from the moment it is logged: a claim case is created in the disputes platform, routed to work-baskets, progressed through statuses (pending / processed / rejected), escalated to managers/auditors, and finally resolved and closed. This group is exercised by **every** flow in the library.

## L2 Capabilities

### OPS-CAS-01 — Create Case

Creating the dispute/claim case in the disputes platform, one per disputed transaction (or a claim grouping multiple transactions). Exercised at intake in [[Initiate Dispute Flow]], [[Dispute Transfer to ITR Flow]], and [[First Chargeback Flow]].

### OPS-CAS-02 — Case Routing

Routing cases to the correct work-basket or team — the dispute, challenge, compliance, and acquirer baskets; transfer to the fraud investigations team; referral to specialist mailboxes.

### OPS-CAS-03 — Case Status

Maintaining case status through the lifecycle (pending → processed/rejected; open → resolved → closed) and the status checks performed against the network application.

### OPS-CAS-04 — Audit Track

Audit notes and commentary on the case — the running record of the client conversation, decisions, and supporting documents; the auditable trail required to substantiate a chargeback or write-off.

### OPS-CAS-05 — Escalations

Escalation paths — to the team manager for a final decision, to the Performance Auditor for write-off approval, to the network for compliance, and to Client Care for unresolved complaints.

### OPS-CAS-06 — Resolution

Closing the case with the correct resolution code — Cardholder Liable (CHL), Write-Off (WO), multiprong, acquirer liable, split liability — and ensuring all transactions in the claim are resolved before closing. Exercised across the resolution flows.

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Initiate Dispute Flow]] | OPS-CAS-01, 02 |
| [[Dispute Transfer to ITR Flow]] | OPS-CAS-01, 04 |
| [[Dispute Workbasket Flow]] | OPS-CAS-02, 04, 05, 06 |
| [[First Chargeback Flow]] | OPS-CAS-01, 03, 04 |
| [[Second Presentment Flow]] | OPS-CAS-03, 05, 06 |
| [[Performance Auditor Writeoff Flow]] | OPS-CAS-05, 06 |
| [[Arbitration Flow]] | OPS-CAS-06 |
| [[Pre-Compliance Flow]] | OPS-CAS-02, 03, 05 |
| [[Compliance Flow]] | OPS-CAS-06 |

## Related

[[Transaction Processing]] · [[Fraud Management]] · [[Servicing - Monetary]] · [[Settlement]]
