---
title: Glossary
type: reference
domain: banking-and-payments
tags: [reference, glossary, terminology, cards, offers, retail-banking, canada]
aliases: [Glossary, Terms, Definitions]
---

# Glossary

Terminology used across the [[00 - Card Issuing and Offer Management Index|Card Issuing & Offer Management]] library. Brand/vendor system names and their generic equivalents are in [[Systems and Integration Reference]]; regulatory terms are expanded in [[Canadian Regulatory Context]].

## Domain Terms

| Term | Definition |
|---|---|
| **Acquisition offer / source code** | An offer code that binds a product instance, channel/availability rules, pricing, acquisition channel, and reward — used to acquire customers. See [[Manage Source Code Flow]]. |
| **Affinity (partnership)** | A co-brand/partner relationship that underpins an affinity card product. See [[Manage Affinity Partnership Flow]]. |
| **BT — Balance Transfer** | Moving a balance from another card to this card, often at a promotional rate; presented as a pricing offer. |
| **Benefit (Benefit ID)** | A card-network or program benefit attached to a card product, managed as a Benefit ID. See [[Manage Card Benefits Flow]]. |
| **CLI / CLD — Credit-Limit Increase / Decrease** | A change to a card's credit limit; CLI is a common value-add offer. Servicing execution: [[Servicing - Monetary\|SVC-MON-08]]. |
| **Collateral** | The marketing/communication assets and documents attached to a product (welcome material, carriers, inserts). |
| **Disclosure** | Regulated product/cost information presented to a customer; managed as reusable templates. See [[Disclosure Management Flow]]. |
| **Disposition** | The recorded outcome of an offer presentment (accepted / declined / maybe / removed), written to offer and contact history. |
| **Offer presentment** | Displaying an eligible offer to a customer and capturing their decision (online, phone, IVR, mail, statement). |
| **OMR — Options Maintenance Request** | A controlled change request that propagates a product/option change to the card processing platform across validation and production environments. See [[Submit Options Maintenance Request Flow]]. |
| **Pricing template** | A reusable pricing definition — standard/contract rate, penalty rate, or promotional rate. See [[Manage Pricing Flow]]. |
| **Product instance** | A concrete card product record composed of affinity, reward, collateral, and benefit constructs. See [[Manage Product Instance Flow]]. |
| **Reward ID (reward code)** | The reward construct (an `ARQ`-class identifier with primary/secondary attributes) defining how a card earns rewards. See [[Create Reward Flow]]. |
| **Premium / World-tier card** | A higher-tier card product with elevated rewards earn and tier benefits. See [[Set Up Premium Card Product Flow]]. |
| **Value-add offer** | A non-pricing offer that adds value to an account — CLI, Credit Alert, Product Change. See [[Value-Add Offer Presentment Flow]]. |
| **Channel content zone** | A content scope tied to where content is consumed (Web, POS-portal, Referral, Retail-front). See [[Content Management CPCMS Flow]]. |

## Roles & Channels

| Term | Definition |
|---|---|
| **CSR** | Customer Service Representative — the phone-channel agent presenting offers/servicing requests. |
| **IVR** | Interactive Voice Response — the automated phone front-end that routes and authenticates callers. |
| **TFN** | Toll-Free Number the customer calls to reach the IVR/agent. |
| **Editor / Publisher** | The separated content-management roles: an editor authors/submits; a publisher reviews, confirms legal approval, and releases. |
| **Product Operations (Product Ops)** | The back-office team that sets up and maintains card products, pricing, rewards, benefits, and offers. |
| **Operator** | An internal system user whose entitlements are governed by an operator security profile. See [[Operator Security Administration Flow]]. |

## Technical & Process Terms

| Term | Definition |
|---|---|
| **BoR — Book of Record** | The authoritative system for a data domain (e.g., the product catalogue is the product BoR). |
| **CMS — Content Management System** | The tooling used to author, version, and publish content. |
| **MDM — Master Data Management** | The authoritative customer/account/product master data store. |
| **UAT — User Acceptance Testing** | The pre-production environment/stage where content and changes are validated before go-live. |
| **Validation / Production environment** | The two card-platform environments an OMR is promoted through (source: "V-Region" / "P-Region"). |
| **Pricing strategy code / account-control code** | Card-platform pricing constructs set during pricing-template setup (source: TSP / SAC). |
| **Pricing reservation matrix** | The matrix checked when setting up a pricing template to reserve/assign pricing constructs. |
| **Draft / Inactive / Active / Suspended** | The lifecycle states of catalogue objects (products, benefits, rewards, pricing, source codes). |

## Related

[[Systems and Integration Reference]] · [[Canadian Regulatory Context]] · [[Generic Multi-Functional Bank Capability Model]] · [[Process-to-Capability Mapping Matrix]]
