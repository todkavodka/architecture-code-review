# Federated Product Audit Coordination Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement federated Product audit coordination from a non-Git Coordination Root so Product scope can discover, qualify, reuse, resume, revalidate, or create child audits, compose an exact immutable Product baseline, and later process child source/authority advancement incrementally without creating new semantic authorities.

**Architecture:** Extend the existing session/Product/revalidation contracts only. Coordination remains metadata/orchestration; Project-local authorities remain local; cross-Project technical facts remain under STM/Technical Model Gate; Product updates use exact member vectors and existing `REVALIDATE` / `CHANGE_REVIEW` / contextual `RECONCILE_CHANGE` semantics. No runtime crawler, daemon, scheduler, database, Product STM, new Session Intent, or new capability is introduced.

**Tech Stack:** Markdown normative contracts, file-based coordinator state, deterministic Markdown scenario matrices, shell/Python text assertions, existing `working/INDEX.md` and `working/products/<PROD-key>/` namespace, existing Product/STM/Change Review/Revalidation/Projection contracts.

**Spec:** `docs/superpowers/specs/2026-09-11-federated-product-audit-coordination-design.md`

## Global Constraints

- Coordination Root is a locator/discovery boundary only; it is not a repository, Project, Product, baseline, workspace identity, or semantic authority.
- Product membership remains explicit and immutable per accepted Product revision.
- Existing Session Intents remain exactly `USE_EXISTING | NEW | RESUME | REVALIDATE | EXTEND | CHANGE_REVIEW | PROJECTION_REPAIR`.
- `RECONCILE_CHANGE` remains contextual and proof-gated; it is never a startup intent.
- Existing top-level semantic capabilities remain exactly Architecture Review, Test Engineering, and Code Quality Review.
- Product coordination labels (`REUSE`, `RESUME`, `REVALIDATE`, `CHANGE_REVIEW`, `NEW`, `EXCLUDE`, `BLOCKED`) are derived plan labels only.
- Product baseline remains an immutable exact qualified member/source vector; there is no synthetic root SHA.
- Child authority remains local; Product consumes accepted child state by qualified reference.
- Cross-Project technical facts/relations remain accepted by the Technical Model Gate; Product context never becomes a fact store.
- Product impact/readiness summaries are derived routing/provenance views only; no `PIA-*` family or new freshness lifecycle is introduced.
- `UNAFFECTED` requires sufficient accepted evidence; incomplete dependency coverage routes to `UNKNOWN_IMPACT`.
- Product Coordination Plan and Product Baseline Acceptance are separate human gates; neither bypasses existing child/owner gates.
- Parallel child execution is allowed only when writer scopes do not conflict.
- A frozen Product coordination context must bind Product revision, membership snapshot, base baseline, selected members, exact intended child bindings/actions, requested work, and authorization before dispatch.
- Exact Product/member/source/accepted-authority requalification is mandatory immediately before Product Baseline Acceptance.
- If child work completes at B and source advances to C, B may only be accepted as explicitly selected historical exact state; it must never be represented as current C.
- Independently advanced child authority may satisfy child readiness but never directly advances Product state; Product adoption routes through Product `REVALIDATE` or a new complete-vector Product `CHANGE_REVIEW` as appropriate.
- Logical Product state remains under the single coordinator `working/INDEX.md` authority and Product-qualified `working/products/<PROD-key>/` namespace; physical workspace placement may be configurable.
- Discovery remains bounded metadata discovery; do not build a generic crawler/harness.
- Stop tokens remain applicable: `DO_NOT_BUILD_HARNESS`, `STOP_HARNESS_EXPANSION`, `VALIDATION_BUDGET_EXCEEDED`.

---

## 1. Approved baseline and scope

Planning baseline is remediation commit:

```text
e8494f720d2cca7d53b57a4da08ed21dc9ca609a
```

Approved design:

```text
docs/superpowers/specs/2026-09-11-federated-product-audit-coordination-design.md
```

Independent design review result before remediation:

```text
APPROVE WITH REMEDIATION
READY_AFTER_SPEC_REMEDIATION
HIGH 0 / MEDIUM 4 / LOW 2
```

