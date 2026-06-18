---
id: proposed-integration-and-apis-systems
title: Proposed Integration & APIs Systems (systems-refresh)
type: status-note
status: draft
domain: Integration & APIs
---

# Proposed Integration & APIs Systems

Research sub-agent proposal for the TECHNOLOGY domain **Integration & APIs**. Systems
below are genuinely missing (not already in `glossary/_canonical-names.md` Legacy/Modern
sections) and each realizes one of the 4 top-level tech caps: **API Management,
Integration Platform, Workflow Orchestration, Notification Services**.

Rules applied:
- `realizes` is an existing Integration & APIs top-level tech capability.
- `supersedes` (modern only) names a real legacy system of the **same capability** —
  either already in the registry or added in this same file. No cross-capability pairing.
- Notification Services had **zero** systems; a generic **Legacy SMS Gateway** legacy is
  added so the modern notification systems have a same-capability supersede target.
- Canonical names are 1-4 words, Title Case, globally unique (checked against registry).

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only — SAME capability) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| IBM API Connect | legacy-system | API Management |  | IBM | On-premises/hybrid full-lifecycle API management suite (create, secure, manage, socialize, analyze APIs) with gateway, API manager and developer portal; long-standing incumbent in regulated enterprises. | API Connect, IBM APIC | https://www.ibm.com/products/api-connect ; https://en.wikipedia.org/wiki/IBM_API_Management |
| Gravitee | modern-system | API Management | CA API Gateway | Gravitee.io | Open-source, event-native API management platform covering design, deploy, manage and secure for synchronous and asynchronous APIs; gateway, console and developer portal under Apache 2.0 with optional enterprise support. | Gravitee.io, Gravitee APIM | https://www.gravitee.io/platform/api-management-1 ; https://github.com/gravitee-io/gravitee-api-management |
| AWS API Gateway | modern-system | API Management | CA API Gateway | Amazon Web Services | Fully managed cloud service to create, publish, maintain, monitor and secure REST, HTTP and WebSocket APIs at scale, with throttling, authorization and usage plans; common front door for serverless and microservice backends. | Amazon API Gateway, APIGW | https://aws.amazon.com/api-gateway/ ; https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html |
| Azure API Management | modern-system | API Management | CA API Gateway | Microsoft | Fully managed hybrid, multi-cloud API gateway and management service for publishing, securing, transforming and analyzing APIs, with a developer portal and policy engine. | Azure APIM, APIM | https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts ; https://azure.microsoft.com/en-us/products/api-management |
| IBM App Connect Enterprise | legacy-system | Integration Platform |  | IBM | Enterprise integration/ESB runtime (formerly IBM Integration Bus / WebSphere Message Broker) for routing and transforming messages between disparate applications across SOA; long-standing on-premises middleware in banks. | IBM ACE, IBM Integration Bus, IIB, WebSphere Message Broker | https://en.wikipedia.org/wiki/IBM_App_Connect_Enterprise ; https://www.ibm.com/products/app-connect-enterprise |
| SnapLogic | modern-system | Integration Platform | IBM App Connect Enterprise | SnapLogic | Low-code cloud iPaaS for application and data integration using pre-built connectors ("Snaps"), supporting ETL/ELT pipelines and API-led integration across SaaS and on-premises systems. | SnapLogic iPaaS, SnapLogic Intelligent Integration Platform | https://www.snaplogic.com/ ; https://www.snaplogic.com/blog/top-ipaas-vendors |
| Workato | modern-system | Integration Platform | IBM App Connect Enterprise | Workato | Cloud iPaaS for integration and workflow automation with an AI-assisted, low-code experience aimed at both IT and business "citizen developer" automation ("recipes"). | Workato iPaaS, Workato Recipes | https://www.workato.com/ ; https://www.gartner.com/reviews/market/integration-platform-as-a-service-worldwide/vendor/workato |
| IBM Business Automation Workflow | legacy-system | Workflow Orchestration |  | IBM | Business process management / workflow engine (formerly IBM BPM, WebSphere Lombardi) for modeling, automating and orchestrating human and system tasks across long-running banking processes. | IBM BPM, IBM BAW, WebSphere Lombardi | https://www.ibm.com/products/business-automation-workflow ; https://www.peerspot.com/products/comparisons/appian_vs_ibm-business-automation-workflow |
| Appian | modern-system | Workflow Orchestration | IBM Business Automation Workflow | Appian | Low-code process automation / BPM platform combining workflow orchestration, business rules, case management and RPA/AI to build and run enterprise process applications. | Appian BPM, Appian Platform | https://appian.com/products/platform/process-automation/business-process-management-bpm ; https://www.cio.com/article/401356/top-16-business-process-management-tools.html |
| Bonita | modern-system | Workflow Orchestration | IBM Business Automation Workflow | Bonitasoft | Open-source low-code BPM platform for designing, deploying and running business processes and workflow applications, extensible via open-source connectors and deployable to Bonita Cloud. | Bonitasoft, Bonita BPM | https://www.bonitasoft.com/ ; https://www.softwarereviews.com/research/bonitasoft-bpm-is-now-available-in-the-cloud |
| Legacy SMS Gateway | legacy-system | Notification Services |  | (generic) | Generic on-premises/carrier SMS and email notification gateway representing pre-cloud outbound customer messaging (SMPP/SMTP-based alerting, OTP and statement notices). | On-Prem SMS Gateway, SMPP Gateway, Legacy Notification Gateway | https://en.wikipedia.org/wiki/Short_Message_Peer-to-Peer ; https://en.wikipedia.org/wiki/SMS_gateway |
| Twilio | modern-system | Notification Services | Legacy SMS Gateway | Twilio | Cloud communications platform (CPaaS) with programmable messaging APIs for SMS, MMS, RCS, WhatsApp, plus voice and email, used to deliver customer notifications, OTP and alerts at scale. | Twilio Programmable Messaging, Twilio CPaaS | https://www.twilio.com/en-us/messaging/apis/programmable-messaging-api ; https://www.twilio.com/en-us/cpaas |
| Amazon SNS | modern-system | Notification Services | Legacy SMS Gateway | Amazon Web Services | Fully managed publish-subscribe (pub/sub) messaging and notification service for application-to-application and application-to-person delivery via SMS, push, email and HTTP/SQS endpoints with fan-out. | Simple Notification Service, AWS SNS | https://aws.amazon.com/sns/ ; https://aws.amazon.com/sns/faqs/ |
| Amazon SES | modern-system | Notification Services | Legacy SMS Gateway | Amazon Web Services | Fully managed, high-throughput cloud email service for transactional and notification email (and inbound receiving), with deliverability, bounce/complaint handling and SNS event integration. | Simple Email Service, AWS SES | https://aws.amazon.com/ses/ ; https://docs.aws.amazon.com/ses/latest/dg/Welcome.html |
| Braze | modern-system | Notification Services | Legacy SMS Gateway | Braze | Customer engagement platform for cross-channel, personalized messaging and journey orchestration across push, in-app, email, SMS/MMS and WhatsApp using real-time behavioral data. | Braze Customer Engagement Platform | https://www.braze.com/product/overview ; https://www.braze.com/product/sms |

## Counts

- **Legacy systems: 4** — IBM API Connect (API Management), IBM App Connect Enterprise
  (Integration Platform), IBM Business Automation Workflow (Workflow Orchestration),
  Legacy SMS Gateway (Notification Services).
- **Modern systems: 10** — Gravitee, AWS API Gateway, Azure API Management (API
  Management); SnapLogic, Workato (Integration Platform); Appian, Bonita (Workflow
  Orchestration); Twilio, Amazon SNS, Amazon SES, Braze (Notification Services).

Note: Notification Services modern systems supersede the newly-added generic
**Legacy SMS Gateway** (same capability). Gravitee / AWS API Gateway / Azure API
Management supersede **CA API Gateway** (existing registry legacy, API Management).
Workato/SnapLogic and Appian/Bonita supersede the IBM legacy systems added in this file.
Celigo was considered for Integration Platform but dropped to keep the set tight and
non-redundant with SnapLogic/Workato.
