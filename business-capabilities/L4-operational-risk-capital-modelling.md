---
id: operational-risk-capital-modelling
title: Operational Risk Capital Modelling
type: business-capability
domain: Risk Management
level: L4
aliases: ["Op Risk Capital", "SMA Modelling", "Loss Distribution Approach"]
status: draft
sources: ["https://www.bis.org/bcbs/publ/d424.htm", "https://www.bis.org/publ/bcbs292.pdf"]
---

# Operational Risk Capital Modelling

**Definition.** Operational Risk Capital Modelling estimates operational-risk capital combining internal loss, external data and scenarios, transitioning to the Basel Standardised Approach for operational risk.
**Also known as:** Op Risk Capital, SMA Modelling, Loss Distribution Approach.

## Relationships
- Operational Risk Capital Modelling is defined in the Risk Management domain.
- Operational Risk Capital Modelling is derived from Op Risk Scenario Analysis.
- Operational Risk Capital Modelling depends on the Risk Analytics Engine capability.
- Operational Risk Capital Modelling depends on the Analytics Platform capability.

## Details
Operational Risk Capital Modelling computes capital under the Basel III Standardised Approach (BCBS d424), which replaced AMA: capital equals the Business Indicator Component multiplied by the Internal Loss Multiplier, where the ILM is a log function of the ratio of average annual losses (15× ten-year average) to the BIC. It retains loss-distribution-approach modelling (frequency × severity convolution via Monte-Carlo at the 99.9th percentile) for economic capital and Pillar 2, feeding off the loss database and scenario estimates.

## References
- [Basel III Finalisation — Operational Risk (d424)](https://www.bis.org/bcbs/publ/d424.htm)
- [BCBS Principles for the Sound Management of Operational Risk (bcbs292)](https://www.bis.org/publ/bcbs292.pdf)
