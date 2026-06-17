---
id: accrual-calculation-service
title: Accrual Calculation Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Daily Accrual Service", "Interest Accrual Calculator", "Accrual Engine Service"]
status: draft
sources: ["https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products", "https://www.oracle.com/financial-services/banking/flexcube/core-banking-software/"]
---

# Accrual Calculation Service

**Definition.** Accrual Calculation Service performs daily interest accrual computation across day-count conventions and balance bases, producing accrued amounts for capitalisation, posting and reporting.
**Also known as:** Daily Accrual Service, Interest Accrual Calculator, Accrual Engine Service.

## Relationships
- Accrual Calculation Service is defined in the Core Processing domain.
- Accrual Calculation Service is derived from Interest & Charges Engine.

## Details
Accrual Calculation Service computes a daily accrual amount as balance times rate times a day-count factor, supporting conventions such as Actual/360, Actual/365 and 30/360. It selects the balance base (ledger, cleared or average daily balance), accumulates accrued interest between capitalisation dates, and exposes the running accrual for end-of-day posting and for accrued-interest disclosure on statements. Oracle FLEXCUBE and core-banking ledger designs run accrual as a daily batch or event so accrued interest is always current before periodic capitalisation credits it to the account.

## References
- [Core banking data model and ledger (clefincode)](https://clefincode.com/blog/global-digital-vibes/en/core-banking-erp-part-2-data-model-ledger-core-products)
- [Oracle FLEXCUBE core banking](https://www.oracle.com/financial-services/banking/flexcube/core-banking-software/)
