# PS-165 — Stage F ORM ambiguous access

## Design mapping

`PS-F12`: an ORM model plus ambiguous operation preserves evidence and a
precision limitation.

## Setup / evidence shape

An ORM model names an `orders` entity, but the observed operation is generic or
ambiguous and does not establish whether a specific table or access mode is
used. The model observation is `WEAK_HINT` or bounded inference; the source and
limitation are recorded.

## Expected accepted semantic records

The Technical Model Gate may accept a bounded DS/resource observation or an
unresolved access candidate. It must not accept exact child-resource access or
an exact DATA_ACCESS INT unless an operation and mode are separately evidenced.

## Prohibited inference / authority result

- ORM model exists != confirmed table access;
- model naming does not prove READ, WRITE, or READ_WRITE;
- evidence strength does not replace acceptance or precision;
- a relation, projection, or package cannot promote the hint.

## Expected projection behavior

Technical Documentation retains the ORM evidence and explicit ambiguity. It
does not render an exact table access, invented mode, or clean absence of
access.

## Backward-compatibility constraint

Historical ORM/model observations remain valid bounded evidence. Later exact
operation evidence creates accepted additive state without rewriting history.

## GREEN criteria

GREEN iff the model remains evidence metadata or bounded STM state, exact access
is absent unless separately supported, and the projection exposes the
limitation.

## Verdict

`PS165_PASS_ORM_AMBIGUITY`
