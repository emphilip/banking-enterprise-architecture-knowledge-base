# CONVENTIONS

This knowledge base is optimized for ingestion by **Hive Mind**, a knowledge-graph
pipeline. The way concepts are **named** and **related** is as important as the
content. Follow these conventions for every file. They are not stylistic — they
determine whether the graph extracts correctly.

## 1. One concept per file (atomic / zettelkasten)

Each file describes exactly one concept. The **file name** and the **H1 heading**
ARE the concept's canonical name.

## 2. Canonical names

- Each concept is a short noun phrase, **1–4 words**.
- Use the **exact same spelling everywhere** the concept appears. Dedupe is
  case/whitespace-insensitive but otherwise literal — "Core Banking" and
  "Core-Banking" are different nodes.
- The single source of truth is [`glossary/_canonical-names.md`](glossary/_canonical-names.md).
  Never deviate from it.
- **No pronouns** in relationship sentences. Always repeat the full canonical
  name (write "Payment Orchestration depends on..." not "It depends on...").

## 3. Relationships must be explicit prose, near the TOP of the file

The chunker splits on blank lines into ~2000-char windows and is **not
heading-aware**. The subject + verb + object of every relationship must sit
together **inside the first ~1800 characters** of body text. Put the
`## Relationships` section immediately after the definition. Long detail prose
goes afterward.

## 4. The 7 relationship verbs (ONLY these — others are discarded)

| Verb           | EA meaning |
|----------------|------------|
| `depends_on`   | A business capability/process requires a technology capability; a technology capability is realized/serviced by a system. "X depends on Y." |
| `derived_from` | A sub-capability is derived from its parent capability (child derived_from parent). Used for L1→L2→L3 decomposition. |
| `supersedes`   | A modern/AI system supersedes a legacy system delivering the same technology capability. |
| `defined_in`   | A capability/process belongs to a domain or value stream. "X is defined in the Y domain." |
| `related_to`   | Symmetric cross-domain association where no dependency/hierarchy fits. |
| `causes`       | Process/event causality. "X causes Y." |
| `mentions`     | A soft reference to another concept with no real dependency. |

Write each relationship as a **complete natural sentence** using the verb
verbatim, e.g.:
- "Payments Processing depends on the Payment Orchestration capability."
- "Card Issuing is derived from the Cards Management capability."
- "Thought Machine Vault supersedes Temenos T24."
- "Customer Onboarding is defined in the Customer Management domain."

## 5. Aliases

List aliases in prose so the extractor captures them: `**Also known as:** A, B.`

## 6. File size

Keep each file **< ~6 KB** and never **> 1 MB**. Prefer many small files over
few big ones.

## 7. Frontmatter

YAML frontmatter is allowed and useful for humans / Obsidian / Dataview, but is
**NOT parsed by the pipeline**. Never rely on it for relationships — always
duplicate that information in prose.

## 8. Wikilinks

`[[wikilinks]]` are for humans / Obsidian graph view and validation. The pipeline
ignores them. Every `_index.md` is a Map-of-Content that wikilinks its files.

## Note template

```markdown
---
id: <kebab-canonical-name>
title: <Canonical Name>
type: business-capability | business-process | technology-capability | legacy-system | modern-system | domain | glossary-term
domain: <Domain Name>
level: L1 | L2 | L3            # capabilities only
maturity: legacy | standard | emerging   # systems only
aliases: ["<alias1>", "<alias2>"]
status: draft
sources: ["<url1>", "<url2>"]
---

# <Canonical Name>

**Definition.** <1–3 sentences. Start with the canonical name as the subject.>
**Also known as:** <alias1>, <alias2>.

## Relationships
- <Canonical Name> is defined in the <Domain> domain.
- <Canonical Name> is derived from <Parent Capability>.
- <Canonical Name> depends on <Technology Capability / System>.
- <Modern System> supersedes <Legacy System>.
- <Canonical Name> is related to <Other Concept>.

## Details
<vendors, patterns, typical implementation, AI/cloud-native notes, gotchas>

## References
- [<title>](<url>)
```

## Deep-dive conventions (L4 capabilities + process flows)

These additive conventions support the iterative domain deep-dive. They do not
break v1; they extend it. Progress is tracked in
[`_status/PROGRESS.md`](_status/PROGRESS.md).

### Capability depth (business: L1→L2→L3→L4; technology: L1→L2→L3)

- Business capabilities decompose to **L4** (the smallest independently
  meaningful capability). Each child `derived_from` its parent and `defined_in`
  its domain. Ground L3/L4 in **BIAN** Service Domains / Service Operations and
  align naming to **APQC PCF**.
- Technology capabilities decompose to **L2 and L3**. Record the rung in
  frontmatter (`level: L2 | L3`) and state the hierarchy in prose with
  `derived_from`.
- File naming: business capabilities keep the `L<level>-<kebab>.md` pattern
  (now including `L4-...`). Technology capability files stay flat (`<kebab>.md`)
  with the level in frontmatter and `derived_from` prose.

### Process flows (APQC 5 granularities)

Granularity ladder: **Value Stream → Process Group → Process → Sub-Process →
Task/Step**. v1 already holds Processes; deep-dive adds the finer rungs.

- Step notes live in `process-flows/<kebab-process>/NN-<kebab-step>.md`, where
  `NN` is a zero-padded execution order (`01`, `02`, ...).
- Each step note: `defined_in` its process, `causes` the next step (the ordered
  chain), `depends_on` the capability / technology capability / system it
  consumes, and `mentions` the actors and artifacts involved. Branches at a
  decision point are extra `causes` sentences from the decision step.
- The parent process note gains a `## Flow` section that lists the ordered steps
  as `causes` sentences — this is the authoritative sequence for that process.
- Capture per flow: trigger event, actors/roles, inputs, outputs, decision
  points/branches, systems touched, and key controls (KYC, fraud, limits).

### Supporting concept types

When a flow references them, author atomic notes with these `type` values:
`role` (actor/persona), `event` (business/trigger event), `artifact` (data
object / document). Link them with `mentions` / `related_to`. As always,
frontmatter `type` is for humans; the graph relies on the prose.

### Registry discipline during deep-dive

Every new L3/L4/step/supporting name is minted through the **ontology-steward
gate** and appended to [`glossary/_canonical-names.md`](glossary/_canonical-names.md)
**before** authoring. Check for collisions across capabilities, processes, tech
capabilities, systems, and steps; append a disambiguating word if needed and log
it in the ledger's Decisions log.
