---
id: card-activation
title: Card Activation
type: business-capability
domain: Cards
level: L3
aliases: ["Card Enablement", "First Use Activation"]
status: draft
sources: ["https://bian.org/servicelandscape/", "https://www.apqc.org/process-frameworks"]
---

# Card Activation

**Definition.** Card Activation enables a newly issued or replacement device for transactional use, updating device status in the BIAN Issued Device Administration service domain.
**Also known as:** Card Enablement, First Use Activation.

## Relationships
- Card Activation is defined in the Cards domain.
- Card Activation is derived from Card Issuing.
- Card Activation depends on the Card Processing capability.

## Details
The BIAN Issued Device Administration service domain flips the device from "issued" to "active" so the authorization host will approve ISO 8583 requests; before activation the host declines or routes to stand-in. Activation channels (IVR, app, web) verify cardholder identity, and for EMV cards the first chip transaction may carry an activation flag. Activation is the control point that converts a fulfilled card into a live payment instrument.

## References
- [BIAN Service Landscape](https://bian.org/servicelandscape/)
- [APQC Process Frameworks](https://www.apqc.org/process-frameworks)
