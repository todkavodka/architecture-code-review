# PS-145 — Product conflicting evidence

## Input state

Project A evidence says an API supports v2, Project B consumer evidence
assumes v1, an external contract declares v1–v2, and runtime evidence shows
v1 only. The Product baseline and selector snapshot are exact.

## Expected semantic behavior

The conflict remains independently preserved in the qualified WS/EV and STM
inputs. Product projections and packages bind the exact selector/baseline
snapshot and expose the limitation until the owning capability or STM gate
adjudicates it.

## Forbidden behavior

- resolving conflict by report order or matrix precedence;
- letting Technical Documentation adjudicate STM facts;
- accepting a stale projection as authority;
- silently broadening the Product selector.

## Affected authority

Shared Evidence preserves observations; the Technical Model Gate owns factual
resolution; Test Engineering and Architecture Review own their respective
interpretations.

## Expected impact scope

The conflicting qualified API slice and dependent Product outputs only; local
facts without that dependency remain preserved.

## Package/projection outcome

Affected required projections or package members are limited or blocked by
their existing gates; unrelated selected outputs remain independent.

## Verdict

`PS145_PASS_CONFLICT_PRESERVED`
