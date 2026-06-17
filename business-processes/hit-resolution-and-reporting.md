---
id: hit-resolution-and-reporting
title: Hit Resolution & Reporting
type: business-process
level: sub-process
domain: Compliance & Financial Crime
aliases: ["Hit Disposition", "Match Resolution"]
status: draft
sources: ["https://www.lenzo.ai/blog/sanctions-screening-false-positives-resolution-criteria/", "https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/customer-screening/8.1.2.10.0/csoug/alert-decision.html"]
---

# Hit Resolution & Reporting

**Definition.** Hit Resolution & Reporting resolves confirmed hits versus false positives under four-eyes, blocks confirmed matches and reports them to OFAC.
**Also known as:** Hit Disposition, Match Resolution.

## Relationships
- Hit Resolution & Reporting is derived from Sanctions Screening Operations.
- Hit Resolution & Reporting is defined in the Compliance & Financial Crime domain.
- Hit Resolution & Reporting depends on the Payment Sanctions Filter capability.

## Details
Hit Resolution & Reporting consumes triaged alerts and evidence and produces the Sanctions Hit disposition and blocking report. Controls include the preponderance standard, four-eyes approval, block and OFAC report within 10 business days, and documentation. The lead actor is the Compliance Screening Officer.

## References
- [Lenzo — False-positive resolution criteria](https://www.lenzo.ai/blog/sanctions-screening-false-positives-resolution-criteria/)
- [Oracle — Customer screening alert decision](https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/customer-screening/8.1.2.10.0/csoug/alert-decision.html)