Targeted re-review result supplied after remediation:

```text
APPROVE
READY_FOR_IMPLEMENTATION_PLANNING
R1-R6 CLOSED
HIGH 0 / MEDIUM 0 / LOW 0
```

In scope:

1. Coordination Root startup and bounded repository/source candidate discovery semantics.
2. Existing child audit qualification/reuse under Product coordination.
3. Immutable Product Coordination Plan/frozen execution context.
4. Aggregate Product authorization that preserves local child/owner gates.
5. Stable child checkpoints and derived dependency/output readiness.
6. Exact Product baseline candidate composition and final requalification.
7. Deterministic bottom-up Product routing for independently advanced child authority.
8. Product impact routing as a derived view over existing dependency/freshness/capability authorities.
9. Existing logical workspace namespace alignment.
10. Deterministic contract and backward-compatibility validation.
11. Minimal user-facing guidance for the new top-down/bottom-up Product flow.

Out of scope:

- runtime repository crawler;
- daemon/watcher;
- scheduler/execution engine;
- database/graph store;
- automatic repository mutation;
- automatic Product membership;
- automatic Change Review/Revalidation/reconciliation/projection regeneration;
- new capability or Session Intent;
- Product technical-fact registry;
- Product finding registry;
- Product-to-Product nesting;
- implementation of external SCM adapters.

## 2. File impact inventory

### Modify

```text
SKILL.md
references/session-orchestration.md
references/review-modes-and-orchestration.md
references/product-multi-project-review.md
references/revalidation-and-freshness.md
docs/guides/reuse-and-change.md
```

### Create

```text
tests/federated-product-audit-coordination-validation.md
tests/federated-product-audit-coordination-backward-compatibility.md
```

### Read-only implementation inputs

```text
docs/superpowers/specs/2026-09-11-federated-product-audit-coordination-design.md
references/shared-technical-model.md
references/technical-model-dependencies.md
references/shared-evidence-model.md
references/projection-impact.md
references/projection-regeneration.md
references/projection-gates-and-packages.md
tests/change-review-baseline-reconciliation-validation.md
docs/roadmap.md
```

No implementation task may add a new normative contract unless an actual contradiction is discovered. If one is discovered, stop and return to design review rather than creating a parallel framework.

## 3. Dependency graph and review checkpoints

```text
Task 1 fail-first validation skeleton
  -> Task 2 session startup + bounded discovery + frozen plan
  -> Task 3 Product contract + stable barrier + baseline acceptance
  -> Task 4 bottom-up routing + derived impact/readiness semantics
  -> Task 5 coordinator state/entrypoint integration
  -> Task 6 backward compatibility + pressure closure
  -> Task 7 user guidance + final verification
```

Review checkpoints:

- **Checkpoint A — Tasks 1–2:** startup/discovery/frozen-plan semantics are coherent.
- **Checkpoint B — Tasks 3–4:** Product baseline, bottom-up routing, and impact semantics are coherent.
- **Checkpoint C — Tasks 5–6:** integration/backward compatibility is green.
- **Checkpoint D — Task 7:** user-facing flow and final verification are complete.

Implementation should use an isolated worktree at execution time via `superpowers:using-git-worktrees`. This planning task does not create the worktree or branch.

---

### Task 1: Create fail-first federated coordination validation contracts

**Files:**
- Create: `tests/federated-product-audit-coordination-validation.md`
- Create: `tests/federated-product-audit-coordination-backward-compatibility.md`

**Interfaces:**
- Consumes: approved design invariants and current normative references.
- Produces: deterministic scenario IDs used by Tasks 2–7 as closure evidence.

- [ ] **Step 1: Write the fail-first validation matrix**

Create `tests/federated-product-audit-coordination-validation.md` with named rows covering at least:

