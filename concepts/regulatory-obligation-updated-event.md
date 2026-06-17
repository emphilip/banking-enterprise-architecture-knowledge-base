---
id: regulatory-obligation-updated-event
title: Regulatory Obligation Updated Event
type: event
domain: Compliance & Financial Crime
aliases: ["Reg Change Embedded Event", "Obligation Updated Event"]
status: draft
sources: ["https://finreg-e.com/horizon-scanning/"]
---

# Regulatory Obligation Updated Event

**Definition.** Regulatory Obligation Updated Event is the business event signalling that a regulatory change has been mapped, remediated and attested, updating the obligation library. Regulatory Obligation Updated Event marks that the new requirement is embedded and operating.
**Also known as:** Reg Change Embedded Event, Obligation Updated Event.

## Relationships
- Regulatory Obligation Updated Event is related to the Compliance & Financial Crime domain.
- Regulatory Obligation Updated Event mentions Regulatory Change Management.
- Regulatory Obligation Updated Event mentions Regulatory Obligation.
- Regulatory Obligation Updated Event causes Attest Change Compliance.

## Details
Regulatory Obligation Updated Event carries the obligation identifier, the source regulation reference, the affected policies and controls, the remediation outcome and the attestation record with owner and date. It is emitted at the close of the regulatory change lifecycle once controls are implemented and tested, and it updates the obligation library to keep the bank's control mapping current. The event provides the traceability the bank relies on to demonstrate to regulators that the change has been embedded and is operating effectively.

## References
- [Horizon scanning practice](https://finreg-e.com/horizon-scanning/)
- [FCA regulatory expectations](https://www.fca.org.uk/)
