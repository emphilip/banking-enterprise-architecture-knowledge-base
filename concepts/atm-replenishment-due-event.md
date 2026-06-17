---
id: atm-replenishment-due-event
title: ATM Replenishment Due Event
type: event
domain: Channels & Engagement
aliases: ["Cash-Out Forecast Event", "Replenishment Triggered Event"]
status: draft
sources: ["https://www.ncratleos.com/banking/atm-itm/software/management/cash-management"]
---

# ATM Replenishment Due Event

**Definition.** ATM Replenishment Due Event is the event raised when a terminal's forecast crosses the cash-out threshold and replenishment becomes due. ATM Replenishment Due Event triggers cash ordering and replenishment within the ATM cash supply chain flow.

**Also known as:** Cash-Out Forecast Event, Replenishment Triggered Event.

## Relationships
- ATM Replenishment Due Event is related to the Channels & Engagement domain.
- ATM Replenishment Due Event causes Plan Cash Order.
- ATM Replenishment Due Event mentions ATM Cash Management.
- ATM Replenishment Due Event is related to ATM Cash Forecast.

## Details
ATM Replenishment Due Event fires when forecasting predicts a terminal will fall below its minimum cash level, signalling the custodian to convert the forecast into cash orders and per-terminal load plans by denomination. The event drives armoured cash-in-transit scheduling and cassette replenishment under dual custody, and is governed by forecast model controls and idle-cash limits that balance availability against the cost of cash held in the estate.

## References
- https://www.ncratleos.com/banking/atm-itm/software/management/cash-management