```text
FC01 non-Git Coordination Root remains locator only
FC02 discovery stops ordinary descent at repository boundary
FC03 symlink/root-escape/cycle handling is bounded
FC04 worktree/submodule/nested repo are explicit candidates, not auto-members
FC05 Project != repository mapping remains explicit
FC06 independently-created accepted child audit is reusable after qualification
FC07 confirmed coordination plan freezes Product revision/membership/base baseline/member bindings/requested work
FC08 Product revision change during child work invalidates aggregation eligibility
FC09 child completes at B, source advances to C before acceptance -> requalify/replan
FC10 conflicting writer scopes serialize despite parallel-by-default
FC11 derived readiness does not create capability/freshness authority
FC12 bottom-up child A->B routes through Product REVALIDATE for accepted-state update
FC13 candidate assessment uses new full-vector Product CHANGE_REVIEW
FC14 old Product CR is not reusable when complete vector differs
FC15 RECONCILE_CHANGE remains contextual/proof-gated
FC16 impact result is derived AFFECTED|UNAFFECTED|UNKNOWN_IMPACT only
FC17 incomplete dependency coverage -> UNKNOWN_IMPACT
FC18 Product workspace uses single working/INDEX.md + working/products/<PROD-key>/
FC19 multiple Products under one Coordination Root remain isolated
FC20 moved Coordination Root does not change Product identity
FC21 Product baseline candidate contains exact member vector + plan ref
FC22 baseline acceptance rechecks Product/member/source/owner bindings
FC23 no automatic membership/change review/revalidation/reconcile/regeneration
FC24 Product relation authority remains STM/Technical Model Gate
```

For each row include columns:

```text
ID | Preconditions | Required contract outcome | Forbidden outcome | Owning contract | Status
```

Initial status must be `GAP PRESENT` where the current implementation lacks explicit federated semantics; do not falsely mark closure before edits.

- [ ] **Step 2: Write backward-compatibility assertions**

Create `tests/federated-product-audit-coordination-backward-compatibility.md` with at least these invariants:

```text
BC01 single-repository Project startup remains unchanged
BC02 Product mode remains explicit/opt-in
BC03 seven Session Intents unchanged
BC04 three semantic capabilities unchanged
BC05 RECONCILE_CHANGE remains contextual
BC06 Product baseline remains exact vector
BC07 existing Product Change Review vector-equality rule unchanged
BC08 Project↔repository cardinalities remain supported
BC09 reports/projections remain non-authoritative
BC10 projection regeneration remains explicit
BC11 child local authority remains local
BC12 working/INDEX.md remains sole coordinator workflow authority
```

- [ ] **Step 3: Run fail-first text check**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
files = [
    Path('references/session-orchestration.md'),
    Path('references/product-multi-project-review.md'),
    Path('references/revalidation-and-freshness.md'),
]
text = '\n'.join(p.read_text() for p in files)
required = [
    'Coordination Root',
    'frozen coordination',
    'derived dependency-readiness',
]
missing = [x for x in required if x not in text]
print('missing=', missing)
raise SystemExit(0 if missing else 1)
PY
```

Expected before implementation: exit `0` with at least one required federated term missing. If all terms are already present because another change landed, stop and re-baseline the plan.

- [ ] **Step 4: Commit validation skeleton**

```bash
git add tests/federated-product-audit-coordination-validation.md \
        tests/federated-product-audit-coordination-backward-compatibility.md
