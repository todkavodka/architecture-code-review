# PS-93 — Shared evidence layer

## Observed RED baseline

At `main@10233b80eb6a46ff1f8d4348c4be890cf1d1f4a2`, Test Engineering labels
`WS-*` as temporary working/investigation state
(`capabilities/test-review/references/test-engineering-contract.md:15-28`),
while Architecture Review routes evidence through its own working artifacts.
No baseline contract defines shared `WS-*` worksets, globally addressable
`EV-*` observations, or the required retrieval order. This omission supports a
static isolation risk but does not prove a runtime write/rewrite occurred.

Observed verdict: `PS93_INCONCLUSIVE`.

## Fixture

One repository observation is useful to Architecture Review and Test
Engineering. The repository later advances from the evidence baseline to a new
HEAD.

## GREEN contract

- `WS-*` are shared cross-capability worksets;
- `EV-*` are logical, globally addressable observations inside worksets;
- every observation is bound to baseline and provenance;
- old evidence remains historical after HEAD changes;
- capabilities reference the same evidence without duplicating it;
- normal retrieval is `index -> semantic object -> evidence -> raw source`.

## Failure conditions

- separate architecture/test silos duplicate one observation;
- `EV-*` is treated as a finding or accepted technical fact;
- old evidence is rewritten to match a new baseline;
- one physical Markdown file is required for every `EV-*`.

## Verdict vocabulary

```text
PS93_RED_EVIDENCE_SILOED_OR_REWRITTEN
PS93_RED_EVIDENCE_BECOMES_SEMANTIC_AUTHORITY
PS93_GREEN_SHARED_EVIDENCE_LAYER
PS93_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
