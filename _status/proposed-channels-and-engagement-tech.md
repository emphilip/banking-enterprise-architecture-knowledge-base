---
id: proposed-channels-and-engagement-tech
title: Proposed Channels & Engagement Technology Decomposition (Sub-Capabilities + Systems Refresh)
type: proposal
status: draft
author: tech-decomposition sub-agent
date: 2026-06-17
---

# Proposed Channels & Engagement Technology Decomposition

Scope: decompose the two existing top-level **Channels & Engagement** technology
capabilities — **Digital Channel Platform** and **Contact Center Platform** — into
L2 (and L3 where useful) sub-capabilities, plus a **systems refresh** of notable
channel platforms not yet in the registry. **CRM Platform** is already decomposed
(Contact & Account Management, Case Management Workbench, Campaign Automation,
Customer 360 View); this proposal adds **one** clearly-missing CRM L2
(Knowledge Base Service) and does not re-add the existing four.

Grounding: digital-banking-platform reference architectures and vendor docs
(Backbase Engagement Banking, Temenos Infinity / Kony DBX, Q2, Alkami,
Thought Machine), CCaaS reference architectures and vendor docs (Genesys Cloud CX,
Amazon Connect, NICE CXone, Five9, Twilio Flex, Glia, Avaya, Cisco UCCE, Verint),
CNCF cloud-native patterns (progressive delivery / feature flags), PSD2 Strong
Customer Authentication, and WCAG accessibility.

Naming note: all canonical names were checked against `glossary/_canonical-names.md`
for global uniqueness. Tech sub-cap names are deliberately kept distinct from
**business** capabilities (tech **Mobile App Framework** vs business *Mobile
Banking*; tech **Web Banking Portal** vs business *Online Banking*; tech
**Interactive Voice Response** vs any *Self-Service IVR* business capability) and
from existing tech sub-caps / caps (Notification Services, Conversational AI,
Customer Identity, Customer Authentication, API Management, Analytics Platform).
All sub-capabilities are `defined_in` the **Channels & Engagement** domain (same as
their parent). Relationships use only the 7 verbs: `depends_on`, `derived_from`,
`supersedes`, `defined_in`, `related_to`, `causes`, `mentions`.

---

## 1) Technology sub-capabilities

