# PS-95 — Hybrid dependency graph

## Observed RED baseline

The baseline has compact `INDEX.md` routing state but requires freshness against
owning artifacts before downstream use (`SKILL.md:83-85`). It has no typed
semantic dependency vocabulary, generated reverse-index contract, impact
strength, or selector/set dependency. The missing contracts do not establish
that an existing index has become authority; runtime index behavior is absent.

Observed verdict: `PS95_INCONCLUSIVE`.

## Fixture

An authoritative projection depends on a direct fact ID and on a selector whose
membership gains a new matching technical object. Its generated central index
is lost or stale, and one dependency changes with each impact strength.

## GREEN contract

- each authoritative artifact owns direct outbound typed dependencies;
- generated central indexes provide reverse and aggregate traversal only;
- lost/stale indexes are repairable from authoritative metadata;
- an index is never reconstructed as direct semantic authority;
- dependency change initiates impact assessment/revalidation by strength, not
  automatic falsification;
- projections support explicit IDs and selector/set dependencies, so a new
  matching object can make a projection stale.

Required dependency vocabulary:

```text
EVIDENCED_BY
DERIVED_FROM
DEPENDS_ON
REFERENCES
SUPERSEDES
PROJECTS_FROM
```

Required impact vocabulary:

```text
HARD
CONDITIONAL
INFORMATIONAL
```

## Verdict vocabulary

```text
PS95_RED_INDEX_BECOMES_AUTHORITY
PS95_RED_DEPENDENCY_CHANGE_MEANS_FALSE
PS95_RED_NEW_OBJECT_NOT_SEEN_BY_PROJECTION_SELECTOR
PS95_GREEN_HYBRID_DEPENDENCY_GRAPH
PS95_INCONCLUSIVE
```

Evidence type: static contract inspection until a coordinator runtime exists.
