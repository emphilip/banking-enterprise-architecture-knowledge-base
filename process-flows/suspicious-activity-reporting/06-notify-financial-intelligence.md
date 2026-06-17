---
id: notify-financial-intelligence
title: Notify Financial Intelligence
type: process-step
process: Suspicious Activity Reporting
order: 6
aliases: ["Confirm SAR", "FIU Notification Step"]
status: draft
sources: ["https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-suspicious-activity-report-sar", "https://www.americascreditunions.org/blogs/compliance/fincen-issues-frequently-asked-questions-clarify-sar-requirements"]
---

# Notify Financial Intelligence

**Definition.** Notify Financial Intelligence confirms SAR receipt, observes tipping-off rules and retains records, and emits the Suspicious Activity Detected Event.
**Also known as:** Confirm SAR, FIU Notification Step.

## Relationships
- Notify Financial Intelligence is defined in the Suspicious Activity Reporting process.
- Notify Financial Intelligence depends on the Regulatory Reporting Engine capability.
- Notify Financial Intelligence mentions MLRO.
- Notify Financial Intelligence mentions Suspicious Activity Detected Event.

## Details
The MLRO confirms receipt of the SAR Filing and retains the record. Controls include the tipping-off prohibition, 5-year retention, acknowledgement capture and continuing-activity tracking, with completion signalled by the Suspicious Activity Detected Event. This is the final step of Suspicious Activity Reporting.

## References
- [FinCEN — SAR FAQ](https://www.fincen.gov/resources/frequently-asked-questions-regarding-fincen-suspicious-activity-report-sar)
- [America's Credit Unions — FinCEN SAR FAQ](https://www.americascreditunions.org/blogs/compliance/fincen-issues-frequently-asked-questions-clarify-sar-requirements)