`derived_from` links a sub-cap to its parent; `defined_in` links it to the domain.

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Mobile App Framework | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | Native and hybrid mobile app runtime, SDKs and design system delivering banking journeys on iOS/Android, including device binding and app shielding. | Mobile SDK Platform, Mobile Banking Framework, Multi-Experience Framework | derived_from Digital Channel Platform; defined_in Channels & Engagement; depends_on API Management; related_to Customer Identity | https://engineering.backbase.com/2025/02/18/backbase-engagement-banking-platform-tech-stack/ ; https://www.temenos.com/products/infinity/ |
| Web Banking Portal | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | Browser-based responsive/PWA banking web application and widget framework for retail and business users. | Internet Banking Portal, Web Channel, Online Banking Portal | derived_from Digital Channel Platform; defined_in Channels & Engagement; depends_on API Management | https://www.backbase.com/engagement-banking-platform ; https://www.alkami.com/digital-banking-solutions/ |
| Channel Orchestration Layer | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | Mid-tier that orchestrates data, workflows and shared customer state across mobile, web, branch and contact-centre execution surfaces. | Experience Orchestration, Backend-for-Frontend, Journey Orchestration Mid-Tier | derived_from Digital Channel Platform; defined_in Channels & Engagement; depends_on Integration Platform; depends_on Workflow Orchestration | https://www.backbase.com/blog/digital-banking-platform ; https://www.temenos.com/products/infinity/ |
| Digital Onboarding Journey | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | Configurable account-opening and origination journeys delivered through digital channels, with form orchestration, document upload and progress save/resume. | Digital Account Opening, Onboarding Journey Engine, Origination Front-End | derived_from Digital Channel Platform; defined_in Channels & Engagement; depends_on KYC Onboarding Platform; related_to Loan Origination Platform | https://www.temenos.com/products/infinity/ ; https://www.alkami.com/digital-banking-solutions/ |
| Digital SCA Service | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | In-channel strong customer authentication enforcement for digital sessions and transactions: step-up, dynamic linking, biometrics and transaction risk analysis per PSD2 SCA. | Step-Up Authentication Service, In-App SCA, Dynamic Linking Service | derived_from Digital Channel Platform; defined_in Channels & Engagement; depends_on Customer Identity; related_to Customer Authentication | https://www.onespan.com/blog/strong-customer-authentication-under-psd2-good-bad-and-ugly ; https://www.saltedge.com/products/strong_customer_authentication |
| In-App Messaging | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | Secure two-way in-session messaging, alerts and contextual prompts rendered inside digital channels (distinct from cross-channel Notification Services delivery). | In-Session Messaging, Secure Inbox, Contextual Messaging | derived_from Digital Channel Platform; defined_in Channels & Engagement; depends_on Notification Services; related_to Conversational AI | https://www.backbase.com/engagement-banking-platform ; https://www.glia.com/banking |
| Personalisation Engine | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | Real-time content, offer and next-best-action targeting that tailors digital experiences using customer context and behavioural signals. | Personalization Engine, Offer Targeting Engine, Next-Best-Experience Engine | derived_from Digital Channel Platform; defined_in Channels & Engagement; depends_on Analytics Platform; related_to Campaign Automation | https://www.temenos.com/products/infinity/ ; https://www.backbase.com/blog/digital-banking-platform |
| Digital Analytics | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | Capture and analysis of digital behavioural events, journey funnels and conversion/engagement metrics across web and mobile channels. | Digital Behavioural Analytics, Journey Analytics, Product Analytics | derived_from Digital Channel Platform; defined_in Channels & Engagement; depends_on Analytics Platform | https://www.temenos.com/products/infinity/ ; https://www.alkami.com/digital-banking-solutions/ |
| Feature Flag Service | technology-sub-capability | L2 | Digital Channel Platform | Channels & Engagement | Runtime flagging, progressive delivery and remote configuration enabling controlled rollout of digital features (canary, ring, kill-switch). | Feature Toggle Service, Release Flagging, Progressive Delivery Service | derived_from Digital Channel Platform; defined_in Channels & Engagement; related_to Digital Analytics | https://www.cncf.io/blog/2023/02/02/progressive-delivery/ ; https://engineering.backbase.com/2025/02/18/backbase-engagement-banking-platform-tech-stack/ |
| Native Mobile SDK | technology-sub-capability | L3 | Mobile App Framework | Channels & Engagement | Embeddable native iOS/Android software development kit exposing banking widgets, secure storage and biometric APIs for in-house and partner apps. | Mobile Banking SDK, Embeddable Mobile SDK | derived_from Mobile App Framework; defined_in Channels & Engagement | https://engineering.backbase.com/2025/02/18/backbase-engagement-banking-platform-tech-stack/ ; https://www.alkami.com/industry-leading-mobile-banking-platform-for-banks-credit-unions/ |
| Progressive Web App Runtime | technology-sub-capability | L3 | Web Banking Portal | Channels & Engagement | Installable, offline-capable progressive-web-app delivery of the web banking portal with service-worker caching and responsive layout. | PWA Runtime, Responsive Web Runtime | derived_from Web Banking Portal; defined_in Channels & Engagement | https://www.backbase.com/engagement-banking-platform ; https://web.dev/articles/what-are-pwas |
| A/B Testing Service | technology-sub-capability | L3 | Feature Flag Service | Channels & Engagement | Experimentation framework for controlled A/B and multivariate tests measuring impact of digital variants on engagement and conversion. | Experimentation Service, Multivariate Testing | derived_from Feature Flag Service; defined_in Channels & Engagement; related_to Digital Analytics | https://www.cncf.io/blog/2023/02/02/progressive-delivery/ ; https://www.backbase.com/blog/digital-banking-platform |
| Interactive Voice Response | technology-sub-capability | L2 | Contact Center Platform | Channels & Engagement | Self-service voice front door using DTMF and conversational prompts, menu/flow design, text-to-speech and call data collection before routing. | IVR Engine, Voice Self-Service Engine, Conversational IVR | derived_from Contact Center Platform; defined_in Channels & Engagement; related_to Conversational AI | https://www.genesys.com/capabilities ; https://docs.aws.amazon.com/prescriptive-guidance/latest/ivr-design-on-connect/features.html |
| Automatic Call Distribution | technology-sub-capability | L2 | Contact Center Platform | Channels & Engagement | Queueing and distribution engine that places, prioritises and matches inbound contacts to available agents. | ACD Engine, Queue Management, Call Distribution Engine | derived_from Contact Center Platform; defined_in Channels & Engagement | https://www.genesys.com/capabilities ; https://aws.amazon.com/connect/features/ |
| Omnichannel Routing Engine | technology-sub-capability | L2 | Contact Center Platform | Channels & Engagement | Unified routing across voice, chat, email, messaging and tasks using skills, predictive and journey-aware logic to a single agent workforce. | Omnichannel Routing, Interaction Routing Engine, Universal Queue | derived_from Contact Center Platform; defined_in Channels & Engagement; related_to Automatic Call Distribution | https://aws.amazon.com/connect/features/ ; https://www.genesys.com/genesys-cloud |
| Agent Desktop | technology-sub-capability | L2 | Contact Center Platform | Channels & Engagement | Unified agent workspace presenting interactions, customer context, guided workflows and AI assist across all channels in one interface. | Agent Workspace, Unified Agent Desktop, Contact Centre Desktop | derived_from Contact Center Platform; defined_in Channels & Engagement; depends_on Computer Telephony Integration; related_to Agent Assist | https://aws.amazon.com/connect/features/ ; https://www.genesys.com/capabilities |
| Interaction Analytics | technology-sub-capability | L2 | Contact Center Platform | Channels & Engagement | Speech and text analytics over recorded and live interactions for sentiment, topic, compliance and coaching insight (distinct from enterprise Analytics Platform). | Speech Analytics, Conversation Analytics, Interaction Insights | derived_from Contact Center Platform; defined_in Channels & Engagement; related_to Workforce Engagement Management | https://www.genesys.com/capabilities ; https://aws.amazon.com/connect/features/ |
| Workforce Engagement Management | technology-sub-capability | L2 | Contact Center Platform | Channels & Engagement | Forecasting, scheduling, quality management, recording and performance/coaching tooling for contact-centre staff (WEM/WFO). | WEM, Workforce Optimization, WFO | derived_from Contact Center Platform; defined_in Channels & Engagement | https://www.verint.com/workforce-management-solutions-wfm-software/ ; https://www.genesys.com/genesys-cloud |
| Computer Telephony Integration | technology-sub-capability | L2 | Contact Center Platform | Channels & Engagement | Middleware linking telephony events to business applications: call control, screen pop, click-to-dial and context passing to the desktop/CRM. | CTI, Telephony Integration, Call Control Service | derived_from Contact Center Platform; defined_in Channels & Engagement; related_to CRM Platform | https://www.genesys.com/capabilities ; https://aws.amazon.com/connect/features/ |
| Outbound Dialer | technology-sub-capability | L2 | Contact Center Platform | Channels & Engagement | Predictive, progressive and preview outbound calling and campaign engine with compliance pacing for collections and proactive contact. | Predictive Dialer, Campaign Dialer, Proactive Outbound | derived_from Contact Center Platform; defined_in Channels & Engagement; related_to Campaign Automation | https://www.five9.com/ ; https://www.genesys.com/capabilities |
| Skills-Based Routing | technology-sub-capability | L3 | Omnichannel Routing Engine | Channels & Engagement | Routing logic matching interactions to agents by skill, proficiency and priority across the universal queue. | Skill Routing, Proficiency Routing | derived_from Omnichannel Routing Engine; defined_in Channels & Engagement | https://aws.amazon.com/connect/features/ ; https://www.genesys.com/capabilities |
| Real-Time Transcription | technology-sub-capability | L3 | Interaction Analytics | Channels & Engagement | Live speech-to-text transcription of interactions feeding agent assist, real-time alerting and downstream analytics. | Live Transcription, Real-Time Speech-to-Text | derived_from Interaction Analytics; defined_in Channels & Engagement; related_to Agent Assist | https://aws.amazon.com/connect/features/ ; https://www.genesys.com/capabilities |
| Quality Management Service | technology-sub-capability | L3 | Workforce Engagement Management | Channels & Engagement | Interaction recording, evaluation, scorecards and automated quality scoring for agent coaching and compliance. | Quality Management, QM, Automated QA | derived_from Workforce Engagement Management; defined_in Channels & Engagement | https://www.verint.com/workforce-optimization-wfo-in-contact-centers/ ; https://www.genesys.com/capabilities |
| Screen Pop Service | technology-sub-capability | L3 | Computer Telephony Integration | Channels & Engagement | Event-driven presentation of caller identity and context to the agent desktop on contact arrival. | Screen Pop, Contextual Pop | derived_from Computer Telephony Integration; defined_in Channels & Engagement; related_to Agent Desktop | https://www.genesys.com/capabilities ; https://aws.amazon.com/connect/features/ |
| Knowledge Base Service | technology-sub-capability | L2 | CRM Platform | Channels & Engagement | Centralised, searchable knowledge articles and guided answers surfaced to agents and self-service to drive consistent resolution. | Knowledge Management, Service Knowledge Base, Answer Library | derived_from CRM Platform; defined_in Channels & Engagement; related_to Case Management Workbench | https://www.genesys.com/genesys-cloud ; https://www.glia.com/digital-customer-service |

