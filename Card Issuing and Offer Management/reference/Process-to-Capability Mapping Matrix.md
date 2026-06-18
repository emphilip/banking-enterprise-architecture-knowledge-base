---
title: Process-to-Capability Mapping Matrix
type: reference
domain: banking-and-payments
tags: [reference, mapping, traceability, capability-model, process-flow, l2-capabilities]
aliases: [Mapping Matrix, Capability Matrix, Traceability Matrix]
---

# Process-to-Capability Mapping Matrix

Full traceability between the [[00 - Card Issuing and Offer Management Index|library's]] 26 process flows and the **L2 capabilities** of the [[Generic Multi-Functional Bank Capability Model|master capability model (slide 4)]]. Legend: **P** = primary (the flow *is* this capability in action) · **S** = supporting (exercised but not the flow's purpose) · **—** = not exercised.

L1 column codes: **CNT** = [[Content Management|CEN-CNT]] · **OFR** = [[Offers|CEN-OFR]] · **CON** = [[Contact Management|CEN-CON]] · **RWD** = [[Rewards|CLP-RWD]] · **LOY** = [[Loyalty|CLP-LOY]] · **CRD** = [[Cards|PLB-CRD]] · **INS** = [[Insurance|PLB-INS]] · **MKS** = [[Marketing and Sales]] · **MON** = [[Servicing - Monetary|SVC-MON]]. *Adjacent* lists L0 domains exercised outside the nine columns (ONB = Onboarding & Origination incl. CCC disclosures; OPS = Operations; ENT = Enterprise Support; IAA = Identity/Auth; CHN = Channels; FRR = Fraud & Risk).

## Matrix — L1 Summary

| Process Flow | CNT | OFR | CON | RWD | LOY | CRD | INS | MKS | MON | Adjacent |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---|
| [[Create and Update Content Management Flow]] | **P** | S | — | S | — | — | — | — | — | ONB, OPS |
| [[Value-Add Offers Flow]] | S | **P** | S | — | — | — | **P** | — | — | ONB |
| [[Content Management CPCMS Flow]] | **P** | S | — | — | — | — | — | **P** | S | ONB, FRR |
| [[Disclosure Management Flow]] | **P** | — | — | — | — | — | — | — | — | ONB, FRR |
| [[Content Management Site Refresh Flow]] | **P** | — | — | — | — | — | — | — | — | ONB, OPS |
| [[Publish Rewards Flow]] | — | — | S | **P** | — | — | — | **P** | — | ENT |
| [[Create Reward Flow]] | — | — | — | **P** | — | S | — | — | — | ENT, OPS |
| [[Manage Affinity Partnership Flow]] | — | — | — | — | **P** | S | — | — | — | OPS, ENT |
| [[Manage Card Benefits Flow]] | — | — | — | — | S | **P** | — | — | — | OPS, ENT |
| [[Set Up Premium Card Product Flow]] | — | — | — | S | **P** | **P** | — | — | — | OPS, ENT |
| [[Manage Insurance Product Setup Flow]] | — | S | — | — | — | — | **P** | — | — | OPS, ENT |
| [[Submit Options Maintenance Request Flow]] | — | — | — | — | — | S | — | — | — | **OPS**, **ENT** |
| [[Operator Security Administration Flow]] | — | — | — | — | — | S | — | — | — | **IAA** |
| [[Manage Pricing Flow]] | — | — | — | — | — | S | — | — | **P** | FRR, OPS, ENT |
| [[Manage Product Instance Flow]] | — | — | — | S | S | **P** | — | — | — | OPS, ENT |
| [[Manage Source Code Flow]] | — | **P** | — | S | — | — | — | **P** | S | OPS, ENT |
| [[Direct Marketing Campaign Flow]] | — | **P** | **P** | — | — | — | — | **P** | — | ENT |
| [[Online Campaign Flow]] | — | **P** | S | — | — | — | — | — | — | ONB, CHN |
| [[Phone Campaign Existing Customer Flow]] | — | **P** | S | — | — | — | — | S | — | ONB, CHN |
| [[Phone Campaign New Customer Flow]] | — | **P** | — | — | — | — | — | **P** | — | **ONB** |
| [[Pricing Offer Presentment Flow]] | — | **P** | S | — | — | S | — | — | **P** | ONB, CHN |
| [[Value-Add Offer Presentment Flow]] | — | **P** | — | — | — | S | — | S | **P** | ONB |
| [[Insurance Offer Presentment Flow]] | — | **P** | S | — | — | — | **P** | — | — | ONB |
| [[Apply List to Offers Flow]] | — | S | **P** | — | — | — | — | **P** | — | ENT |
| [[Add Insurance Product Phone Channel Flow]] | — | S | — | — | — | — | **P** | — | — | ONB, CHN |
| [[Phone Channel Outbound Flow]] | — | **P** | **P** | — | — | — | — | S | — | ONB, CHN |

## Matrix — Flow to Primary L2 Capabilities

Each flow's primary L2 capabilities (step-level detail lives in each flow's *Capability Mapping* table and `Step` headings).

### Content Management

