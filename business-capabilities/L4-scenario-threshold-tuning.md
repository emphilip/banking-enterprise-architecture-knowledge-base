---
id: scenario-threshold-tuning
title: Scenario Threshold Tuning
type: business-capability
domain: Compliance & Financial Crime
level: L4
aliases: ["Detection Tuning", "Rule Optimisation"]
status: draft
sources: ["https://wolfsberg-group.org/resources/correspondent-banking", "https://bsaaml.ffiec.gov/manual"]
---

# Scenario Threshold Tuning

**Definition.** Scenario Threshold Tuning optimises detection-scenario rules and thresholds to balance coverage and false positives, consistent with Wolfsberg Group transaction-monitoring guidance and FFIEC model expectations.
**Also known as:** Detection Tuning, Rule Optimisation.

## Relationships
- Scenario Threshold Tuning is defined in the Compliance & Financial Crime domain.
- Scenario Threshold Tuning is derived from Suspicious Activity Detection.
- Scenario Threshold Tuning depends on the Machine Learning Platform capability.
- Scenario Threshold Tuning depends on the Transaction Monitoring Platform capability.

## Details
The Wolfsberg Group's monitoring guidance and the FFIEC manual expect institutions to validate and tune transaction-monitoring scenarios so that thresholds are demonstrably appropriate for the risk profile. Above-the-line / below-the-line testing samples alerts just above and below current thresholds to confirm productive alerts are captured without an excessive false-positive burden. Tuning must be documented, periodically repeated, and governed under model risk management, since arbitrary thresholds are a common examination finding.

## References
- [Wolfsberg Group resources](https://wolfsberg-group.org/resources/correspondent-banking)
- [FFIEC BSA/AML Examination Manual](https://bsaaml.ffiec.gov/manual)
