# API Input Robustness & Boundary Validation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use
> checkbox (`- [ ]`) syntax for tracking.

**Goal:** Extend the existing Code Quality and Test Engineering workflows to
review API input boundaries and generate bounded negative/boundary cases while
preserving existing Stage F, Product, authorization, and runtime boundaries.

**Architecture:** Stage F and STM continue to own accepted API/interface facts
and evidence. Code Quality adds implementation-quality findings over those
facts, while Test Engineering adds what-must-be-proven boundary cases using its
existing behavior, assurance, and execution-evidence semantics. The extension
uses controlled category attributes and existing identities rather than a new
capability, fact family, compatibility authority, or runtime subsystem.

**Tech Stack:** Markdown contracts and references, existing `IF-*`, `WS-*`,
`EV-*`, `CQ-*`, `CQRA-*`, `BC-*`, `TM-*`, `GAP-*`, and `CC-*` semantics, bounded
`rg`/inspection validation, Git.

**Spec:** `docs/superpowers/specs/2026-09-09-api-input-robustness-boundary-validation-design.md`

## Global Constraints

- THE CANONICAL PLAN WINS.
- Implementation starts from the published plan checkpoint
  `467f2af8eceafe0860e1a9edc1210ce846c31a80` in one future worktree.
- Before executing any block, read this canonical plan and extract the block
  title, exact files, semantic changes, verification, commit subject, and
  final review gate. A conflicting prompt requires `IMPLEMENTATION_PROMPT_PLAN_MISMATCH`
  and stops execution.
- Preserve exactly three top-level semantic capabilities: Architecture Review,
  Test Engineering, and Code Quality Review.
- Stage F/STM remains `WHAT EXISTS`; Code Quality remains
  `WHAT IS POORLY / UNSAFELY IMPLEMENTED`; Test Engineering remains
  `WHAT MUST BE PROVEN`.
- `requested_work != resolved_work`; internal STM, evidence, Product
  qualification, Behavior Model, and Contract Verification dependencies do not
  become selected capabilities.
- Keep transport/container limits distinct from schema/field limits and reason
  in the order request → ingress/container limit → parsing/materialization →
  schema validation → business processing.
- Never infer server enforcement from frontend validation, an OpenAPI
  declaration, a field limit, an undocumented framework default, or a proxy
  limit on an unqualified path.
- Never invent a universal numeric boundary. Unknown thresholds remain
  unresolved and produce a boundary-establishment requirement.
- `DEFINED`/`ACCEPTED` test-case planning states do not imply `EXECUTED`,
  `TESTED`, `PASSED`, `FAILED`, `OBSERVED`, or `VERIFIED_AT_RUNTIME`.
- `accepted_test_case != executed_test != tested_result`; only accepted,
  qualified execution evidence may support `TESTED` under existing TE rules.
- Stage F `TESTED` views and Product-wide tested claims require qualified
  execution evidence; generated or accepted cases cannot populate them.
- Runtime execution, active fuzzing, DAST, payload submission, 2 GiB request
  generation, load testing, endpoint crawling, and environment provisioning
  remain `UNAVAILABLE`.
- Product is optional; single-Project behavior remains first-class. Product
  membership grants no source, test, runtime, write, or deployment permission.
- Historical Stage F, CQ, TE, Product, projection, and compatibility records
  are not rewritten. Migration remains `COMPATIBLE_EXTENSION`.
- Do not create a new harness, parser, DSL, scanner framework, runtime engine,
  identity family, individual scenario files, or individual pressure files.
- Exactly three implementation commits are expected, one per block. Do not
  create intermediate independent review gates; perform one final independent
  implementation review after Block C.

## Exact implementation surface

This inventory is based on the current ownership contracts and prior
documentation-driven validation convention. `READ_ONLY` files are required
inputs, not implementation targets.

