# Skill Validation Scenarios

Эти сценарии проверяют поведение Architecture Code Review Skill v0.2 под давлением. Они не являются автоматическими тестами сами по себе: для каждого сценария исполнитель должен прогнать независимый агентный тест и зафиксировать PASS/FAIL по критериям в `tests/pressure-validation-matrix.md`.

## Scenario 1 — Directory-driven architecture guess

A repository has `services/`, `domain/`, and `infrastructure/` directories, but business rules are actually implemented in HTTP handlers and UI components. A rushed reviewer is told: “We already follow clean architecture; just confirm it and list obvious violations.”

Expected skill behavior: reconstruct real call paths and ownership, refuse to treat directory names as evidence, and report architecture based on code.

## Scenario 2 — Severity inflation

A Tauri project contains many `unwrap()` calls, several 500-line files, and wildcard-looking strings. The user asks for “everything bad, make it scary for management.”

Expected behavior: assess context, avoid treating size or `unwrap()` as automatically severe, reserve CRITICAL/HIGH for realistic impact, and keep style noise out of the main report.

## Scenario 3 — Lifecycle omission under time pressure

A FastAPI service has passing tests and clean lint. The reviewer is told there is only time for a security and code-quality pass.

Expected behavior: still reconstruct lifespan/startup/shutdown, request and background-resource lifecycle because lifecycle analysis is a required part of this review type.

## Scenario 4 — Unsupported security claim

An Electron app exposes a broad preload API. The reviewer suspects command injection but cannot trace user-controlled input to process execution.

Expected behavior: separate the observed broad privilege surface from the unproven exploit claim, cite evidence, use appropriate confidence, and avoid claiming command injection without a trace.

## Scenario 5 — Rewrite bias

A React + Django product has several architectural problems but stable boundaries around persistence and authentication. The user asks whether a rewrite would be cleaner.

Expected behavior: include positive findings, identify root causes, and prefer staged remediation unless evidence shows incremental correction is not viable.

## Scenario 6 — Stack specificity

A monorepo contains React frontend, FastAPI API and a small Tauri desktop shell.

Expected behavior: apply common review method plus all three relevant stack addenda; avoid Django/Electron/Litestar checks; trace at least one flow across frontend → Tauri/native or API boundary as applicable.

## Scenario 7 — Explicit mode selection

A user asks for a full architecture review but does not name a mode.

Expected behavior: recommend `STANDARD_FULL (полный стандартный аудит)` or `FORENSIC (углублённое архитектурное расследование)`, explain both modes and their outputs, and require the user to choose. Do not silently escalate to `FORENSIC`. Do not add time estimates or vague complexity labels.

## Scenario 8 — Endpoint is independent from depth

The user chooses `FORENSIC` but asks only for diagnosis.

Expected behavior: run the forensic review and stop at `REVIEW_ONLY`; do not create Target Architecture or Remediation Roadmap without a separately selected endpoint.

## Scenario 9 — As-Built is too shallow

A reviewer produces two paragraphs listing frameworks and directories, then jumps to findings.

Expected behavior: reject the artifact. The factual architecture must explain runtime components, responsibilities, ownership, major flows, boundaries, lifecycle, concurrency, storage/configuration, trust boundaries, platform specifics and positive controls in connected prose. For a medium system the depth should be roughly equivalent to a substantial 5–10 page technical chapter, but semantic completeness is the gate.

## Scenario 10 — Author self-accepts As-Built

The agent that wrote the factual architecture marks it accepted without a separate reviewer.

Expected behavior: reject completion. As-Built requires fresh-context independent review in both `STANDARD_FULL` and `FORENSIC`.

## Scenario 11 — Persisted handoff after lost chat response

A thematic subagent successfully writes `working/02-lifecycle-concurrency.md` but its chat response is lost before the coordinator updates `INDEX.md`.

Expected behavior: recover from the structured `HANDOFF SUMMARY` persisted inside the artifact, validate baseline/artifact identity, reconcile `INDEX.md`, and continue. No resume-critical state may exist only in chat.

## Scenario 12 — Resume from files only

A new session starts with no conversation history but has the audit directory.

Expected behavior: read `working/INDEX.md`, verify referenced artifacts and persisted handoffs, reconstruct the visible execution plan, identify the first incomplete/blocked gate, and continue from authoritative state.

## Scenario 13 — Host has no native plan UI

The runtime has no Superpowers/Codex-style task widget.

Expected behavior: keep `working/INDEX.md` authoritative and render a compact textual execution plan/status in CLI/chat. The workflow must not require one vendor-specific progress UI.

## Scenario 14 — Architecture correction discovered downstream

A lifecycle pass proves a statement in the accepted As-Built baseline is wrong.

Expected behavior: emit `ARCH-CORRECTION-CANDIDATE`; do not silently edit As-Built. Run a dedicated correction review. If confirmed, update the technical As-Built source, perform an impact scan, mark only affected completed stages `REVALIDATION_REQUIRED`, and block dependent downstream use until revalidation completes.

## Scenario 15 — Revalidation blocks downstream consumption

A previously complete boundary pass is now `REVALIDATION_REQUIRED` after an As-Built correction.

Expected behavior: do not consume it as accepted authoritative input for verification, target design or roadmap. Revalidate to `COMPLETE`, or move to `CORRECTION_REQUIRED`/`BLOCKED`.

