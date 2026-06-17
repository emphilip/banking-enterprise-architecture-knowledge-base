---
id: channel-servicing
title: Channel Servicing
type: business-process
domain: Channels & Engagement
aliases: ["Omnichannel Servicing", "Self-Service Channel Process"]
status: draft
sources: ["https://www.ringcentral.com/us/en/blog/omnichannel-banking-trends/", "https://www.smartcommunications.com/resources/guides/the-ultimate-guide-to-omnichannel-orchestration/", "https://magenest.com/en/omnichannel-banking-solutions/"]
---

# Channel Servicing

**Definition.** Channel Servicing is the omnichannel self-service and assisted-servicing process across digital, IVR and branch channels that authenticates the channel user, orchestrates the session, resolves self-service requests, and escalates to assisted servicing with context preserved.
**Also known as:** Omnichannel Servicing, Self-Service Channel Process.

## Relationships
- Channel Servicing is defined in the Channels & Engagement domain.
- Channel Servicing depends on the Channel Management capability.
- Channel Servicing depends on the Digital Self-Service capability.

## Details
Channel Servicing is operated by the Channel Operations Analyst. Inputs are the Channel Session and a customer self-service request; outputs are a resolved request and an Interaction Record. Controls include SCA / step-up authentication, consistent cross-channel context, accessibility, and escalation handoff control.

## Flow
- Open Channel Session causes Authenticate Channel User.
- Authenticate Channel User causes Identify Service Intent.
- Identify Service Intent causes Orchestrate Channel Journey.
- Orchestrate Channel Journey causes Resolve Self-Service Request.
- Resolve Self-Service Request causes Escalate To Assisted Servicing.
- Escalate To Assisted Servicing causes Record Channel Interaction.

## References
- [RingCentral omnichannel banking trends](https://www.ringcentral.com/us/en/blog/omnichannel-banking-trends/)
- [SmartCommunications omnichannel orchestration](https://www.smartcommunications.com/resources/guides/the-ultimate-guide-to-omnichannel-orchestration/)
- [Magenest omnichannel banking](https://magenest.com/en/omnichannel-banking-solutions/)