git commit -m "test: define federated product coordination contract matrix"
```

---

### Task 2: Extend startup orchestration with Coordination Root discovery and frozen plan semantics

**Files:**
- Modify: `references/session-orchestration.md`

**Interfaces:**
- Consumes: existing repository identity / previous-audit discovery / Product context pinning / Session Intent routing.
- Produces: bounded Coordination Root discovery route, child candidate qualification, immutable Product Coordination Plan envelope, aggregate authorization boundary.

- [ ] **Step 1: Add Coordination Root startup route**

Extend startup routing so a non-repository directory can be recognized as an explicit Product coordination candidate without becoming repository or Project identity.

Normative route to add:

```text
START at non-repository coordination root
→ confirm/resolve Product context
→ load accepted Product revision/membership when present
→ bounded child repository/source candidate discovery
→ existing previous-audit qualification per candidate
→ propose Product Coordination Plan
→ explicit plan confirmation
→ dispatch existing child workflows
```

State explicitly:

```text
Coordination Root != repository identity
Coordination Root != Project identity
Coordination Root != Product identity
Coordination Root != Product baseline
filesystem containment != Product membership
```

- [ ] **Step 2: Add conservative discovery rules**

Add deterministic metadata-discovery rules:

```text
canonicalize path only for traversal/cycle detection
never use canonical path as semantic identity
maintain visited filesystem/repository-worktree set
never follow symlink outside explicit root by default
prevent traversal cycles
stop ordinary descent at discovered repository root
nested repos/submodules/worktrees -> explicit source candidates, never automatic Product members
missing/changed remote -> qualification limitation, not automatic identity decision
ambiguous Project↔repository mapping -> existing Product descriptor/user reconciliation
```

Do not specify a crawler implementation or source scan.

- [ ] **Step 3: Add frozen Product Coordination Plan contract**

Persist an immutable/superseding orchestration record that binds:

```text
plan_ref
product_id
selected_product_revision
membership_snapshot_ref
base_product_baseline_ref
selected_member/project keys
per-member repository/source/scope qualification
intended exact source binding
confirmed child Session Intent/action
requested capabilities
standalone outputs/lenses
coordination authorization result
```

Explicitly forbid retargeting by mutable `current_revision`, child `HEAD`, `latest audit`, or filesystem path.

- [ ] **Step 4: Preserve local child gates**

State that Product plan confirmation authorizes only the orchestration dispatch. Existing child source-access, capability, Change Review/reconciliation, test, and owner acceptance gates remain required.

- [ ] **Step 5: Run Task 2 focused assertion**

```bash
python3 - <<'PY'
from pathlib import Path
p = Path('references/session-orchestration.md')
t = p.read_text()
need = [
  'Coordination Root',
  'filesystem containment != Product membership',
  'membership_snapshot_ref',
  'base_product_baseline_ref',
  'intended exact source binding',
  'symlink',
  'worktree',
]
missing = [x for x in need if x not in t]
assert not missing, missing
for forbidden in ['FEDERATED_REVALIDATE', 'FEDERATED_REFRESH', 'PIA-*']:
    assert forbidden not in t, forbidden
print('Task 2 contract assertions PASS')
PY
```

Expected: `Task 2 contract assertions PASS`.

- [ ] **Step 6: Update FC01–FC10 status rows with exact owning-section evidence**

Mark only rows actually closed by this task as `CLOSED`; leave others open.

- [ ] **Step 7: Commit**

```bash
git add references/session-orchestration.md \
        tests/federated-product-audit-coordination-validation.md
