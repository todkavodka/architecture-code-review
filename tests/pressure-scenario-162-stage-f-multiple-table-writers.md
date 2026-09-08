# PS-162 — Stage F multiple table writers

## Design mapping

`PS-F09`: two services writing one table remain separate INT WRITE facts, each
may derive `WRITES_TO`, and ownership/interpretation remain separate.

## Setup / evidence shape

Services A and B each have exact, independently Project-qualified evidence of a
write to the same table DS. The two source operations and revisions are
distinct; the target DS identity is shared and qualified.

## Expected accepted semantic records

STM may accept two distinct `INT-*` records with `interaction_kind=DATA_ACCESS`
and `access_mode=WRITE`, one for each source. Each may derive its own
`WRITES_TO` navigation relation. `OWNS_STATE`, if accepted, remains a separate
relation with its own scope and evidence.

## Prohibited inference / authority result

- the two INTs must not collapse because their target DS is equal;
- one writer cannot be inferred to own state or migration authority;
- multiple writers do not automatically become an RF-*;
- derived relations cannot become a hidden access authority.

## Expected projection behavior

Service and Product data views retain both qualified source INTs and display
their separate evidence, access modes, and derived navigation. Product baseline
qualification prevents same-text local IDs from colliding.

## Backward-compatibility constraint

Historical broad WRITES_TO relations remain broad. Adding a second precise INT
does not rewrite or deduplicate existing accepted facts.

## GREEN criteria

GREEN iff both INT WRITE records remain independently addressable, each relation
is derived from its own INT when shown, and no ownership, migration, or finding
is inferred from multiplicity.

## Verdict

`PS162_PASS_MULTIPLE_INT_WRITERS`
