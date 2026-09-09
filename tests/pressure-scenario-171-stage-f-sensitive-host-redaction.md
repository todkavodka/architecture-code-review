# PS-171 — Stage F sensitive host redaction

## Design mapping

`PS-F18`: a private hostname is redacted or replaced by a safe logical
identifier.

## Setup / evidence shape

An observation points to a private host represented as
`internal-host.example.invalid` and classifies it `SENSITIVE_INTERNAL`. The
source pointer and Project binding are retained; no secret-bearing URL or
credential is included.

## Expected accepted semantic records

STM/evidence may retain a bounded external or internal logical identity and an
approved safe alias such as `orders-provider`. The raw private hostname is not
a general-display identifier and is not silently reclassified as safe.

## Prohibited inference / authority result

- sensitive hostnames cannot be copied into user-facing catalogs;
- `SENSITIVE_INTERNAL` is not `SAFE_TECHNICAL_IDENTIFIER` by convenience;
- a host observation alone does not prove an interaction or provider;
- the projection cannot create a second classification authority.

## Expected projection behavior

Projections render the approved logical alias or a redacted form, with safe
provenance and limitation. They omit the raw private locator from metadata,
fingerprints, summaries, and package output.

## Backward-compatibility constraint

Historical source pointers retain their evidentiary meaning. Applying the safe
alias is compatible presentation handling, not a semantic identity rewrite.

## GREEN criteria

GREEN iff the raw sensitive host is absent from output, only an approved alias
or redaction is rendered, and no interaction fact is inferred from the host.

## Verdict

`PS171_PASS_SENSITIVE_HOST_REDACTION`