---

## 2) New top-level technology capabilities

None proposed. The three existing Channels & Engagement top-level tech caps
(Digital Channel Platform, Contact Center Platform, CRM Platform) cover the domain;
all new work above is sub-capability decomposition. (Digital Customer Service /
"unified interaction management" platforms such as Glia are treated as systems
realizing the existing Contact Center Platform rather than as a new top-level cap,
to avoid overlap with Contact Center Platform and Conversational AI.)

---

## 3) Systems refresh

Only genuinely new systems are listed (already covered and therefore excluded:
Legacy Online Banking, Avaya Aura, Cisco UCCE [legacy]; Backbase, Q2, Amazon
Connect, Genesys Cloud [modern]). `supersedes` pairs are same-capability only
(digital→digital, CCaaS→CCaaS). Kony DBX is added as a **legacy** digital system
and Temenos Infinity as the **modern** successor that consolidated it.

### Legacy systems

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only — N/A) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| Kony DBX | legacy-system | Digital Channel Platform | — | Temenos (Kony) | Pre-acquisition multi-experience digital banking platform delivering web, mobile, ATM and branch journeys; technology folded into Temenos Infinity. | Kony Digital Banking, DBX | https://www.temenos.com/press_release/kony-is-now-temenos/ ; https://www.finextra.com/pressarticle/80429/temenos-integrates-kony-into-infinity |
| Verint WFM | legacy-system | Contact Center Platform | — | Verint | Established (often on-premise) workforce management / workforce optimisation suite for forecasting, scheduling, recording and quality in voice-centric contact centres. | Verint Workforce Management, Verint WFO, Verint Impact 360 | https://www.verint.com/workforce-management-solutions-wfm-software/ ; https://www.verint.com/workforce-optimization-wfo-in-contact-centers/ |

