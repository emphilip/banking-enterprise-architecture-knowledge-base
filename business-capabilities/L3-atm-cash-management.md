---
id: atm-cash-management
title: ATM Cash Management
type: business-capability
domain: Channels & Engagement
level: L3
aliases: ["ATM Cash Replenishment", "ATM Estate Cash Forecasting"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://us.brinks.com/branch-services"]
---

# ATM Cash Management

**Definition.** ATM Cash Management is the Channels & Engagement capability that forecasts, replenishes and reconciles cash holdings across the ATM estate, realising the cash-tracking aspect of the BIAN ATM Network Operations service domain.
**Also known as:** ATM Cash Replenishment, ATM Estate Cash Forecasting.

## Relationships
- ATM Cash Management is defined in the Channels & Engagement domain.
- ATM Cash Management is derived from ATM Management.
- ATM Cash Management depends on the Analytics Platform capability.

## Details
ATM Cash Management realises the cash-tracking aspect of BIAN ATM Network Operations: it forecasts per-device demand by denomination, schedules cash-in-transit replenishment, and reconciles dispensed-versus-loaded balances to detect shrinkage. The optimisation problem trades the cost of idle cash and CIT visits against dispense-failure (cassette empty) risk, so demand models account for paydays, holidays and seasonality. Reconciliation matches the device journal and switch totals against CIT manifests to surface discrepancies for investigation. It coordinates with branch Cash & Vault Management for shared float and feeds CIT scheduling.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [Brinks Branch Services](https://us.brinks.com/branch-services)
- [APQC Process Frameworks](https://www.apqc.org/process-frameworks)
