---
id: scenario-detection-engine
title: Scenario Detection Engine
type: technology-capability
domain: AI & Automation
level: L2
aliases: ["Behavior Detection Engine", "Scenario Engine", "AML Detection Engine", "Typology Engine"]
status: draft
sources: ["https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/behavior-detection/8.1.2.9.0/smubd/overview-fccm.html", "https://www.niceactimize.com/glossary/transaction-monitoring-software"]
---

# Scenario Detection Engine

**Definition.** Scenario Detection Engine is the configurable behavior-detection technology sub-capability that runs typology scenarios, thresholds and segmented rules over transactions and account behaviour to detect suspicious activity.
**Also known as:** Behavior Detection Engine, Scenario Engine, AML Detection Engine, Typology Engine.

## Relationships
- Scenario Detection Engine is defined in the AI & Automation domain.
- Scenario Detection Engine is derived from Transaction Monitoring Platform.
- Scenario Detection Engine depends on Data Warehousing.
- Scenario Detection Engine is related to AML Monitoring.

## Details
Scenario Detection Engine implements the rules/scenario layer of AML transaction monitoring as in Oracle FCCM Behavior Detection and NICE Actimize SAM: out-of-the-box and custom typology scenarios are parameterised by customer segment, with thresholds and look-back periods evaluated against transaction and account-behaviour data drawn from the warehouse. It batches and, increasingly, streams detection runs, raising matches that downstream alert scoring consolidates. Segmentation lets thresholds reflect peer-group norms so that detection reflects expected behaviour for similar customers.

## References
- [Oracle FCCM Behavior Detection Overview](https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/behavior-detection/8.1.2.9.0/smubd/overview-fccm.html)
- [NICE Actimize Transaction Monitoring Software](https://www.niceactimize.com/glossary/transaction-monitoring-software)
