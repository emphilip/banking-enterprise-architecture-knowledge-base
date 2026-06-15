---
id: treatment-strategy-management
title: Treatment Strategy Management
type: business-capability
domain: Lending & Credit
level: L4
aliases: ["Collections Strategy", "Treatment Path Management"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://medium.com/adl-blog/a-deep-dive-into-the-bian-landscape-understanding-service-domains-through-a-lending-example-6a5ec26eaf6a"]
---

# Treatment Strategy Management

**Definition.** Treatment Strategy Management is the capability that defines and assigns collections treatment paths and contact strategies by risk segment, mapping to the BIAN Delinquent Account Handling service domain.
**Also known as:** Collections Strategy, Treatment Path Management.

## Relationships
- Treatment Strategy Management is defined in the Lending & Credit domain.
- Treatment Strategy Management is derived from Delinquency Management.
- Treatment Strategy Management depends on the Analytics Platform capability.
- Treatment Strategy Management depends on the Workflow Orchestration capability.

## Details
The BIAN Delinquent Account Handling service domain executes treatment paths that Treatment Strategy Management designs and assigns by segment. A concrete banking specific: champion-challenger testing assigns delinquent accounts to differentiated paths (e.g. SMS-only for low-risk early arrears versus agent calls for high-risk), and contact timing/frequency must respect FDCPA / FCA CONC limits on harassment.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [BIAN lending service domains walkthrough](https://medium.com/adl-blog/a-deep-dive-into-the-bian-landscape-understanding-service-domains-through-a-lending-example-6a5ec26eaf6a)
