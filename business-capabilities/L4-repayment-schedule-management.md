---
id: repayment-schedule-management
title: Repayment Schedule Management
type: business-capability
domain: Lending & Credit
level: L4
aliases: ["Amortization Scheduling", "Schedule Recalculation"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Repayment Schedule Management

**Definition.** Repayment Schedule Management is the capability that builds and maintains amortization schedules and recalculates them on events, mapping to the BIAN Repayment service domain.
**Also known as:** Amortization Scheduling, Schedule Recalculation.

## Relationships
- Repayment Schedule Management is defined in the Lending & Credit domain.
- Repayment Schedule Management is derived from Repayment Processing.
- Repayment Schedule Management depends on the Core Banking Processing capability.

## Details
The BIAN Repayment service domain holds the repayment plan that Repayment Schedule Management generates and revises. A concrete banking specific: an amortising loan's schedule is derived from principal, rate and term so that each level instalment splits into declining interest and rising principal, and it must be rebuilt whenever a rate reset, modification or prepayment changes the balance.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
