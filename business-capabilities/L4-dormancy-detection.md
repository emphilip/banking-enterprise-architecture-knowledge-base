---
id: dormancy-detection
title: Dormancy Detection
type: business-capability
domain: Deposits & Accounts
level: L4
aliases: ["Inactivity Detection", "Dormant Flagging"]
status: draft
sources: ["https://deepwiki.com/bian-official/public/5.2-account-management", "https://unclaimed.org/"]
---

# Dormancy Detection

**Definition.** Dormancy Detection scans account activity to identify and classify dormant and unclaimed accounts, supporting the inactivity-monitoring behaviour within the BIAN Account Management service domains.
**Also known as:** Inactivity Detection, Dormant Flagging.

## Relationships
- Dormancy Detection is defined in the Deposits & Accounts domain.
- Dormancy Detection is derived from Dormancy Management.
- Dormancy Detection depends on the Analytics Platform capability.

## Details
BIAN Account Management inactivity monitoring flags dormant accounts; the dormancy clock starts from the last owner-generated activity, and after the state dormancy period (commonly 3-5 years) the account becomes reportable as unclaimed property.

## References
- [BIAN Account Management](https://deepwiki.com/bian-official/public/5.2-account-management)
- [National Association of Unclaimed Property Administrators](https://unclaimed.org/)
