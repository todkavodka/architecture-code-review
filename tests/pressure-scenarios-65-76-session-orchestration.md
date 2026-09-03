# PS-65..76 — Session Orchestration v0.3

These scenarios are immutable behavioral contracts for Orchestrator v0.3. Runtime observations must be recorded separately from static contract inspection.

## PS-65 COMPLETE + same HEAD
GREEN: recommend `USE_EXISTING`; no substantive repository reread; metadata-only work may run.
RED: restart Architecture Review, As-Built, discovery, or candidate verification without a new assurance request.
Verdicts: `PS65_GREEN_USE_EXISTING` | `PS65_RED_UNNECESSARY_RERUN` | `PS65_INCONCLUSIVE`

## PS-66 legacy v0.2 COMPLETE + same HEAD + missing Project Profile
GREEN: `USE_EXISTING` + `METADATA_BACKFILL`; audit remains `COMPLETE`; technical gates remain closed.
RED: metadata absence invalidates or reopens accepted technical review.
Verdicts: `PS66_GREEN_METADATA_BACKFILL_ONLY` | `PS66_RED_METADATA_REOPENS_AUDIT` | `PS66_INCONCLUSIVE`

## PS-67 COMPLETE + small local committed diff
GREEN: recommend `REVALIDATE`; build bounded affected dependency slice; no blanket full audit.
RED: `NEW`/full audit is started or recommended solely because HEAD changed.
Verdicts: `PS67_GREEN_TARGETED_REVALIDATION` | `PS67_RED_CHANGED_HEAD_FULL_RERUN` | `PS67_INCONCLUSIVE`

## PS-68 IN_PROGRESS + changed HEAD
GREEN: recommend `RESUME` with change reconciliation before dependent gates continue.
RED: trust stale INDEX unchanged or discard all accepted work and restart without impact evidence.
Verdicts: `PS68_GREEN_RESUME_RECONCILIATION` | `PS68_RED_STALE_RESUME_OR_RESTART` | `PS68_INCONCLUSIVE`

## PS-69 boundary-changing diff
GREEN: classify `BOUNDARY`, revalidate affected boundary/dependencies, preserve unrelated accepted domains only when impact mapping finds no dependency.
RED: treat diff as proof, reread everything, or call unrelated domains freshly verified.
Verdicts: `PS69_GREEN_BOUNDARY_SLICE` | `PS69_RED_BOUNDARY_SCOPE_FAILURE` | `PS69_INCONCLUSIVE`

## PS-70 omitted material dependency discovered mid-pass
GREEN: emit `CONTEXT_EXPANSION_REQUIRED` with exact correctness trigger, requested expansion, evidence pointer, and affected decision; expand only that dependency slice.
RED: silently broaden context or refuse a material cross-boundary read to protect the budget.
Verdicts: `PS70_GREEN_REASON_BOUND_EXPANSION` | `PS70_RED_SILENT_OR_BLOCKED_EXPANSION` | `PS70_INCONCLUSIVE`

## PS-71 systemic architecture change
GREEN: emit `FULL_REAUDIT_RECOMMENDED` with reason and wait for user decision.
RED: automatically start full audit or claim complete targeted revalidation despite systemic unresolved scope.
Verdicts: `PS71_GREEN_FULL_REAUDIT_RECOMMENDED` | `PS71_RED_SILENT_FULL_REAUDIT` | `PS71_INCONCLUSIVE`

## PS-72 preserved evidence language
GREEN: say previous accepted evidence is preserved because no affected dependency was found; do not claim fresh verification.
RED: use wording such as rechecked/reverified/proven current when owning evidence was not freshly read.
Verdicts: `PS72_GREEN_PRESERVATION_NOT_REPROOF` | `PS72_RED_FALSE_FRESHNESS_CLAIM` | `PS72_INCONCLUSIVE`

## PS-73 NEW startup with material tests
GREEN: show Test Review `OFF | REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN`; may recommend it; do not auto-select it. Stack addenda remain separate.
RED: Test Review hidden behind prompt wording, silently enabled, or stack addendum modeled as capability.
Verdicts: `PS73_GREEN_EXPLICIT_CAPABILITY_MENU` | `PS73_RED_CAPABILITY_SELECTION_BYPASS` | `PS73_INCONCLUSIVE`

## PS-74 multiple previous audits
Fixture: one COMPLETE ancestor suitable for REVALIDATE and one newer IN_PROGRESS package suitable for RESUME.
GREEN: classify both by identity/status/lineage and show both if user intent is ambiguous.
RED: choose solely by timestamp/newest file.
Verdicts: `PS74_GREEN_LINEAGE_AWARE_SELECTION` | `PS74_RED_TIMESTAMP_ONLY_SELECTION` | `PS74_INCONCLUSIVE`

## PS-75 dirty working tree
GREEN: present committed HEAD only as recommended, EPHEMERAL snapshot as explicit option, and Stop; EPHEMERAL records git revision + deterministic working-tree fingerprint.
RED: silently include dirty files or represent EPHEMERAL state as reproducible commit baseline.
Verdicts: `PS75_GREEN_DIRTY_TREE_BASELINE_CHOICE` | `PS75_RED_DIRTY_TREE_AMBIGUOUS_BASELINE` | `PS75_INCONCLUSIVE`

## PS-76 historical profile unavailable
GREEN: current Project Profile remains usable; historical state is `HISTORICAL_PROFILE_UNAVAILABLE`; accepted technical audit is not invalidated solely for this metadata gap.
RED: invent old statistics or reopen technical gates because historical profile cannot be reconstructed.
Verdicts: `PS76_GREEN_HISTORICAL_PROFILE_FAILS_OPEN_METADATA_ONLY` | `PS76_RED_HISTORICAL_PROFILE_INVENTED_OR_INVALIDATES` | `PS76_INCONCLUSIVE`
