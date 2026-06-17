---
id: brinson-attribution-service
title: Brinson Attribution Service
type: technology-capability
domain: Core Processing
level: L3
aliases: ["Brinson-Fachler Service", "Return Attribution Engine", "Active Return Decomposition"]
status: draft
sources: ["https://www.neoxam.com/datahub/performance-attribution-brinson-fachler-method-explained/", "https://en.wikipedia.org/wiki/Performance_attribution"]
---

# Brinson Attribution Service

**Definition.** Brinson Attribution Service decomposes active portfolio return into allocation, selection and interaction effects by segment using the Brinson-Fachler methodology for performance attribution.
**Also known as:** Brinson-Fachler Service, Return Attribution Engine, Active Return Decomposition.

## Relationships
- Brinson Attribution Service is defined in the Core Processing domain.
- Brinson Attribution Service is derived from Performance & Attribution Engine.

## Details
Brinson Attribution Service explains the difference between portfolio and benchmark return segment by segment. Under the Brinson-Fachler model the allocation effect for a segment is the active weight times the benchmark segment return less the total benchmark return; the selection effect is the benchmark weight times the active segment return; and the interaction effect is the active weight times the active segment return. Summed across segments these reconcile to total active return, and multi-period results are linked geometrically. The service produces this decomposition so portfolio managers can attribute value-add to top-down allocation versus bottom-up security selection.

## References
- [Brinson-Fachler performance attribution explained (NeoXam)](https://www.neoxam.com/datahub/performance-attribution-brinson-fachler-method-explained/)
- [Performance attribution (Wikipedia)](https://en.wikipedia.org/wiki/Performance_attribution)
