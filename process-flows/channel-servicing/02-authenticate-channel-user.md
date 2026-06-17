---
id: authenticate-channel-user
title: Authenticate Channel User
type: process-step
process: Channel Servicing
order: 2
aliases: ["Channel User Authentication", "Step-Up Auth"]
status: draft
sources: ["https://www.descope.com/learn/post/sca"]
---

# Authenticate Channel User

**Definition.** Authenticate Channel User authenticates the customer for the channel with SCA and step-up as risk requires.
**Also known as:** Channel User Authentication, Step-Up Auth.

## Relationships
- Authenticate Channel User is defined in the Channel Servicing process.
- Authenticate Channel User causes Identify Service Intent.
- Authenticate Channel User depends on the Customer Authentication capability.
- Authenticate Channel User mentions Channel Operations Analyst.
- Authenticate Channel User mentions Channel Session.

## Details
The Channel Operations Analyst manages caller and channel-user authentication. Inputs are the Channel Session and credentials; outputs are an authenticated session. At the decision point, if authentication fails the flow steps up or denies. Controls include SCA and adaptive / step-up authentication.

## References
- [Descope strong customer authentication](https://www.descope.com/learn/post/sca)
