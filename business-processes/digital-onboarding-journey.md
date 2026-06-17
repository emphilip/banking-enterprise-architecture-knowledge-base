---
id: digital-onboarding-journey
title: Digital Onboarding Journey
type: business-process
domain: Channels & Engagement
aliases: ["Digital Account Opening Journey", "Online Onboarding Flow"]
status: draft
sources: ["https://www.onespan.com/blog/redefining-digital-account-opening-and-onboarding-customer-journey", "https://www.csiweb.com/what-to-know/content-hub/blog/your-7-step-guide-to-a-digital-account-opening-system/", "https://www.innovatrics.com/ekyc-online-customer-onboarding-and-identity-verification/"]
---

# Digital Onboarding Journey

**Definition.** Digital Onboarding Journey is the customer-facing digital account-opening process across web and mobile that captures the application, runs electronic identity verification (eKYC), funds and activates the channel, and hands off to back-office Customer Onboarding and KYC.
**Also known as:** Digital Account Opening Journey, Online Onboarding Flow.

## Relationships
- Digital Onboarding Journey is defined in the Channels & Engagement domain.
- Digital Onboarding Journey depends on the Digital Banking capability.
- Digital Onboarding Journey depends on the Digital Onboarding capability.

## Details
Digital Onboarding Journey is owned by the Digital Onboarding Specialist. Inputs are the Digital Application and applicant identity data; outputs are an activated digital customer and a Channel Session. Controls include eKYC and digital-identity handoff, strong customer authentication (SCA) enrolment, consent capture, accessibility (WCAG), and abandonment / save-and-resume handling.

## Flow
- Start Digital Application causes Capture Applicant Details.
- Capture Applicant Details causes Verify Digital Identity.
- Verify Digital Identity causes Enrol Strong Authentication.
- Enrol Strong Authentication causes Fund Digital Account.
- Fund Digital Account causes Activate Digital Channel.

## References
- [OneSpan digital account opening journey](https://www.onespan.com/blog/redefining-digital-account-opening-and-onboarding-customer-journey)
- [CSI digital account opening guide](https://www.csiweb.com/what-to-know/content-hub/blog/your-7-step-guide-to-a-digital-account-opening-system/)
- [Innovatrics eKYC onboarding](https://www.innovatrics.com/ekyc-online-customer-onboarding-and-identity-verification/)
