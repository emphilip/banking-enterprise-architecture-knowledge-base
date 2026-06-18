# LLM-Judge Report — Integration & APIs (TECHNOLOGY only)

Run scope: decomposition of API Management, Integration Platform, Workflow
Orchestration, and Notification Services into 29 new tech sub-capabilities plus
15 systems. Sampled 22 of those files (14 capabilities + 8 systems).

Date: 2026-06-18 · Reviewer: judge sub-agent · cwd:
`/home/user/banking-enterprise-architecture-knowledge-base`

## Verification performed
- Confirmed all four parent capabilities (`api-management`, `integration-platform`,
  `workflow-orchestration`, `notification-services`) exist as L1 domain capabilities;
  L2 sub-caps derive from them and L3 sub-caps (`oauth-token-service` → API Security &
  Throttling L2; `dmn-decision-service` → Workflow Decision Engine L2) derive from a
  sensible L2 — grain is correct.
- Confirmed every relationship object resolves to a real registry note
  (Integration Message Broker, Event Streaming Bus, Workflow Decision Engine,
  Notification Template Manager, Data Mapping & Transformation, CA API Gateway,
  IBM MQ, IBM Business Automation Workflow, Legacy Online Banking, Kong, Workato,
  Bonita, Amazon SNS) — canonical names used exactly, no aliases as objects.
- Web-corroborated: Gravitee (Apache 2.0, event-native, sync+async, gateway/console/
  portal) ✔; Amazon SES (email-only, no SMS, SNS bounce/complaint events) ✔;
  Appian vs IBM Business Automation Workflow (same BPM/workflow-orchestration
  category → supersedes valid) ✔.

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|------|:--:|:--:|:--:|:--:|:--:|------|
| technology-capabilities/api-gateway-service.md | 5 | 5 | 5 | 5 | 5 | Data-plane definition matches Azure APIM control/data-plane split & Amazon API Gateway; derived_from API Management correct. |
| technology-capabilities/oauth-token-service.md | 5 | 4 | 5 | 5 | 5 | Accurate OAuth2/OIDC/JWKS detail; derived_from API Security & Throttling sensible. Sources are generic API-mgmt pillars, not an OAuth/OIDC spec — grounding adequate but not authoritative. |
| technology-capabilities/api-security-and-throttling.md | 5 | 5 | 5 | 5 | 5 | 429/retry-after, quota vs rate-limit, mTLS all standard; depends_on API Gateway Service is right direction. |
| technology-capabilities/enterprise-service-bus.md | 5 | 5 | 5 | 5 | 5 | Mediation/itinerary routing/protocol bridging accurate; IBM Integration Bus + MuleSoft examples valid; bottleneck caveat well-judged. |
| technology-capabilities/b2b-edi-gateway.md | 5 | 5 | 5 | 5 | 5 | X12 810/850, EDIFACT, 997/CONTRL, ISA/GS/ST, AS2/VAN all correct; depends_on Data Mapping & Transformation apt. |
| technology-capabilities/managed-file-transfer.md | 5 | 5 | 5 | 5 | 5 | SFTP/FTPS/AS2, PGP, checkpoint restart correct; related to B2B/EDI Gateway sensible. |
| technology-capabilities/integration-event-mesh.md | 5 | 5 | 5 | 5 | 4 | Solace event-mesh broker-bridging/subscription-propagation accurate; related to Event Streaming Bus apt. Slight conceptual overlap with Integration Message Broker, but distinct grain. |
| technology-capabilities/bpmn-process-engine.md | 5 | 5 | 5 | 5 | 5 | OMG BPMN 2.0 token semantics, gateways, incidents match Camunda docs; derived_from Workflow Orchestration correct. |
| technology-capabilities/dmn-decision-service.md | 5 | 5 | 5 | 5 | 5 | DRD/decision tables/hit policies/FEEL accurate per OMG DMN + Camunda; L3 under Workflow Decision Engine fits. |
| technology-capabilities/saga-orchestration-service.md | 5 | 4 | 5 | 5 | 5 | Saga vs 2PC, compensation, orchestrated-vs-choreographed correct; sources are generic Camunda pages (not saga-specific) so grounding adequate not pinpoint. derived_from Workflow Orchestration fits. |
| technology-capabilities/sms-gateway.md | 5 | 5 | 5 | 5 | 5 | SMPP/REST, GSM-7/UCS-2, DLR, sender IDs accurate; derived_from Notification Services, depends_on Template Manager correct. |
| technology-capabilities/email-delivery-service.md | 5 | 5 | 5 | 5 | 5 | SPF/DKIM/DMARC, bounce/complaint/FBL, IP warm-up accurate; relationships correct. |
| technology-capabilities/push-notification-service.md | 5 | 5 | 5 | 5 | 5 | APNs HTTP/2 token-JWT auth, FCM, token pruning, topic fan-out accurate; relationships correct. |
| technology-capabilities/channel-preference-router.md | 5 | 4 | 5 | 5 | 4 | Preference/consent/quiet-hours/fallback logic sound; sources are general system-design blogs (acceptable). Slight grain overlap with parent Notification Services orchestration role, but distinct as the router sub-cap. |
| systems/legacy/ibm-api-connect.md | 5 | 5 | 5 | 5 | 5 | DataPower gateway + manager + portal full-lifecycle accurate; "API Management depends on IBM API Connect" correct direction; related to CA API Gateway (peer) apt. |
| systems/legacy/ibm-app-connect-enterprise.md | 5 | 5 | 5 | 5 | 5 | ACE = successor to IIB/WebSphere Message Broker correct; Integration Platform depends_on, related to IBM MQ both apt. |
| systems/legacy/legacy-sms-gateway.md | 4 | 4 | 4 | 5 | 4 | Generic placeholder system; definition stretches SMS gateway to also cover email/SMTP, which strains the "SMS Gateway" name and creates the SES mismatch below. Wikipedia-only source. |
| systems/modern/gravitee.md | 5 | 5 | 4 | 5 | 5 | Apache 2.0 / event-native / sync+async / gateway-console-portal all web-verified. supersedes CA API Gateway and IBM API Connect both same-capability (API mgmt) — valid; double-supersedes is acceptable. |
| systems/modern/snaplogic.md | 5 | 5 | 5 | 5 | 5 | Snaps/visual pipelines/ETL-ELT/API-led accurate; supersedes IBM App Connect Enterprise same-capability (iPaaS vs ESB) valid; related to Workato apt. |
| systems/modern/appian.md | 5 | 5 | 5 | 5 | 5 | Low-code BPM + rules + case + RPA/AI accurate; supersedes IBM Business Automation Workflow web-confirmed same BPM category; related to Bonita apt. |
| systems/modern/twilio.md | 5 | 5 | 5 | 5 | 5 | CPaaS SMS/MMS/RCS/WhatsApp+voice/email accurate; supersedes Legacy SMS Gateway same-capability (messaging) valid; related to Amazon SNS apt. |
| systems/modern/amazon-ses.md | 5 | 5 | 3 | 5 | 5 | SES facts (email-only, SNS bounce/complaint events) web-verified and accurate. BUT "Amazon SES supersedes Legacy SMS Gateway" is a cross-capability mismatch: SES is email-only and cannot supersede an SMS gateway. supersedes should target an email/SMTP gateway, not the SMS gateway. |

