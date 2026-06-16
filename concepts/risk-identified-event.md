---
id: risk-identified-event
title: Risk Identified Event
type: event
domain: Risk Management
aliases: ["New Risk Event", "Risk Registered Event"]
status: draft
sources: ["https://www.coso.org/guidance-erm", "https://www.flowgrc.com/blog/how-to-build-a-risk-register"]
---

# Risk Identified Event

**Definition.** Risk Identified Event is the business event raised when a new risk is identified and registered, triggering the assessment and treatment activities of the risk-management lifecycle.

**Also known as:** New Risk Event, Risk Registered Event.

## Relationships
- Risk Identified Event is related to the Risk Management domain.
- Risk Identified Event causes Identify Risk Event.
- Risk Identified Event mentions Risk Register.

## Details
Risk Identified Event is emitted when a risk surfaces from business activities, loss events, control failures or emerging-risk scanning and is logged into the Risk Register with a description, category and provisional owner. The event opens the downstream COSO ERM workflow: inherent scoring on likelihood-by-impact scales, assessment of control effectiveness to derive residual risk, comparison against appetite, and a treatment decision. By making identification an explicit event, the bank can ensure taxonomy completeness, mandatory-field capture and timely routing to assessment, and can re-trigger the cycle when a register review date falls due or material changes warrant re-assessment.

## References
- https://www.coso.org/guidance-erm
- https://www.flowgrc.com/blog/how-to-build-a-risk-register
