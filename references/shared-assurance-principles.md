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

Architecture Discovery Coverage owns the architecture-domain matrix. A capability
such as Test Review owns its own assurance-target universe; neither inventory is
silently substituted for the other.

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
