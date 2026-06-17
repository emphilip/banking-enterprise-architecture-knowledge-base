---
id: risk-reporting
title: Risk Reporting
type: business-process
domain: Risk Management
aliases: ["Risk Data Aggregation & Reporting", "RDARR", "Board Risk Reporting"]
status: draft
sources: ["https://www.regnology.net/en/resources/regulatory-topics/rdarr/", "https://en.wikipedia.org/wiki/BCBS_239"]
---

# Risk Reporting

**Definition.** Risk Reporting is the process of aggregating risk data and producing risk reports that measure the bank's profile against appetite, including limit-breach monitoring and escalation, board and committee reporting and regulatory submission, per BCBS 239.
**Also known as:** Risk Data Aggregation & Reporting, RDARR, Board Risk Reporting.

## Relationships
- Risk Reporting is defined in the Risk Management domain.
- Risk Reporting depends on the Enterprise Risk Management capability.

## Details
Risk Reporting consumes risk data, the Risk Register, risk limits and the Stress Test Result and produces the Risk Report, limit-breach escalations and regulatory returns. Controls include BCBS 239 risk data aggregation and reporting, limit-breach escalation, board and committee reporting, data quality and lineage, and regulatory submission.

## Flow
- Aggregate Risk Exposure causes Reconcile Risk Data.
- Reconcile Risk Data causes Compare Against Limits.
- Compare Against Limits causes Escalate Limit Breach.
- Escalate Limit Breach causes Compile Risk Report.
- Compile Risk Report causes Distribute Risk Report.

## References
- [Regnology — RDARR](https://www.regnology.net/en/resources/regulatory-topics/rdarr/)
- [BCBS 239](https://en.wikipedia.org/wiki/BCBS_239)