### Modern systems

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, SAME capability) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| Temenos Infinity | modern-system | Digital Channel Platform | Legacy Online Banking; Kony DBX | Temenos | Cloud-native, composable omnichannel digital banking engagement platform (microservices/APIs) for acquisition, onboarding and engagement; successor that absorbed Kony DBX. | Infinity, Temenos Digital, Infinity Engage | https://www.temenos.com/products/infinity/ ; https://www.forrester.com/blogs/temenos-acquires-kony-two-leaders-unite |
| Alkami | modern-system | Digital Channel Platform | Legacy Online Banking | Alkami Technology | Cloud-based digital sales and service platform (retail/business online and mobile banking, onboarding, data and marketing) for U.S. banks and credit unions. | Alkami Platform, Alkami Digital Banking, ORB | https://www.alkami.com/digital-banking-solutions/ ; https://www.alkami.com/about-alkami/ |
| NICE CXone | modern-system | Contact Center Platform | Avaya Aura | NICE | Enterprise cloud CCaaS platform with omnichannel routing, IVR, recording, quality management and integrated WEM/analytics. | CXone, NICE CXone Mpower, inContact | https://www.nice.com/info/nice-cxone-vs-five9 ; https://www.cxtoday.com/contact-center/genesys-vs-nice-vs-five9/ |
| Five9 | modern-system | Contact Center Platform | Cisco UCCE | Five9 | Cloud CCaaS platform noted for strong outbound/predictive dialing alongside inbound omnichannel, IVR and WEM. | Five9 Intelligent CX Platform | https://www.five9.com/ ; https://www.nextiva.com/blog/five9-vs-nice-contact-center.html |
| Twilio Flex | modern-system | Contact Center Platform | Avaya Aura | Twilio | Programmable, API-first cloud contact-centre platform that layers omnichannel routing and a customisable agent desktop over existing systems. | Flex, Twilio Flex CCaaS | https://www.twilio.com/en-us/flex ; https://www.babelforce.com/blog/the-definitive-ccaas-buyers-guide-2025-how-to-choose-the-right-contact-center-platform/ |
| Glia | modern-system | Contact Center Platform | Cisco UCCE | Glia | Digital customer service / unified interaction (ChannelLess) platform combining voice, chat, video, messaging and AI for finance and insurance. | Glia Interaction Platform, Digital Customer Service, DCS | https://www.glia.com/banking ; https://www.glia.com/news/glia-challenges-dated-ccaas-paradigm-with-unified-interaction-management |
| Verint WFM Cloud | modern-system | Contact Center Platform | Verint WFM | Verint | Cloud-native workforce engagement / workforce management suite (AI forecasting, omnichannel scheduling, quality and performance) succeeding on-premise WFM/WFO. | Verint Workforce Management Cloud, Verint WEM, Verint Open Platform WFM | https://www.verint.com/workforce-management-solutions-wfm-software/ ; https://www.verint.com/guides/how-modern-wfm-technology-solves-critical-contact-center-challenges/ |