## Per-dimension means (n=22)

| Dimension | Mean |
|-----------|:----:|
| Definitional accuracy | 4.95 |
| Groundedness | 4.82 |
| Relationship sensibility | 4.73 |
| Canonical-naming fidelity | 5.00 |
| Granularity fit | 4.86 |

## Verdict

**PASS.**

- Every dimension mean ≥ 4.0 (lowest 4.73).
- No individual note scores <3 on Groundedness or Relationship sensibility
  (the two gating dimensions). The lowest gating score is amazon-ses Relationship
  sensibility = 3, which is acceptable (the gate fails only at <3).

The amazon-ses supersedes mismatch is the one note sitting exactly at the gate
floor and should be fixed before the domain is marked `done`, but it does not
fail the gate.

## Required fixes (recommended, non-blocking)

- **systems/modern/amazon-ses.md** — Replace `Amazon SES supersedes Legacy SMS
  Gateway`. SES is email-only and cannot supersede an SMS gateway. Either (a)
  introduce/target a legacy email/SMTP gateway note as the supersede object, or
  (b) downgrade to `is related to` the email side, or (c) widen the legacy note's
  scope explicitly so SES supersedes only its email/SMTP portion.
- **systems/legacy/legacy-sms-gateway.md** — The note is titled "SMS Gateway" but
  its definition folds in SMTP/email. This dual scope is what makes SES (email)
  appear to supersede an "SMS" gateway. Tighten the definition to SMS/SMPP only
  (and let the email side be a separate legacy mail-gateway note), or rename to a
  generic "Legacy Notification Gateway" so both Twilio and SES superseding it is
  coherent.
- **technology-capabilities/oauth-token-service.md** and
  **saga-orchestration-service.md** (minor) — Add one authoritative source each
  (e.g. RFC 6749/OIDC Core for OAuth; a saga-pattern reference for the saga note)
  to lift Groundedness from 4 to 5; current generic vendor/blog sources are
  adequate but not pinpoint to the load-bearing claims.
