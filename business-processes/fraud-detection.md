---
id: fraud-detection
title: Fraud Detection
type: business-process
domain: Risk Management
aliases: ["Fraud Screening"]
status: draft
---

# Fraud Detection

**Definition.** Fraud Detection is the process of identifying potentially fraudulent activity in real time and near real time through scoring, rules, and behavioral analytics on transactions and events.
**Also known as:** Fraud Screening.

## Relationships
- Fraud Detection is defined in the Risk Management domain.
- Fraud Detection depends on the Fraud Management capability.
- Fraud Detection depends on the Fraud Analytics capability.
- Fraud Detection causes Fraud Investigation.

## Details
Fraud Detection ingests transaction and event streams, applies machine learning models and rules to score risk, and generates alerts or blocks for suspicious activity. Actors include fraud analysts and automated decisioning services. Systems involved include a fraud analytics platform, data streaming, and a machine learning platform.

## Flow
- Ingest Transaction Stream causes Screen Transaction Risk.
- Screen Transaction Risk causes Generate Fraud Alert.
- Generate Fraud Alert causes Apply Detection Block.
- Apply Detection Block causes Route Fraud Alert.

## References
- [APQC Process Classification Framework](https://www.apqc.org/process-frameworks)
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
