---
id: route-interaction
title: Route Interaction
type: process-step
process: Contact Centre Interaction
order: 3
aliases: ["Distribute Interaction", "Skills Routing Step"]
status: draft
sources: ["https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9154627"]
---

# Route Interaction

**Definition.** Route Interaction performs skills-based routing of the interaction to the most appropriate available agent.
**Also known as:** Distribute Interaction, Skills Routing Step.

## Relationships
- Route Interaction is defined in the Contact Centre Interaction process.
- Route Interaction causes Handle Customer Interaction.
- Route Interaction depends on the Contact Center Platform capability.
- Route Interaction mentions Contact Centre Agent.

## Details
The Contact Centre Agent receives the routed interaction. Inputs are the authenticated caller; outputs are a routed interaction. At the decision point, if the caller self-served in IVR the flow proceeds to wrap-up; otherwise it routes. Controls include routing rules and queue / SLA controls.

## References
- [USPTO contact center routing patent](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9154627)
