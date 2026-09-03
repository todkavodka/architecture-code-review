# Projection Repair — Validation Record

## Scope

Behavioral change: add `PROJECTION_REPAIR` as a first-class Session Intent for repairing accepted final/user-facing review projections without reopening technical audit stages unless semantic drift is discovered.

## Fail-first evidence

Baseline: `main@b39b6f0321db20981ffcac6d585a1b4cd5bed46b`.

At baseline:

- `references/session-orchestration.md` persisted exactly five Session Intents: `USE_EXISTING | NEW | RESUME | REVALIDATE | EXTEND`;
- `PROJECTION_REVALIDATION` already existed as an editorial correction mechanism after final assembly;
- there was no first-class startup route for a user returning later to a `COMPLETE` audit solely to repair final documents;
- README likewise documented exactly five Session Intents.

Result: `PS80_RED_NO_PROJECTION_REPAIR_INTENT`.

This is an orchestration/presentation gap, not evidence that the existing projection revalidation mechanism was technically wrong.

## Candidate static contract check

Candidate contract introduced across:

- `references/session-orchestration.md`;
- `references/revalidation-and-freshness.md`;
- root `SKILL.md`;
- `README.md`;
- `tests/pressure-scenario-80-projection-repair.md`.

Fresh static inspection confirms:

1. Session Intent set now contains exactly six tokens including `PROJECTION_REPAIR`.
2. `COMPLETE` + same baseline + explicit final-document repair routes to `PROJECTION_REPAIR`; ordinary consumption still recommends `USE_EXISTING`.
3. Changed project baseline remains a `REVALIDATE` concern; projection repair cannot hide source changes.
4. Repair scope is limited to presentation/projection concerns: language, structure, links, Markdown, navigation, terminology, references, duplicate/stale projection, and Mermaid syntax/renderability without changing the accepted mechanism.
5. Accepted evidence, root boundary, severity/exploitability, owner/invariant, product-intent state, finding disposition, target mechanism, roadmap dependencies/gates, security assumptions, and safe-activation semantics are outside projection-writer authority.
6. Each changed projection is bound to accepted authority refs and uses `PROJECTION_REVALIDATION`.
7. Projection-level checks include links, Markdown/reference consistency, terminology/language, stale projection, final status consistency, and Mermaid parser/render validation when tooling exists.
8. Missing Mermaid tooling must remain `MERMAID_RENDER_VALIDATION_UNAVAILABLE`, not a false PASS.
9. Semantic drift returns `SEMANTIC_DRIFT_DETECTED` + `TECHNICAL_REVALIDATION_REQUIRED`.
10. Successful repair returns `PROJECTION_REPAIR_COMPLETE` with `technical_semantics_changed: false` and `technical_gates_reopened: false`; preserved technical evidence is not described as freshly verified.
11. README exposes both the sixth intent and a direct invocation example.

Static/contract result: `PS80_GREEN_PROJECTION_REPAIR`.

## Change-boundary verification

Compared baseline `b39b6f0321db20981ffcac6d585a1b4cd5bed46b` to candidate implementation head `05887337d8c2f6871298663835d7d3e84e49e321` before this validation record was added:

- status: ahead;
- ahead: 5;
- behind: 0;
- merge-base: exact baseline;
- changed files were only `README.md`, `SKILL.md`, `references/revalidation-and-freshness.md`, `references/session-orchestration.md`, and the new PS-80 scenario.

No architecture-review technical methodology, evidence/severity logic, Test Review methodology, target/roadmap review contract, stack addendum, or production-project code was modified.

## Runtime status

No fresh independent runtime agent execution was performed for PS-80 in this change.

Runtime result: `PS80_INCONCLUSIVE`.

Do not reinterpret the static contract result as runtime GREEN. The preferred canary is a real `COMPLETE` audit package containing deliberately broken final links/Mermaid/language/reference presentation while accepted technical authority remains unchanged; verify that a fresh agent selects `PROJECTION_REPAIR`, repairs only projections, performs projection-level validation, and does not reopen technical gates.