git commit -m "feat: define federated product startup coordination"
```

---

### Task 3: Extend Product contract with stable child barrier, derived readiness, and exact baseline acceptance

**Files:**
- Modify: `references/product-multi-project-review.md`

**Interfaces:**
- Consumes: frozen coordination plan from Task 2 and existing Product identity/revision/membership/baseline semantics.
- Produces: child readiness composition rules, stable checkpoints, Product baseline candidate requirements, final exact requalification, logical workspace namespace rules.

- [ ] **Step 1: Define qualified child reuse and stable checkpoint**

Add explicit reuse qualification for independently-created child audits:

```text
Project identity
repository/source identity
selected scope
exact source binding
accepted owner identity/revision
lineage/provenance
semantic freshness for the consuming dependency
coverage/required scope
availability/limitations
Product/member qualification at consumption time
```

Define stable checkpoint fields:

```text
member/project key
coordination_plan_ref
exact analyzed source binding
accepted owner revisions/results consumed
requested dependency/output coverage
limitations
completion/provenance trace
```

- [ ] **Step 2: Define derived dependency/output readiness**

Use a derived presentation view only. Make explicit:

```text
Architecture Review / Test Engineering / Code Quality Review = capabilities
STM = technical-model dependency
TD = projection/output dependency
REUSE_READY / UPDATED_READY / PARTIAL_USABLE / UNAVAILABLE / BLOCKED = coordination views only
```

No universal Product `PARTIAL`/`BLOCKED` semantic state is created.

- [ ] **Step 3: Bind Product baseline candidate to frozen plan**

Require every candidate baseline to include:

```text
product_id
accepted product_revision
coordination_plan_ref
membership_snapshot_ref
exact qualified member/source vector
availability/dirty/noncanonical limitations
qualified accepted owner refs needed by consuming Product work
```

A candidate may not combine results from different coordination plans or Product revisions.

- [ ] **Step 4: Add exact pre-acceptance requalification**

Immediately before Product Baseline Acceptance re-check:

```text
product_id / selected accepted Product revision
membership snapshot / selected member set
base Product baseline when applicable
Project/repository/scope qualification
intended source binding
actual completed child source binding
accepted owner revisions/results used
requested work / authorization scope
relevant availability and dirty/noncanonical limitations
```

If any acceptance-relevant binding moved, invalidate/supersede the candidate and route to bounded requalification/replan.

State the exact race case:

```text
child completed at B; source now C
→ B is not current C
→ requalify/replan
→ B only allowed when explicitly selected as exact historical binding and policy permits
```

- [ ] **Step 5: Align workspace namespace**

Preserve:

```text
working/INDEX.md
working/products/<PROD-key>/
```

as the logical coordinator/Product namespace. Physical workspace may live under a Coordination Root or elsewhere, but Product identity and history cannot depend on that path. Multiple Products under one root use separate `<PROD-key>` namespaces. Do not introduce a second Product `INDEX.md` authority.

- [ ] **Step 6: Run Task 3 focused assertion**

```bash
python3 - <<'PY'
from pathlib import Path
t = Path('references/product-multi-project-review.md').read_text()
need = [
  'coordination_plan_ref',
  'membership_snapshot_ref',
  'exact source binding',
  'working/products/<PROD-key>/',
  'working/INDEX.md',
  'PARTIAL_USABLE',
]
missing = [x for x in need if x not in t]
assert not missing, missing
assert 'Product STM' not in t
print('Task 3 contract assertions PASS')
PY
```

- [ ] **Step 7: Update FC06–FC11, FC18–FC22 rows with exact evidence and commit**

```bash
git add references/product-multi-project-review.md \
        tests/federated-product-audit-coordination-validation.md
git commit -m "feat: define federated product baseline coordination"
```

---

### Task 4: Define deterministic bottom-up Product routing and derived impact semantics

**Files:**
- Modify: `references/revalidation-and-freshness.md`
- Modify: `references/product-multi-project-review.md`

**Interfaces:**
- Consumes: exact accepted Product baseline and independently advanced qualified child authority.
- Produces: deterministic accepted-state vs candidate-assessment routing and bounded impact result without new authority.

- [ ] **Step 1: Define bottom-up accepted-state update route**

For:

```text
PB-N has backend @ A
backend independently reaches accepted B
```

state explicitly:

```text
qualified local B may satisfy child readiness
Product adoption does not happen directly
accepted-state update -> Product REVALIDATE over pinned PB-N and candidate vector
```

Do not allow `ADOPT_CHILD_UPDATE -> PB advance` as a shortcut.

- [ ] **Step 2: Define candidate-assessment route**

When user requests read-only candidate assessment:

```text
create new Product CHANGE_REVIEW
base = complete exact accepted Product vector
candidate = complete exact candidate Product vector
```

An older Product CR is not reusable when the complete vector / Product revision / member qualification differs. `RECONCILE_CHANGE` is available only after normal completed-review reuse/base-binding/material-delta/owner gates.

- [ ] **Step 3: Define Product impact as derived routing**

Use existing dependency/freshness/capability owners:

```text
member/source/accepted-authority advancement
→ changed authoritative scope
→ existing dependency traversal
→ existing Product REVALIDATE / owner adjudication
→ derived UNAFFECTED | AFFECTED | UNKNOWN_IMPACT
→ minimum bounded follow-up
```

Add explicit prohibitions:

```text
no PIA-* semantic family
no Product impact authority
no new dependency authority
no new Product freshness lifecycle
```

`UNAFFECTED` requires sufficient accepted evidence. Missing/incomplete dependency coverage returns `UNKNOWN_IMPACT`.

- [ ] **Step 4: Preserve source advancement vs semantic-authority advancement distinction**

Document both axes independently so a new Architecture/CQ/TE accepted revision on the same source commit does not masquerade as a source baseline change.

- [ ] **Step 5: Run Task 4 focused assertion**

```bash
python3 - <<'PY'
from pathlib import Path
t = '\n'.join([
  Path('references/revalidation-and-freshness.md').read_text(),
  Path('references/product-multi-project-review.md').read_text(),
])
need = [
  'UNKNOWN_IMPACT',
  'Product REVALIDATE',
  'complete exact candidate Product vector',
  'no `PIA-*`',
]
missing = [x for x in need if x not in t]
assert not missing, missing
print('Task 4 contract assertions PASS')
PY
```

- [ ] **Step 6: Update FC12–FC17, FC23–FC24 rows and commit**

```bash
git add references/revalidation-and-freshness.md \
        references/product-multi-project-review.md \
        tests/federated-product-audit-coordination-validation.md