---

## Summary of counts

- **Technology sub-capabilities proposed: 25** (17 L2 + 8 L3).
  Breakdown by parent:
  - Digital Channel Platform: 9 L2 (Mobile App Framework, Web Banking Portal,
    Channel Orchestration Layer, Digital Onboarding Journey, Digital SCA Service,
    In-App Messaging, Personalisation Engine, Digital Analytics, Feature Flag
    Service) + 3 L3 (Native Mobile SDK, Progressive Web App Runtime, A/B Testing
    Service) = 12.
  - Contact Center Platform: 8 L2 (Interactive Voice Response, Automatic Call
    Distribution, Omnichannel Routing Engine, Agent Desktop, Interaction Analytics,
    Workforce Engagement Management, Computer Telephony Integration, Outbound
    Dialer) + 4 L3 (Skills-Based Routing, Real-Time Transcription, Quality
    Management Service, Screen Pop Service) = 12.
  - CRM Platform: 1 L2 (Knowledge Base Service) = 1.
  - Total = 25 (12 + 12 + 1).
- **New top-level technology capabilities: 0.**
- **Systems: 9** — 2 legacy (Kony DBX, Verint WFM) + 7 modern (Temenos Infinity,
  Alkami, NICE CXone, Five9, Twilio Flex, Glia, Verint WFM Cloud).
