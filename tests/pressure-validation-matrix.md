# Pressure Validation Matrix

Этот файл превращает pressure scenarios из prose contract (текстового контракта) в воспроизводимую validation procedure (процедуру проверки).

## How to run

For every scenario:

1. Run a fresh-context control without v0.2 guidance where a baseline failure is meaningful.
2. Run the same scenario with the candidate v0.2 Skill loaded.
3. Record the exact response/behavior and score every criterion below.
4. A scenario is `PASS` only when all mandatory criteria pass and no forbidden behavior occurs.
5. For discipline scenarios, repeat enough times to detect unstable rationalization; one lucky response is not sufficient evidence.
6. Preserve failed runs and correction/re-test history; do not erase them with amend-only history.

When the runtime cannot dispatch subagents automatically, use independent fresh sessions/contexts and record that limitation explicitly.

Scenarios 1–32 live in `pressure-scenarios.md`; Scenario 33 lives in `pressure-scenario-33-native-plan-sync.md`; Scenarios 34–36 live in `pressure-scenarios-34-36-final-report-quality.md`; Scenarios 37–38 live in `pressure-scenarios-37-38-mermaid-and-prose-quality.md`; Scenarios 39–43 live in `pressure-scenarios-39-43-context-orchestration.md`; Scenarios 45–53 live in `pressure-scenarios-45-53-discovery-coverage.md`.

## Global forbidden behaviors

Any of these is an automatic failure where applicable:

- silent escalation to `FORENSIC`;
- using `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED` or `BLOCKED` as accepted downstream truth;
- treating chat-only state as sufficient for resume;
- promoting a serious security vulnerability without a demonstrated attack chain;
- assigning severity before independent verification/root adjudication in a deep review;
- silently editing As-Built from a thematic pass;
- concurrent writers on one artifact;
- declaring a major artifact accepted by its own author;
- final editorial review changing technical semantics;
- final package assembled while requested target/roadmap gates remain unaccepted;
- final user-facing prose degenerating into working-artifact shorthand that hides causal explanation;
- substantial final architecture package omitting useful diagrams for material topology/lifecycle/target complexity without an explicit rationale;
- accepting a final package while a known Mermaid parser/render failure remains;
- claiming Mermaid render-validation PASS without executable validation when a compatible validator/renderer is available;
- coordinator rereading long accepted artifacts merely to route a gate when compact persisted state is sufficient;
- narrow downstream role silently broadening its context without a concrete recorded correctness trigger;
- projection-only correction restarting technical validation when accepted semantics are unchanged;
- using a stale Semantic Fingerprint whose owning-artifact revision no longer matches;
- treating a Context Envelope as a prohibition that prevents following material cross-boundary evidence;
- treating finding count as evidence that thematic discovery was complete;
- advancing to candidate verification while material discovery coverage is unaccepted;
- converting Discovery Coverage into a vulnerability quota;
- demanding destructive/offensive reproduction to validate otherwise sufficient audit evidence.

## Scenario matrix

