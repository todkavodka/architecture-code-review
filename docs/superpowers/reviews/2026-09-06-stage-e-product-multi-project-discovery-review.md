# Stage E — Product / Multi-Project Discovery: Independent Review

**Review date:** 2026-09-06  
**Review type:** Independent Discovery Review only  
**Reviewed baseline:** `63bef65c765d0a381b63a7b4fdffe1679d89eee5`  
**Canonical branch:** `main`

## Scope and sources

Reviewed:

- `docs/superpowers/specs/2026-09-06-stage-e-product-multi-project-discovery.md`
- `docs/roadmap.md`
- `SKILL.md`
- session/orchestration, evidence, STM, dependency, revalidation, projection,
  package, ownership, review-method, and finding contracts under `references/`
- `capabilities/test-review/SKILL.md` and
  `capabilities/test-review/references/test-engineering-contract.md`
- `capabilities/code-quality-review/SKILL.md` and the Code Quality contract,
  lifecycle, and projection references

The roadmap's stale Stage D label was treated as metadata debt, as required by
the Discovery artifact. No implementation, normative contract, roadmap, or
Discovery changes were made.

## Summary verdict

The Discovery is directionally sound and architecture-safe enough to preserve
the current single-project model. It correctly rejects Product-as-mandatory-
root, Project-as-repository, report-as-authority, relation-as-dependency, and
dirty-state cleanup. The hybrid Option C is compatible with current contracts
provided that its cross-project layer remains bounded and does not become a
second factual or capability authority.

The Discovery is not yet safe to promote directly into Design. Two rows marked
`DISCOVERY_RESOLVED` contain unresolved semantic ownership/routing decisions,
and the persistence of Product identity is recommended more strongly than the
current contracts require. These are medium findings, not contradictions in
Option C. One low-risk pressure-scenario gap should also be closed or
explicitly accepted before Design.

**Verdict:** `STAGE_E_DISCOVERY_REVIEW_FINDINGS`

## Findings

### F-01 — MEDIUM — Product persistence is a direction, not yet a proven constraint

**Classification:** `PREMATURE_DESIGN` / `MISSING_DECISION`

The Discovery says Product should have a stable persistent identity, history,
and membership provenance. Stable baseline-bound evidence and accepted semantic
records already provide revision-bound provenance without, by themselves,
requiring a persistent Product aggregate. Persistence may be justified for
membership continuity, later `REVALIDATE`, and historical package identity, but
the Discovery does not establish which of those guarantees cannot be supplied
by a stable scoped Product context or baseline identity.

Design must therefore prove the minimum persistence requirement and separately
decide Product ownership, lifecycle, creation authority, and whether a
single-member Product is valid. It must preserve the explicit constraint that
Product remains optional and is not a mandatory hierarchy root. Option C remains
viable; the issue is the strength and justification of the constraint.

### F-02 — MEDIUM — Cross-project evidence is not fully `DISCOVERY_RESOLVED`

**Classification:** `MISSING_DECISION`

The Discovery correctly establishes that cross-project claims need addressable
multi-source bindings and cannot be inferred from concatenated reports. That is
a safe constraint. However, the decision-register label
`Cross-project evidence = DISCOVERY_RESOLVED` overstates what is settled. An
addressable cross-project observation/adjudication still requires Design to
define whether it is:

- an extension of `WS-*`/`EV-*` observation semantics;
- an STM fact/relation accepted by the Technical Model Gate; or
- a capability-owned interpretation that references multiple local evidence
  records.

The owner, lifecycle, acceptance gate, coherent multi-source baseline binding,
and conflict handling are not determined by current contracts. Without this
correction, Design could accidentally create a new evidence authority while
believing the Discovery already resolved the boundary.

The row should be `DESIGN_DECISION_REQUIRED`, while retaining the existing
constraints: preserve every source binding, do not make reports authoritative,
and do not infer compatibility from co-location.

### F-03 — MEDIUM — Membership-changing `EXTEND` needs an explicit semantic route

**Classification:** `MISSING_DECISION`

The current `EXTEND` contract supports additive scope and output expansion
without reopening unrelated accepted work. The Discovery correctly applies
that rule to adding a Project or output. It then says that a membership change
which changes Product meaning is routed to membership adjudication and targeted
revalidation, but still classifies Product `EXTEND` as
`DISCOVERY_RESOLVED`.

