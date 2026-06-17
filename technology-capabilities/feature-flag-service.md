---
id: feature-flag-service
title: Feature Flag Service
type: technology-capability
domain: Channels & Engagement
level: L2
aliases: ["Feature Toggle Service", "Release Flagging", "Progressive Delivery Service"]
status: draft
sources: ["https://www.cncf.io/blog/2023/02/02/progressive-delivery/", "https://engineering.backbase.com/2025/02/18/backbase-engagement-banking-platform-tech-stack/"]
---

# Feature Flag Service

**Definition.** Feature Flag Service is the technology sub-capability providing runtime flagging, progressive delivery and remote configuration that enable controlled rollout of digital features through canary, ring and kill-switch patterns.
**Also known as:** Feature Toggle Service, Release Flagging, Progressive Delivery Service.

## Relationships
- Feature Flag Service is defined in the Channels & Engagement domain.
- Feature Flag Service is derived from Digital Channel Platform.
- Feature Flag Service is related to Digital Analytics.

## Details
Feature Flag Service decouples deploy from release by evaluating flag rules per user, segment or percentage at runtime, supporting progressive delivery patterns (canary, ring-based rollout) and instant kill-switch rollback without redeploying clients. It targets flags by attributes and serves remote configuration to mobile and web channels. CNCF progressive-delivery guidance and engagement-banking stacks position flag evaluation alongside behavioural metrics so rollouts are gated on real impact.

## References
- [CNCF: Progressive delivery](https://www.cncf.io/blog/2023/02/02/progressive-delivery/)
- [Backbase Engagement Banking tech stack](https://engineering.backbase.com/2025/02/18/backbase-engagement-banking-platform-tech-stack/)