| Flow | Primary L2 capabilities |
|---|---|
| [[Create and Update Content Management Flow]] | CEN-CNT-01 Define/Publish, CEN-CNT-02 Version History; CEN-OFR-01 Offer Mgmt; CLP-RWD-05 Presentment |
| [[Value-Add Offers Flow]] | CEN-OFR-01/02; PLB-INS-06 Quotes, PLB-INS-07 Issuance; CEN-CON-06 Consent |
| [[Content Management CPCMS Flow]] | CEN-CNT-01/02/03; CEN-OFR-03 Promo/Source Codes; MKS-MKT-02 Campaign Mgmt; SVC-MON-01 Rate/APR |
| [[Disclosure Management Flow]] | CEN-CNT-01/02; ONB-CCC-01 Customer Disclosures |
| [[Content Management Site Refresh Flow]] | CEN-CNT-01/02; ONB-CCC-01 |

### Rewards

| Flow | Primary L2 capabilities |
|---|---|
| [[Publish Rewards Flow]] | CLP-RWD-05 Presentment; MKS-MKT-02/03; CEN-CON-04/05 |
| [[Create Reward Flow]] | CLP-RWD-01 Earn, 02 Calculate, 03 Track; PLB-CRD-01 |

### Product Setup

| Flow | Primary L2 capabilities |
|---|---|
| [[Manage Affinity Partnership Flow]] | CLP-LOY-04 Affinity, 06 Partners; PLB-CRD-03 Co-Brand |
| [[Manage Card Benefits Flow]] | PLB-CRD-01; CLP-LOY-03 Programs |
| [[Set Up Premium Card Product Flow]] | PLB-CRD-01; CLP-LOY-02 Tiered, 04 Affinity; CLP-RWD-01/08 |
| [[Manage Insurance Product Setup Flow]] | PLB-INS-07 Issuance, 09 Maintenance; CEN-OFR-01 |
| [[Submit Options Maintenance Request Flow]] | OPS-WFR-01 Workflow Init, 02 Approvals; ENT-BOR Reconciliation |
| [[Operator Security Administration Flow]] | IAA-IDM User Groups/Roles, Entitlements; IAA-AUTHZ Access Controls |
| [[Manage Pricing Flow]] | SVC-MON-01 Rate/APR, 02 Fee Mgmt |
| [[Manage Product Instance Flow]] | PLB-CRD-01; CLP-LOY-04; CLP-RWD-01 |

### Sales / Value-Add / Offer Management

| Flow | Primary L2 capabilities |
|---|---|
| [[Manage Source Code Flow]] | CEN-OFR-03 Promo/Source Codes; MKS-MKT-04 Lead/Prospect, MKS-CRM-06 Lead Gen |
| [[Direct Marketing Campaign Flow]] | MKS-MKT-02; CEN-OFR-01; CEN-CON-04/05 |
| [[Online Campaign Flow]] | CEN-OFR-01/02; CEN-CON-03 Contact/Offer History |
| [[Phone Campaign Existing Customer Flow]] | CEN-OFR-01/02; MKS-CRM-03 Cross/Upsell; CEN-CON-03 |
| [[Phone Campaign New Customer Flow]] | MKS-MKT-04, MKS-CRM-06; CEN-OFR-04 Intro Offers; ONB-APP-01, ONB-ADJ-01 |
| [[Pricing Offer Presentment Flow]] | CEN-OFR-01; SVC-MON-01/05; PLB-CRD-09 Balance Transfers |
| [[Value-Add Offer Presentment Flow]] | CEN-OFR-01; SVC-MON-08 CLI/CLD; PLB-CRD-08 Card Limits; MKS-CRM-03 |
| [[Insurance Offer Presentment Flow]] | CEN-OFR-01; PLB-INS-06/07/09 |
| [[Apply List to Offers Flow]] | MKS-MKT-03 Segment Mgmt; CEN-CON-04/05; CEN-OFR-01 |
| [[Add Insurance Product Phone Channel Flow]] | PLB-INS-06/07; CEN-OFR-01 |
| [[Phone Channel Outbound Flow]] | CEN-CON-03/05; CEN-OFR-01/02; MKS-CRM-03 |

## Coverage Notes

- **Strongly evidenced by source artifacts:** CEN-CNT (authoring/publish/version), CEN-OFR (offer mgmt, engine, source codes, presentment), CLP-RWD (reward creation, presentment), CLP-LOY (affinity), PLB-CRD (product/benefit setup), PLB-INS (insurance setup/offer), SVC-MON-01/08 (pricing, CLI), MKS (campaigns, lists), OPS-WFR (OMR/approvals), IAA (operator security).
- **Generalized from standard Canadian card-issuer practice** (thin/implicit in source): CLP-RWD-04/06/07 (redeem/consolidate/merchant offers), CLP-LOY-05/07/08 (analytics/member mgmt/engagement), CEN-OFR-05/06 (wallet offers/analytics), the full insurance claims lifecycle (PLB-INS-12–16). These are documented at capability level in the L1 notes so the model stays complete for querying, with the generalization flagged.
- **Adjacent-domain dependencies** (ONB-CCC disclosures, OPS workflow/case mgmt, ENT books-of-record/data, IAA auth, CHN channels, FRR compliance/credit-risk) are referenced inline in the flows rather than given their own notes here.

## Related

[[Generic Multi-Functional Bank Capability Model]] · [[Systems and Integration Reference]] · [[Glossary]] · [[Canadian Regulatory Context]]
