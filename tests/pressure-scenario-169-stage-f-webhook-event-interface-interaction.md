# PS-169 — Stage F webhook event, interface, and interaction

## Design mapping

`PS-F16`: a webhook uses EVENT + IF + INT when all three semantics are
material.

## Setup / evidence shape

A provider declares a webhook callback contract for `order.created`; evidence
also establishes the semantic event and a concrete delivery from the provider
to the consumer. The contract, event, and delivery observations carry exact
applicable Project/revision and provenance bindings.

## Expected accepted semantic records

The Technical Model Gate may accept an `EVENT-*`, an `IF-*` with
`interface_kind=WEBHOOK`, and an `INT-*` with
`interaction_kind=EVENT_PUBLISH` or `EVENT_SUBSCRIBE`. Each retains its own
identity, revision, role/view, and evidence.

## Prohibited inference / authority result

- EVENT, IF, and INT must not be aliased;
- a webhook contract alone does not prove delivery;
- event identity does not become a call edge or compatibility result;
- Product aggregation cannot create a fourth webhook fact family.

## Expected projection behavior

Integration documentation may render EVENT + IF + INT together as linked
accepted facts while keeping their identities and provider/consumer sides
distinct. Missing pieces remain absent or limited rather than fabricated.

## Backward-compatibility constraint

Historical event or webhook IF records remain valid when transport or delivery
details were not recorded. Enrichment is additive and preserves old identity.

## GREEN criteria

GREEN iff all three records are accepted only when separately evidenced, their
identities remain distinct, and the projection links rather than aliases them.

## Verdict

`PS169_PASS_WEBHOOK_IDENTITY_BOUNDARY`
