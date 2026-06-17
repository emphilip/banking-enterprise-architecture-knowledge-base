---
id: atm-monitoring-and-servicing
title: ATM Monitoring & Servicing
type: business-capability
domain: Channels & Engagement
level: L3
aliases: ["ATM Device Monitoring", "ATM Maintenance"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://us.brinks.com/branch-services"]
---

# ATM Monitoring & Servicing

**Definition.** ATM Monitoring & Servicing is the Channels & Engagement capability that detects device faults, alerts and tamper events and dispatches maintenance, realising the device error detection and response aspect of the BIAN ATM Network Operations service domain.
**Also known as:** ATM Device Monitoring, ATM Maintenance.

## Relationships
- ATM Monitoring & Servicing is defined in the Channels & Engagement domain.
- ATM Monitoring & Servicing is derived from ATM Management.
- ATM Monitoring & Servicing depends on the Threat Detection capability.

## Details
ATM Monitoring & Servicing realises the device error detection and response aspect of BIAN ATM Network Operations: it ingests device status (SNMP/XFS health, cassette and journal state, card-reader faults) and dispatches first- and second-line maintenance. Security monitoring is central, detecting card-skimming, cash-trapping, black-box jackpotting and physical tamper, and triggering alarm and law-enforcement response per PCI PIN security and network anti-fraud mandates. Predictive maintenance models device telemetry to pre-empt outages and raise estate uptime, the key SLA. Faults link to ATM Network Management for spares and field-engineer planning.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [PCI Security Standards](https://www.pcisecuritystandards.org/)
- [Brinks Branch Services](https://us.brinks.com/branch-services)
