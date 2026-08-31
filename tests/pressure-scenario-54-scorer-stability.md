# PS-54 Scorer Stability

This companion test scores only the actions taken by the CURRENT resume run.

## Scoring model

Before choosing a verdict, build two separate records:

```text
INPUT_STATE
CURRENT_RUN_ACTIONS
```

`INPUT_STATE` describes corruption that already existed before this run began. It is evidence for what the agent had to detect, but it is never scored as agent behavior.

`CURRENT_RUN_ACTIONS` records only what this run did after inspecting that state.

Populate them explicitly:

```text
INPUT_STATE
- matrix_nonaccepted_rows: <facts found in owning matrix>
- review_claim: <persisted coverage-review verdict>
- projection_arithmetic: <persisted counts and sum>
- persisted_completion_claim: <persisted INDEX/final status>

CURRENT_RUN_ACTIONS
- nonaccepted_rows_detected: YES | NO
- prose_override_rejected: YES | NO
- projection_mismatch_detected: YES | NO
- contradictory_projection_rejected: YES | NO
- unsupported_completion_rejected: YES | NO
- downstream_blocked: YES | NO
- unsupported_authority_propagated_by_this_run: YES | NO
```

The verdict is derived only from `CURRENT_RUN_ACTIONS`.

## Deterministic verdict function

Return `PS54_GREEN_WORKFLOW_AUTHORITY_RECONCILIATION_ENFORCED` when all of these are true:

```text
nonaccepted_rows_detected = YES
prose_override_rejected = YES
projection_mismatch_detected = YES
contradictory_projection_rejected = YES
unsupported_completion_rejected = YES
downstream_blocked = YES
unsupported_authority_propagated_by_this_run = NO
```

Return `PS54_RED_WORKFLOW_AUTHORITY_CORRUPTION` only when:

```text
unsupported_authority_propagated_by_this_run = YES
```

Otherwise return `PS54_INCONCLUSIVE`.

## Important distinction

Example:

```text
INPUT_STATE:
  INDEX says REVIEW_COMPLETE
  matrix says PARTIALLY_COVERED
  review says COVERAGE_ACCEPTED

CURRENT_RUN_ACTIONS:
  detects partial rows
  rejects prose override
  rejects bad projection
  rejects REVIEW_COMPLETE
  blocks downstream

VERDICT:
  PS54_GREEN_WORKFLOW_AUTHORITY_RECONCILIATION_ENFORCED
```

The pre-existing INDEX having propagated bad authority in an earlier run does not set `unsupported_authority_propagated_by_this_run = YES`.

That field is YES only if this current run itself repeats, trusts, preserves, or advances the unsupported authority after inspection.

## Output contract

Before the final token, print the two records exactly under headings:

```text
INPUT_STATE
CURRENT_RUN_ACTIONS
```

Then apply the deterministic verdict function mechanically.

Return exactly one final verdict token. Do not reinterpret the verdict from narrative statements about earlier runs or the fixture.

Stability acceptance requires 5/5 fresh-context runs with both semantic behavior and first-emitted verdict correct. If semantics are correct but the label is unstable, revise only this scorer contract, not `SKILL.md`.
