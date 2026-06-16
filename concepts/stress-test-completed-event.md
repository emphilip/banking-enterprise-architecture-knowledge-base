---
id: stress-test-completed-event
title: Stress Test Completed Event
type: event
domain: Risk Management
aliases: ["Stress Cycle Completed Event", "CCAR Submitted Event"]
status: draft
sources: ["https://www.federalreserve.gov/publications/comprehensive-capital-analysis-and-review-questions-and-anwers.htm", "https://en.wikipedia.org/wiki/Comprehensive_Capital_Analysis_and_Review"]
---

# Stress Test Completed Event

**Definition.** Stress Test Completed Event is the business event signalling that a stress-testing cycle has finished with results produced and the capital plan submitted to the regulator.

**Also known as:** Stress Cycle Completed Event, CCAR Submitted Event.

## Relationships
- Stress Test Completed Event is related to the Risk Management domain.
- Stress Test Completed Event causes Submit Capital Plan.
- Stress Test Completed Event mentions Stress Test Result.

## Details
Stress Test Completed Event is emitted at the close of the Stress Testing process, after validated models have projected losses, revenues and capital ratios across scenarios, capital adequacy has been assessed against minima and buffers, the board has signed off the capital plan, and the plan and results are submitted under CCAR/DFAST (or EBA). The event records cycle completion with the scenario set, result version and submission reference, supporting governance, audit and the documentation trail expected by supervisors. It also closes the loop back to risk appetite and capital planning, since stress outcomes inform whether buffers, limits or management actions need adjustment in the next cycle.

## References
- https://www.federalreserve.gov/publications/comprehensive-capital-analysis-and-review-questions-and-anwers.htm
- https://en.wikipedia.org/wiki/Comprehensive_Capital_Analysis_and_Review
