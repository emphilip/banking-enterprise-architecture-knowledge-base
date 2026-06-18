---
title: Fraud Management
type: capability
level: L1
capability-id: FRR-FRD
parent: Fraud & Risk (FRR)
tags: [capability, fraud, ato, fraud-investigation, case-management, safe-reporting, retail-banking, cards]
aliases: [FRR-FRD, Fraud Management Capability, Fraud Mgmt]
---

# Fraud Management (FRR-FRD)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Fraud & Risk (FRR)]]

The Fraud Management capability group covers fraud strategy, monitoring, detection, **investigation**, and the fraud **case queue**. In the disputes program it owns the **fraud dispute path** — account-takeover (ATO) and fraudulent-application (FA) claims that branch off the standard dispute at intake, the fraud case management in the fraud system, the marking of fraudulent transactions, and **network fraud reporting (SAFE)**.

## L2 Capabilities

### FRR-FRD-01 — Fraud Strategy

Fraud-loss strategy and policy (write-off authorities, liability rules).

### FRR-FRD-02 — Fraud Monitoring

Real-time and batch monitoring; the fraud system receives real-time notification and a monthly file from the customer information file for cardholders.

### FRR-FRD-03 — Fraud Detection

Detection and flagging of fraudulent transactions — the **marking of transactions** in the fraud system and the moving of fraud vs. non-fraud transactions between card numbers. Exercised in [[Initiate Dispute Flow]] and [[Dispute Transfer to ITR Flow]].

### FRR-FRD-04 — Fraud Investigation

Investigation of ATO/FA claims by the **fraud claims specialist / fraud investigations team** — reviewing the account with the client, confirming victim status, deciding challenge vs. goodwill, and determining liability. The home of [[Dispute Transfer to ITR Flow]] and [[Dispute Workbasket Flow]].

### FRR-FRD-05 — Fraud Queue

The fraud case queue / work-basket that routes fraud disputes to specialists.

### FRR-FRD-06 — Mass Comp.

Mass-compromise handling (bulk fraud events). Out of scope for these flows but part of the group.

> **SAFE reporting** (the network's fraud-reporting system) is conducted when a fraud chargeback is raised; removing a transaction from the fraud report is part of resolving a customer-liable outcome (see [[Dispute Workbasket Flow]]).

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Initiate Dispute Flow]] | FRR-FRD-03 |
| [[Dispute Transfer to ITR Flow]] | FRR-FRD-04, 03 |
| [[Dispute Workbasket Flow]] | FRR-FRD-04, 05 |
| [[First Chargeback Flow]] | FRR-FRD-02 (SAFE reporting) |

## Related

[[Case Management]] · [[Servicing - Monetary]] · [[Transaction Processing]] · [[Systems and Integration Reference]]
