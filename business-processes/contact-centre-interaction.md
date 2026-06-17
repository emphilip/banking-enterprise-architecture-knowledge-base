---
id: contact-centre-interaction
title: Contact Centre Interaction
type: business-process
domain: Channels & Engagement
aliases: ["Call Centre Interaction Handling", "Contact Handling Process"]
status: draft
sources: ["https://www.teneo.ai/blog/ivr-call-center", "https://www.pindrop.com/blog/customer-authentication-guide", "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9154627"]
---

# Contact Centre Interaction

**Definition.** Contact Centre Interaction is the inbound contact-centre interaction-lifecycle process covering IVR self-service capture, caller authentication, skills-based routing to an agent, interaction handling and resolution, and wrap-up with quality assurance.
**Also known as:** Call Centre Interaction Handling, Contact Handling Process.

## Relationships
- Contact Centre Interaction is defined in the Channels & Engagement domain.
- Contact Centre Interaction depends on the Contact Center capability.
- Contact Centre Interaction depends on the Inbound Contact Servicing capability.

## Details
Contact Centre Interaction is handled by the Contact Centre Agent. Inputs are the inbound contact and caller authentication inputs; outputs are a resolved interaction and an Interaction Record. Controls include caller authentication (including voice biometrics), call recording and consent, QA monitoring and scorecards, and data protection.

## Flow
- Capture IVR Selection causes Authenticate Caller.
- Authenticate Caller causes Route Interaction.
- Route Interaction causes Handle Customer Interaction.
- Handle Customer Interaction causes Wrap Up Interaction.
- Wrap Up Interaction causes Score Interaction Quality.

## References
- [Teneo IVR call center](https://www.teneo.ai/blog/ivr-call-center)
- [Pindrop customer authentication guide](https://www.pindrop.com/blog/customer-authentication-guide)
- [USPTO contact center routing patent](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/9154627)
