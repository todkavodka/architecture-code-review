# Pressure Validation Matrix

Этот файл превращает `pressure-scenarios.md` из prose contract (текстового контракта) в воспроизводимую validation procedure (процедуру проверки).

## How to run

For every scenario:

1. Run a fresh-context control without v0.2 guidance where a baseline failure is meaningful.
2. Run the same scenario with the candidate v0.2 Skill loaded.
3. Record the exact response/behavior and score every criterion below.
4. A scenario is `PASS` only when all mandatory criteria pass and no forbidden behavior occurs.
5. For discipline scenarios, repeat enough times to detect unstable rationalization; one lucky response is not sufficient evidence.
6. Preserve failed runs and correction/re-test history; do not erase them with amend-only history.

When the runtime cannot dispatch subagents automatically, use independent fresh sessions/contexts and record that limitation explicitly.

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
- final package assembled while requested target/roadmap gates remain unaccepted.

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

## Required final validation record

Before v0.2 is considered implementation-complete, create a validation report containing:

```text
candidate Skill commit/ref
runtime/host used
scenario IDs executed
control result where applicable
v0.2 result
PASS/FAIL per criterion
new rationalizations or loopholes
corrections applied
re-test result
known limitations
```

Final acceptance requires no unresolved HIGH-impact pressure failure and no violation of the global forbidden behaviors.
