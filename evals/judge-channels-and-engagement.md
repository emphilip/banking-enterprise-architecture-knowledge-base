# Judge Report — Channels & Engagement Deep-Dive (28-file sample)

Reviewer: judge sub-agent (strict). Date: 2026-06-17.
Rubric: `evals/rubric.md`. Scores 1–5 per dimension (3 = acceptable, <3 = fail).

## Corroboration performed
- BIAN service domains confirmed against BIAN Service Landscape v9.1: **Party Authentication, Customer Access Entitlement, Contact Center Operations, Servicing Issue, Customer Workbench, Session Dialogue, Channel Activity History** are all real domains (Cross Channel / Servicing areas).
- **"Servicing Position Management"** (in `L3-servicing-resource-management.md`) is **NOT** a BIAN v9.1 service domain — not found in the landscape. Likely fabricated domain name → Groundedness penalty.
- Temenos→Kony acquisition confirmed (Aug 2019, closed Sep 2019; Kony DBX folded into Infinity; DBX supported wearables/AR). Kony DBX and Temenos Infinity notes are accurate and well-grounded.
- PSD2 SCA / dynamic linking / TRA, eIDAS QWAC/QSEAL, Berlin Group NextGenPSD2, UK Open Banking Standard, NIST SP 800-63A IAL2, Erlang C, RASP/cert-pinning — all standard, correctly used.
- Registry check: `avaya-aura.md` and `cisco-ucce.md` both exist as legacy contact-center systems. THREE modern systems (Amazon Connect, NICE CXone, Twilio Flex) all `supersede Avaya Aura`; Cisco UCCE is left with no superseding modern system. Same-capability test passes (CCaaS supersedes on-prem voice), but the many-to-one fan onto a single legacy node while orphaning Cisco UCCE is a relationship-grain weakness on the new CCaaS notes.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|---|---|---|---|---|---|---|
| technology-capabilities/mobile-app-framework.md | 5 | 4 | 5 | 5 | 5 | Accurate L2 def (native/hybrid runtime, device binding, RASP); Backbase+Temenos cited and relevant; derived_from Digital Channel Platform + depends_on API Management correct. |
| technology-capabilities/onboarding-journey-orchestrator.md | 5 | 4 | 5 | 5 | 5 | Form orchestration/save-resume/low-code accurate; Temenos+Alkami support claims; depends_on KYC Onboarding Platform, related_to Loan Origination sensible. |
| technology-capabilities/digital-sca-service.md | 5 | 5 | 5 | 5 | 5 | PSD2 SCA, dynamic linking, TRA, FIDO/passkey all correct; OneSpan+Salt Edge directly support; delegates credentials to identity layer — clean grain. |
| technology-capabilities/omnichannel-routing-engine.md | 5 | 4 | 5 | 5 | 5 | Universal-queue/skills/predictive routing accurate; Genesys+Amazon Connect support; related_to ACD and derived_from Contact Center Platform correct. |
| technology-capabilities/interactive-voice-response.md | 5 | 4 | 5 | 5 | 5 | DTMF/ASR/TTS/conversational IVR accurate; Genesys+AWS cited; related_to Conversational AI sensible. |
| technology-capabilities/workforce-engagement-management.md | 5 | 4 | 5 | 5 | 5 | WEM=WFM+QM/recording/coaching, Erlang C; Verint+Genesys support; related_to Interaction Analytics correct. |
| systems/legacy/kony-dbx.md | 5 | 5 | 4 | 5 | 5 | Pre-acquisition Kony DBX folded into Infinity confirmed; sources relevant. Rel: "Digital Channel Platform depends on Kony DBX" + related Legacy Online Banking fine; supersession asserted in prose, edge handled by Infinity note. |
| systems/legacy/verint-wfm.md | 5 | 4 | 5 | 5 | 5 | On-prem WFM/WFO suite accurate; Verint sources support; depends-on + related_to Avaya Aura sensible (voice-centric WFM). |
| systems/modern/temenos-infinity.md | 5 | 5 | 5 | 5 | 5 | Cloud-native composable engagement platform; supersedes Kony DBX (same-capability, confirmed) and Legacy Online Banking — correct. |
| systems/modern/nice-cxone.md | 5 | 4 | 4 | 5 | 5 | CCaaS feature set accurate; sources are comparison pages (adequate, not vendor-doc). Rel: supersedes Avaya Aura same-capability OK, but 3rd modern system to claim the same single legacy node; Cisco UCCE orphaned. |
| systems/modern/twilio-flex.md | 5 | 4 | 4 | 5 | 5 | Programmable/API-first CCaaS accurate; Twilio + buyer-guide source. Rel: supersedes Avaya Aura duplicates Amazon Connect & NICE CXone onto one node — grain weakness, but same-capability test passes. |
| business-capabilities/L3-digital-onboarding.md | 5 | 5 | 5 | 5 | 4 | Fronts Party Authentication + eBranch; SCA/eIDAS/eKYC accurate; explicitly disambiguated from Customer Onboarding process. Real BIAN domains. |
| business-capabilities/L3-open-banking-channel.md | 5 | 5 | 5 | 5 | 5 | XS2A/AISP/PISP, Berlin Group, UK OB Standard, QWAC/QSEAL, Customer Access Entitlement — all correct and grounded. |
| business-capabilities/L3-inbound-contact-servicing.md | 5 | 5 | 5 | 5 | 5 | Contact Center Operations + Servicing Issue are real BIAN; FFIEC auth guidance correct; disambiguated from Contact Dialogue Management. |
| business-capabilities/L3-servicing-resource-management.md | 3 | 2 | 4 | 3 | 4 | **FAIL (grounded=2):** claims it realises BIAN "Servicing Position Management" — not a BIAN v9.1 service domain (unverifiable/fabricated). WFM content otherwise sound. Naming dinged: references "Channel Interaction Routing" (not a registry/BIAN canonical name). |
| business-capabilities/L4-digital-identity-verification.md | 5 | 4 | 5 | 5 | 5 | Doc+NFC+liveness, eIDAS/eKYC, NIST IAL2 correct. Vendors (Onfido/Jumio/iProov) named but only generic onboarding source cites them — minor grounded ding; vendors are well-known/accurate. |
| business-capabilities/L4-wearable-banking.md | 5 | 4 | 5 | 5 | 5 | Glanceable/tap-to-pay, network tokenisation, wrist-detection+passcode as possession+inherence SCA accurate; honestly flagged "beyond BIAN's named domains"; ebankIT source supports wearable channel. |
| business-capabilities/L4-agent-desktop-servicing.md | 5 | 5 | 5 | 5 | 5 | Customer Workbench is real BIAN; Channel Activity History for omni context; entitlement/masking/agent-assist all correct; disambiguated from Agent Assist tech sub-capability. |
| business-processes/digital-onboarding-journey.md | 5 | 4 | 5 | 5 | 5 | End-to-end DAO process; flow steps coherent; owner/inputs/outputs/Channel Session artifact correct; sources support. |
| business-processes/contact-centre-interaction.md | 5 | 4 | 5 | 5 | 5 | IVR→auth→route→handle→wrap→QA lifecycle accurate; voice-biometrics control valid; Teneo+Pindrop sources relevant. |
| process-flows/digital-onboarding-journey/01-start-digital-application.md | 4 | 4 | 5 | 5 | 5 | Single-action step (open journey, product select, start application); causes Capture Applicant Details; eKYC deferred to identity step — correct grain. |
| process-flows/digital-onboarding-journey/05-fund-digital-account.md | 4 | 4 | 5 | 5 | 5 | Atomic funding step with zero-balance decision branch; depends_on Payment Orchestration; AML-on-first-deposit control valid. |
| process-flows/atm-cash-servicing/01-forecast-atm-demand.md | 5 | 4 | 5 | 5 | 5 | Per-terminal forecast from usage/seasonality; NCR Atleos source supports; mentions ATM Custodian + ATM Cash Forecast — correct grain. |
| process-flows/atm-cash-servicing/04-replenish-atm-cash.md | 5 | 5 | 5 | 5 | 5 | Dual-custody cassette replenishment, CIT expected-vs-actual; Sonas source directly supports; single action. |
| process-flows/contact-centre-interaction/01-capture-ivr-selection.md | 4 | 4 | 4 | 4 | 5 | IVR greet+capture intent accurate. Rel/naming ding: "Contact Centre Agent picks up after IVR capture" implies agent owns an IVR-only self-service step — role attribution mismatched at this altitude. |
| process-flows/contact-centre-interaction/04-handle-customer-interaction.md | 4 | 3 | 4 | 4 | 5 | Handle/resolve with agent-assist OK. Grounded=3: depends_on Conversational AI for a human-agent handling step is a stretch and the lone USPTO patent source weakly supports the claim. |
| concepts/channel-session.md | 5 | 4 | 5 | 5 | 5 | Stateful cross-channel session artifact; carries auth/step-up/intent; single omnichannel-orchestration source adequate for a concept note. |
| concepts/atm-custodian.md | 5 | 4 | 5 | 5 | 5 | Role def accurate (forecast/replenish/reconcile under dual custody + CIT chain-of-custody); Sonas source supports replenishment scope. |

