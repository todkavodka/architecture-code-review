# PS-178 — Stage F weak hint is not an API call

## Design mapping

`PS-F25`: weak-hint configuration does not become an accepted API call.

## Setup / evidence shape

A synthetic configuration key contains a base API URL and an SDK dependency is
present, but no call site, runtime use, declaration, or test establishes an
operation. Both observations are `WEAK_HINT` and retain explicit limitations.

## Expected accepted semantic records

Evidence may route a candidate or bounded external logical identity for further
investigation. The Technical Model Gate must not accept a concrete consumed
IF, provider implementation, or `INT-*` CALL from these hints alone.

## Prohibited inference / authority result

- config URL != proven call;
- SDK dependency != proven use;
- candidate state is not compatibility or accepted integration;
- no parser, scanner, crawler, or projection prose can promote the hint.

## Expected projection behavior

Technical Documentation may show a safe non-authoritative candidate/not-
evaluated limitation, but not an accepted API call, exact operation, or
compatibility result.

## Backward-compatibility constraint

Historical weak-hint observations remain valid bounded evidence. Later direct
or strong evidence creates new accepted state without rewriting the hints.

## GREEN criteria

GREEN iff both observations remain `WEAK_HINT`, no concrete IF/INT call is
accepted, and user-facing output clearly distinguishes candidate from fact.

## Verdict

`PS178_PASS_WEAK_HINT_NOT_CALL`
