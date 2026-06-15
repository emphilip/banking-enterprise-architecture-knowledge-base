---
id: capture-request
title: Capture Request
type: process-step
process: Service Request Handling
order: 1
aliases: ["Log Request", "Request Capture Step"]
status: draft
sources: ["https://www.givainc.com/resources/itil/service-request-management/", "https://www.connectwise.com/blog/the-importance-of-service-request-management"]
---

# Capture Request

**Definition.** Capture Request captures a customer service request from a channel and creates a ticket with the request type and details.
**Also known as:** Log Request, Request Capture Step.

## Relationships
- Capture Request is defined in the Service Request Handling process.
- Capture Request causes Authenticate Requester.
- Capture Request depends on the Contact Center Platform capability.
- Capture Request mentions Service Advisor.
- Capture Request mentions Service Request Ticket.
- Capture Request mentions Service Request Raised Event.

## Details
The Service Advisor captures the request. The Service Request Raised Event triggers the flow. Inputs are the Service Request Ticket; outputs are a logged request. Controls include channel intake logging and mandatory-fields capture.

## References
- [Giva service request management](https://www.givainc.com/resources/itil/service-request-management/)
- [ConnectWise service request management](https://www.connectwise.com/blog/the-importance-of-service-request-management)
