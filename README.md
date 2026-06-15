# Banking Enterprise Architecture Knowledge Base

An Obsidian-style, atomic markdown knowledge base modeling the enterprise
architecture of **Retail & Commercial Banking** for a consulting EA practice.
It is engineered to be ingested by **Hive Mind**, a knowledge-graph pipeline, so
every concept lives in its own file with explicit, vocabulary-controlled
relationship prose.

> New here? Read [`CONVENTIONS.md`](CONVENTIONS.md) first — it defines the note
> template, the canonical-naming rules, and the 7-verb relationship vocabulary
> that make the graph extract cleanly.

## The five pillars modeled

1. **Business capabilities** — an L1→L2→L3 capability map for retail & commercial
   banking, grounded in BIAN and APQC PCF. → [`business-capabilities/`](business-capabilities/_index.md)
2. **Business processes / value streams** — how work flows. → [`business-processes/`](business-processes/_index.md)
3. **Technology capabilities** — the tech functions that enable the business
   capabilities. → [`technology-capabilities/`](technology-capabilities/_index.md)
4. **Legacy / current-state systems** — incumbent vendor products and categories
   servicing those technology capabilities. → [`systems/legacy/`](systems/legacy/_index.md)
5. **Modern / AI systems** — emerging cloud-native, AI-driven systems that now
   enable the same technology capabilities, each mapped to the legacy system it
   supersedes. → [`systems/modern/`](systems/modern/_index.md)

The downstream goal: agents query this base to synthesize artifacts,
requirements, process flows, and current→future-state recommendations for
engagements. Every legacy system has a modern/AI successor mapped.

## How to navigate

- **Domains / value streams** — start at [`domains/_index.md`](domains/_index.md).
  Each domain is a Map-of-Content linking its capabilities and processes.
- **Capability map** — [`business-capabilities/_index.md`](business-capabilities/_index.md).
- **Glossary & canonical names** — [`glossary/_canonical-names.md`](glossary/_canonical-names.md)
  is the single source of truth for every concept's name and aliases.
- **Maps**:
  - [`maps/capability-to-tech.md`](maps/capability-to-tech.md) — business→technology
    capability matrix.
  - [`maps/current-to-future-state.md`](maps/current-to-future-state.md) — legacy→modern
    successor matrix.

## How to validate

See [`VALIDATION.md`](VALIDATION.md) for the QA checklist. In short:

1. Every relationship sentence references a name in
   [`glossary/_canonical-names.md`](glossary/_canonical-names.md).
2. No file relies on frontmatter for relationships (prose duplicates it).
3. Relationship prose sits within the first ~1800 characters of the body.
4. Every `_index.md` links its files; there are no orphan concepts.

## Repository structure

```
README.md                      # this file
CONVENTIONS.md                 # note template + 7-verb mapping + naming rules
VALIDATION.md                  # QA checklist + gaps
glossary/                      # canonical-names registry + glossary terms
domains/                       # value streams / capability domains (MOCs)
business-capabilities/         # L1/L2/L3 capability notes
business-processes/            # process / value-stream notes
technology-capabilities/       # technology capability notes
systems/legacy/                # current-state / incumbent systems
systems/modern/                # modern / cloud-native / AI systems
maps/                          # cross-cutting matrices
```
