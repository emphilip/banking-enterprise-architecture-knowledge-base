---
id: performance-reporting
title: Performance Reporting
type: business-process
domain: Wealth & Investments
aliases: ["Investment Reporting", "Client Reporting"]
status: draft
sources: ["https://www.gipsstandards.org/standards/gips-standards-for-firms/gips-standards-handbook-for-firms/", "https://www.kitces.com/blog/twr-dwr-irr-calculations-performance-reporting-software-methodology-gips-compliance/", "https://en.wikipedia.org/wiki/Performance_attribution"]
---

# Performance Reporting

**Definition.** Performance Reporting is the periodic process that values the portfolio, reconciles positions including corporate actions, computes time-weighted returns versus benchmark with attribution, and produces and delivers the client Performance Report.
**Also known as:** Investment Reporting, Client Reporting.

## Relationships
- Performance Reporting is defined in the Wealth & Investments domain.
- Performance Reporting depends on the Portfolio Management capability.

## Details
Performance Reporting values holdings at period end, processes corporate actions, reconciles positions and cash against custody, computes time-weighted returns since inception, compares to benchmark with attribution, and delivers the client Performance Report. Controls include GIPS time-weighted return methodology, benchmark consistency, valuation/reconciliation controls, disclosure accuracy, and four-eyes sign-off. Actors include the Performance Analyst.

## Flow
- Value Portfolio causes Process Corporate Actions.
- Process Corporate Actions causes Reconcile Positions.
- Reconcile Positions causes Calculate Returns.
- Calculate Returns causes Compute Attribution.
- Compute Attribution causes Produce Performance Report.

## References
- [GIPS Standards Handbook for Firms](https://www.gipsstandards.org/standards/gips-standards-for-firms/gips-standards-handbook-for-firms/)
- [TWR/DWR/IRR and GIPS compliance](https://www.kitces.com/blog/twr-dwr-irr-calculations-performance-reporting-software-methodology-gips-compliance/)
