# PS-79 — Test Assurance Summary

This scenario is the behavioral contract for the human-facing decision layer of Test Review.

## Observed RED baseline

A real Test Review canary produced a technically strong `01-test-assurance-map.md` and `02-test-plan.md` with bounded accounting, detailed evidence, gaps, and workstreams, but no mandatory concise user-facing answer to the questions:

- Can the current test system be trusted for the material behavior that matters?
- What are the most important things that are wrong with the test system?
- Which problems create false confidence rather than merely missing coverage?
- What should be fixed first?

The result required the reader to reconstruct the decision from MAT/GAP/WS/RF/TM/TASK detail. That is a presentation failure even when the underlying assurance analysis is correct.

Baseline verdict: `PS79_RED_NO_DECISION_SUMMARY`.

## GREEN contract

At completion of Test Review, before detailed evidence artifacts, produce a concise user-facing Test Assurance Summary. When capability artifacts are persisted, the summary is owned by Test Review and written as:

```text
00-test-assurance-summary.md
```

The summary must be understandable without reading the detailed assurance map or test plan first.

It contains, in this order:

1. **Verdict** — one plain decision token plus a one-sentence explanation.
2. **What is working well** — only material strengths supported by accepted evidence.
3. **What is wrong** — the 3–7 most decision-relevant weaknesses, ordered by material consequence; explicitly distinguish misleading/false-confidence tests from merely absent evidence when applicable.
4. **Assurance state** — compact bounded accounting (`Adequate / Partial / Not evidenced / Unknown`) with denominator.
5. **What to do first** — a short ordered priority list, normally P0/P1/P2 or equivalent, derived from the accepted assurance map/Test Plan rather than inventing a second roadmap.
6. **Important limitations** — only limitations that materially affect the verdict, such as runtime validation being unavailable.
7. **Links/pointers** — references to the detailed assurance map and Test Plan for evidence and implementation detail.

The summary MUST NOT become another evidence ledger. `MAT-*`, `GAP-*`, `RF-*`, `TM-*`, `TASK-*`, and `WS-*` identifiers may appear as compact traceability references, but they must not be the primary prose.

Recommended size: roughly one to two screens. If a reader cannot understand the verdict, the major weaknesses, and the first actions in about one minute, the presentation is not accepted.

The detailed `01-test-assurance-map.md` remains the evidence/authority layer. `02-test-plan.md` remains the engineering execution layer when that endpoint is selected. The summary is a projection of accepted capability evidence and may not strengthen, weaken, or invent technical conclusions.

## Failure conditions

RED if any of these occurs:

- only the detailed map/plan is produced and the user must infer the decision;
- the summary is primarily IDs, counts, or internal workflow jargon;
- the summary lists every gap instead of prioritizing the important few;
- the summary invents severity or roadmap changes not owned by Test Review;
- a material runtime/evidence limitation affecting the verdict is omitted;
- the summary contradicts the accepted assurance map or Test Plan;
- a concise summary exists only in chat but is not persisted when capability artifacts are persisted.

Verdicts:

`PS79_GREEN_DECISION_SUMMARY` | `PS79_RED_NO_DECISION_SUMMARY` | `PS79_RED_SUMMARY_DRIFT` | `PS79_INCONCLUSIVE`
