# Pressure Scenario 33 — Native plan synchronization

This regression scenario covers a host that exposes a native Todo/task/plan UI while the Architecture Code Review Skill also maintains `working/INDEX.md` as the persistent workflow authority.

## RED evidence

Observed during a real OpenCode review run against an unrelated repository:

- `working/INDEX.md` and the actual coordinator workflow advanced through thematic discovery into independent falsification verification;
- five verifier agents completed their candidate-verification work;
- the native OpenCode Todo sidebar still showed earlier stages as pending and therefore no longer represented the actual workflow state.

Baseline result: `RED_CONFIRMED`.

The failure is specifically a stale native-plan projection. It does not imply that `working/INDEX.md` or the underlying review orchestration is incorrect.

## Scenario

The host provides a native Todo/task/plan UI.

The review begins with the native plan showing the same coarse stages as `working/INDEX.md`. The coordinator then progresses through material state transitions such as:

```text
As-Built COMPLETE
→ thematic discovery COMPLETE
→ independent verification IN_PROGRESS
```

A batch of subagents finishes and the coordinator validates their persisted handoffs, updates the corresponding artifacts, and advances `working/INDEX.md`.

The native plan still shows the original earlier stages as `PENDING`.

## Expected behavior

The Skill must:

1. treat `working/INDEX.md` as the only persistent workflow authority;
2. treat native Todo/task/plan UI as a non-authoritative projection of that state;
3. synchronize the native projection after every material coordinator state transition;
4. synchronize after a completed subagent batch once handoffs/artifacts have been validated and `INDEX.md` has been updated;
5. on session resume, reconstruct true state from `INDEX.md` and reconcile a stale native plan before continuing;
6. never restart accepted work merely because the native UI is stale;
7. not require UI updates for microscopic tool calls or intermediate internal thoughts.

## Material synchronization points

At minimum, reconciliation is required when a tracked stage changes among states such as:

```text
PENDING
IN_PROGRESS
ARTIFACT_WRITTEN
REVIEW_REQUIRED
CORRECTION_REQUIRED
REVALIDATION_REQUIRED
BLOCKED
COMPLETE
NOT_APPLICABLE
```

and when the coordinator changes the active top-level phase.

## PASS criteria

`PASS` requires all of the following:

- the native plan is brought back into agreement with `working/INDEX.md` after material coordinator transitions;
- after a subagent batch, the native UI is updated only after persisted results are validated and `INDEX.md` is authoritative;
- resume reconciles stale native UI from `INDEX.md` rather than trusting the UI;
- completed work is not re-run because of display drift;
- hosts without native plan UI still use the existing text fallback.

## FAIL criteria

Any of the following is a failure:

- native plan is initialized once and then allowed to remain stale for multiple material phases;
- native UI is treated as authority over `working/INDEX.md`;
- stale UI causes already accepted stages to be restarted;
- the Skill updates the native UI before persisted artifacts/handoffs and `INDEX.md` establish the new state;
- synchronization is attempted after every microscopic tool action, creating noisy or unstable progress behavior.
