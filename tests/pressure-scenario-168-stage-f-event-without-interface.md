# PS-168 — Stage F event without interface

## Design mapping

`PS-F15`: event production or consumption works without a duplicate IF.

## Setup / evidence shape

Evidence establishes a semantic `order.created` message being published or
consumed through a broker. No material callable or contract surface is
established. Producer/consumer observations are separately Project-qualified.

## Expected accepted semantic records

The Technical Model Gate may accept an `EVENT-*` semantic message and an
`INT-*` with `interaction_kind=EVENT_PUBLISH` or `EVENT_SUBSCRIBE` when the
concrete edge is evidenced. No `IF-*` is required or created solely to host the
event.

## Prohibited inference / authority result

- EVENT is not an IF, INT, or FLOW;
- a broker configuration alone does not prove production or consumption;
- event presence does not force a callable API identity;
- projections do not alias event and interface identities.

## Expected projection behavior

The integration projection renders the EVENT and any accepted INT separately.
It may omit IF because no interface exists; absence of IF is not a failure or
empty-clean result.

## Backward-compatibility constraint

Historical event records remain valid without protocol-specific IF fields. New
transport or callable evidence may add separately identified facts only.

## GREEN criteria

GREEN iff the semantic EVENT remains independently representable, any INT is
concrete and evidenced, no duplicate IF is invented, and absence of IF remains
explicitly valid.

## Verdict

`PS168_PASS_EVENT_WITHOUT_IF`
