---
id: a-b-testing-service
title: A/B Testing Service
type: technology-capability
domain: Channels & Engagement
level: L3
aliases: ["Experimentation Service", "Multivariate Testing"]
status: draft
sources: ["https://www.cncf.io/blog/2023/02/02/progressive-delivery/", "https://www.backbase.com/blog/digital-banking-platform"]
---

# A/B Testing Service

**Definition.** A/B Testing Service is the technology sub-capability providing an experimentation framework for controlled A/B and multivariate tests that measure the impact of digital variants on engagement and conversion.
**Also known as:** Experimentation Service, Multivariate Testing.

## Relationships
- A/B Testing Service is defined in the Channels & Engagement domain.
- A/B Testing Service is derived from Feature Flag Service.
- A/B Testing Service is related to Digital Analytics.

## Details
A/B Testing Service randomly assigns users to control and variant arms, holds assignment stable per user, and computes statistical significance on conversion and engagement metrics, supporting multivariate combinations and holdout groups. It builds on flag-based variant delivery for assignment and reads behavioural metrics to evaluate outcomes, so feature rollouts can be promoted or rolled back on evidence. CNCF progressive-delivery practice treats experimentation as the measurement complement to controlled rollout.

## References
- [CNCF: Progressive delivery](https://www.cncf.io/blog/2023/02/02/progressive-delivery/)
- [Backbase digital banking platform](https://www.backbase.com/blog/digital-banking-platform)
