---
id: authenticate-caller
title: Authenticate Caller
type: process-step
process: Contact Centre Interaction
order: 2
aliases: ["Caller Authentication", "Voice Verification"]
status: draft
sources: ["https://www.pindrop.com/blog/customer-authentication-guide"]
---

# Authenticate Caller

**Definition.** Authenticate Caller authenticates the caller in the IVR or agent flow using knowledge factors or voice biometrics.
**Also known as:** Caller Authentication, Voice Verification.

## Relationships
- Authenticate Caller is defined in the Contact Centre Interaction process.
- Authenticate Caller causes Route Interaction.
- Authenticate Caller depends on the Customer Authentication capability.
- Authenticate Caller mentions Contact Centre Agent.

## Details
The Contact Centre Agent confirms caller authentication. Inputs are the captured intent and credentials; outputs are an authenticated caller. At the decision point, if authentication fails the flow steps up or denies. Controls include caller authentication, voice biometrics and encryption.

## References
- [Pindrop customer authentication guide](https://www.pindrop.com/blog/customer-authentication-guide)
