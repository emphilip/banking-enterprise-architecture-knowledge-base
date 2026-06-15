# LLM-Judge Rubric (semantic eval)

The deterministic harness (`evals/checks.py`) cannot judge *meaning*. This rubric
is applied by a `judge` sub-agent to a **sample** of notes after each domain
deep-dive (and may be run ad hoc). The judge reads each sampled note **and the
sources it cites**, then scores each dimension 1–5. Record results in
`evals/judge-<domain>.md` and summarize in `VALIDATION.md`.

## Sampling
- Per domain run: judge **all new L1/L2 capability notes**, a **random 20%** of
  new L3/L4 notes, **all new system notes**, and **every process-flow index +
  2 random step notes per flow**. Minimum 12 notes, maximum 40.

## Dimensions (score 1–5 each; 3 = acceptable, <3 = fail)

1. **Definitional accuracy** — Is the definition factually correct and aligned to
   the cited framework (BIAN service domain / APQC element) or vendor doc? Does it
   start with the canonical name and stay within 1–3 sentences?
2. **Groundedness** — Does every non-obvious claim (especially vendor/product
   facts, framework mappings) trace to a cited, relevant source? Penalize
   invented versions, dates, customers, or capabilities not supported by the
   source. (This is the anti-hallucination gate.)
3. **Relationship sensibility** — Are the `## Relationships` semantically correct
   (right verb, right direction, right grain)? E.g. a business capability
   `depends_on` a technology capability (not the reverse); a child
   `derived_from` the correct parent; a modern system `supersedes` a *same-
   capability* legacy system.
4. **Canonical-naming fidelity** — Are all referenced concepts spelled exactly as
   in the registry, with no aliases used as relationship objects and no smuggled
   synonyms that should have been deduped?
5. **Granularity fit** — Is the note at the right altitude for its level (L4 is
   atomic/actionable; a step is a single action; a value stream is end-to-end),
   and is it free of overlap/duplication with a sibling note?

## Scoring & gate
- Compute the mean per dimension across the sample.
- **Gate:** mean ≥ 4.0 on every dimension AND no individual note scoring <3 on
  **Groundedness** or **Relationship sensibility**. Any note failing those two
  dimensions must be fixed and re-judged before the domain is marked `done`.
- Output format per note: `path | accuracy | grounded | rel | naming | gran | notes`.

## Judge prompt (use verbatim when spawning the judge sub-agent)
> You are a strict EA knowledge-base reviewer. For each file listed, read the
> file and fetch each URL in its References/sources. Score the 5 rubric
> dimensions 1–5 with a one-line justification, citing the specific source line
> that supports (or contradicts) each factual claim. Do not be generous: a claim
> with no supporting source scores ≤2 on Groundedness. Return a markdown table
> plus a short list of required fixes. Do not edit any files.
