---
id: regulatory-filing-submitted-event
title: Regulatory Filing Submitted Event
type: event
domain: Compliance & Financial Crime
aliases: ["Filing Submitted Event", "Return Filed Event"]
status: draft
sources: ["https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-currency-transaction-report-ctr"]
---

# Regulatory Filing Submitted Event

**Definition.** Regulatory Filing Submitted Event is the business event signalling that a regulatory return — such as a Currency Transaction Report — has been submitted to the regulator and acknowledged within deadline. Regulatory Filing Submitted Event confirms the filing obligation is met and the record can be archived.
**Also known as:** Filing Submitted Event, Return Filed Event.

## Relationships
- Regulatory Filing Submitted Event is related to the Compliance & Financial Crime domain.
- Regulatory Filing Submitted Event mentions Regulatory Filing.
- Regulatory Filing Submitted Event mentions CTR Filing.
- Regulatory Filing Submitted Event causes Submit Regulatory Return.

## Details
Regulatory Filing Submitted Event carries the return type and reference (e.g. FinCEN Form 112), the reporting period, the submission timestamp, the regulator acknowledgement identifier and the submitting analyst. It is emitted on successful e-filing within the statutory deadline (for the CTR, 15 days with no extension) and triggers acknowledgement capture and five-year retention of the filing record for audit. The event closes the filing obligation and feeds compliance management information on timeliness and completeness.

## References
- [FinCEN CTR FAQs](https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-currency-transaction-report-ctr)
- [FinCEN BSA E-Filing](https://bsaefiling.fincen.treas.gov/main.html)
