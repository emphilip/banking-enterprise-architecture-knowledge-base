# LLM-Judge Results — Deposits & Accounts (sample of 12)

Judged: 2026-06-15. Reviewer: judge sub-agent (strict). Scale 1–5 (3 = acceptable, <3 = fail).

## Scores

| path | accuracy | grounded | rel | naming | gran | notes |
|------|---------|----------|-----|--------|------|-------|
| systems/legacy/fiserv-premier.md | 5 | 5 | 4 | 4 | 5 | Accurate: Premier is a long-established Fiserv community-bank deposit/loan core (Fiserv, KC Fed, Gartner corroborate). "related to Fiserv DNA" is sensible (sibling Fiserv core). Sources relevant. |
| systems/legacy/fis-horizon.md | 5 | 5 | 4 | 4 | 5 | Accurate: HORIZON is an FIS community-bank core (FIS brochure/XCelent corroborate). "sitting alongside FIS IBS" and "related to FIS Profile" are correct sibling framing. Well grounded. |
| systems/modern/tuum.md | 5 | 5 | 4 | 4 | 5 | Accurate: Estonian, founded as Modularbank (2019→Tuum 2021), cloud-native API-first microservices with modular accounts engine — all corroborated. `supersedes Fiserv Premier` is a same-capability deposit-core supersede (sensible grain, though no doc of actual migration). |
| systems/modern/saascada.md | 5 | 5 | 4 | 4 | 5 | Accurate: cloud-native, CQRS + event-sourcing, Product Sequencer, multi-ledger/multi-currency no-code products — all confirmed on saascada.com. `supersedes Jack Henry Core Director` is same-capability (deposit core) and sensible. |
| technology-capabilities/deposit-account-management.md | 5 | 4 | 5 | 5 | 5 | Strong definition of deposit system-of-record; Vault Core and SAP Deposits Management both support it. Relationships correct (tech cap derived_from Core Banking Processing, related to Account Servicing). Minor: SAP source is the same generic doc reused. |
| technology-capabilities/dormancy-and-escheatment-service.md | 4 | 3 | 5 | 5 | 4 | Definition sound. Groundedness weaker: Alogent "banking definitions" page is generic boilerplate and SAP doc does not specifically substantiate escheatment workflows; dormancy/escheatment automation claim only thinly sourced. Relationships correct. |
| business-capabilities/L3-deposit-account-origination.md | 4 | 3 | 5 | 3 | 4 | CIP/31 CFR 1020.220 claim is accurate and well sourced. BIAN naming is the issue: BIAN has Current Account, Savings Account and Term Deposit domains — there is no distinct "Deposit Account" service domain; cited Open Risk catalog does not confirm the trio as named. Relationships correct (derived_from Account Opening, depends_on Deposit Account Management). |
| business-capabilities/L3-deposit-interest-accrual.md | 4 | 3 | 5 | 3 | 4 | Reg DD 1030.7 daily/average-daily-balance + APY claim accurate and sourced. "BIAN Interest Determination service domain" not confirmed as a canonical BIAN domain name (interest is handled within account domains); generic catalog source does not substantiate it. Relationships sensible. |
| business-capabilities/L4-early-withdrawal-handling.md | 4 | 4 | 5 | 4 | 5 | Atomic L4, correct altitude. BIAN Term Deposit domain confirmed; Reg DD 1030.4 disclosure correct. "minimum penalty on time deposits withdrawn within six days" conflates the time-account definition/seven-days-interest rule slightly but is defensible and sourced. |
| process-flows/account-closure/07-escheat-dormant-account.md | 4 | 3 | 4 | 4 | 5 | Single-action step at right grain. Escheatment-to-state claim is correct, but sources are blog/firm posts (incharge.org, witheisen) — weak for a regulatory step. "CASS rules" is a UK client-money concept, an odd/incorrect control to cite for US state escheatment. Relationships ok. |
| process-flows/deposit-account-opening/05-disclose-account-terms.md | 5 | 5 | 5 | 5 | 5 | Accurate: Reg DD / Truth-in-Savings disclosure prior to account establishment, sourced to 12 CFR Part 1030. Single action, correct grain. `causes Establish Deposit Account` is correct sequencing. |
| concepts/dormancy-notice.md | 4 | 3 | 4 | 4 | 4 | Definition of due-diligence/abandoned-property letter is correct in substance, but both sources are a bank marketing page and an accounting-firm blog — thin for the statutory due-diligence-window claim. Relationships (mentions Issue Dormancy Notice, Dormancy & Escheatment) sensible. |

## Per-dimension means (n=12)

- Definitional accuracy: (5+5+5+5+5+4+4+4+4+4+5+4)/12 = **4.50**
- Groundedness: (5+5+5+5+4+3+3+3+4+3+5+3)/12 = **4.00**
- Relationship sensibility: (4+4+4+4+5+5+5+5+5+4+5+4)/12 = **4.50**
- Canonical-naming fidelity: (4+4+4+4+5+5+3+3+4+4+5+4)/12 = **4.08**
- Granularity fit: (5+5+5+5+5+4+4+4+5+5+5+4)/12 = **4.67**

## Verdict

**PASS (marginal).**

Gate test:
1. Mean ≥ 4.0 on every dimension — met (lowest is Groundedness at exactly 4.00).
2. No individual note <3 on Groundedness or Relationship sensibility — met (the lowest Groundedness scores are 3, not below).

The domain passes, but **Groundedness is on the floor (4.00)** and four notes sit at the minimum acceptable 3 — the margin is thin and any further weak-sourced note would break the gate.

## Recommended fixes (not blocking, but should be addressed before `done`)

- **L3-deposit-account-origination.md / L3-deposit-interest-accrual.md (naming + grounding):** Replace the unverified BIAN domain names. BIAN canonical domains are *Current Account*, *Savings Account*, *Term Deposit* (no standalone "Deposit Account" domain); "Interest Determination" is not a confirmed BIAN service domain. Cite a specific BIAN service-domain page rather than the generic Open Risk Manual category index, or soften the claim.
- **dormancy-and-escheatment-service.md (grounding):** The Alogent "banking definitions" page is generic boilerplate and the SAP doc does not substantiate escheatment workflows. Add a source that specifically documents dormancy/escheatment as a core function.
- **07-escheat-dormant-account.md (accuracy + grounding):** Remove or correct the "CASS rules" control — CASS is UK client-money/asset regulation, not US state unclaimed-property/escheatment. Replace blog sources with a state unclaimed-property statute or NAUPA reference.
- **concepts/dormancy-notice.md (grounding):** The statutory due-diligence-window claim rests on a bank marketing page and an accounting-firm blog; cite a state unclaimed-property due-diligence statute.
- **L4-early-withdrawal-handling.md (accuracy, minor):** Tighten the "withdrawn within six days of opening" phrasing to match the 12 CFR 1030 time-account definition (maturity ≥ 7 days; ≥ 7 days' simple interest penalty if withdrawn within the first 6 days).
