---
id: outbound-dialer-management
title: Outbound Dialer Management
type: business-capability
domain: Channels & Engagement
level: L4
aliases: ["Dialer Operations", "Predictive Dialing"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.nextiva.com/blog/bank-call-center-software.html"]
---

# Outbound Dialer Management

**Definition.** Outbound Dialer Management is the Channels & Engagement capability that runs predictive and preview dialing campaigns with compliance pacing and list management, supporting the BIAN Contact Center Operations service domain's outbound activity.
**Also known as:** Dialer Operations, Predictive Dialing.

## Relationships
- Outbound Dialer Management is defined in the Channels & Engagement domain.
- Outbound Dialer Management is derived from Outbound Engagement.
- Outbound Dialer Management depends on the Contact Center Platform capability.

## Details
Outbound Dialer Management supports the outbound side of BIAN Contact Center Operations by pacing predictive, progressive and preview dialing, suppressing numbers and enforcing contact frequency. Compliance is the binding constraint: the US TCPA restricts autodialed and prerecorded calls and caps abandonment rate, the FDCPA limits collections call times and frequency, and Do-Not-Call and reassigned-number databases must be scrubbed before every campaign. The dialer reads consent flags from Consent & Preference Management and time-zone windows so no contact violates calling hours. Right-party-contact and answer rates tune pacing algorithms fed by Campaign Execution lists.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [FTC Telemarketing and TCPA Rules](https://www.fcc.gov/general/telemarketing-and-robocalls)
- [Bank Call Center Software](https://www.nextiva.com/blog/bank-call-center-software.html)
