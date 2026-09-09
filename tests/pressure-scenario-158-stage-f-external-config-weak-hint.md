# PS-158 — Stage F external configuration weak hint

## Design mapping

`PS-F05`: external base configuration without call evidence remains a weak hint,
not an accepted call.

## Setup / evidence shape

A configuration contains a synthetic base URL such as
`https://api.example.invalid`. No route, client invocation, runtime trace, or
declaration establishes a concrete call. The observation is classified
`WEAK_HINT` and records its source and limitation.

## Expected accepted semantic records

The Technical Model Gate may retain a bounded external identity or unresolved
observation with the evidence reference. It must not accept a concrete
`INT-*`, consumed IF, or external provider interaction from this observation
alone.

## Prohibited inference / authority result

- configured base URL != confirmed API call;
- weak evidence does not promote itself to a concrete integration;
- no provider, operation, compatibility, or data access fact is fabricated;
- the catalog cannot become factual authority.

## Expected projection behavior

Integration documentation may show a safe logical external reference and an
explicit weak-hint limitation. It does not render a called service or exact
operation.

## Backward-compatibility constraint

Existing configuration facts remain usable as bounded observations; adding
call evidence later creates accepted new semantic state without rewriting the
historical observation.

## GREEN criteria

GREEN iff the source remains `WEAK_HINT`, no concrete IF/INT is accepted solely
from configuration, and user-facing output contains only safe logical identity
plus the limitation.

## Verdict

`PS158_PASS_EXTERNAL_WEAK_HINT`
