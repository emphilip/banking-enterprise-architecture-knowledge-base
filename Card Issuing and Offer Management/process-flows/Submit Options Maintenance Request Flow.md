---
title: Submit Options Maintenance Request Flow
type: process-flow
stage: product-setup
channel: back-office
products: [credit-card]
capabilities: [OPS-WFR, ENT-BOR, PLB-CRD]
tags: [process-flow, omr, change-management, card-platform, validation, production, workflow, retail-banking, canada]
aliases: [Submit OMR, Options Maintenance Request, OMR Flow, Manage Options - Submit OMR]
---

# Submit Options Maintenance Request Flow

**Purpose:** The controlled change-management process that **propagates a product/option change to the card processing platform** — populating and submitting an **Options Maintenance Request (OMR)**, approving it, applying it first in a **validation environment** (test and reconcile against the extracted change file), then in the **production environment**, with error paths that notify a system administrator.

**Position:** The shared "last mile" invoked by nearly every product-setup flow — [[Create Reward Flow]], [[Manage Affinity Partnership Flow]], [[Manage Card Benefits Flow]], [[Set Up Premium Card Product Flow]], [[Manage Pricing Flow]], and [[Manage Product Instance Flow]] — whenever a change must reach the card processing platform. An Operations *Workflow & Rules* capability. Source spans two diagram pages (1–2 of 2).

## Flow

```mermaid
flowchart TD
    S[Start] --> POP[Populate OMR fields]
    POP --> SUB[Submit OMR]
    SUB --> APP1{Product Ops:<br/>request approved?}
    APP1 -->|No| E1[End]
    APP1 -->|Yes| PROC[Card platform: process OMR<br/>in validation environment]
    PROC --> EXT[Extract file of changed options]
    EXT --> CHK{Catalogue: extract matches<br/>submitted OMR?}
    CHK -->|Yes| UPDV[Update status to validation]
    CHK -->|No| ERRV[Error → notify system admin]
    UPDV --> TESTV{Workflow: passed<br/>test in validation?}
    TESTV -->|No| ERRV
    TESTV -->|Yes| APP2{Approved for production?}
    ERRV --> SA1[System admin: contact platform team,<br/>resolve issue] --> E1
    APP2 -->|No| E1
    APP2 -->|Yes| SUBP[Submit OMR in production env]
    SUBP --> PROCP[Card platform: process OMR<br/>in production environment]
    PROCP --> EXTP[Extract file of changed options]
    EXTP --> CHKP{Extract matches submitted?}
    CHKP -->|Yes| UPDP[Update option in production]
    CHKP -->|No| ERRP[Error → notify system admin]
    UPDP --> VALP{Validation passed?}
    VALP -->|Yes| ACT[Change status to active]
    VALP -->|No| ERRP
    ERRP --> SA2[System admin: contact platform team,<br/>resolve issue] --> E2[End]
    ACT --> E2
```

## Step Detail

### Step OMR-01 — Populate and Submit

> **Step ID:** `OMR-01` · **Capability:** OPS-WFR-01 (workflow init) · **Actor:** Product Catalogue / requester · **Exits:** → OMR-02

The OMR fields are populated (the change set exported by the calling product-setup flow) and the **OMR is submitted**.

### Step OMR-02 — Approval

> **Step ID:** `OMR-02` · **Capability:** OPS-WFR-02 (approvals) · **Actor:** Product Ops team · **Preconditions:** OMR-01 · **Exits:** approved → OMR-03; not approved → End

The Product Ops team **approves the request for the OMR**. An unapproved request ends the flow.

### Step OMR-03 — Apply in Validation Environment

> **Step ID:** `OMR-03` · **Capability:** OPS-WFR-01; DEVSECOPS — Testing (adjacent) · **Preconditions:** OMR-02 approved · **Exits:** matches + test passes → OMR-04; mismatch/fail → OMR-ERR

The **card processing platform processes the OMR in the validation environment** and **extracts a file of changed options**. The product catalogue **checks the extract against the submitted OMR** (automated reconciliation). If it matches, status is updated to validation and the change is **tested in the validation environment (manual)**. A passed test advances to production approval.

### Step OMR-04 — Apply in Production Environment

> **Step ID:** `OMR-04` · **Capability:** OPS-WFR-01; ENT-BOR · **Preconditions:** OMR-03 passed + approved for production · **Exits:** matches + validation passes → status Active (End); mismatch/fail → OMR-ERR

On production approval the **OMR is submitted in the production environment**, the platform **processes it and extracts the changed-options file**, the catalogue **reconciles the extract against the submission**, the option is **updated in production**, and after a passed production validation the **status is changed to Active**.

### Step OMR-ERR — Error Handling

> **Step ID:** `OMR-ERR` · **Capability:** OPS — Case Mgmt. (adjacent) · **Trigger:** reconciliation mismatch or failed test/validation · **Exits:** End

On any reconciliation mismatch or failed test/validation, the platform **throws an error code and generates a notification for the system administrator**; an **error-notification screen** is shown, and the **system administrator contacts the card-platform team to resolve the issue**.

## Business Rules (Generalized)

| Rule | Statement |
|---|---|
| Approval before apply | An OMR is approved before it touches any environment |
| Validation before production | Changes are applied and tested in validation before production |
| Automated reconciliation | The extracted changed-options file is reconciled against the submitted OMR at each stage |
| Two-gate promotion | Separate approvals gate validation entry and production entry |
| Error to admin | Any mismatch/failure raises an error notification routed to a system administrator |

## Capability Mapping

| Capability | How exercised |
|---|---|
| Operations — Workflow & Rules OPS-WFR-01/02 | OMR initiation, approvals, environment promotion |
| Enterprise Support — Books of Record ENT-BOR | Product catalogue reconciliation and status of record |
| [[Cards]] PLB-CRD-01 | The card-platform option/product the change applies to |

## Source Traceability

Generalized from the MBNA Product Ops *Manage Options — Submit OMR (1–2 of 2)* flow. "V-Region"/"P-Region" abstracted to validation/production environments; TSYS and the MBNA System Administrator per [[Systems and Integration Reference]]; source deck is DRAFT.