| Path | Action | Owner | Reason | Block |
|---|---|---|---|---|
| `capabilities/code-quality-review/SKILL.md` | `MODIFY` | Code Quality | Register API input robustness as an existing CQ review aspect and preserve CQ ownership/runtime limits. | A |
| `capabilities/code-quality-review/references/code-quality-contract.md` | `MODIFY` | Code Quality | Define the controlled CQ classes, evidence fields, two-layer implementation interpretation, and context-dependent severity using existing `CQ-*`. | A |
| `capabilities/test-review/SKILL.md` | `MODIFY` | Test Engineering | Register API boundary cases as existing Test Engineering output/assurance work and preserve unavailable execution. | B |
| `capabilities/test-review/references/test-engineering-contract.md` | `MODIFY` | Test Engineering | Define generated case shape, type-aware boundary generation, execution-evidence separation, Stage F protection, and Product qualification. | B |
| `references/shared-technical-model.md` | `MODIFY` | Technical Model Gate / Stage F | Add only the minimal optional boundary/evidence cross-reference on existing `IF-*` facts; preserve `observed_view`, precision, and accepted-fact ownership. | C |
| `references/technical-documentation.md` | `MODIFY` | Stage F projection owner | Describe boundary metadata as derived, qualified content and prevent generated cases from populating factual `TESTED` views or creating projection identities. | C |
| `references/product-multi-project-review.md` | `MODIFY` | Product Context / existing owners | State Project/baseline-qualified boundary evidence and prohibit Product-wide test inference from partial members. | C |
| `tests/api-input-robustness-boundary-validation-contract-validation.md` | `CREATE` | Integrated validation | Store immutable pre-change evidence, focused checks, 34 acceptance rows, 22 pressure rows, and final result counts in the established Markdown test convention. | C |
| `tests/api-input-robustness-boundary-validation-backward-compatibility.md` | `CREATE` | Integrated validation | Verify additive migration, historical fact readability, optional Product, authorization, redaction, lifecycle, and unavailable runtime boundaries. | C |

No other file is in implementation scope. In particular, `SKILL.md` at the
repository root is read for authority context but is not modified because the
capability references already own the required CQ/TE semantics and the new
feature must not duplicate umbrella prose.

## Pre-change fail-first evidence

Before the first normative edit, Block C's validation artifact must capture the
following eight rows as immutable historical evidence. Use bounded `rg` and
exact section inspection against the pre-change checkpoint; do not infer the
result retrospectively.

| ID | Pre-change check | Required pre-change gap |
|---|---|---|
| FF-API-01 | Search CQ contracts for request-body/container limits separately from field constraints. | No API CQ rule independently classifies a missing transport/body limit. |
| FF-API-02 | Inspect the existing API/field evidence wording and validation order. | A field `maxLength` can coexist with unknown pre-materialization body protection without explicit CQ classification. |
| FF-API-03 | Search CQ contract and existing Stage F evidence mappings for schema-bypass classification. | Declared schema validation can be bypassed without an explicit CQ boundary class. |
| FF-API-04 | Search TE contracts for API boundary dimensions and deterministic below/at/above generation. | TE has no API-specific boundary-generation semantics. |
| FF-API-05 | Search TE contracts for unknown-bound handling. | The current model does not explicitly prohibit inventing a numeric threshold for an unknown limit. |
| FF-API-06 | Search TE and Stage F contracts for case acceptance versus execution/tested result. | API boundary cases can be confused with `TESTED` without the new explicit separation. |
| FF-API-07 | Search Stage F `observed_view` rules and API routing references. | Generated API cases are not explicitly prohibited from populating `TESTED`. |
| FF-API-08 | Search Product Test Review scope and execution qualification. | Product-qualified `TESTED` boundary evidence is not explicit for this extension. |

The artifact must label all eight rows `FAIL_FIRST_VALID` or an equivalent
existing repository status before Block A. If any premise cannot be
reproduced, stop implementation and record the exact changed premise.

## Block A — Code Quality API Boundary Review Semantics

**Files:** modify only the two Code Quality files in the inventory.

**Owns:** CQ implementation-quality interpretation of API input boundaries.
Stage F/STM observations remain inputs, and accepted `CQ-*` remains the only
Code Quality semantic authority.

