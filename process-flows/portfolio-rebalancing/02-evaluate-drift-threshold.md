---
id: evaluate-drift-threshold
title: Evaluate Drift Threshold
type: process-step
process: Portfolio Rebalancing
order: 2
aliases: ["Threshold Evaluation Step", "Tolerance Check Step"]
status: draft
sources: ["https://resonanzcapital.com/insights/the-art-and-science-of-portfolio-rebalancing-a-timeless-framework-for-all-market-environments"]
---

# Evaluate Drift Threshold

**Definition.** Evaluate Drift Threshold evaluates drift against tolerance bands and decides whether to rebalance, branching breach or within tolerance.
**Also known as:** Threshold Evaluation Step, Tolerance Check Step.

## Relationships
- Evaluate Drift Threshold is defined in the Portfolio Rebalancing process.
- Evaluate Drift Threshold causes Generate Rebalance Proposal.
- Evaluate Drift Threshold depends on the Portfolio Management capability.
- Evaluate Drift Threshold mentions Portfolio Manager.
- Evaluate Drift Threshold mentions Rebalance Triggered Event.

## Details
The Portfolio Manager evaluates the drift report against tolerance bands, branching breach or within tolerance and raising the Rebalance Triggered Event on a breach. Controls include drift tolerance bands and IPS limits; a within-tolerance outcome takes no action.

## References
- [The art and science of portfolio rebalancing](https://resonanzcapital.com/insights/the-art-and-science-of-portfolio-rebalancing-a-timeless-framework-for-all-market-environments)
