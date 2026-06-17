---
id: loan-application-submitted-event
title: Loan Application Submitted Event
type: event
domain: Lending & Credit
aliases: ["Application Received Event", "Origination Started Event"]
status: draft
sources: ["https://addy.so/blog/loan-origination-system-workflow", "https://www.amerisave.com/learn/mortgage-loan-processing-in-the-stages-between-application-and-closing"]
---

# Loan Application Submitted Event

**Definition.** Loan Application Submitted Event is the business trigger marking receipt of a new loan or mortgage application that starts origination. Loan Application Submitted Event opens the origination flow.

**Also known as:** Application Received Event, Origination Started Event.

## Relationships
- Loan Application Submitted Event is related to the Lending & Credit domain.
- Loan Application Submitted Event causes Capture Loan Application.
- Loan Application Submitted Event causes Take Mortgage Application.
- Loan Application Submitted Event mentions Loan Origination Workflow.

## Details
Loan Application Submitted Event fires when a borrower submits a loan request through a channel, carrying the applicant identifier, product requested and timestamp. For consumer loans the event triggers Capture Loan Application in the Loan Origination Workflow; for mortgages it triggers Take Mortgage Application in the Mortgage Origination flow, which also starts the regulatory disclosure clock. The event establishes the application date used for TRID and other timeline controls and initiates KYC capture.

## References
- https://addy.so/blog/loan-origination-system-workflow
- https://www.amerisave.com/learn/mortgage-loan-processing-in-the-stages-between-application-and-closing
