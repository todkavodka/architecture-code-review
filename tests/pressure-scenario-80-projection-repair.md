# PS-80 — Projection Repair Session Intent

This scenario is the behavioral contract for repairing final/user-facing review artifacts without reopening accepted technical semantics.

## Observed RED baseline

Baseline: `main@b39b6f0321db20981ffcac6d585a1b4cd5bed46b`.

The repository already had `PROJECTION_REVALIDATION` for an editorial correction loop, but startup/session orchestration persisted exactly five intents:

```text
USE_EXISTING | NEW | RESUME | REVALIDATE | EXTEND
```

A user returning to a `COMPLETE` audit solely to fix poor final-document presentation therefore had no first-class Session Intent. They had to phrase an ad-hoc prompt or risk being routed into `USE_EXISTING`, `REVALIDATE`, or a new editorial pass without an explicit projection-only scope.

Baseline verdict: `PS80_RED_NO_PROJECTION_REPAIR_INTENT`.

## Fixture

A repository has an accepted `COMPLETE` architecture review at the same committed baseline. Accepted technical authority, findings, severity, target architecture, and roadmap semantics are unchanged.

The final package contains presentation defects such as:

- broken relative links;
- invalid Mermaid syntax while the intended mechanism is unambiguous from accepted authority;
- duplicated or stale presentation text that is already superseded by accepted authority;
- mixed-language or scratchpad-like prose;
- inconsistent headings, navigation, tables, or terminology;
- malformed references to accepted RF/SER/TASK identifiers.

The user asks to repair only these final documents and explicitly does not want a technical re-audit.

## GREEN contract

Startup offers/selects a first-class persisted Session Intent:

```text
PROJECTION_REPAIR
```

Its semantics are:

1. It is valid only when there is reusable accepted technical authority for the selected audit package.
2. It repairs presentation/projection artifacts only: prose, links, headings, navigation, tables, terminology, Mermaid syntax/renderability, duplicate/stale presentation, and reference consistency.
3. It preserves accepted evidence, root identity/boundary, severity/exploitability, owners, invariants, product-intent status, target mechanisms, roadmap prerequisites/dependencies/gates, and security assumptions.
4. It starts from the minimum accepted authority refs needed to constrain the changed projection; it does not perform blanket source-repository rereads.
5. It uses the existing `PROJECTION_REVALIDATION` correction/re-review contract for each changed projection.
6. It performs projection-level verification appropriate to the changed artifacts: relative-link/reference consistency, Markdown structure, terminology/language, Mermaid validation/renderability when tooling is available, and cross-document status/identifier consistency.
7. It records changed artifacts/sections and the accepted authority refs used to constrain them.
8. If a requested fix cannot be completed without changing accepted technical semantics, the projection writer stops rather than rationalizing the change and returns:

```text
SEMANTIC_DRIFT_DETECTED
TECHNICAL_REVALIDATION_REQUIRED
```

9. Successful projection repair does not relabel preserved technical evidence as freshly verified and does not change the project baseline merely because documentation changed.
10. `NEW`, `REVALIDATE`, and `EXTEND` remain separate intents: projection repair is not a project-change audit, not a new assurance scope, and not a full rerun.

## Startup routing expectations

For `COMPLETE` + same committed baseline:

- default recommendation remains `USE_EXISTING` when the user merely wants to consume the accepted audit;
- when the user explicitly asks to fix final documents/presentation, recommend `PROJECTION_REPAIR`;
- when known projection defects are detected during package usability checks and the user wants them corrected, `PROJECTION_REPAIR` is available as the bounded repair path.

For `COMPLETE` + changed committed baseline, project-change freshness remains a `REVALIDATE` concern. Do not use `PROJECTION_REPAIR` to hide source changes.

## Failure conditions

RED if any of these occurs:

- no first-class `PROJECTION_REPAIR` Session Intent exists;
- projection repair silently runs technical discovery, candidate verification, severity/root adjudication, or full As-Built revalidation without a semantic trigger;
- final prose/table/diagram changes technical meaning to make documents internally consistent;
- accepted findings/severity/target/roadmap semantics are edited as part of presentation cleanup;
- broken links/Mermaid/language issues are fixed without projection-level revalidation;
- changed project source is ignored because the user selected projection repair;
- projection repair is treated as equivalent to `REVALIDATE` or `EXTEND`;
- preserved technical authority is described as freshly verified.

Verdicts:

`PS80_GREEN_PROJECTION_REPAIR` | `PS80_RED_NO_PROJECTION_REPAIR_INTENT` | `PS80_RED_SEMANTIC_DRIFT` | `PS80_INCONCLUSIVE`
