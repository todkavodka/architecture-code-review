# PS-97 — Technical Documentation projection

## Observed RED baseline

The baseline makes accepted As-Built the factual authority
(`references/report-contract.md:41-49`) and defines no Technical Documentation
projection from STM. Its existing final-report projection rules cannot prove
the future documentation scope, non-authority, or conflict behavior. This is a
static omission, not evidence that a projection changed facts at runtime.

Observed verdict: `PS97_INCONCLUSIVE`. Static inspection establishes that the
projection contract is absent, but cannot prove that documentation became
semantic authority or changed facts.

## Fixture

Accepted STM facts describe system overview, components, provided/consumed
interfaces, integrations, data/persistence, runtime/deployment, auth/trust,
material flows, and failure behavior. Two factual authorities conflict.

## GREEN contract

Technical Documentation is generated or synthesized from accepted STM facts. It
is a human-readable factual projection, never semantic authority. It may cover
the fixture surfaces, but Stage A does not add onboarding, local setup, “how to
run,” “how to change,” or tutorial semantics. Prose cannot resolve a factual
authority conflict.

## Verdict vocabulary

```text
PS97_RED_DOCUMENTATION_BECOMES_AUTHORITY
PS97_RED_DEVELOPER_HOWTO_SCOPE
PS97_RED_PROJECTION_RESOLVES_FACT_CONFLICT
PS97_GREEN_TECHNICAL_DOCUMENTATION_PROJECTION
PS97_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
