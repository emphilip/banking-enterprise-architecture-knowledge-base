---
id: proposed-customer-management-tech
title: Proposed Customer Management Tech Capability Decomposition
type: status-note
status: draft
author: tech-decomposition sub-agent
date: 2026-06-15
---

# Proposed Customer Management — Technology Capability Decomposition + Systems Refresh

Scope: enabling technology capabilities for the Customer Management domain. L2 (and
selected L3) sub-capabilities for the four existing parent tech capabilities, plus a
systems refresh. Sub-capabilities are `defined_in` the SAME tech domain as their parent
and `derived_from` that parent.

Parents (verbatim, do not duplicate):
- CRM Platform — domain: Channels & Engagement
- Master Data Management — domain: Data & Analytics
- Customer Identity — domain: Security & Identity
- Conversational AI — domain: AI & Automation

All proposed names checked against `glossary/_canonical-names.md` for global uniqueness and
to keep tech names distinct from business capability names (e.g. business cap "Case
Management" -> tech "Case Management Workbench"; business cap "Customer Segmentation"
exists -> tech named "Customer 360 View"; "Consent Management Service" suffixed to avoid
collision with any consent business capability).

## 1) Technology sub-capabilities

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Contact & Account Management | technology-capability | L2 | CRM Platform | Channels & Engagement | CRM module maintaining person/household and legal-entity records, relationships and interaction history as the system-of-engagement view of the customer. | Account & Contact Management; Party Record Management | derived_from CRM Platform; defined_in Channels & Engagement; depends_on Master Data Management; related_to Customer Profile Management | https://noltic.com/stories/the-ultimate-guide-to-salesforce-financial-services-cloud; https://trailhead.salesforce.com/content/learn/modules/financial-services-cloud-basics/deliver-specialized-banking-services |
| Case Management Workbench | technology-capability | L2 | CRM Platform | Channels & Engagement | CRM agent workspace for logging, routing, prioritising and resolving service cases, complaints and requests with SLA tracking and automated assignment. | Service Case Workbench; Service Console | derived_from CRM Platform; defined_in Channels & Engagement; related_to Case Management; depends_on Workflow Orchestration | https://noltic.com/stories/the-ultimate-guide-to-salesforce-financial-services-cloud; https://www.salesforce.com/news/stories/financial-services-cloud-ai-capabilities/ |
| Campaign Automation | technology-capability | L2 | CRM Platform | Channels & Engagement | Marketing-automation engine that designs, triggers and measures multi-channel, behaviour-driven outreach campaigns and journeys from the CRM. | Marketing Automation; Journey Orchestration | derived_from CRM Platform; defined_in Channels & Engagement; related_to Campaign Management; depends_on Customer 360 View | https://www.salesforce.com/products/what-is-customer-360/; https://www.ksolves.com/blog/salesforce/customer-360 |
| Customer 360 View | technology-capability | L2 | CRM Platform | Channels & Engagement | Unified, aggregated profile assembling holdings, transactions, interactions and life events into a single actionable view for advisors and service agents. | Single Customer View; C360 | derived_from CRM Platform; defined_in Channels & Engagement; depends_on Master Data Management; related_to Customer Segmentation | https://www.salesforce.com/products/what-is-customer-360/; https://www.nexgenarchitects.com/blog-posts/customer-360-view-banking-salesforce |
| Party Matching & Merge | technology-capability | L2 | Master Data Management | Data & Analytics | Entity-resolution engine applying deterministic and probabilistic match rules plus merge/unmerge to deduplicate party records across source systems. | Entity Resolution; Match & Merge | derived_from Master Data Management; defined_in Data & Analytics; related_to Party Data Management; depends_on Machine Learning Platform | https://www.reltio.com/products/entity-resolution/; https://lumendata.com/technology/how-to-get-the-golden-master-copy-of-your-data-using-match-merge-amp-survivorship-in-informatica-mdm-saas/ |
| Golden Record Management | technology-capability | L2 | Master Data Management | Data & Analytics | Survivorship and best-version-of-truth engine that constructs and maintains the trusted golden party record with crosswalks and lineage. | Survivorship Engine; Best Record Management | derived_from Master Data Management; defined_in Data & Analytics; related_to Customer Profile Management; depends_on Data Governance | https://www.reltio.com/master-data-management/; https://www.reltio.com/resources/blog/master-data-management-best-practices/ |
| Data Stewardship Workflow | technology-capability | L2 | Master Data Management | Data & Analytics | Steward workbench with task queues, escalations and SLA-driven review for resolving potential matches, data-quality exceptions and manual overrides. | Stewardship Console; Bulk Match Review | derived_from Master Data Management; defined_in Data & Analytics; depends_on Workflow Orchestration; related_to Data Governance | https://www.reltio.com/resources/blog/master-data-management-best-practices/; https://www.reltio.com/products/entity-resolution/ |
| Customer Authentication | technology-capability | L2 | Customer Identity | Security & Identity | Adaptive, multi-factor and passwordless (FIDO/passkey) authentication service governing customer login and step-up across digital channels. | Adaptive Authentication; MFA Service | derived_from Customer Identity; defined_in Security & Identity; related_to Digital Banking; depends_on Threat Detection | https://medium.com/razi-chaudhry/a-guide-to-key-ciam-capabilities-and-implementation-blueprints-ciam-part-3-7621d1966105; https://www.hypr.com/resources/guide-fido-authentication |
| Consent Management Service | technology-capability | L2 | Customer Identity | Security & Identity | Service capturing, enforcing and auditing customer consent, privacy preferences and communication opt-ins/opt-outs for regulatory compliance. | Consent & Preference Management; Privacy Management | derived_from Customer Identity; defined_in Security & Identity; related_to Regulatory Compliance; depends_on Data Governance | https://wso2.com/whitepapers/customer-identity-and-access-management-a-wso2-reference-architecture/; https://medium.com/razi-chaudhry/a-guide-to-key-ciam-capabilities-and-implementation-blueprints-ciam-part-3-7621d1966105 |
| Identity Proofing Service | technology-capability | L2 | Customer Identity | Security & Identity | Orchestrated identity-verification service validating document, biometric and data signals to establish customer identity at onboarding and high-risk events. | Identity Verification Service; ID Proofing | derived_from Customer Identity; defined_in Security & Identity; related_to Identity Verification; depends_on Intelligent Document Processing | https://medium.com/razi-chaudhry/a-guide-to-key-ciam-capabilities-and-implementation-blueprints-ciam-part-3-7621d1966105; https://www.paloaltonetworks.com/cyberpedia/what-is-ciam |
| Virtual Assistant | technology-capability | L2 | Conversational AI | AI & Automation | Customer-facing conversational agent (chat/voice) using NLU/NLG to answer queries, surface data and execute self-service banking tasks with human handoff. | Digital Assistant; Customer Chatbot | derived_from Conversational AI; defined_in AI & Automation; related_to Customer Servicing; depends_on Generative AI Platform | https://kasisto.com/products/kai-platform/; https://www.xenonstack.com/blog/banking-chatbots-amazon-lex-agenticai |
| Agent Assist | technology-capability | L2 | Conversational AI | AI & Automation | AI co-pilot embedded in the agent desktop that transcribes, recommends next-best-action and drafts responses to support live human service agents. | Agent Copilot; Next Best Action Assist | derived_from Conversational AI; defined_in AI & Automation; related_to Contact Center; depends_on Generative AI Platform | https://www.salesforce.com/agentforce/einstein-copilot/; https://www.salesforce.com/news/stories/financial-services-cloud-ai-capabilities/ |