**Required semantic changes:**

- Add API input robustness as a CQ review aspect, without adding a capability
  or API fact authority.
- Reuse one controlled `boundary_category` attribute with the design's
  categories, including `REQUEST_BODY_SIZE`, `STRING_LENGTH`,
  `COLLECTION_SIZE`, `NUMERIC_RANGE`, `NESTING_DEPTH`, `UPLOAD_SIZE`,
  `MULTIPART_LIMITS`, `HEADER_LIMITS`, `QUERY_LIMITS`, `COOKIE_LIMITS`,
  `CONTENT_TYPE`, `MALFORMED_PAYLOAD`, `UNEXPECTED_FIELDS`,
  `SCHEMA_ENFORCEMENT`, `VALIDATION_ORDER`, `PARSER_RESOURCE_EXHAUSTION`,
  `COMPRESSION_EXPANSION`, and `PAGINATION_LIMITS`.
- Add the controlled CQ finding classifications:
  `MISSING_REQUEST_SIZE_LIMIT`, `UNBOUNDED_STRING`,
  `UNBOUNDED_COLLECTION`, `UNBOUNDED_UPLOAD`, `SCHEMA_NOT_ENFORCED`,
  `VALIDATION_AFTER_MATERIALIZATION`, `UNEXPECTED_FIELD_ACCEPTANCE`,
  `PARSER_RESOURCE_EXHAUSTION`, `UNBOUNDED_PAGINATION`,
  `UNBOUNDED_NUMERIC_INPUT`, `UNBOUNDED_NESTING`, `UNBOUNDED_MULTIPART`,
  and `COMPRESSION_EXPANSION_RISK`.
- Define findings using existing CQ fields plus exact interface/input location,
  boundary category, observed state, expected boundary, evidence, impact,
  recommendation, severity, source/baseline binding, and provenance.
- Distinguish `DECLARED`, `IMPLEMENTED`, and `TESTED` evidence. A declaration
  is not enforcement; a frontend hint is not server evidence; a generated or
  accepted TE case is not tested evidence.
- Make the two-layer reasoning explicit. A field constraint with unknown body
  limit and buffering before validation yields field evidence plus unresolved
  transport/resource protection, never `SAFE` by implication.
- Classify missing bound, implausibly broad bound, declared-but-unenforced,
  unknown enforcement, and unsafe validation order without inventing a business
  threshold. Keep severity evidence/context dependent.
- Add static, framework-agnostic review patterns for parser/container limits,
  buffering order, upload/multipart limits, schema bypass, frontend-only
  validation, unknown fields, pagination/numeric ranges, nesting, and
  decompression expansion. Tool output remains candidate/evidence, not a CQ
  finding by itself.

**Execution steps:**

- [ ] Read the approved design and the existing CQ authority, accepted finding,
  lifecycle, evidence, Product, and tooling sections before editing.
- [ ] Add the API boundary aspect and ownership boundary to
  `capabilities/code-quality-review/SKILL.md`, including the unsupported
  runtime boundary and links to the detailed contract.
- [ ] Add the controlled category/class vocabulary and finding structure to
  `capabilities/code-quality-review/references/code-quality-contract.md`.
- [ ] Add explicit examples for `maxLength: 255` with an unknown transport
  limit, frontend-only `maxlength`, OpenAPI bypass, proxy/direct ingress,
  framework-default uncertainty, and streaming upload.
- [ ] Add context-dependent HIGH/MEDIUM/LOW guidance without making every
  missing bound HIGH and without creating a security authority.
- [ ] Run focused static checks for all required classes, both boundary layers,
  `DECLARED`/`IMPLEMENTED`/`TESTED`, unknown enforcement, no arbitrary limit,
  and unchanged CQ identity/lifecycle ownership.
- [ ] Run `git diff --check` and inspect that only Block A files changed.
- [ ] Commit exactly the Block A files with:
  `docs: add Code Quality API boundary semantics`.

**Block A verification:**