The additive invariant is resolved; the semantic transition is not. Design must
define how a membership revision changes the Product baseline, package
membership snapshot, direct impact roots, preserved set, and affected Product
interpretations. It must also distinguish adding a selected member from
changing the meaning or requiredness of an existing member. Until then, the
register should classify the whole Product `EXTEND` row as
`DESIGN_DECISION_REQUIRED`, with the additive portion explicitly retained as a
resolved invariant.

## Option C assessment

**`OPTION_C_RECOMMENDATION: SUPPORTED`**

Option C preserves the current contracts when bounded as follows:

- single-project `NEW` remains valid without Product;
- Project remains a logical scope/context distinct from repository, review
  target, and workspace/session;
- Project-local STM and capability records retain their owners;
- Product membership and any Product baseline are explicit, revision-bound
  inputs rather than inferred from reports or paths;
- cross-project facts remain within STM authority or an explicitly designed,
  non-duplicating authority boundary;
- dependency metadata and impact traversal remain distinct from factual
  relations and generated reverse indexes;
- Product outputs remain derived projections with declared dependencies,
  package membership, and freshness;
- `REVALIDATE` remains impact-driven and preserves unrelated accepted state;
- `EXTEND` remains additive unless a membership semantic change explicitly
  enters its own adjudication/revalidation route.

There is no current invariant that makes the hybrid direction contradictory.
The phrase “minimal cross-project layer” must remain a Design constraint on
scope, not an authorization to create a new universal semantic owner.

## Decision-register assessment

| Topic | Independent assessment |
|---|---|
| Product identity | `DESIGN_DECISION_REQUIRED`; F-01 applies to the necessity/strength of persistence. |
| Project identity | `DESIGN_DECISION_REQUIRED`; correctly avoids overcommitting to aggregate vs descriptor. |
| Product membership | `DESIGN_DECISION_REQUIRED`; ownership, cardinality, history, and change policy remain open. |
| Repository relationship | Pass as a constraint; repository is provenance/source, not Project identity. |
| Product baseline | `DESIGN_DECISION_REQUIRED`; vector is necessary directionally but needs acceptance, coherency, partiality, and external-source rules. |
| Cross-project evidence | `DESIGN_DECISION_REQUIRED`; reclassify from `DISCOVERY_RESOLVED` per F-02. |
| Cross-project STM | `DESIGN_DECISION_REQUIRED`; correctly defers scope/provenance and relation-boundary design. |
| Dependency semantics | Pass as a distinction; relation, direct dependency, index, and impact result remain separate. Traversal/root design remains open. |
| Shared ownership | `DESIGN_DECISION_REQUIRED`; usage, membership, dependency, and ownership are correctly separated. |
| Product findings | `DESIGN_DECISION_REQUIRED`; RF reuse is a hypothesis requiring scope/provenance proof. |
| Code Quality aggregation | `DESIGN_DECISION_REQUIRED`; Project CQ remains authoritative and Product interpretation owner is open. |
| Test Engineering | `DESIGN_DECISION_REQUIRED`; no second Behavior Model authority is proposed. |
| Compatibility | `DESIGN_DECISION_REQUIRED`; version, declared range, observed compatibility, and finding remain distinct. |
| Product `REVALIDATE` | `DESIGN_DECISION_REQUIRED`; impact root, traversal, and baseline coherency remain foundational decisions. |
| Product `EXTEND` | `DESIGN_DECISION_REQUIRED` for membership meaning changes per F-03; additive extension invariant passes. |
| Partial availability | `DESIGN_DECISION_REQUIRED`; current models support bounded coverage/freshness, not a new universal Product status. |
| Dirty state | Pass as a constrained handling rule only; exact state is preserved and acceptance remains open for Design. |
| Projections | `DESIGN_DECISION_REQUIRED`; candidates are not silently promoted to mandatory outputs or authority. |
| Package model | `DESIGN_DECISION_REQUIRED`; reuse of finite Stage B membership/snapshot mechanics is sound, Product policy is open. |
| Authorization | Pass; membership and Product presence do not grant clone, write, execution, deployment, or publication authority. |
| Context/scale | Pass as a bounded strategy; staged dependency-directed evidence acquisition is compatible with minimum-slice routing. |
| New identifier families | `DEFERRED_FUTURE_SCOPE`; correctly requires a demonstrated contract gap first. |

