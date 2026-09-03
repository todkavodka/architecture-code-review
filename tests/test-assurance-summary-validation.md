# Test Assurance Summary — Validation Record

## Scope

Behavioral change: Test Review must provide a concise decision-oriented user-facing summary before its detailed assurance map and optional Test Plan.

## Fail-first evidence

Observed real-world canary before the change:

- detailed Test Assurance Map existed;
- detailed Test Plan existed;
- bounded accounting and traceability were strong;
- no mandatory concise persisted summary answered whether the test system could be trusted, what the few most important weaknesses were, and what should be done first;
- the user had to reconstruct the decision from MAT/GAP/WS/RF/TM/TASK detail.

Result: `PS79_RED_NO_DECISION_SUMMARY`.

This is an observed behavioral/presentation failure, not a synthetic claim that the underlying assurance analysis was wrong.

## Candidate contract check

Candidate contract in `capabilities/test-review/SKILL.md` now requires:

- capability-owned `00-test-assurance-summary.md` when artifacts are persisted;
- verdict + one-sentence reason;
- material strengths;
- 3–7 prioritized weaknesses;
- compact bounded accounting;
- ordered first actions without creating a second roadmap;
- material limitations;
- pointers to the detailed map and Test Plan;
- IDs only as traceability, not primary prose;
- summary semantics constrained to accepted capability evidence;
- umbrella report surfaces the summary verdict instead of duplicating detailed evidence.

Static/contract result: `PS79_GREEN_DECISION_SUMMARY`.

## Runtime status

No fresh independent runtime agent execution was performed for PS-79 in this change.

Runtime result: `PS79_INCONCLUSIVE`.

Do not reinterpret the static contract check as runtime GREEN. The next real Test Review is the preferred canary: verify that `00-test-assurance-summary.md` is produced and that a reader can understand verdict, major weaknesses, and first actions without opening `01-test-assurance-map.md` or `02-test-plan.md`.