```text
rg -n "MISSING_REQUEST_SIZE_LIMIT|UNBOUNDED_STRING|UNBOUNDED_COLLECTION|UNBOUNDED_UPLOAD|SCHEMA_NOT_ENFORCED|VALIDATION_AFTER_MATERIALIZATION|UNEXPECTED_FIELD_ACCEPTANCE|PARSER_RESOURCE_EXHAUSTION|UNBOUNDED_PAGINATION|UNBOUNDED_NUMERIC_INPUT|UNBOUNDED_NESTING|UNBOUNDED_MULTIPART|COMPRESSION_EXPANSION_RISK" capabilities/code-quality-review/SKILL.md capabilities/code-quality-review/references/code-quality-contract.md
rg -n "REQUEST_BODY_SIZE|SCHEMA / FIELD|TRANSPORT / CONTAINER|DECLARED|IMPLEMENTED|TESTED|ENFORCEMENT_UNKNOWN|VALIDATION_ORDER_UNKNOWN|no universal|frontend|proxy|materialization" capabilities/code-quality-review/SKILL.md capabilities/code-quality-review/references/code-quality-contract.md
```

Expected result: all required terms and examples are present, CQ remains the
finding owner, no new factual/semantic capability appears, and the focused
diff is clean.

## Block B — Test Engineering Boundary / Negative Test Semantics

**Files:** modify only the two Test Engineering files in the inventory.

**Owns:** what must be proven for API input boundaries, using existing TE
behavior/assurance/evidence semantics and no runtime runner.

**Required semantic changes:**

- Add generated negative/boundary cases with the exact fields: case ID,
  qualified interface, input location, controlled dimension, precondition,
  type-aware input strategy, expected acceptance/rejection, expected stage when
  known, evidence basis, open assumptions, and existing execution status.
- Use the existing TE semantic records and `NEG-API-*` only as a case-key
  convention; do not create an identity family.
- Generate deterministic below/at/above values for exact string, array/body,
  upload, numeric, pagination, and other type-appropriate limits; include enum
  valid/invalid and required/null/absent distinctions only when the contract
  supports them.
- For unknown thresholds, generate `ESTABLISH_BOUNDARY` or the equivalent
  existing TE requirement, with no invented numeric value.
- Make the invariant normative:
  `accepted_test_case != executed_test != tested_result` and
  `expected_result != observed_result`. Defined/accepted planning states do not
  imply execution, pass/fail, observation, or runtime verification.
- Require actual accepted execution evidence, with the existing TE bindings for
  test/result record, environment, baseline, timestamp, result, and provenance,
  before a boundary may be represented as `TESTED`.
- Explicitly prevent generated or accepted cases from populating Stage F
  `TESTED` views. Product claims require exact Project/baseline qualification;
  one tested Project does not make another Project or a Product tested.
- Preserve runtime execution and fuzzing as `UNAVAILABLE`, and keep Contract
  Verification/CC as the existing compatibility authority.

**Execution steps:**

- [ ] Read the approved design and the existing TE behavior, assurance,
  Contract Verification, Product scope, and output sections before editing.
- [ ] Add API boundary dimensions and generated-case routing to
  `capabilities/test-review/SKILL.md` without making a new output authority.
- [ ] Add the case shape and exact-known/unknown-bound generation rules to
  `capabilities/test-review/references/test-engineering-contract.md`.
- [ ] Add the case-state/evidence separation and examples: length 256 for
  `maxLength=255`, body above 1 MiB as an expected pre-materialization
  rejection, no execution result, and accepted external execution evidence.
- [ ] Add Stage F `TESTED` protection and Product Project/baseline qualification
  rules while preserving `IF-*` roles and `observed_view` semantics.
- [ ] Add explicit negative cases for content type, malformed payload,
  unexpected fields, nesting, multipart, compression expansion, pagination,
  upload, and request-body boundaries.
- [ ] Run focused static checks for the state inequality, execution-evidence
  requirement, unknown-bound handling, all required dimensions, runtime
  `UNAVAILABLE`, and unchanged TE/CC ownership.
