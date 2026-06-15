---
id: delinquency-management
title: Delinquency Management
type: business-capability
domain: Lending & Credit
level: L3
aliases: ["Arrears Management", "Early Collections"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://medium.com/adl-blog/a-deep-dive-into-the-bian-landscape-understanding-service-domains-through-a-lending-example-6a5ec26eaf6a"]
---

# Delinquency Management

**Definition.** Delinquency Management is the capability that identifies, segments and treats accounts in early and late arrears, mapping to the BIAN Delinquent Account Handling service domain.
**Also known as:** Arrears Management, Early Collections.

## Relationships
- Delinquency Management is defined in the Lending & Credit domain.
- Delinquency Management is derived from Collections & Recovery.
- Delinquency Management depends on the Analytics Platform capability.
- Delinquency Management depends on the Workflow Orchestration capability.

## Details
The BIAN Delinquent Account Handling service domain manages accounts that have fallen into arrears, which Delinquency Management drives via risk-based treatment strategies. A concrete banking specific: a credit account is typically bucketed by days-past-due (e.g. 1-29, 30-59, 60-89), and once 90+ days past due it is generally classified as non-performing and moved to higher-intensity recovery treatment.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [BIAN lending service domains walkthrough](https://medium.com/adl-blog/a-deep-dive-into-the-bian-landscape-understanding-service-domains-through-a-lending-example-6a5ec26eaf6a)
