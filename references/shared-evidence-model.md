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

## 6. Product-scoped multi-source evidence

When Product mode is selected, a `WS-*` may investigate more than one Project
or an explicitly declared external source. The existing `WS-*`/`EV-*`
identities and evidence ownership are reused; Product scope does not create a
second evidence family. A Product-scoped workset and each observation record
must additionally retain:

```text
product_id: PROD-*
product_revision: <accepted revision>
product_baseline_ref: <immutable baseline vector>
project_bindings:
  - project_id
    repository_binding
    scope_selector
    exact_revision_or_content_binding
external_source_bindings: <exact locator/revision or limitation>
observed_view: DECLARED | IMPLEMENTED | CONSUMED | TESTED
conflict: <independent observations and unresolved disagreement, if any>
limitations: <availability, coverage, freshness, or source limitations>
```

Every source binding is qualified by stable Project identity and exact Product
baseline context; equal local IDs in different Projects therefore remain
distinct. External participation records the external source and provenance,
not Product ownership. The evidence writer records observations and conflicts;
the owning STM or capability gate adjudicates their meaning. A report,
summary, `INDEX.md`, or generated reverse index may route to this evidence but
cannot accept, revise, or replace it.

The Product baseline may be `COHERENT`, `MIXED_EXPLICIT`, or `UNKNOWN` as
defined by the Product context contract. That value is provenance metadata and
does not override an unavailable source, stale observation, insufficient
coverage, or a package gate. Conflicting observations remain independently
preserved until the appropriate owner emits a bounded conflict or
revalidation request; evidence does not auto-resolve by precedence.