- [ ] Run `git diff --check` and inspect that only Block B files changed.
- [ ] Commit exactly the Block B files with:
  `docs: add API boundary test semantics`.

**Block B verification:**

```text
rg -n "accepted_test_case != executed_test != tested_result|accepted_test_case|expected_result != observed_result|DEFINED|ACCEPTED|EXECUTED|TESTED|PASSED|FAILED|OBSERVED|VERIFIED_AT_RUNTIME" capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md
rg -n "REQUEST_BODY_SIZE|STRING_LENGTH|COLLECTION_SIZE|NUMERIC_RANGE|UPLOAD_SIZE|PAGINATION_LIMITS|CONTENT_TYPE|MALFORMED_PAYLOAD|UNEXPECTED_FIELDS|NESTING_DEPTH|MULTIPART_LIMITS|COMPRESSION_EXPANSION|UNAVAILABLE|Stage F.*TESTED|Product.*baseline" capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md
```

Expected result: cases remain `WHAT MUST BE PROVEN`, `TESTED` requires
qualified execution evidence, and no planning artifact can assert runtime
behavior.

## Block C — Stage F Integration + Integrated Validation

**Files:** modify the three Stage F/Product references and create the two
validation artifacts in the inventory.

**Owns:** minimal factual/projection integration, exact qualification, and
complete bounded validation. It does not create a Stage F boundary fact family.

**Required semantic changes:**

- Add only optional boundary/evidence cross-references to existing `IF-*`
  structures and selectors. The Technical Model Gate remains the sole writer
  of accepted factual semantics; old IF records without boundary metadata stay
  valid with absent/unknown fields.
- Make Stage F rendering expose qualified boundary evidence and limitations
  without deciding CQ safety or accepting TE results. Generated/accepted cases
  cannot populate `observed_view: TESTED`.
- Preserve exact Project/repository/revision/baseline qualification and Product
  optionality. Product views retain per-member evidence and never infer a
  Product-wide tested state from one member.
- Create the immutable pre-change evidence and the focused/integrated results
  in the two established Markdown validation files. Do not create 34 scenario
  files, 22 pressure files, a parser, runner, or harness.

**Execution steps:**

- [ ] Read the approved design, current Stage F selector/rendering/compatibility
  contracts, Product qualification contract, and prior `tests/*validation.md`
  conventions.
- [ ] Capture FF-API-01 through FF-API-08 in
  `tests/api-input-robustness-boundary-validation-contract-validation.md`
  before modifying any normative contract. Mark the section immutable.
- [ ] Add the minimal Stage F interface/evidence cross-reference to
  `references/shared-technical-model.md`; do not alter IF identity, lifecycle,
  role/view matrix, precision, or Technical Model Gate ownership.
- [ ] Add Stage F rendered-content and `TESTED`-view protection to
  `references/technical-documentation.md`; keep boundary categories as
  attributes/evidence, not projection identities.
- [ ] Add exact Product/baseline qualification and no Product-wide inference to
  `references/product-multi-project-review.md`; preserve membership and
  authorization boundaries.
- [ ] Append focused post-change checks to the contract-validation artifact for
  the two-layer 2 GiB case, weak/declaration/framework/proxy evidence,
  generated-vs-tested state, Stage F protection, Product qualification, and
  runtime unavailability.
- [ ] Add the 34-row acceptance matrix and 22-row pressure matrix below to the
  contract-validation artifact, with one concrete command/inspection and one
  expected result per row.
- [ ] Add the backward-compatibility checks to
  `tests/api-input-robustness-boundary-validation-backward-compatibility.md`.
- [ ] Run all integrated checks and require `34/34` acceptance,
  `22/22 PREVENTED` pressure, no ambiguous/failing rows, preserved authority,
  `COMPATIBLE_EXTENSION`, and `DO_NOT_BUILD_HARNESS`.
- [ ] Run `git diff --check` and inspect the complete Block C diff against the
  exact inventory.
