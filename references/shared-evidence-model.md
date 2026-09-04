# Shared Evidence Model

This reference owns the shared, baseline-bound evidence layer for the review
suite. It captures bounded observations from repository and external sources so
the Shared Technical Model (STM) and capabilities can reuse provenance without
duplicating it. Baseline selection remains owned by
[Session Orchestration](session-orchestration.md); evidence strength, candidate
lifecycle, and severity remain owned by
[Evidence and severity](evidence-and-severity.md).

## 1. Ownership boundary

```text
WS-* = bounded investigation/workset and physical evidence grouping
EV-* = logical addressable observation within a WS
```

`WS-*` and `EV-*` are shared cross-capability evidence records. An evidence
record is an observation, not a finding, technical fact, Behavior Contract,
assurance target, gap, recommendation, or verdict. Semantic artifacts retain
ownership of every conclusion they derive from evidence.

## 2. Worksets

A `WS-*` is one bounded investigation and the physical grouping of its evidence
records. It is suitable for a focused agent pass and review; it is not a
product-behavior or capability-semantic authority.

Each workset records at least:

```text
id: WS-*
name
scope
baseline
baseline_type
status
investigated_sources
limitations
EV records
HANDOFF SUMMARY
```

`baseline` identifies the source revision or other selected baseline and
`baseline_type` identifies how that baseline was selected. `status` follows the
shared workflow vocabulary in [Review modes and orchestration](review-modes-and-orchestration.md).
`investigated_sources` identifies what was actually examined; `limitations`
identifies unavailable, incomplete, or otherwise bounded evidence.

One workset has one active writer. Write the complete workset, verify its
required content, and persist its `HANDOFF SUMMARY` before a coordinator uses
it for resume or routing, following the handoff discipline in
[Review modes and orchestration](review-modes-and-orchestration.md). A
capability may add a new shared workset when it gathers new reusable evidence;
that does not transfer ownership of capability-specific conclusions.

## 3. Evidence observations

An `EV-*` is a logical, globally addressable observation within a workset. Refer
to it as `WS-###-name#EV-###`; it may live in the workset file rather than in a
separate physical Markdown file.

Each `EV-*` records at least:

```text
id: EV-*
source_type
repository/path or external locator
symbol or range, when available
baseline binding
observed fact/behavior
optional short excerpt, only when useful
```

The observation states only what the cited source shows at its bound baseline.
Use a short excerpt only to disambiguate the observation; do not copy large
source blocks into evidence. The raw repository or external source remains the
ultimate source and must be reopened when the available evidence is
insufficient, disputed, or stale for the decision being made.

## 4. Historical binding

An `EV-*` remains evidence of the baseline at which it was observed. When a new
baseline needs evidence, create new observations as needed; do not rewrite old
observations to make historical evidence look current. Freshness and impact
decisions are governed by [Revalidation and compact-state freshness](revalidation-and-freshness.md),
not by silently changing the earlier record.

## 5. Shared reuse and reading order

Consumers use the smallest sufficient context in this order:

```text
INDEX
-> semantic artifact
-> WS#EV
-> raw source
```

The semantic artifact explains the consumer-owned fact or conclusion and
references `WS#EV` for its observation. It does not turn an `EV-*` into
semantic authority. Reuse the same addressable evidence across STM and
capabilities instead of creating architecture or test evidence silos for the
same observation. The cross-capability invariant is also recorded in
[Shared assurance principles](shared-assurance-principles.md).
