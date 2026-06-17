---
id: stand-in-processing-service
title: Stand-In Processing Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["STIP Service", "On-Behalf-Of Processing", "Stand-In Authorization"]
status: draft
sources: ["https://network.americanexpress.com/globalnetwork/dam/jcr:7d61622d-72b8-4cd2-9a28-625ef4e2c221/EMV%20Validation%20Service%20Product%20Capability%20Guide.pdf", "https://dwaynegefferie.substack.com/p/modern-issuer-processing"]
---

# Stand-In Processing Service

**Definition.** Stand-In Processing Service is the technology capability that provides stand-in or on-behalf-of (STIP) authorization decisioning when the issuer host is unavailable or times out, applying parameterised limits and risk rules so transactions can still be approved or declined.
**Also known as:** STIP Service, On-Behalf-Of Processing, Stand-In Authorization.

## Relationships
- Stand-In Processing Service is defined in the Core Processing domain.
- Stand-In Processing Service is derived from Card Authorization Engine.
- Stand-In Processing Service is related to Card Authorization.

## Details
Stand-In Processing Service activates when an ISO 8583 authorization cannot reach the issuer host within scheme timeout windows, applying issuer-defined floor limits, velocity caps and risk parameters to approve or decline on the issuer's behalf. Schemes and processors run STIP to preserve approval rates during host outages, then reconcile stand-in decisions with the issuer once connectivity returns. Conservative parameters limit issuer exposure during stand-in.

## References
- [American Express EMV Validation Service Capability Guide](https://network.americanexpress.com/globalnetwork/dam/jcr:7d61622d-72b8-4cd2-9a28-625ef4e2c221/EMV%20Validation%20Service%20Product%20Capability%20Guide.pdf)
- [Modern Issuer Processing](https://dwaynegefferie.substack.com/p/modern-issuer-processing)
