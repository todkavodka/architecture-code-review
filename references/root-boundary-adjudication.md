# Root-Boundary Adjudication

This gate runs after independent verification and before severity assignment. Its purpose is to ensure that one authoritative root finding corresponds to one concrete correction boundary, not merely to a broad or attractive theme.

## 1. Normative root test

For every proposed root, ask:

> If this specific mechanism is corrected, will all listed projections of the problem disappear?

If not:

```text
SPLIT_REQUIRED
```

## 2. Valid root shape

A well-formed root normally has:

- one concrete runtime mechanism;
- one coherent owner/scope;
- one plausible correction boundary;
- a reachable path or scenario;
- projections that are genuinely removed by the same correction.

Do not group findings merely because they belong to the same class, service, “state machine”, IPC area, or concurrency theme.

## 3. Root vs projection vs SER

### Root finding (`RF-*`)

A concrete mechanism that directly creates a material incorrect behavior or risk.

### Projection

An observable manifestation of the same mechanism in another path, UI, event, or file. A projection does not receive a separate root ID when the correction boundary is genuinely the same.

### Supporting Engineering Risk (`SER-*`)

A structural factor that makes recurrence or non-detection more likely, for example:

- semantic ownership is not encoded;
- lifecycle state is spread across flags;
- event identity is discarded by a consumer;
- shared resource allocation is ownerless;
- a deterministic local regression suite is missing.

An SER must not automatically inherit the severity of the Product root finding.

## 4. Split/merge decision

Before merging two verified candidates, check:

```text
same mechanism?
same authoritative owner/scope?
same correction unit?
one fix removes both effects?
```

Any material `no` is a strong signal to split.

Before splitting, check the opposite risk: do not create two IDs for the same mechanism merely because it is visible in two layers.

## 5. Arithmetic integrity

After adjudication, account for:

```text
verified candidates
→ mapped projections
→ authoritative roots
→ SER/open questions
```

Every material verified candidate must have one primary disposition: root, projection, SER, open question, or refuted. Do not allow double primary counting.

## 6. Output

For every proposed root, record:

```text
root ID
source candidates
mechanism
owner/scope
correction boundary
projections
SER links
root test result
final action: ACCEPT_ROOT | SPLIT_REQUIRED | MERGE_WITH | DEMOTE_TO_SER | OPEN_QUESTION
```

## 7. Anti-patterns

Poor root labels that lack a concrete mechanism include:

- “implicit FSM”;
- “bad ownership”;
- “too much global state”;
- “fragile event architecture”.

These may be useful SERs or themes, but a root finding requires a concrete mechanism plus a reachable effect.

## Product RF root boundary

A Product-scoped `RF-*` root must identify the accepted Product revision/baseline, affected Projects, qualified evidence and STM relations, and one material cross-project correction boundary. A local RF remains a local root unless an independent Product consequence is adjudicated. Product aggregation, report text, projections, or index entries are mapped projections and cannot become root authority.