---
id: atm-cash-servicing
title: ATM Cash Servicing
type: business-process
domain: Channels & Engagement
aliases: ["ATM Cash Cycle", "ATM Replenishment Process"]
status: draft
sources: ["https://www.ncratleos.com/banking/atm-itm/software/management/cash-management", "https://www.sonassystems.com/blog/atm-replenishment-and-the-importance-of-identifying-exceptions", "https://brinks-ams.com/cash-optimization-with-brinks-atm-management/"]
---

# ATM Cash Servicing

**Definition.** ATM Cash Servicing is the end-to-end ATM cash supply-chain process that forecasts device cash demand, raises cash orders, replenishes terminals via cash-in-transit under dual custody, and reconciles dispensed versus loaded cash daily.
**Also known as:** ATM Cash Cycle, ATM Replenishment Process.

## Relationships
- ATM Cash Servicing is defined in the Channels & Engagement domain.
- ATM Cash Servicing depends on the ATM Management capability.
- ATM Cash Servicing depends on the ATM Cash Management capability.

## Details
ATM Cash Servicing is owned by the ATM Custodian. Inputs are ATM cash usage data and vault cash; outputs are replenished ATMs, an ATM Cash Forecast and a reconciled GL. Controls include dual custody of ATM keys and cassettes, cash-in-transit (CIT) chain-of-custody, daily ATM GL reconciliation, and cash variance / exception management.

## Flow
- Forecast ATM Demand causes Plan Cash Order.
- Plan Cash Order causes Schedule Cash Delivery.
- Schedule Cash Delivery causes Replenish ATM Cash.
- Replenish ATM Cash causes Reconcile ATM Cash.
- Reconcile ATM Cash causes Resolve Cash Discrepancy.

## References
- [NCR Atleos ATM cash management](https://www.ncratleos.com/banking/atm-itm/software/management/cash-management)
- [Sonas ATM replenishment exceptions](https://www.sonassystems.com/blog/atm-replenishment-and-the-importance-of-identifying-exceptions)
- [Brinks ATM cash optimization](https://brinks-ams.com/cash-optimization-with-brinks-atm-management/)