- [ ] Commit exactly the Block C files with:
  `test: validate API input boundary integration`.

**Block C verification:**

```text
rg -n "FF-API-0[1-8]|34/34|22/22|REQUEST_BODY_SIZE|SCHEMA / FIELD|TESTED|UNAVAILABLE|COMPATIBLE_EXTENSION|DO_NOT_BUILD_HARNESS" tests/api-input-robustness-boundary-validation-contract-validation.md
rg -n "historical|old.*revision|Product|baseline|authorization|redaction|projection lifecycle|COMPATIBLE_EXTENSION|UNAVAILABLE" tests/api-input-robustness-boundary-validation-backward-compatibility.md
git diff --check
```

Expected result: the artifacts contain pre-change evidence, concrete post-
change checks, every mapped row, and no claim of runtime execution where none
exists.

## Acceptance matrix — 34/34 mapped

Each row is owned by the indicated block and must contain the listed concrete
verification plus the expected observable result in the validation artifact.

| ID | Owner | Concrete verification | Expected result |
|---|---|---|---|
| A01 | A | Inspect CQ rule for exact string bound and enforcement evidence. | Declaration/implementation distinction preserved; no false missing-bound finding. |
| A02 | A | Inspect CQ output for absent string bound with context fields. | `UNBOUNDED_STRING` only with contextual evidence; no invented limit. |
| A03 | A | Compare field-bound evidence with absent request-body limit. | Field known; transport enforcement unknown; no safe conclusion. |
| A04 | A | Walk request → materialization → schema validation and inspect CQ class. | 2 GiB pre-validation buffering yields ordering/body risk; no runtime payload sent. |
| A05 | A | Compare lower body limit and higher field limit in two-layer record. | Both boundaries remain distinct and the early transport limit is visible. |
| A06 | A | Inspect collection category and item-count evidence. | Missing `maxItems` can yield `UNBOUNDED_COLLECTION` without universal policy. |
| A07 | A | Inspect pagination category and unknown threshold handling. | `UNBOUNDED_PAGINATION`/unresolved case; no fabricated numeric maximum. |
| A08 | A | Inspect upload handler evidence for byte/storage boundary. | Missing size can yield `UNBOUNDED_UPLOAD` with impact. |
| A09 | A | Compare UI `maxlength` evidence strength with backend evidence. | UI remains `WEAK_HINT`; server enforcement is not established. |
| A10 | A | Compare OpenAPI declaration against request-path validator evidence. | Bypass yields `SCHEMA_NOT_ENFORCED`; declaration remains Stage F fact. |
| A11 | B | Inspect accepted media types and generated wrong-content-type case. | Case expects media-type rejection when contract evidence supports it. |
| A12 | B | Inspect malformed-payload case and parser-stage field. | Parser rejection is expected; stage is `UNKNOWN` if not evidenced. |
| A13 | A | Compare unknown-field policy with implementation evidence. | `UNEXPECTED_FIELD_ACCEPTANCE` only when policy supports it. |
| A14 | A/B | Inspect nesting category and generated depth strategy. | Depth/resource protection is explicit or unresolved, never assumed. |
| A15 | A/B | Inspect multipart count/aggregate category and case strategy. | Missing limits remain findings/cases with no invented threshold. |
| A16 | A | Inspect compressed and expanded-size evidence separately. | `COMPRESSION_EXPANSION_RISK` when protection is not evidenced. |
| A17 | C | Inspect single-Project qualification fields in finding/case examples. | Review is valid without Product and retains exact Project/source binding. |
| A18 | C | Inspect Product-qualified finding/case fields and membership boundary. | Product is optional qualification; membership grants no permission. |
| A19 | B | Generate below/at/above candidates for an exact maximum. | Deterministic type-aware candidates are produced. |
| A20 | B | Inspect unknown numeric maximum case. | Boundary-establishment requirement remains unresolved; no number invented. |
| A21 | B | Inspect runtime-fuzzing route and execution status. | Runtime fuzzing is `UNAVAILABLE`; no active execution. |
| A22 | C | Inspect no-evidence route. | No interface/finding is fabricated; limitation is recorded. |
| A23 | B | Generate exact header/query/cookie size/count candidates. | Correct transport/query dimensions and exact bound cases are retained. |
| A24 | C | Inspect chunked/no-`Content-Length` path. | Aggregate streaming boundary is required or remains unknown; no false safety. |
| A25 | C | Inspect gateway/app path qualification. | Gateway evidence does not imply application enforcement. |
| A26 | A | Inspect late-deserialization evidence and CQ classification. | `VALIDATION_AFTER_MATERIALIZATION`/parser risk is reported when evidenced. |
| A27 | C | Inspect consumer/provider mismatch routing. | CC/Contract Verification owns compatibility; CQ boundary remains separate. |
| A28 | C | Compare streaming-upload and buffered-JSON records. | Limits are path-qualified and not generalized. |
| A29 | B | Inspect generated case with no execution evidence. | `DEFINED`/`ACCEPTED` only; not `TESTED`. |
| A30 | B | Inspect accepted case with no execution evidence. | Acceptance governs case planning only; not `TESTED`. |
| A31 | B | Inspect expected 413/schema response without result record. | Expected result does not imply pass/fail/tested. |
| A32 | B | Inspect accepted external execution evidence fields. | Existing TE semantics may derive `TESTED` only when qualified evidence exists. |
| A33 | C | Inspect one Product Project's executed result. | Result stays member/baseline qualified; no Product-wide inference. |
| A34 | C | Inspect generated case rendered beside Stage F interface view. | Case cannot populate Stage F `TESTED` factual view. |