git commit -m "feat: route federated product updates through existing change semantics"
```

---

### Task 5: Integrate coordinator state and skill entrypoint without adding a new lifecycle

**Files:**
- Modify: `references/review-modes-and-orchestration.md`
- Modify: `SKILL.md`

**Interfaces:**
- Consumes: Task 2 Product Coordination Plan fields and Task 3 baseline/ready-state semantics.
- Produces: resume-critical coordinator serialization and user-visible routing from the umbrella skill.

- [ ] **Step 1: Extend coordinator state serialization**

In `references/review-modes-and-orchestration.md`, add Product coordination fields only as coordinator/orchestration state under existing `working/INDEX.md` ownership. Persist references to:

```text
coordination_plan_ref
selected_product_revision
membership_snapshot_ref
base_product_baseline_ref
selected child actions
child checkpoint refs
Product baseline candidate ref
limitations
```

Do not create a new coordinator authority or a second INDEX.

- [ ] **Step 2: Add resume rules**

On resume, the coordinator must re-load the frozen plan and compare current Product/member/source context. A mismatch must not mutate the old plan; it routes to bounded requalification/replan.

- [ ] **Step 3: Update umbrella entrypoint**

In `SKILL.md`, add concise Product coordination routing for a non-Git parent directory while preserving explicit Product opt-in. User requests such as:

```text
покажи состояние продукта
обнови существующие дочерние аудиты
доведи весь продукт до актуального аудита
покажи влияние изменений backend
я уже обновил backend отдельно, подхвати изменения
```

must normalize to existing Product/requested-work/child intent semantics, never to new persisted intents.

- [ ] **Step 4: Add no-mega-audit rule**

State that a broad Product request from a Coordination Root first resolves membership + plan and does not silently interpret every discovered repository as a member or full-audit target.

- [ ] **Step 5: Run Task 5 focused assertion**

```bash
python3 - <<'PY'
from pathlib import Path
t = Path('references/review-modes-and-orchestration.md').read_text() + '\n' + Path('SKILL.md').read_text()
for x in ['coordination_plan_ref', 'membership_snapshot_ref', 'Coordination Root']:
    assert x in t, x
for x in ['FEDERATED_REFRESH', 'FEDERATED_REVALIDATE', 'PRODUCT_AUDIT_COORDINATION']:
    assert x not in t, x
print('Task 5 integration assertions PASS')
PY
```

- [ ] **Step 6: Commit**

```bash
git add references/review-modes-and-orchestration.md SKILL.md \
        tests/federated-product-audit-coordination-validation.md
