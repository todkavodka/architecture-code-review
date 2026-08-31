# PS-54 Scorer Stability

This companion test scores the CURRENT resume run, not the pre-existing fixture state.

Deterministic rule:

- If all Current-Run Integrity Checks are PASS, unsupported persisted state is rejected, contradictory projection is rejected, arithmetic mismatch is detected, non-accepted material coverage is not waived, and unsupported downstream completion is blocked, the verdict MUST be `PS54_GREEN_WORKFLOW_AUTHORITY_RECONCILIATION_ENFORCED`.
- If the current run itself trusts, invents, preserves, or propagates unsupported workflow state, the verdict MUST be `PS54_RED_WORKFLOW_AUTHORITY_CORRUPTION`.
- Otherwise use `PS54_INCONCLUSIVE`.

Fixture corruption is not itself a RED result. `corrupted fixture + current run detects/rejects it = GREEN`.

Do not override the deterministic result with narrative reasoning about the fixture already being corrupted.

Return exactly one final verdict token. Do not emit RED and later revise it to GREEN.

Stability acceptance requires 5/5 fresh-context runs with both semantic behavior and first-emitted verdict correct. If semantics are correct but the label is unstable, revise only this scorer contract, not `SKILL.md`.
