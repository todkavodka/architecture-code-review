# PS-154 — Stage F provider REST operation

## Design mapping

`PS-F01`: a provider REST operation declared by router/OpenAPI evidence becomes
a provided interface with declaration evidence.

## Setup / evidence shape

A Project contains an accepted router route and an OpenAPI operation for
`GET /orders/{id}`. The observations are bound to the same Project revision;
the OpenAPI observation is `DIRECT_DECLARATION` with `observed_view=DECLARED`,
and the route observation is `STRONG_INFERENCE` with
`observed_view=IMPLEMENTED`.

## Expected accepted semantic records

The Technical Model Gate may accept one `IF-*` with `direction=PROVIDED`,
`interface_kind=HTTP_REST`, operation identity, safe address, contract
reference, `precision=EXACT`, and both evidence references. Provider declaration
and provider implementation remain distinct contract roles/views. No `INT-*`
is accepted unless a concrete invocation is separately evidenced.

## Prohibited inference / authority result

- evidence prose or the projection cannot accept the IF;
- a route cannot become an INT merely because it is declared;
- an OpenAPI path cannot create a compatibility result;
- no new API identity family is introduced.

Shared Evidence owns observations, STM owns accepted facts, and Technical
Documentation remains a derived projection.

## Expected projection behavior

The provided-interface projection renders the qualified IF, operation, safe
address, contract reference, precision, observed view, and provenance. It does
not invent a consumer, interaction, compatibility result, or missing field.

## Backward-compatibility constraint

An existing broad HTTP IF without an operation remains valid; the new operation
detail is an additive revision or enrichment, not an identity rewrite.

## GREEN criteria

GREEN iff the exact Project-bound provided IF is accepted only through the
Technical Model Gate, declaration/implementation provenance remains distinct,
no INT or compatibility fact is inferred, and the projection renders only the
accepted safe fields.

## Verdict

`PS154_PASS_PROVIDER_REST_IF`
