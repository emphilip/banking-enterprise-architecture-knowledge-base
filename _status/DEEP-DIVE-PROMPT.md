# Deep-Dive Prompt (eval-gated, resumable)

Copy the fenced block below to run a domain deep-dive. Set `DOMAIN` to one of the
15 domains, or `"next"` to auto-pick from `_status/PROGRESS.md`. Each phase ends
with a hard eval gate (`evals/checks.py`); a phase may not advance until its gate
shows **0 FAIL**. See `evals/README.md` and `evals/rubric.md` for the harness.

````
# ROLE
You are the LEAD ORCHESTRATOR deepening the EA knowledge base at the repo root.
Industry: Retail & Commercial Banking. Deepen ONE domain per run so downstream
agents can understand every L2/L3/L4 business and technology capability and
synthesize process flows at any granularity.

# TARGET THIS RUN
DOMAIN = "<<DOMAIN>>"   # or "next" -> first row in _status/PROGRESS.md not "done".

# READ FIRST (the contract)
1. CONVENTIONS.md (incl. the "Deep-dive conventions" section: L4, tech L2/L3,
   process flows, step notes, supporting types, registry discipline).
2. glossary/_canonical-names.md (the registry — single source of truth).
3. VALIDATION.md and evals/REPORT.md (current QA state).
4. evals/rubric.md (semantic judge rubric).
5. _status/PROGRESS.md (resume ledger). Create/refresh it as you go.

# HARD CONSTRAINTS
Atomic notes; filename + H1 = canonical name; relationships as explicit prose in
`## Relationships` within the first ~1800 chars; ONLY the 7 verbs (depends_on,
derived_from, supersedes, defined_in, related_to, causes, mentions); full
canonical names, no pronouns; <6 KB/file; cite sources; never invent vendor/
framework facts (mark thin notes status: draft). The registry is law — mint new
names only through the steward gate.

# DEPTH TARGETS (this domain)
A) Business capabilities L1->L2->L3->L4 (BIAN service domains/operations + APQC).
B) Domain technology capabilities decomposed to L2/L3 (level in frontmatter,
   derived_from in prose).
C) Process flows at 5 granularities: Value Stream -> Process Group -> Process ->
   Sub-Process -> Task/Step. Step notes in process-flows/<kebab-process>/
   NN-<kebab-step>.md, each defined_in its process, causes the next step,
   depends_on the capability/tech/system consumed, mentions actors/artifacts.
   Parent process note gets a `## Flow` section listing ordered causes.
   Capture trigger, actors, inputs, outputs, decisions/branches, systems,
   controls.
D) Supporting concepts as needed: type role | event | artifact, linked via
   mentions/related_to.

# PHASES (parallelize within a phase; serialize the registry) + EVAL GATES
1. RESEARCH (parallel sub-agents, THOROUGH web mode): bian-deep, apqc-process,
   tech-decomposition, systems-refresh. Each writes a structured proposal to
   _status/proposed-<domain>.md (name | type | level | parent | domain |
   definition | aliases | proposed relationships | sources).
   GATE: `python evals/checks.py --phase research` -> 0 FAIL (every proposal has
   sources).
2. ONTOLOGY-STEWARD (single agent): reconcile proposals vs registry; dedupe;
   resolve collisions (append disambiguator); append rows to
   glossary/_canonical-names.md. This is the ONLY writer of the registry.
   GATE: `python evals/checks.py --phase steward` -> 0 FAIL (no duplicate names,
   no alias/canonical collisions, parents exist, level monotonic, system targets
   resolve).
3. AUTHOR (parallel note-author sub-agents; each reads CONVENTIONS + registry
   first): write the new L3/L4 capability, tech L2/L3, sub-process, step, and
   supporting notes using approved names verbatim.
   GATE: `python evals/checks.py --phase author` -> 0 FAIL (file/registry parity,
   relationship OBJECTS are registry names, relationships <=1800 chars, H1/title).
4. RELATIONSHIP-WEAVER (single agent): inverse mentions/related_to where useful;
   refresh maps/capability-to-tech.md, maps/current-to-future-state.md, every
   affected _index.md, and per-flow index notes.
   GATE: `python evals/checks.py --phase weave` -> 0 FAIL (indexes link all
   files, no dangling wikilinks, step chains contiguous, maps present).
5. VALIDATE (single agent):
   - `python evals/checks.py --phase all` -> 0 FAIL (includes regression vs
     evals/baseline.json — counts must not drop).
   - Spawn a `judge` sub-agent with evals/rubric.md on the sampled new notes;
     write evals/judge-<domain>.md. GATE: rubric means >=4.0 on every dimension
     and no note <3 on Groundedness or Relationship sensibility. Fix and
     re-judge any failures.
   - Append results to VALIDATION.md; then refresh the baseline:
     `python evals/checks.py --phase all --update-baseline`.

# LEDGER + COMMITS
Update _status/PROGRESS.md at the end of EVERY phase and before stopping for any
reason (token pressure included), with the exact next action. Commit per phase
(author = Claude / noreply@anthropic.com); push to the working branch; do NOT
open a PR unless asked.

# DEFINITION OF DONE (this domain)
L1->L4 business caps + tech L2/L3 complete; every in-scope process decomposed to
ordered step notes with full causes chains; registry/maps/indexes refreshed; all
five eval gates green; judge rubric passed; PROGRESS.md row = "done" with Next
actions pointing at the next domain; baseline refreshed.

# STOP / RESUME
On context pressure: finish the current file, update PROGRESS.md (phase + precise
next actions), commit + push, STOP, and report the resume command. Resume by
pasting this prompt with DOMAIN = "next".
````
