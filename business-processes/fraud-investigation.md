---
id: fraud-investigation
title: Fraud Investigation
type: business-process
domain: Risk Management
aliases: ["Fraud Case Handling"]
status: draft
---

# Fraud Investigation

**Definition.** Fraud Investigation is the process of triaging, investigating, and resolving fraud alerts and cases, including evidence gathering, customer contact, and loss recovery.
**Also known as:** Fraud Case Handling.

## Relationships
- Fraud Investigation is defined in the Risk Management domain.
- Fraud Investigation depends on the Fraud Management capability.
- Fraud Investigation depends on the Case Management capability.

## Details
Fraud Investigation receives alerts from detection, assembles case context, confirms or dismisses fraud, blocks or recovers funds, and feeds outcomes back into models. Actors include fraud investigators and case managers. Systems involved include a case management platform, fraud analytics, and customer servicing tooling.

## Flow
- Adjudicate Fraud Alert causes Open Fraud Case.
- Open Fraud Case causes Investigate Fraud Case.
- Investigate Fraud Case causes Recover Fraud Loss.
- Recover Fraud Loss causes File Suspicious Activity Report.
- File Suspicious Activity Report causes Feed Detection Models.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
