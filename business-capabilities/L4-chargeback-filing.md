---
id: chargeback-filing
title: Chargeback Filing
type: business-capability
domain: Cards
level: L4
aliases: ["Reason Code Assignment", "Chargeback Submission"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://usa.visa.com/support/consumer/visa-rules.html"]
---

# Chargeback Filing

**Definition.** Chargeback Filing assembles and submits the chargeback to the network with reason code and supporting evidence, supporting the BIAN Card Case service domain.
**Also known as:** Reason Code Assignment, Chargeback Submission.

## Relationships
- Chargeback Filing is defined in the Cards domain.
- Chargeback Filing is derived from Chargeback Handling.
- Chargeback Filing depends on the Workflow Orchestration capability.

## Details
Within the BIAN Card Case service domain this capability selects the correct scheme dispute condition (e.g. Visa 13.1 "merchandise not received", 10.4 "card-absent fraud") and lodges the case in Visa VCR or Mastercard Mastercom with the required documentation and within the reason-code-specific time limit. Filing the wrong reason code or missing the deadline causes the chargeback to be rejected, so this step encodes the scheme rulebook decision tree.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Visa Core Rules and Visa Product and Service Rules](https://usa.visa.com/support/consumer/visa-rules.html)