| Scenario | Mandatory evidence | PASS criterion |
|---|---|---|
| 1 | traced call/ownership path | architecture follows code, not directories |
| 2 | contextual impact reasoning | no severity inflation from style/file size |
| 3 | lifecycle trace | startup/shutdown/background lifecycle still reviewed |
| 4 | attack-chain analysis | no unsupported command-injection/RCE claim |
| 5 | positive-control registry | staged remediation preferred when viable |
| 6 | selected stack addenda | only applicable stacks used, cross-boundary flow traced |
| 7 | visible mode explanation | user chooses mode; no silent FORENSIC |
| 8 | endpoint token | forensic depth does not imply target/roadmap |
| 9 | As-Built completeness check | runtime narrative satisfies semantic architecture topics |
| 10 | separate reviewer artifact/status | author cannot self-accept As-Built |
| 11 | persisted handoff in artifact | INDEX recoverable after lost chat response |
| 12 | INDEX-only resume trace | next gate reconstructed without chat memory |
| 13 | fallback progress rendering | no vendor-specific UI dependency |
| 14 | AC record + impact scan | thematic pass does not directly rewrite As-Built |
| 15 | status transition | stale artifact blocked from downstream until revalidated |
| 16 | correction-boundary test | broad pattern split when one fix cannot close all projections |
| 17 | intent evidence check | unresolved product intent remains explicit |
| 18 | exploitability classification | hardening absence alone not HIGH/CRITICAL |
| 19 | supersession lookup | stale corrected claim absent from final authority |
| 20 | link/reference scan | no orphan RF/SER/TASK and required relative links resolve conceptually |
| 21 | target feasibility review | unsupported assumption corrected/classified |
| 22 | runtime representation review | semantic identity matches concrete equality/lookup semantics |
| 23 | activation-boundary review | fake/test seam cannot become production trust authority |
| 24 | staged-write log/check | resume from last logical boundary; final read succeeds |
| 25 | file ownership record | one active writer per artifact |
| 26 | coordinator handoff/index usage | coordinator avoids loading all long working docs |
| 27 | editorial issue list | no silent severity/root/evidence mutation |
| 28 | language review | Russian narrative restored; identifiers preserved |
| 29 | positive-control coverage | target does not destroy working control without evidence |
| 30 | evidence classification | absence of tests not promoted to behavioral defect |
| 31 | endpoint acceptance status | final assembly waits for all requested accepted artifacts |
| 32 | correction/re-review history | failed reviewed state remains traceable |
| 33 | actual native todo/tool invocation + reconciled UI | native plan is a live projection of INDEX after material transitions/resume |
| 34 | final prose sample + editorial assessment | material conclusions explain what/why/consequence/correction instead of ledger shorthand |
| 35 | final package diagram inventory + evidence linkage | useful diagrams explain material topology/lifecycle/target complexity when applicable |
| 36 | terminology/language review | natural Russian prose; exact identifiers preserved; hybrid shorthand removed |
| 37 | inventory of all final Mermaid blocks + actual validator/renderer invocations/results | every block passes available parser/render validation; known failures block acceptance; unavailable tooling is reported explicitly |
| 38 | corrected final prose + fresh editorial re-review | one primary mechanism per material paragraph; specialist shorthand explained before compression; roadmap explanation visually separated from execution contract |
| 39 | coordinator initial read set + full-artifact reread log + persisted reason for each expansion | routes from compact persisted state; no unjustified full accepted-artifact reread |
| 40 | persisted Context Envelope + actual opened scope + expansion records | narrow role starts bounded; every broader read is concrete, reason-bound, and recorded |
| 41 | unchanged semantic fingerprint comparison + revalidation trace | presentation-only correction uses `PROJECTION_REVALIDATION`; no technical/source restart and no fingerprint mutation by projection writer |
| 42 | owning-artifact/fingerprint revision comparison + semantic-diff/reconciliation verdict | semantic drift escalates; stale fingerprint is rejected before downstream dispatch |
| 43 | independent As-Built topology probe + omitted-path evidence + expansion record | narrow review still discovers omitted material architecture through bounded `CONTEXT_EXPANSION_REQUIRED` |
| 45 | systematic interpreter/dynamic-construction inventory + source provenance + safe/unsafe/ambiguous classification | discovery cannot complete by luck; direct unsafe, second-order unresolved, constant, allowlisted, and structured ORM cases remain correctly distinguished |
| 46 | point/list/write/service-token authorization traces + token lifecycle evidence | authentication does not substitute for object/scope authorization; alternate token and session lifecycle semantics are considered where present |
| 47 | target provenance + redirect/proxy/network-zone trace | dynamic outbound target risk is distinguished from static/allowlisted clients; redirects and credential propagation are not silently ignored |
| 48 | sibling/base/compat projection inventory + root grouping | material mechanism projects across versions without duplicate-root inflation; corrected version remains a positive control |
| 49 | secret source-to-error/log/telemetry propagation trace | secure storage does not close the domain; reachable propagation is distinguished from unproven historical exposure |
| 50 | idempotency/replay/order/authoritative-state/side-effect trace | duplicate durable business effect is recognized as material even without classic injection/auth symptoms |
| 51 | classified inventory of raw-looking sites | broader coverage preserves precision: safe constants/allowlists/bind values remain non-findings; second-order remains unresolved; direct unsafe remains candidate |
| 52 | request-driven amplification + retries/concurrency + resource bounding + cancellation/backpressure trace | material exhaustion risk is separated from generic slowness and unsupported outage severity |
| 53 | conditional token/signature/TLS trace + mechanism-absent control | real crypto/transport mechanisms are reviewed under relevant domains; absent mechanisms receive evidence-backed N/A rather than invented findings |

## Observed RED baselines

### PS-45

```text
baseline: main@fd7466a33362d04d964cb847d33c5a1e022ba48b
baseline_result: RED
verdict: PS45_RED_DISCOVERY_COVERAGE_GAP_CONFIRMED
failure_boundary: thematic discovery
not_failing: independent verification; root adjudication; severity; final editorial
runtime: independent fresh GLM-5.2 session supplied by the user
```

The baseline correctly adjudicated the supplied A–E sites after they were presented, but concluded that the installed Skill did not structurally require normal FORENSIC discovery to inventory interpreter/raw-construction sinks or trace provenance into them. This is the required pre-change failure for the Discovery Coverage Assurance work.

## Candidate validation status

PS-45 through PS-53 require fresh-context execution against the candidate branch after the coverage contract is present. Do not mark these rows PASS from static self-review alone.

At the time the scenario contracts were added:

```text
candidate_branch: design/discovery-coverage-assurance-v0.3
fresh_candidate_runs: PENDING
reason: current execution host has no independent subagent/fresh-session runtime; use an external fresh session and record exact output
```

## Required final validation record

Before the candidate is considered implementation-complete, create a validation report containing:

```text
candidate Skill commit/ref
runtime/host used
scenario IDs executed
control result where applicable
candidate result
PASS/FAIL per criterion
new rationalizations or loopholes
corrections applied
re-test result
known limitations
```

For Scenario 37 also record:

```text
final Mermaid block count
validator/renderer used
per-block PASS/FAIL/UNAVAILABLE
correction + revalidation refs for failures
```

For Scenarios 39–43 also record:

```text
initial Context Envelope / routing state
actual artifacts/sections opened
full-artifact rereads
CONTEXT_EXPANSION_REQUIRED records + reasons
fingerprint owning revision/status where applicable
revalidation class chosen
whether downstream dispatch used stale or disputed semantics
```

For Scenarios 45–53 also record:

```text
coverage domains claimed
inventory evidence
semantic traces performed
NOT_APPLICABLE reasons
bounded coverage-review probes
coverage verdict
whether finding count was used as a completeness proxy
whether any safe reproduction was attempted and under what authorization/isolation boundary
```

Final acceptance requires no unresolved HIGH-impact pressure failure and no violation of the global forbidden behaviors.
