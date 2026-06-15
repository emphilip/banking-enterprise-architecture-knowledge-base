---
id: proposed-payments-tech
title: Proposed Payments Technology Decomposition (Payment Orchestration)
type: proposal
status: draft
author: tech-decomposition sub-agent
date: 2026-06-15
---

# Proposed Payments Technology Decomposition — Payment Orchestration

Scope: L2 (and selected L3) technology-capability decomposition under the existing
parent technology capability **Payment Orchestration** (defined in the **Core
Processing** domain; aliases "Payment Hub"). Plus a systems refresh covering
notable payment platforms not already in the registry.

Grounded in payment-hub / payment-orchestration reference architectures (Volante
VolPay Hub, FIS Open Payment Framework, Finastra Global PAYplus, ACI Enterprise
Payments Platform, Form3), the ISO 20022 standard, SWIFT exceptions &
investigations guidance, and CNCF event-driven cloud-native patterns.

Naming note: all canonical names below were checked against
`glossary/_canonical-names.md` for global uniqueness. They are deliberately
distinct from business capabilities such as *Payment Execution*, *Payment
Initiation*, *Payment Clearing & Settlement*, *Sanctions Screening* and *Fraud
Management* (e.g. tech "Payment Validation Engine" vs any business "Payment
Validation"; tech "Payment Sanctions Filter" vs business "Sanctions Screening").
Relationships use only the 7 verbs: `depends_on`, `derived_from`, `supersedes`,
`defined_in`, `related_to`, `causes`, `mentions`.

## 1) Technology capabilities

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| Payment Routing Engine | technology-capability | L2 | Payment Orchestration | Core Processing | Rules-driven selection of the optimal clearing rail, scheme and processing path for each payment based on type, cost, speed, cut-off and availability. | Smart Routing, Least-Cost Routing | derived_from Payment Orchestration; defined_in Core Processing; related_to Scheme Connectivity Gateway; related_to Payment Routing (note: business cap "Payment Clearing & Settlement" depends_on it) | https://www.volantetech.com/payment-hub/ ; https://www.fisglobal.com/products/open-payment-framework ; https://www.aciworldwide.com/solutions/aci-enterprise-payments-platform |
| Scheme Connectivity Gateway | technology-capability | L2 | Payment Orchestration | Core Processing | Connectivity adapters and gateways linking the bank to clearing and settlement networks and rails (SWIFT, Fedwire/CHIPS, FedNow, RTP, ACH/NACHA, SEPA, TARGET2, CHAPS, Faster Payments). | Rail Connectivity, Network Adapters, Scheme Connectivity | derived_from Payment Orchestration; defined_in Core Processing; depends_on Payment Message Transformer; related_to Payment Routing Engine | https://www.volantetech.com/us-payments/ ; https://www.form3.tech/platform ; https://www.fisglobal.com/products/open-payment-framework |
| Payment Message Transformer | technology-capability | L2 | Payment Orchestration | Core Processing | Canonical normalization, format transformation and data enrichment of payment messages across standards (ISO 20022 MX, ISO 8583, SWIFT MT, NACHA), including MT/MX coexistence and truncation handling. | Message Transformation, ISO 20022 Translation, Payment Message Transformation | derived_from Payment Orchestration; defined_in Core Processing; mentions ISO 20022; related_to Payment Validation Engine | https://www.bottomline.com/uk/payments-connectivity-compliance-financial-institutions/message-transformation-and-enrichment ; https://www.volantetech.com/iso-20022-services/ ; https://www.swift.com/standards/iso-20022 |
| Payment Validation Engine | technology-capability | L2 | Payment Orchestration | Core Processing | Schema, syntactic, business-rule and scheme-format validation of payment instructions to maximise straight-through processing and reject malformed payments early. | Validation Engine, STP Validation | derived_from Payment Orchestration; defined_in Core Processing; related_to Payment Message Transformer; related_to Payment Repair Workbench | https://www.fisglobal.com/products/open-payment-framework ; https://www.testingxperts.com/blog/iso-20022-new-payment-standard/ ; https://www.finastra.com/solutions/global-payplus |
| Payment Repair Workbench | technology-capability | L2 | Payment Orchestration | Core Processing | Automated and manual repair, exception handling and investigations (incl. ISO 20022 E&I) of failed or non-STP payments, restoring them to a processable state. | Auto-Repair, Exceptions and Investigations, STP Repair | derived_from Payment Orchestration; defined_in Core Processing; depends_on Payment Validation Engine; related_to Workflow Orchestration | https://www.redcompasslabs.com/insights/iso-20022-exceptions-and-investigations-ei/ ; https://www.swift.com/standards/iso-20022/supercharge-your-payments-business/chapter-6 ; https://www.finastra.com/solutions/global-payplus |
| Settlement Instruction Engine | technology-capability | L2 | Payment Orchestration | Core Processing | Generation, sequencing and management of settlement instructions, nostro/vostro position updates and settlement-cycle handling against clearing infrastructures. | Settlement Engine, Settlement Instruction | derived_from Payment Orchestration; defined_in Core Processing; related_to Liquidity & Limit Checker; related_to Scheme Connectivity Gateway | https://www.aciworldwide.com/solutions/aci-enterprise-payments-platform ; https://www.volantetech.com/payment-hub/ ; https://www.finastra.com/solutions/global-payplus |
| Liquidity & Limit Checker | technology-capability | L2 | Payment Orchestration | Core Processing | Real-time funds availability, liquidity buffer and limit / debit-cap checks performed before a payment is released for settlement. | Limit Check, Funds Control, Liquidity Check | derived_from Payment Orchestration; defined_in Core Processing; related_to Settlement Instruction Engine; related_to Liquidity Management | https://www.flagright.com/post/mandatory-sepa-instant-payments-real-time-compliance ; https://www.aciworldwide.com/solutions/aci-enterprise-payments-platform ; https://www.volantetech.com/payment-hub/ |
| Payment Sanctions Filter | technology-capability | L2 | Payment Orchestration | Core Processing | In-flight, sub-second sanctions/watchlist and fraud-control hooks embedded in the payment flow that hold, release or reject payments before settlement. | Inline Sanctions Filter, In-Flight Screening | derived_from Payment Orchestration; defined_in Core Processing; depends_on Transaction Monitoring Platform; related_to Fraud Analytics; mentions Sanctions Screening | https://tispayments.com/solutions/payments-hub/sanctions-screening/ ; https://www.sanctions.io/blog/real-time-payments-and-sanctions-risk ; https://www.feedzai.com/blog/transaction-screening/ |

### Selected L3 capabilities

| Canonical Name | type | level | parent | domain | definition | aliases | proposed relationships | sources |
|---|---|---|---|---|---|---|---|---|
| ISO 20022 Translation Service | technology-capability | L3 | Payment Message Transformer | Core Processing | Dedicated bidirectional MT/MX translation, schema mapping and coexistence handling for the ISO 20022 standard during and after migration. | MX Translation, MT-MX Mapping | derived_from Payment Message Transformer; defined_in Core Processing; mentions ISO 20022 | https://www.volantetech.com/iso-20022-services/ ; https://www.bottomline.com/uk/payments-connectivity-compliance-financial-institutions/message-transformation-and-enrichment |
| Least-Cost Routing Service | technology-capability | L3 | Payment Routing Engine | Core Processing | Cost-based routing logic that selects the cheapest viable rail/scheme meeting the payment's speed and cut-off requirements. | Cost-Based Routing | derived_from Payment Routing Engine; defined_in Core Processing; related_to Scheme Connectivity Gateway | https://www.fisglobal.com/products/open-payment-framework ; https://www.volantetech.com/payment-hub/ |
| SWIFT Connectivity Adapter | technology-capability | L3 | Scheme Connectivity Gateway | Core Processing | SWIFT-network connectivity (incl. gpi/Go, FIN and InterAct/FileAct) feeding the scheme gateway. | SWIFT Adapter, SWIFT gpi Connector | derived_from Scheme Connectivity Gateway; defined_in Core Processing; related_to Payment Message Transformer | https://www.aciworldwide.com/solutions/aci-enterprise-payments-platform ; https://www.swift.com/standards/iso-20022 |

## 2) Systems refresh

Already covered (excluded): ACI BASE24, Legacy Payment Hub, ACH Batch Processor,
Stripe, Adyen, Modern Treasury, Volante Payments. New systems below realize one or
more of the proposed L2 tech capabilities (all sit under the parent Payment
Orchestration tech capability). Modern systems include the legacy they supersede.

| Canonical Name | type | realizes (tech cap) | supersedes (legacy, modern only) | vendor | definition | aliases | sources |
|---|---|---|---|---|---|---|---|
| FIS Open Payment Framework | legacy-system | Payment Routing Engine | — | FIS | ISO 20022-native enterprise payment hub providing parsing, validation, cost-based routing and warehousing across instant, high-value and ACH rails; long-deployed at tier-1 banks. | OPF, FIS OPF | https://www.fisglobal.com/products/open-payment-framework ; https://www.fisglobal.com/-/media/fisglobal/files/pdf/brochure/open-payment-framework-north-america.pdf |
| Finastra Global PAYplus | legacy-system | Payment Validation Engine | — | Finastra | Modular multi-rail enterprise payments hub with highly configurable workflows, ISO 20022-native processing and automated repair for high-value, mass and real-time payments. | GPP, Global PAYplus | https://www.finastra.com/solutions/global-payplus ; https://www.finastra.com/viewpoints/brochure/finastra-global-payplus-factsheet |
| ACI Enterprise Payments Platform | legacy-system | Settlement Instruction Engine | — | ACI Worldwide | Proven-at-scale, multi-bank/multi-currency enterprise payments platform orchestrating all payment types across 50+ networks (RTGS, ACH, instant, cross-border, card) with SWIFT gpi/Go. | ACI EPP, UP Real-Time Payments | https://www.aciworldwide.com/solutions/aci-enterprise-payments-platform ; https://investor.aciworldwide.com/news-releases/news-release-details/aci-worldwide-recognized-datos-insights-global-payment-hub |
| Form3 | modern-system | Scheme Connectivity Gateway | Legacy Payment Hub | Form3 | Cloud-native, multi-cloud Payments-as-a-Service platform delivering zero-downtime account-to-account processing and single-API access to domestic and international payment schemes. | Form3 Financial Cloud, Form3 PaaS | https://www.form3.tech/platform ; https://www.form3.tech/en-us/about |
| ACI Connetic | modern-system | Payment Routing Engine | ACI BASE24 | ACI Worldwide | Cloud-native SaaS payments hub from ACI consolidating multi-rail orchestration, routing and processing on a modern microservices stack. | Connetic | https://www.aciworldwide.com/solutions/payments-hub ; https://www.aciworldwide.com/solutions/aci-enterprise-payments-platform |
| Bottomline Payments | modern-system | Payment Message Transformer | ACH Batch Processor | Bottomline Technologies | Cloud payments and ISO 20022 message transformation/enrichment platform enabling translation, validation and connectivity across business-to-bank payment flows. | Bottomline, PTX | https://www.bottomline.com/uk/payments-connectivity-compliance-financial-institutions/message-transformation-and-enrichment ; https://www.bottomline.com/resources/iso-20022-frequently-asked-questions |