**Decision-register result:** `FINDINGS` because the cross-project evidence and
Product `EXTEND` rows are over-classified as resolved.

## Pressure-scenario assessment

Scenarios 1–16 cover the requested core risks: standalone operation, clean
multi-project baseline, unavailable and dirty sources, baseline advancement,
API compatibility, shared components, true and false Product findings,
additive `EXTEND`, targeted `REVALIDATE`, stale projections, compatible old
versions, conflicting evidence, blocked packages, and multi-Product reuse.

The following coverage is adequate:

- Scenario 1 protects Product optionality and single-project compatibility.
- Scenarios 2–5 exercise vector provenance, partiality, dirty bindings, and
  baseline movement.
- Scenarios 6–9 exercise cross-project evidence, finding ownership, and shared
  components.
- Scenarios 10–12 exercise additive extension, minimum-slice revalidation, and
  projection freshness separation.
- Scenarios 13–16 exercise compatibility, conflict, package blocking, and
 multiple membership.

### F-04 — LOW — Single-member Product transition is not an explicit pressure case

There is no explicit scenario for a
single-member Product or for transitioning between a standalone Project and a
single-member Product. That scenario would catch accidental mandatory-root or
cardinality assumptions not exercised by scenario 1 alone.

This is a pressure-coverage improvement, not evidence that the architecture is
unsafe.

**Pressure-scenario result:** `FINDINGS` (one `LOW` gap; existing 16 scenarios
remain useful and materially cover the requested Stage E risks).

## Architecture invariant check

| Invariant | Result | Reason |
|---|---|---|
| Single-project operation first-class | `PASS` | Product is explicitly optional and local authorities remain usable. |
| Product not universal semantic owner | `PASS` with Design gate | Discovery repeatedly forbids hidden Product authority; F-02 requires the evidence seam to retain that boundary. |
| Project not repository/session/workspace | `PASS` | Monorepo and multi-repository cases are explicitly recognized. |
| Capability ownership intact | `PASS` | RF/CQ/TE/STM ownership is preserved; product summaries remain projections unless Design proves new authority. |
| Projections derived | `PASS` | Candidate Product outputs use existing projection/package mechanics. |
| Revision-bound provenance | `PASS` with Design gate | Vector baseline direction is correct; coherency/acceptance rules remain open. |
| Impact-driven `REVALIDATE` | `PASS` with Design gate | Minimum-slice rule is preserved; cross-project impact root and membership transitions remain open. |
| Additive `EXTEND` | `PASS` for ordinary additions; `FINDINGS` for semantic membership changes | F-03. |

No HIGH finding was identified. Option C does not currently contradict a
frozen/current invariant.

## Required corrections before Design

1. Reclassify Cross-project evidence as `DESIGN_DECISION_REQUIRED`, retaining
   its evidence-first constraints.
2. Split Product `EXTEND` into a resolved additive invariant and a
   `DESIGN_DECISION_REQUIRED` membership-semantic transition, or classify the
   whole row as design-required.
3. Make Product persistence an explicit Design hypothesis/constraint with a
   proof obligation for provenance, membership history, and revalidation; do
   not let it imply mandatory Product parentage or Product ownership.
4. Add the single-member Product / standalone-to-Product pressure scenario, or
   record an explicit rationale for deferring it.
5. In Design, explicitly bind partial availability, dirty acceptance, external
   contract revisions, baseline coherency, Product finding ownership, and
   package membership snapshots to existing status and freshness axes rather
   than introducing a universal Product status or second package authority.

## Design entry recommendation

`STAGE_E_DISCOVERY_REMEDIATION` is recommended before `STAGE_E_DESIGN`.
Remediation can be limited to correcting the Discovery classification and
making the listed proof obligations explicit; it does not require changing
implementation or normative contracts. After those corrections, Option C is a
safe bounded input to Design.

## Review metadata

- `HIGH`: 0
- `MEDIUM`: 3
- `LOW`: 1
- `finding_ids`: `F-01`, `F-02`, `F-03`, `F-04`
- `normative_files_changed`: `NO`
- `discovery_file_changed`: `NO`
- `roadmap_changed`: `NO`
- `implementation_performed`: `NO`
- `commit_performed`: `NO`
- `push_performed`: `NO`
