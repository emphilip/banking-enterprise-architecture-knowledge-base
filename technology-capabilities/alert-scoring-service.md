---
id: alert-scoring-service
title: Alert Scoring Service
type: technology-capability
domain: AI & Automation
level: L2
aliases: ["Alert Prioritisation Service", "Alert Correlation Service", "Alert Triage Engine", "Alert Generation Engine"]
status: draft
sources: ["https://docs.oracle.com/cd/E91253_01/PDF/8.0.7.0.0/OFS%20BD%208.0.7.0.0%20Release%20Notes.pdf", "https://www.niceactimize.com/glossary/transaction-monitoring-software"]
---

# Alert Scoring Service

**Definition.** Alert Scoring Service is the technology sub-capability that consolidates, deduplicates, prioritises and risk-scores alerts from detection, analytics and screening, routing them for investigation and reducing false positives.
**Also known as:** Alert Prioritisation Service, Alert Correlation Service, Alert Triage Engine, Alert Generation Engine.

## Relationships
- Alert Scoring Service is defined in the AI & Automation domain.
- Alert Scoring Service is derived from Transaction Monitoring Platform.
- Alert Scoring Service depends on Scenario Detection Engine.
- Alert Scoring Service is related to Behavioural Risk Analytics.

## Details
Alert Scoring Service correlates matches from scenario detection, behavioural analytics and watchlist screening into deduplicated, entity-level alerts, then applies risk scores and prioritisation so investigators work the highest-risk cases first. Machine-learning triage and hibernation of low-risk alerts materially reduce false positives, a primary cost driver in AML operations. Scored, ranked alerts are promoted into case management for investigation, with the scoring rationale retained for audit and for feedback into model and threshold tuning.

## References
- [Oracle FCCM Behavior Detection Release Notes](https://docs.oracle.com/cd/E91253_01/PDF/8.0.7.0.0/OFS%20BD%208.0.7.0.0%20Release%20Notes.pdf)
- [NICE Actimize Transaction Monitoring Software](https://www.niceactimize.com/glossary/transaction-monitoring-software)
