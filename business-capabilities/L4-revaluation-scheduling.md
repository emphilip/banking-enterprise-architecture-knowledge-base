---
id: revaluation-scheduling
title: Revaluation Scheduling
type: business-capability
domain: Lending & Credit
level: L4
aliases: ["Collateral Revaluation", "Valuation Refresh"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Revaluation Scheduling

**Definition.** Revaluation Scheduling is the capability that triggers periodic and event-driven revaluation of pledged collateral, mapping to the BIAN Collateral Asset Administration service domain.
**Also known as:** Collateral Revaluation, Valuation Refresh.

## Relationships
- Revaluation Scheduling is defined in the Lending & Credit domain.
- Revaluation Scheduling is derived from Collateral Valuation.
- Revaluation Scheduling depends on the Analytics Platform capability.
- Revaluation Scheduling depends on the Workflow Orchestration capability.

## Details
The BIAN Collateral Asset Administration service domain holds collateral values that Revaluation Scheduling keeps current. A concrete banking specific: marketable securities pledged as collateral are revalued and margined frequently (often daily, triggering margin calls), while property collateral is revalued periodically or on a material market move so loan-to-value and capital calculations stay accurate.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