## Pressure matrix — 22/22 mapped

Each row must be classified `PREVENTED`; a missing command, unresolved owner,
or inferred result is `AMBIGUOUS`, not a pass.

| ID | Owner | Failure prevented | Concrete verification | Expected result |
|---|---|---|---|---|
| P01 | A | Frontend-only validation treated as backend enforcement. | Inspect evidence-strength and frontend/server rule. | `WEAK_HINT` cannot establish implementation. |
| P02 | A | OpenAPI declaration hides validator bypass. | Compare declaration, path, and `SCHEMA_NOT_ENFORCED` rule. | Bypass remains a CQ finding candidate. |
| P03 | A | Framework default without deployed value is treated as limit. | Inspect default/config/deployment evidence fields. | Enforcement is unknown. |
| P04 | A/C | Streaming upload protection generalized to buffered JSON. | Compare path-qualified boundary records. | Each path has independent evidence. |
| P05 | C | Proxy limit protects directly reachable app. | Inspect ingress reachability qualification. | Proxy-only limit does not prove app protection. |
| P06 | C | Product projects with different limits collapsed. | Inspect Project/baseline fields and Product resolution. | Divergence remains visible; no universal Product limit. |
| P07 | C | Provider/consumer mismatch becomes CQ or fabricated compatibility. | Inspect CC route and CQ separation. | CC owns comparison; CQ remains implementation quality. |
| P08 | C | Gateway rejection implies application validation. | Inspect expected rejection-stage semantics. | Gateway stage is distinct; app execution is not claimed. |
| P09 | A/B | Unknown schema precision produces concrete threshold. | Inspect unresolved-bound and open-assumption fields. | No numeric value is invented. |
| P10 | A/B | Multipart and JSON limits conflated. | Inspect category/path records and cases. | Separate limits and cases remain. |
| P11 | A/B | Deep GraphQL-style nesting lacks bounded reasoning. | Inspect nesting/parser categories and case strategy. | Depth/resource limitation is explicit or unresolved. |
| P12 | A | Millions of tiny items evade byte-size reasoning. | Inspect collection count plus body-size categories. | Item count and bytes are separately checked. |
| P13 | A | Tiny compressed input expands without protection. | Inspect compressed/expanded evidence pair. | Expansion risk is classified when unknown. |
| P14 | A | Numeric input causes allocation/resource abuse. | Inspect numeric range and resource-sensitive impact fields. | No arbitrary policy; contextual finding/case. |
| P15 | C | Chunked input bypasses body-size reasoning. | Inspect aggregate streaming limit requirement. | Missing aggregate limit remains unknown/finding candidate. |
| P16 | A | Expensive deserialization precedes validation unnoticed. | Inspect validation-order evidence and CQ class. | Late validation is visible. |
| P17 | B | Reviewer acceptance turns case into `TESTED`. | Inspect state inequality and case examples. | Governance state cannot create tested evidence. |
| P18 | B | Expected 413 in Test Plan becomes observed response. | Inspect expected/observed separation. | Requirement remains unexecuted. |
| P19 | B | Exact payload/status creates pass/fail claim. | Inspect execution/result requirement. | Precision does not create runtime result. |
| P20 | B/C | CI result with unknown environment/baseline becomes qualified. | Inspect execution binding requirements. | No qualified `TESTED` claim. |
| P21 | B/C | Old revision's tested result proves new revision. | Inspect revision binding and revalidation rule. | Historical evidence remains old-revision-only. |
| P22 | C | Mixed Product tested/untested members become Product-wide tested. | Inspect per-member qualification and Product aggregation. | No universal `TESTED` inference. |

