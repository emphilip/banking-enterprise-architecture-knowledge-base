---
id: atm-fault-detection
title: ATM Fault Detection
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["Device Alert Detection", "ATM Alarm Handling"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://us.brinks.com/branch-services"]
---

# ATM Fault Detection

**Definition.** ATM Fault Detection is the Channels & Engagement capability that identifies device errors, jams and tamper alerts and triggers response workflows, realising the device error detection aspect of the BIAN ATM Network Operations service domain.
**Also known as:** Device Alert Detection, ATM Alarm Handling.

## Relationships
- ATM Fault Detection is defined in the Channels & Engagement domain.
- ATM Fault Detection is derived from ATM Monitoring & Servicing.
- ATM Fault Detection depends on the Threat Detection capability.

## Details
ATM Fault Detection realises the device error detection aspect of BIAN ATM Network Operations, ingesting WOSA/XFS and SNMP telemetry to spot card-reader faults, note jams, cassette-empty conditions, low-paper and offline states, and raising tickets to ATM Monitoring & Servicing. Security detection is co-resident: skimmer and shimmer presence, cash-trap and black-box jackpotting attempts, and physical tamper trigger alarms and law-enforcement escalation under PCI PIN security mandates. Anomaly models on dispense and error patterns flag developing faults for predictive maintenance, protecting estate uptime. Each alert is correlated to suppress storms and routed by severity to field or remote remediation.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [PCI Security Standards](https://www.pcisecuritystandards.org/)
- [Brinks Branch Services](https://us.brinks.com/branch-services)
