# PS-117 — Smell or metric is not automatically a finding

## Observed RED baseline

At the approved pre-implementation baseline, there is no Code Quality
capability or `CQ-*` semantic contract. Existing review guidance treats file
length, warnings, literals, and similar signals as insufficient without
concrete impact, but provides no Code Quality finding authority or materiality
adjudication for these signals.

Observed verdict: `PS117_PASS_AS_RED`

## Setup / input state

A selected function is large and has a high complexity metric. A linter also
reports a warning, but no material consequence or evidence-backed risk is
provided.

## Required semantic behavior

The mechanical observations may produce transient candidate evidence, but must
not become an accepted `CQ-*` finding without evidence and materiality
adjudication.

## Forbidden behavior

- treating a metric, warning, line count, or smell label as semantic authority;
- creating a persistent finding from the signal alone;
- assigning severity from warning count or size alone.

## Expected post-implementation invariant

`tool warning != accepted CQ finding` and `metric/smell != finding` without
material consequence.

## Verdict vocabulary

`PS117_PASS_AS_RED`
`PS117_GREEN_SIGNAL_REJECTED_WITHOUT_MATERIALITY`
