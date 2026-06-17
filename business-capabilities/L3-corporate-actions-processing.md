---
id: corporate-actions-processing
title: Corporate Actions Processing
type: business-capability
domain: Wealth & Investments
level: L3
aliases: ["Corporate Action Handling", "Asset Servicing Events"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.sechistorical.org/collection/papers/2010/2010_0701_DTCCServices.pdf"]
---

# Corporate Actions Processing

**Definition.** Corporate Actions Processing captures, validates, and applies corporate action events such as dividends, splits, and tenders to client positions and elections; it is realised through the BIAN Corporate Action service domain.
**Also known as:** Corporate Action Handling, Asset Servicing Events.

## Relationships
- Corporate Actions Processing is defined in the Wealth & Investments domain.
- Corporate Actions Processing is derived from Brokerage & Trading.
- Corporate Actions Processing depends on the Order Management System capability.
- Corporate Actions Processing depends on the Core Banking Processing capability.

## Details
The BIAN Corporate Action service domain manages issuer-driven events. Concretely, Corporate Actions Processing distinguishes mandatory events (cash dividends, stock splits) that automatically adjust positions from voluntary events (rights issues, tender offers) that require client election by a deadline. It scrubs announcements from sources such as DTCC, applies entitlements on ex-date and pay-date, and reconciles holdings against the depository.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [SEC Historical Society — DTCC Services](https://www.sechistorical.org/collection/papers/2010/2010_0701_DTCCServices.pdf)
