---
id: forecast-atm-demand
title: Forecast ATM Demand
type: process-step
process: ATM Cash Servicing
order: 1
aliases: ["Cash Forecasting (ATM)", "Per-Terminal Forecast"]
status: draft
sources: ["https://www.ncratleos.com/banking/atm-itm/software/management/cash-management", "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8827151"]
---

# Forecast ATM Demand

**Definition.** Forecast ATM Demand forecasts per-terminal cash demand from usage history and seasonality to produce an ATM Cash Forecast.
**Also known as:** Cash Forecasting (ATM), Per-Terminal Forecast.

## Relationships
- Forecast ATM Demand is defined in the ATM Cash Servicing process.
- Forecast ATM Demand causes Plan Cash Order.
- Forecast ATM Demand depends on the ATM Management capability.
- Forecast ATM Demand mentions ATM Custodian.
- Forecast ATM Demand mentions ATM Cash Forecast.

## Details
The ATM Custodian forecasts demand. Inputs are ATM usage data; outputs are an ATM Cash Forecast. Controls include forecast model governance and idle-cash limits, feeding the dual-custody replenishment cycle.

## References
- [NCR Atleos ATM cash management](https://www.ncratleos.com/banking/atm-itm/software/management/cash-management)
- [USPTO ATM cash forecasting patent](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8827151)