git commit -m "feat: integrate federated product coordination routing"
```

---

### Task 6: Close pressure scenarios and backward compatibility

**Files:**
- Modify: `tests/federated-product-audit-coordination-validation.md`
- Modify: `tests/federated-product-audit-coordination-backward-compatibility.md`

**Interfaces:**
- Consumes: all normative changes from Tasks 2–5.
- Produces: deterministic closure evidence that the implementation satisfies the approved design without breaking existing semantics.

- [ ] **Step 1: Add targeted race/vector scenarios**

Add explicit PASS rows for:

```text
PV01 Product revision changes during child execution -> old plan remains frozen; no mixed aggregation
PV02 child finishes B, source advances C -> exact requalification; B != current C
PV03 independently updated child A->B -> child reuse + Product REVALIDATE/new vector CR only
PV04 one monorepo, two Projects -> scopes remain separate
PV05 one Project, two repos -> one member with binding set
PV06 symlink/worktree aliases -> bounded discovery, no path-based duplicate membership
PV07 incomplete dependency coverage -> UNKNOWN_IMPACT
PV08 all children current, Product relations/projections stale -> freshness remains independent
PV09 overlapping writer scope -> serialize conflicting writes
PV10 Coordination Root moves -> Product identity/history unchanged
```

- [ ] **Step 2: Close FC01–FC24 only with exact normative citations**

Each `CLOSED` row must name the exact owning reference section/mechanism. No row may close merely because the design spec says so.

- [ ] **Step 3: Validate immutable semantic sets**

Run:

```bash
python3 - <<'PY'
from pathlib import Path
s = Path('references/session-orchestration.md').read_text()
for intent in ['USE_EXISTING','NEW','RESUME','REVALIDATE','EXTEND','CHANGE_REVIEW','PROJECTION_REPAIR']:
    assert intent in s, intent
assert 'RECONCILE_CHANGE' in s
skill = Path('SKILL.md').read_text()
for cap in ['Architecture Review','Test Engineering','Code Quality Review']:
    assert cap in skill, cap
print('semantic-set assertions PASS')
PY
```

- [ ] **Step 4: Run regression search for forbidden architecture drift**

```bash
rg -n "FEDERATED_[A-Z_]+|Product STM|PIA-\*.*authority|automatic.*projection regeneration|filesystem containment.*membership" \
  SKILL.md references tests/federated-product-audit-coordination-*.md
```

Expected: no new federated intent/capability/authority terms. Any positive hit must be manually inspected; explicit prohibition text is allowed.

- [ ] **Step 5: Cross-check Change Review compatibility**

Verify that the new Product routing does not contradict `tests/change-review-baseline-reconciliation-validation.md`, especially full-vector Product reuse and contextual `RECONCILE_CHANGE` gates.

- [ ] **Step 6: Commit**

```bash
git add tests/federated-product-audit-coordination-validation.md \
        tests/federated-product-audit-coordination-backward-compatibility.md
git commit -m "test: close federated product coordination scenarios"
```

---

### Task 7: Update practical guidance and run final verification

**Files:**
- Modify: `docs/guides/reuse-and-change.md`
- Verify: all files from Tasks 2–6

**Interfaces:**
- Consumes: implemented normative semantics.
- Produces: user-facing Product coordination workflow plus final implementation evidence.

- [ ] **Step 1: Add practical Product coordination section**

Explain the two supported directions:

```text
TOP-DOWN
Product detects stale/changed child
→ Product Coordination Plan
→ existing child workflow
→ stable accepted child result
→ Product exact-vector requalification
→ Product baseline acceptance
→ bounded Product impact/review

BOTTOM-UP
child independently audited
→ Product later discovers accepted advancement
→ qualify local authority
→ Product REVALIDATE or new full-vector CHANGE_REVIEW
→ explicit Product baseline acceptance
```

Include the non-Git root example and explicitly state that filesystem layout does not define Product membership.

- [ ] **Step 2: Add concise status example**

Use a derived status table such as:

```text
Member     Current source   Local accepted source   Product binding   Recommended route
backend    B                B                       A                 Product revalidation candidate
frontend   F1               F1                      F1                none
shared     S2               S1                      S1                child revalidation/change review
```

Do not label this table as semantic authority.

- [ ] **Step 3: Run placeholder and contradiction scan**

```bash
rg -n "TBD|TODO|FIXME|implement later|FEDERATED_(REFRESH|REVALIDATE)|Product STM" \
  SKILL.md references/session-orchestration.md \
  references/review-modes-and-orchestration.md \
  references/product-multi-project-review.md \
  references/revalidation-and-freshness.md \
  docs/guides/reuse-and-change.md \
  tests/federated-product-audit-coordination-*.md