### Selected L3 (under the most important L2s)

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Probabilistic Match Engine | technology-capability | L3 | Party Matching & Merge | Data & Analytics | ML/LLM-augmented fuzzy matching with weighted, relevance-based scoring to resolve party records beyond exact deterministic rules. | Fuzzy Match Engine; AI Matching | derived_from Party Matching & Merge; defined_in Data & Analytics; depends_on Machine Learning Platform | https://www.reltio.com/products/entity-resolution/ |
| Survivorship Rule Engine | technology-capability | L3 | Golden Record Management | Data & Analytics | Configurable field-level survivorship rules that select the prevailing attribute value across crosswalk records to build the golden record. | Survivorship Rules; Field Survivorship | derived_from Golden Record Management; defined_in Data & Analytics; related_to Data Governance | https://lumendata.com/technology/how-to-get-the-golden-master-copy-of-your-data-using-match-merge-amp-survivorship-in-informatica-mdm-saas/; https://www.reltio.com/master-data-management/ |
| Passwordless Authentication | technology-capability | L3 | Customer Authentication | Security & Identity | FIDO2/passkey public-key credential service enabling phishing-resistant, password-free customer login and transaction approval. | Passkey Service; FIDO2 Service | derived_from Customer Authentication; defined_in Security & Identity; related_to Threat Detection | https://www.hypr.com/resources/guide-fido-authentication; https://www.microsoft.com/en-us/security/business/security-101/what-is-fido2 |
| Identity Orchestration Engine | technology-capability | L3 | Identity Proofing Service | Security & Identity | Visual workflow engine that sequences anti-fraud, document and biometric proofing services into consistent identity journeys. | Identity Orchestration; Proofing Orchestration | derived_from Identity Proofing Service; defined_in Security & Identity; related_to Workflow Orchestration | https://medium.com/razi-chaudhry/a-guide-to-key-ciam-capabilities-and-implementation-blueprints-ciam-part-3-7621d1966105; https://guptadeepak.com/customer-identity-hub/customer-identity-access-management-architecture-complete-guide |