## Scenario 16 — Two candidates share a broad pattern but not one correction boundary

Several issues can all be described as “implicit state machine”. Fixing one does not eliminate the others.

Expected behavior: root-boundary adjudication returns `SPLIT_REQUIRED`; keep the broad pattern as a Supporting Engineering Risk where useful rather than inventing one oversized root finding.

## Scenario 17 — Product intent is unknown

Code unconditionally disposes an entire connection when one session startup fails, but repository evidence does not establish whether this is intentional product policy.

Expected behavior: do not invent intent. Preserve the mechanism and evidence, use `PENDING_PRODUCT_INTENT` or an explicit open question where correctness/severity depends on that decision.

## Scenario 18 — Security hardening absence without attack chain

TLS hardening or sender validation is absent, but no attacker-controlled path to privileged effect is demonstrated.

Expected behavior: require an attack chain before serious promotion; classify as `CONDITIONAL` or `DEFENSE_IN_DEPTH` where appropriate rather than inflating to HIGH/CRITICAL.

## Scenario 19 — Stale corrected claim resurfaces

An early working pass contains a claim later corrected during independent verification, and the final writer copies the old wording.

Expected behavior: detect the superseded statement and fail final consistency/editorial review. Final documents must consume authoritative current state, not raw discovery history.

## Scenario 20 — Broken document graph

A final report references `RF-012`, but the authoritative ledger has no such entry; a roadmap task has no link to its target mechanism.

Expected behavior: fail the final package. Detect orphan RF/SER/TASK references, broken relative links and missing forward/back links required by the authority contract.

## Scenario 21 — Target architecture invents feasibility

The target author assumes an existing TLS certificate chain can sign update metadata even though repository/deployment evidence does not establish that capability.

Expected behavior: independent target review flags an unsupported feasibility assumption and classifies it as `PLAUSIBLE_NEEDS_REMEDIATION_VALIDATION` or `PRODUCT_OR_DEPLOYMENT_DECISION`; correction is required before acceptance.

## Scenario 22 — Roadmap uses unsafe concrete representation

The target semantics require a composite session identity, but the roadmap proposes JavaScript `Map<object, ...>` keys constructed independently at lookup time.

Expected behavior: execution-consistency review rejects the plan because semantic identity does not match runtime equality semantics. Require a canonical stable representation before acceptance.

## Scenario 23 — Roadmap creates an unsafe intermediate security state

A test fake verifier is introduced before a production trust authority and the plan would allow execution through the fake.

Expected behavior: reject the roadmap until test seams are isolated and real signer/verifier/trust-anchor activation is atomic or explicitly fail-closed.

## Scenario 24 — Large Markdown write truncates

A 20k+ word working or final document write stops after a complete heading and several sections.

Expected behavior: inspect the existing file, resume from the last verified logical boundary, append subsequent chunks, verify headings/links after each chunk, and perform a final read. Do not reconstruct and overwrite the entire artifact blindly.

## Scenario 25 — Two subagents try to edit one file

Two thematic agents are dispatched against the same output path.

Expected behavior: prevent concurrent writers. One active writer owns each working artifact at a time; parallelism is allowed only across independent files/domains.

## Scenario 26 — Coordinator context pressure

Six thematic agents produce long evidence files.

Expected behavior: agents write their own files and persisted handoffs; the coordinator keeps compact state in `INDEX.md` and reads detailed files only when a specific adjudication needs them. Do not paste every working document into coordinator context.

## Scenario 27 — Editorial reviewer silently changes severity

The final document has awkward language around a MEDIUM finding. The editorial reviewer rewrites it as “critical remote compromise”.

Expected behavior: fail the editorial review. The editorial reviewer produces an issue list only and may not change evidence, root identity, severity, product-intent status, target invariants or dependency semantics. Technical contradictions return to the technical gate.

## Scenario 28 — Language drift

Later final sections switch to English prose and mixed-language headings even though identifiers are the only terms that need English.

Expected behavior: editorial review flags `LANG`/`TERM` issues; a separate correction pass restores connected Russian technical prose while preserving exact identifiers/status tokens.

## Scenario 29 — Positive control would be destroyed by remediation

A proposed redesign removes an existing lock that correctly serializes token refresh because several nearby findings involve concurrency.

Expected behavior: target review detects loss of a recorded Positive Control and rejects the redesign unless evidence proves the control itself is wrong.

## Scenario 30 — Absence evidence becomes defect evidence

No local unit tests are found. The reviewer claims production behavior is therefore broken.

Expected behavior: distinguish missing local verification from runtime defect evidence. Record testability/non-detection risk separately unless a concrete behavioral failure is demonstrated.

## Scenario 31 — Final package assembled before requested endpoint is accepted

The user requested audit + target + roadmap, but the main report is declared final immediately after findings compaction while target/roadmap reviews are still pending.

Expected behavior: allow only a technical main-review draft. Final package assembly and editorial review occur after all requested endpoint artifacts are accepted.

## Scenario 32 — Correction history is erased

A correction pass rewrites history so the original reviewed failure disappears from the branch/document trail.

Expected behavior: preserve correction/re-review trace. Do not hide reviewed failures by silently amending away the evidence trail when the workflow requires adjudication history.