```

Expected: no unresolved placeholders or new forbidden semantic constructs. Explicit negative examples/prohibitions must be manually distinguished from implementation terms.

- [ ] **Step 4: Run final contract assertions**

```bash
python3 - <<'PY'
from pathlib import Path
paths = [
 'SKILL.md',
 'references/session-orchestration.md',
 'references/review-modes-and-orchestration.md',
 'references/product-multi-project-review.md',
 'references/revalidation-and-freshness.md',
 'tests/federated-product-audit-coordination-validation.md',
 'tests/federated-product-audit-coordination-backward-compatibility.md',
]
text = '\n'.join(Path(p).read_text() for p in paths)
required = [
 'Coordination Root',
 'coordination_plan_ref',
 'membership_snapshot_ref',
 'working/products/<PROD-key>/',
 'UNKNOWN_IMPACT',
 'Product REVALIDATE',
]
missing = [x for x in required if x not in text]
assert not missing, missing
for bad in ['FEDERATED_REVALIDATE', 'FEDERATED_REFRESH']:
    assert bad not in text, bad
print('FINAL FEDERATED PRODUCT CONTRACT CHECK PASS')
PY
```

- [ ] **Step 5: Verify git scope**

```bash
git status --short
git diff --stat <implementation-base>..HEAD
git diff --name-only <implementation-base>..HEAD
```

Expected modified/created scope only:

```text
SKILL.md
references/session-orchestration.md
references/review-modes-and-orchestration.md
references/product-multi-project-review.md
references/revalidation-and-freshness.md
docs/guides/reuse-and-change.md
tests/federated-product-audit-coordination-validation.md
tests/federated-product-audit-coordination-backward-compatibility.md
```

Any additional file requires explicit justification and review before completion.

- [ ] **Step 6: Commit guidance/final verification state**

```bash
git add docs/guides/reuse-and-change.md
git commit -m "docs: explain federated product audit coordination"
```

---

## 4. Final acceptance checklist

Before claiming implementation complete, verify all of the following:

```text
[ ] Coordination Root is locator only.
[ ] Existing Product membership is primary; discovery only validates/finds candidates.
[ ] Discovery is bounded and identity-safe for symlink/worktree/submodule/nested cases.
[ ] No new Session Intent or capability exists.
[ ] Product Coordination Plan is frozen before dispatch.
[ ] Aggregate Product confirmation does not bypass local owner gates.
[ ] Independent child tasks are parallel only when writer scopes do not conflict.
[ ] Stable checkpoints are exact and plan-bound.
[ ] Readiness is derived per dependency/output, not a new semantic state.
[ ] Product baseline candidate is exact-vector and plan-bound.
[ ] Exact requalification occurs immediately before Product Baseline Acceptance.
[ ] B cannot be represented as current C after source advancement.
[ ] Independently advanced child authority cannot directly advance Product state.
[ ] Product accepted-state update uses Product REVALIDATE.
[ ] Product candidate assessment uses a new complete-vector Product CHANGE_REVIEW where vectors differ.
[ ] RECONCILE_CHANGE remains contextual/proof-gated.
[ ] Product impact is derived from existing owners; no PIA-* authority exists.
[ ] Incomplete dependency coverage produces UNKNOWN_IMPACT.
[ ] Product cross-project technical facts remain STM/Technical Model Gate-owned.
[ ] Single working/INDEX.md authority and working/products/<PROD-key>/ namespace are preserved.
[ ] No automatic projection regeneration exists.
[ ] Single-project and existing Product behavior remain backward compatible.
[ ] All FC/PV/BC validation rows close with exact normative evidence.
```

## 5. Implementation review boundary

After Tasks 1–7 are complete and all checks pass, stop before promotion/merge. Run an independent implementation review focused on:

- authority boundaries;
- frozen plan and race handling;
- complete-vector bottom-up routing;
- discovery identity safety;
- derived impact/readiness semantics;
- backward compatibility;
- no hidden runtime/harness expansion.

Do not update roadmap/current-status or promote to `main` until implementation review/remediation is complete and explicitly approved.
