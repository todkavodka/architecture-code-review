# Pressure Scenario 33 — Native plan synchronization

This regression scenario covers a host that exposes a native Todo/task/plan UI while the Architecture Code Review Skill also maintains `working/INDEX.md` as the persistent workflow authority.

## RED evidence

Observed during a real OpenCode review run against an unrelated repository:

- `working/INDEX.md` and the actual coordinator workflow advanced through thematic discovery into independent falsification verification;
- five verifier agents completed their candidate-verification work;
- the native OpenCode Todo sidebar still showed earlier stages as pending and therefore no longer represented the actual workflow state;
- an explicit instruction to invoke OpenCode's native todo tool succeeded immediately, proving that the native tool was available and functional in that runtime.

Baseline result: `RED_CONFIRMED`.

The failure is specifically that the Skill's previous wording allowed the coordinator to interpret "mirror/synchronize the plan" without actually invoking the available native todo tool. It does not imply that `working/INDEX.md` or the underlying review orchestration is incorrect.

## Scenario

The host provides a native Todo/task/plan tool and UI.

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
3. when a native todo/task/plan tool is available, **actually invoke that tool** to create/update the visible projection — prose claims or `INDEX.md` edits alone do not count;
4. invoke the native tool after every material coordinator state transition, after first persisting the authoritative state;
5. invoke it after a completed subagent batch once handoffs/artifacts have been validated and `INDEX.md` has been updated;
6. on session resume, reconstruct true state from `INDEX.md` and invoke the native tool before continuing;
7. never restart accepted work merely because the native UI is stale;
8. not require UI updates for microscopic tool calls or intermediate internal thoughts.

If the runtime exposes a specific tool name such as `todowrite`, use that available runtime tool. The Skill must remain vendor-neutral in its contract; the behavioral requirement is a real tool invocation.

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

- evidence shows a real native todo/task/plan tool invocation when such a tool is available;
- the native plan is brought back into agreement with `working/INDEX.md` after material coordinator transitions;
- after a subagent batch, the native tool is called only after persisted results are validated and `INDEX.md` is authoritative;
- resume invokes the native tool using state reconstructed from `INDEX.md` rather than trusting stale UI;
- completed work is not re-run because of display drift;
- hosts without native plan UI still use the existing text fallback.

## FAIL criteria

Any of the following is a failure:

- the agent says the plan was synchronized but never invokes the available native todo/task/plan tool;
- native plan is initialized once and then allowed to remain stale for multiple material phases;
- native UI is treated as authority over `working/INDEX.md`;
- stale UI causes already accepted stages to be restarted;
- the Skill invokes the native UI tool before persisted artifacts/handoffs and `INDEX.md` establish the new state;
- synchronization is attempted after every microscopic tool action, creating noisy or unstable progress behavior.
