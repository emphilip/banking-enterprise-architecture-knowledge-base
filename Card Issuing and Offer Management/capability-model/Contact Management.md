---
title: Contact Management
type: capability
level: L1
capability-id: CEN-CON
parent: Customer Engagement (CEN)
tags: [capability, contact-management, outreach, consent, channel-preference, retail-banking]
aliases: [CEN-CON, Contact Management Capability]
---

# Contact Management (CEN-CON)

**Parent:** [[Generic Multi-Functional Bank Capability Model|Customer Engagement (CEN)]]

The Contact Management capability group governs **how, when, and through which channel** the bank reaches a customer, and the **consent and history** that constrain outreach. For card campaigns and offer presentment it owns contact-frequency rules, channel preference, the contact/offer history that prevents over-contact, and the consent records that authorize marketing communication — the controls that turn a raw customer list into a compliant, channel-appropriate outreach plan.

## L2 Capabilities

### CEN-CON-01 — Frequency

Contact-frequency caps and suppression rules that limit how often a customer is contacted across campaigns.

### CEN-CON-02 — Call Reasons

Classification of the reason for each contact, used for routing, reporting, and compliance.

### CEN-CON-03 — Contact History

The record of prior contacts and **offer dispositions**, read at presentment time so an offer already declined is not inappropriately re-presented and so wrap-up dispositions are captured. Central to the phone and online presentment flows.

### CEN-CON-04 — Channel Preference

The customer's preferred and permitted channels (phone, email, direct mail, statement insert), used when a campaign list is split to channels.

### CEN-CON-05 — Outreach Mgmt.

Orchestrating outbound campaigns: building and applying lists, splitting to channels, dispatching to vendors (telemarketing, direct-mail, statement-generation), and tracking dispatch and response. Realized by [[Apply List to Offers Flow]], [[Direct Marketing Campaign Flow]], [[Publish Rewards Flow]], and [[Phone Channel Outbound Flow]].

### CEN-CON-06 — Consent Tracking

Capturing and honouring marketing and disclosure consent (CASL-aligned express/implied consent for electronic messages), recorded against the customer and checked before outreach and at offer disclosure. See [[Canadian Regulatory Context]].

## Process Flows Exercising This Capability

| Flow | L2s exercised |
|---|---|
| [[Apply List to Offers Flow]] | CEN-CON-04, 05 |
| [[Direct Marketing Campaign Flow]] | CEN-CON-04, 05 |
| [[Publish Rewards Flow]] | CEN-CON-05 |
| [[Phone Channel Outbound Flow]] | CEN-CON-03, 05 |
| [[Online Campaign Flow]] | CEN-CON-03 |
| [[Phone Campaign Existing Customer Flow]] | CEN-CON-03 |
| [[Pricing Offer Presentment Flow]] | CEN-CON-06 |
| [[Insurance Offer Presentment Flow]] | CEN-CON-06 |

## Related

[[Offers]] · [[Marketing and Sales]] · [[Content Management]] · [[Canadian Regulatory Context]]
