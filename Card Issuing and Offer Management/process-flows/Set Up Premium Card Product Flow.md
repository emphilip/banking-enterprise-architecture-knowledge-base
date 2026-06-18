---
title: Set Up Premium Card Product Flow
type: process-flow
stage: product-setup
channel: back-office
products: [credit-card, premium-card]
capabilities: [PLB-CRD, CLP-LOY, CLP-RWD]
tags: [process-flow, product-setup, premium-card, world-card, product-instance, affinity, reward, benefit, omr, retail-banking, canada]
aliases: [Set Up Premium Card Product, Setup World Card, Setup WorldCard, Premium Card Setup]
---

# Set Up Premium Card Product Flow

**Purpose:** The composite back-office process to **set up a premium-tier (World-class) card product instance** — creating the product instance and composing its **affinity, reward, collateral, and benefit** constructs (creating any that do not yet exist), validating, routing through approval, exporting to the **card processing platform** via an Options Maintenance Request, and publishing the product instance Active.

**Position:** A specialized create path on top of [[Manage Product Instance Flow]] that orchestrates [[Manage Affinity Partnership Flow]], [[Create Reward Flow]], and [[Manage Card Benefits Flow]] as sub-constructs. Premium tiers attach higher reward earn and tier benefits — see [[Loyalty|CLP-LOY-02]] and [[Rewards|CLP-RWD-08]].

## Flow

```mermaid
flowchart TD
    S[Start] --> CW[Select option to create<br/>premium card product]
    CW --> ATTR[Product-instance<br/>attributes screen displayed]
    ATTR --> AF{Affinity exists?}
    AF -->|No| AFN[[Create new affinity]]
    AF -->|Yes| AFS[Set affinity]
    AFN --> RW{Reward exists?}
    AFS --> RW
    RW -->|No| RWN[[Create new reward]]
    RW -->|Yes| RWS[Set reward]
    RWN --> CO{Collateral exists?}
    RWS --> CO
    CO -->|No| CON[Create new collateral]
    CO -->|Yes| COS[Set collateral]
    CON --> BE{Benefit exists?}
    COS --> BE
    BE -->|No| BEN[[Create new benefit]]
    BE -->|Yes| BES[Set benefit]
    BEN --> OTHER[Set other attributes]
    BES --> OTHER
    OTHER --> SUB[Submit form]
    SUB --> VAL{All fields valid?}
    VAL -->|No| ERR[Notify user to correct errors]
    ERR --> ATTR
    VAL -->|Yes| PIID[Create product-instance ID]
    PIID --> APP{Request approved?}
    APP -->|No| REJ[Notify rejection via email]
    APP -->|Yes| DRAFT[Save product instance Draft]
    DRAFT --> EXP[Export required card-platform components]
    EXP --> OMR[[Process Options Maintenance Request]]
    OMR --> PUB[Publish product instance Active]
    PUB --> NOT[Notify success via email]
    NOT --> E[End]
```

## Step Detail

### Step PCP-01 — Initiate and Display Attributes

> **Step ID:** `PCP-01` · **Capability:** PLB-CRD-01 · **Actor:** Product Operations user · **Exits:** → PCP-02

The user **selects to create a premium card product**; the **product-instance attributes screen** is displayed (served by the workflow/UI).

### Step PCP-02 — Compose Affinity, Reward, Collateral, Benefit

> **Step ID:** `PCP-02` · **Capability:** CLP-LOY-02/04, CLP-RWD-01/08, PLB-CRD-01 · **Preconditions:** PCP-01 · **Exits:** → PCP-03

For each construct the flow checks **whether it already exists**: if yes, the user **sets** (selects) it; if not, the corresponding **create sub-process** is invoked inline:

- **Affinity** — set or [[Manage Affinity Partnership Flow|create new affinity]].
- **Reward** — set or [[Create Reward Flow|create new reward]].
- **Collateral** — set or create new collateral.
- **Benefit** — set or [[Manage Card Benefits Flow|create new benefit]].

The user then **sets the other product attributes**.

### Step PCP-03 — Validate and Create Instance

> **Step ID:** `PCP-03` · **Capability:** PLB-CRD-01 · **Preconditions:** PCP-02 · **Inputs:** field validation · **Exits:** invalid → correct errors (back to attributes); valid → PCP-04

On **submit**, the system validates all selected fields. Invalid fields drive an **error-notification screen** and a correction loop. When valid, the **product-instance ID is created**.

### Step PCP-04 — Approve, Export, Publish, Notify

> **Step ID:** `PCP-04` · **Capability:** OPS — Workflow & Rules (approvals, adjacent); ENT-BOR · **Preconditions:** PCP-03 · **Inputs:** approver decision · **Exits:** End

The request is routed for **approval**. On rejection the user is emailed. On approval: the **product instance is saved Draft**, **required card-platform components are exported**, the change is propagated via an **Options Maintenance Request** ([[Submit Options Maintenance Request Flow]]), the **product instance is published Active**, and the user **receives a success email**.

## Business Rules (Generalized)

| Rule | Statement |
|---|---|
| Composite setup | A premium product composes affinity, reward, collateral, and benefit constructs |
| Create-if-absent | Any construct that does not yet exist is created inline before selection |
| Validation gate | All selected fields must validate before a product-instance ID is created |
| Approval gate | The product instance is approved before being saved and published |
| Draft → Active via OMR | Saved Draft, exported to the card platform via OMR, then published Active |

## Capability Mapping

| Capability | How exercised |
|---|---|
| [[Cards]] PLB-CRD-01 | Premium card product-instance creation |
| [[Loyalty]] CLP-LOY-02/04 | Tiered (premium) status and affinity composition |
| [[Rewards]] CLP-RWD-01/08 | Reward and tiered-reward composition |
| Operations / Enterprise Support (adjacent) | Approval workflow; product catalogue BoR |

## Source Traceability

Generalized from the MBNA Product Ops *Manage Product Instances — Setup World Card (1–2 of 2)* flow. "World Card" abstracted to a generic premium/World-tier card product; TSYS, workflow management system, and product catalogue per [[Systems and Integration Reference]]; source deck is DRAFT.