## 2) Systems refresh

Already covered (excluded): Siebel CRM, Salesforce Financial Services Cloud, IBM Tivoli
Identity Manager, Ping Identity, Auth0, Legacy IVR System, Kasisto. (ForgeRock already in
registry under Identity Access Management.) `realizes` must be an existing top-level tech
capability: CRM Platform, Master Data Management, Customer Identity, or Conversational AI.

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| SAP CRM | legacy-system | CRM Platform | — | SAP | On-premise SAP Customer Relationship Management suite (part of SAP Business Suite) for sales, service and marketing, now in maintenance and superseded by cloud CRM. | SAP CRM 7.0; mySAP CRM | https://www.cxtoday.com/crm/gartner-magic-quadrant-crm-customer-engagement-center-2025/ |
| Microsoft Dynamics 365 | modern-system | CRM Platform | SAP CRM | Microsoft | Cloud CRM/ERP suite whose Customer Service and Contact Center apps unify CRM, CCaaS and agentic AI for banking sales and service. | Dynamics 365 Customer Service; D365 | https://www.microsoft.com/en-us/dynamics-365; https://www.cxtoday.com/crm/gartner-magic-quadrant-crm-customer-engagement-center-2025/ |
| Pega Customer Service | modern-system | CRM Platform | Siebel CRM | Pegasystems | Case-centric customer service and engagement application built on Pega's low-code platform, used for banking service, complaints and next-best-action. | Pega CRM; Pega CS | https://www.peerspot.com/products/pega-crm-pros-and-cons; https://www.getapp.com/operations-management-software/a/dynamics-365/compare/pega-crm-solution/ |
| Informatica MDM | legacy-system | Master Data Management | — | Informatica | Established multidomain master data management platform (PowerCenter-era on-prem heritage) providing match-merge, survivorship and stewardship for party data. | Informatica MDM Hub; Siperian | https://www.infotech.com/software-reviews/categories/master-data-management/compare/reltio-data-cloud-vs-informatica-master-data-management; https://lumendata.com/technology/how-to-get-the-golden-master-copy-of-your-data-using-match-merge-amp-survivorship-in-informatica-mdm-saas/ |
| Reltio | modern-system | Master Data Management | Informatica MDM | Reltio | Cloud-native, AI-driven multidomain MDM SaaS providing real-time entity resolution, dynamic survivorship and stewardship for the golden party record. | Reltio Data Cloud; Reltio MDM | https://www.reltio.com/master-data-management/; https://www.reltio.com/products/entity-resolution/ |
| Amazon Lex | modern-system | Conversational AI | Legacy IVR System | Amazon Web Services | Managed conversational-AI service with ASR and NLU for building voice/text banking virtual assistants and automated self-service. | AWS Lex; Lex V2 | https://www.xenonstack.com/blog/banking-chatbots-amazon-lex-agenticai |

## Naming / collision notes
- "Case Management Workbench" (tech) distinct from business cap "Case Management".
- "Customer 360 View" chosen so as not to collide with business cap "Customer Segmentation"; aliases include Single Customer View.
- "Consent Management Service" suffixed with "Service" to keep tech name distinct from any business consent capability.
- "Customer Authentication", "Identity Proofing Service", "Virtual Assistant", "Agent Assist" verified absent from registry.
- "Virtual Assistant" is listed as an alias of the parent Conversational AI in the registry; promoting it to a distinct L2 canonical name may need reviewer confirmation, OR rename to "Self-Service Virtual Assistant" to be safe.