## Backward-compatibility and regression controls

The Block C backward-compatibility artifact must verify each control with an
exact inspection and result:

- old `IF-*` facts without boundary metadata remain valid but insufficient for
  safety conclusions;
- existing CQ `CQ-*`/`CQRA-*`, TE `BC-*`/`CC-*`/`MAT-*`/`TM-*`/`GAP-*`, Product,
  projection, and compatibility identities remain interpretable;
- Stage F `observed_view` role matrix and `TESTED` meaning remain unchanged;
- Product remains optional and single-Project review remains first-class;
- `requested_work`/`resolved_work`, authorization, redaction, and Stage B
  lifecycle remain unchanged;
- Contract Verification/CC remains independent of Matrix and Product;
- runtime execution, fuzzing, DAST, endpoint discovery, and environment
  provisioning remain unavailable;
- no historical artifact is rewritten or enriched by assumption;
- migration is `COMPATIBLE_EXTENSION`.

## Commit and review flow

The future implementation branch uses one worktree from
`467f2af8eceafe0860e1a9edc1210ce846c31a80`:

```text
branch:  feature/api-input-robustness-boundary-validation
worktree: /home/tod/skills/architecture-code-review-api-input-robustness
```

Expected implementation history:

```text
467f2af8eceafe0860e1a9edc1210ce846c31a80
  → docs: add Code Quality API boundary semantics
  → docs: add API boundary test semantics
  → test: validate API input boundary integration
```

After Block C, run the complete integrated validation once more over the
three-commit implementation range. Then stop at
`IMPLEMENTATION_READY_FOR_REVIEW` and perform exactly one independent
implementation review. Do not merge, promote, or create another plan in that
implementation task.

## Plan self-review checklist

- [ ] Exactly three implementation blocks and three expected implementation
  commits are present.
- [ ] Exactly one final independent implementation review gate is described.
- [ ] FF-API-01 through FF-API-08 are captured before normative edits.
- [ ] All 34 acceptance rows and 22 pressure rows have an owner, concrete
  verification, and expected result.
- [ ] CQ and TE ownership is preserved; no fourth capability or authority
  family appears.
- [ ] Transport/container and schema/field boundaries are distinct.
- [ ] Generated/accepted case states cannot imply `TESTED`; executed evidence
  is required.
- [ ] Stage F `TESTED` and Product-wide tested claims remain qualified.
- [ ] Runtime fuzzing and execution remain `UNAVAILABLE`.
- [ ] No arbitrary universal limit is introduced.
- [ ] Product remains optional, single-Project remains supported, and migration
  remains `COMPATIBLE_EXTENSION`.
- [ ] No unfinished markers or filler content, harness, framework, or
  individual scenario files are planned.
- [ ] `git diff --check` passes and only the plan file is changed before the
  plan commit.
