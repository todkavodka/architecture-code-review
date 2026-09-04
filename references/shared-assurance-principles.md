# Shared Assurance Principles

This is the single compact cross-capability contract for the umbrella review
suite. It promotes four proven invariants without duplicating specialist
methodology.

## 1. Authority before substantive verdict

When materially conflicting authorities would lead to different conclusions,
first establish precedence, supersession, approval, ownership decision, or an
equivalent explicit authority mechanism.

```text
material authority conflict
+ no explicit precedence/supersession/approval/owner decision
→ AUTHORITY_STATUS = UNRESOLVED
→ UNKNOWN / AUTHORITY_UNRESOLVED
→ no substantive defect/recommendation from that conflict alone
```

Urgency, recency, document naming, implementation alignment, current tests, CI
status, or apparent formality do not independently resolve authority.

## 2. Claim scope must not exceed evidence scope

Every capability bounds its claim to the material behavior and boundaries it
directly exercised or directly evidenced:

```text
supported claim scope <= directly exercised / directly evidenced material scope
```

Narrow evidence supports a narrow claim. Unexercised adjacent paths normally
remain `PARTIAL`, `NOT_PROVEN`, or `UNKNOWN`, not a defect by missing evidence
alone.

## 3. Completeness requires bounded material accounting

Before an overall assurance or completeness claim, establish a bounded inventory
of the applicable material targets/domains and account for every item. Selective
deep inspection is compatible with bounded accounting; sampling, file count,
test count, or finding count is not a completeness proof.

Technical Model Coverage owns the bounded factual-domain matrix for the Shared
Technical Model; Architecture Discovery Coverage owns the architecture-domain
matrix. A capability such as Test Review owns its own assurance-target universe.
Neither inventory is silently substituted for another. A full Architecture
Review needs the accepted factual coverage gate before its architecture
mechanism analysis; see [Technical Model Coverage](technical-model-coverage.md).

## 4. Candidate decomposition preserves material contracts

Decompose a candidate into its mechanism or smell, its consequence, and any
separately material behavioral/architectural contract. Rejecting a mechanism does
not discard a material contract discovered inside it. Record an explicit
disposition: represented, unresolved, non-material with reason, or promoted
through the applicable verification and adjudication gates.

## 5. Shared evidence is reusable, not semantic authority

Capabilities and the STM reuse shared baseline-bound observations by reference;
they do not duplicate one observation into capability evidence silos. `WS-*`
and `EV-*` remain observational records, while capability-owned semantic
artifacts retain ownership of conclusions. See
[Shared Evidence Model](shared-evidence-model.md).

## 6. Projection lifecycle does not demote authority

Stage B projections are explicitly classified derived artifacts, not a second
semantic model. Stable `PRJ-*` identity, verified projection revision, and
`CURRENT`/`STALE`/`BLOCKED` freshness are lifecycle metadata owned by the
projection contract. They do not transfer meaning from STM, Architecture
findings/semantic ledgers, or Test Engineering BC/CC/MAT/TM/GAP authorities.

`working/INDEX.md` remains coordinator-owned workflow authority and is outside
automatic projection classification. A semantic workflow may finish while a
dependent projection is `STALE`; projection staleness is loss of freshness
proof, not proof that the semantic authority is false. Regeneration follows
authority and never changes it to match projection prose. See
[Projection lifecycle authority](projection-lifecycle.md).