## Per-dimension means (n=28)

| dimension | mean |
|---|---|
| Definitional accuracy | 4.75 |
| Groundedness | 4.14 |
| Relationship sensibility | 4.75 |
| Canonical-naming fidelity | 4.82 |
| Granularity fit | 4.93 |

## Verdict: **FAIL**

- Gate requires mean ≥ 4.0 on every dimension AND no individual note scoring <3 on Groundedness or Relationship sensibility.
- All five dimension means clear 4.0. **However**, `L3-servicing-resource-management.md` scores **2 on Groundedness** (fabricated BIAN domain "Servicing Position Management"). One note <3 on Groundedness triggers a hard fail. This note must be fixed and re-judged before the domain is marked `done`.

## REQUIRED FIXES

- **business-capabilities/L3-servicing-resource-management.md (Groundedness 2 — BLOCKER):**
  - Remove/replace the claim that it "realises the BIAN Servicing Position Management service domain." No such domain exists in BIAN Service Landscape v9.1. Map instead to a real domain (e.g. align WFM/scheduling to an actual BIAN servicing/resource domain, or state explicitly that it extends beyond BIAN's named domains as the wearable-banking note honestly does).
  - Fix canonical naming: "Channel Interaction Routing" is not a registry/BIAN canonical term — use the registry name for the routing capability (e.g. the Omnichannel Routing Engine tech capability or BIAN Contact Routing).

- **process-flows/contact-centre-interaction/04-handle-customer-interaction.md (Groundedness 3 — recommended):**
  - The `depends on Conversational AI` for a human-agent handling step is weakly justified by a single patent. Either point the dependency at the Agent Desktop / Agent Assist capability (more accurate for a human-handled interaction) or add a source that supports conversational-AI involvement in live agent handling.

- **process-flows/contact-centre-interaction/01-capture-ivr-selection.md (Rel/naming — minor):**
  - "The Contact Centre Agent picks up after IVR capture" attributes an IVR self-service step to the agent role. Reword so the IVR step is system/self-service owned, with the agent entering only at the routing/handling step, to keep role grain correct.

- **systems/modern/nice-cxone.md & systems/modern/twilio-flex.md (Rel — advisory, not blocking):**
  - Three modern systems now `supersede Avaya Aura` while `cisco-ucce` (legacy contact-center) has no superseding modern system. Same-capability test passes, so not a gate failure, but consider distributing supersedes so Cisco UCCE is also covered, and/or model the relationship at the platform/capability grain rather than fanning every CCaaS onto one legacy node.
  - NICE CXone/Twilio Flex cite comparison/buyer-guide pages rather than primary vendor capability docs; adding a primary vendor source would lift Groundedness.
