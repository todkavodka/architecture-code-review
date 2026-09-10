# API Input Robustness & Boundary Validation Contract Validation

## PRE-CHANGE BASELINE — IMMUTABLE

Captured before the first normative contract edit in Block A at the approved
plan checkpoint `d0718fb1ea197be83e4375eb4a16a446833efe8d`.

The following bounded searches were run against the pre-change worktree. Empty
matches are recorded as `NO_MATCH`; the unrelated STM `materialized` matches
were inspected and concern data-access relations, not API input validation.

| ID | Exact pre-change check | Evidence/result | Required gap |
|---|---|---|---|
| FF-API-01 | `rg -n "MISSING_REQUEST_SIZE_LIMIT|UNBOUNDED_STRING|UNBOUNDED_COLLECTION|UNBOUNDED_UPLOAD|SCHEMA_NOT_ENFORCED|VALIDATION_AFTER_MATERIALIZATION|PARSER_RESOURCE_EXHAUSTION|UNBOUNDED_PAGINATION|UNBOUNDED_NUMERIC_INPUT|UNBOUNDED_NESTING|UNBOUNDED_MULTIPART|COMPRESSION_EXPANSION_RISK" capabilities/code-quality-review/SKILL.md capabilities/code-quality-review/references/code-quality-contract.md` | `NO_MATCH` | No CQ rule independently classifies a missing request-body/container limit. |
| FF-API-02 | `rg -n "maxLength|request.?body|materiali[sz]|pre.?material|REQUEST_BODY_SIZE|VALIDATION_ORDER" capabilities/code-quality-review capabilities/test-review references/shared-technical-model.md references/technical-documentation.md` | No API-boundary matches; only unrelated STM data-relation `materialized` text at `shared-technical-model.md:445,448`. | Field constraints and pre-materialization transport protection are not explicit CQ semantics. |
| FF-API-03 | `rg -n "SCHEMA_NOT_ENFORCED|validator bypass|schema.*bypass|bypass.*schema" capabilities/code-quality-review capabilities/test-review references` | `NO_MATCH` | Schema declarations can lack an explicit CQ validator-bypass classification. |
| FF-API-04 | `rg -n "NEG-API|boundary_dimension|boundary-value|below/at/above|max \+ 1|min - 1|boundary generation|input boundary" capabilities/test-review capabilities/code-quality-review references` | `NO_MATCH` | TE has no API-specific deterministic boundary-generation semantics. |
| FF-API-05 | `rg -n "ESTABLISH_BOUNDARY|unknown threshold|unknown.*limit|invent.*(number|threshold)|unknown numeric" capabilities/test-review capabilities/code-quality-review references` | `NO_MATCH` | Unknown numeric limits are not explicitly protected from invented thresholds. |
| FF-API-06 | `rg -n "accepted_test_case|executed_test|tested_result|expected_result.*observed_result|generated.*TESTED|accepted.*TESTED" capabilities/test-review references/shared-technical-model.md references/technical-documentation.md` | `NO_MATCH` for API case-state separation; existing STM only says `TESTED` is orthogonal evidence at `shared-technical-model.md:313`. | API boundary case acceptance is not explicitly separated from execution/tested result. |
| FF-API-07 | `rg -n "observed_view:.*TESTED|Stage F.*TESTED|generated.*case|test plan.*TESTED" references/shared-technical-model.md references/technical-documentation.md capabilities/test-review` | Existing IF shape exposes `observed_view: ... TESTED` at `shared-technical-model.md:288`; no generated-case protection. | Generated API cases are not explicitly prohibited from populating Stage F `TESTED`. |
| FF-API-08 | `rg -n "Product.*TESTED|TESTED.*Product|Product.*execution|Product.*baseline.*test|tested.*Project" references/product-multi-project-review.md capabilities/test-review capabilities/test-review/references` | `NO_MATCH` | Product-qualified TESTED evidence is not explicit for API boundary cases. |

All eight fail-first premises are reproduced before normative implementation:
`8/8 FAIL_FIRST_VALID`.

This section is immutable historical evidence. Later blocks may append focused
and final results but must not rewrite these rows.

## Block C focused post-change checks

| Check | Exact inspection | Expected result |
|---|---|---|
| CQ categories and findings | `rg -n "REQUEST_BODY_SIZE|STRING_LENGTH|COLLECTION_SIZE|NUMERIC_RANGE|MISSING_REQUEST_SIZE_LIMIT|UNBOUNDED_STRING|SCHEMA_NOT_ENFORCED|VALIDATION_AFTER_MATERIALIZATION|COMPRESSION_EXPANSION_RISK" capabilities/code-quality-review/SKILL.md capabilities/code-quality-review/references/code-quality-contract.md` | All required CQ boundary vocabulary is present. |
| Two-layer order | `rg -n "transport/container|schema/field|parsing/materialization|business processing|pre-materialization|never implies.*SAFE" capabilities/code-quality-review/SKILL.md capabilities/code-quality-review/references/code-quality-contract.md` | Transport and field limits remain distinct; unknown body protection is not safe by implication. |
| Evidence strength | `rg -n "DECLARED|IMPLEMENTED|TESTED|frontend|OpenAPI|framework default|reverse-proxy|qualified" capabilities/code-quality-review/references/code-quality-contract.md` | Declarations, implementation, execution evidence, and weak hints remain distinct. |
| TE case states | `rg -n "case_key: NEG-API|DEFINED|ACCEPTED|EXECUTED|TESTED|PASSED|FAILED|OBSERVED|VERIFIED_AT_RUNTIME|accepted_test_case != executed_test != tested_result|expected_result != observed_result" capabilities/test-review/references/test-engineering-contract.md` | Case planning cannot imply execution or result. |
| Stage F attribute | `rg -n "boundary_evidence|observed_view: TESTED|generated or accepted|cannot populate|historical IF" references/shared-technical-model.md references/technical-documentation.md` | Existing IF view is optionally qualified and generated cases cannot populate `TESTED`. |
| Product qualification | `rg -n "Product-wide|Project.*baseline|generated or accepted|executed result|Product.*TESTED" references/product-multi-project-review.md capabilities/test-review/references/test-engineering-contract.md` | Product claims remain exact-member qualified. |
| Runtime boundary | `rg -n "runtime execution|fuzzing|DAST|UNAVAILABLE|does not execute|payload submission" capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md` | No runtime mechanism is introduced. |

## Acceptance matrix — 34/34 PASS

Each row was checked against the final contract text using the stated bounded
inspection. These rows are evidence, not a new authority.

| ID | Owning check | Concrete verification | Result |
|---|---|---|---|
| A01 | CQ evidence | Inspect `DECLARED`/`IMPLEMENTED` and exact `STRING_LENGTH` rules in `code-quality-contract.md`. | PASS |
| A02 | CQ class | `rg -n "UNBOUNDED_STRING|no universal" capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A03 | Two layers | Inspect `REQUEST_BODY_SIZE` and `STRING_LENGTH` separately with `ENFORCEMENT_UNKNOWN`. | PASS |
| A04 | Ordering | Inspect `pre-materialization`, `VALIDATION_AFTER_MATERIALIZATION`, and 2 GiB example. | PASS |
| A05 | Early limit | Compare transport/container and schema/field paragraphs in CQ contract. | PASS |
| A06 | Collection | `rg -n "COLLECTION_SIZE|UNBOUNDED_COLLECTION|maxItems" capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A07 | Pagination | `rg -n "PAGINATION_LIMITS|UNBOUNDED_PAGINATION|unknown" capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A08 | Upload | `rg -n "UPLOAD_SIZE|UNBOUNDED_UPLOAD|upload handler" capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A09 | UI-only | `rg -n "frontend.*maxlength|weak hint|server enforcement" capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A10 | Schema bypass | `rg -n "SCHEMA_NOT_ENFORCED|bypassed schema" capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A11 | Media type | `rg -n "CONTENT_TYPE|media type|wrong-content-type" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A12 | Malformed payload | `rg -n "MALFORMED_PAYLOAD|parser|expected_stage" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A13 | Unknown fields | `rg -n "UNEXPECTED_FIELDS|unknown-field|UNEXPECTED_FIELD_ACCEPTANCE" capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A14 | Nesting | `rg -n "NESTING_DEPTH|parser/resource|nesting" capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A15 | Multipart | `rg -n "MULTIPART_LIMITS|UNBOUNDED_MULTIPART|part count" capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A16 | Compression | `rg -n "COMPRESSION_EXPANSION|COMPRESSION_EXPANSION_RISK|expanded" capabilities/code-quality-review/references/code-quality-contract.md capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A17 | Single Project | `rg -n "single Project|without Product|Project/source" references/technical-documentation.md references/product-multi-project-review.md`. | PASS |
| A18 | Product | `rg -n "Product-qualified|Product baseline|membership.*does not" references/product-multi-project-review.md`. | PASS |
| A19 | Exact maximum | `rg -n "below/at/above|numeric min/max|string length|item count" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A20 | Unknown bound | `rg -n "ESTABLISH_BOUNDARY|never invent a numeric" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A21 | Fuzzing | `rg -n "fuzzing.*UNAVAILABLE|runtime execution.*UNAVAILABLE" capabilities/test-review/SKILL.md capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A22 | No evidence | Inspect unresolved evidence rule in CQ contract and no-fabrication rule in STM. | PASS |
| A23 | Header/query/cookie | `rg -n "HEADER_LIMITS|QUERY_LIMITS|COOKIE_LIMITS" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A24 | Chunked body | `rg -n "Content-Length|streaming|aggregate" references/technical-documentation.md references/shared-technical-model.md`. | PASS |
| A25 | Gateway | `rg -n "gateway|ingress|enforcement stage|qualified" references/technical-documentation.md capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A26 | Deserialization | `rg -n "VALIDATION_AFTER_MATERIALIZATION|deserialization|materialization" capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A27 | Compatibility | `rg -n "Contract Verification|CC-\*|provider/consumer" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A28 | Streaming upload | `rg -n "input path|streaming|UPLOAD_SIZE|REQUEST_BODY_SIZE" references/technical-documentation.md capabilities/code-quality-review/references/code-quality-contract.md`. | PASS |
| A29 | Generated case | `rg -n "generated case|not.*TESTED|DEFINED" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A30 | Accepted case | `rg -n "accepted Test Engineering case|case being accepted is insufficient" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A31 | Expected response | `rg -n "expected 4xx|expected result|PASSED|FAILED" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A32 | Executed evidence | `rg -n "actual execution|execution/result record|environment and baseline|TESTED may" capabilities/test-review/references/test-engineering-contract.md`. | PASS |
| A33 | Product member | `rg -n "One Project|other Projects|Product-wide|execution-result qualification" references/product-multi-project-review.md`. | PASS |
| A34 | Stage F view | `rg -n "cannot populate.*TESTED|WHAT EXISTS|boundary case" references/shared-technical-model.md references/technical-documentation.md`. | PASS |

## Pressure matrix — 22/22 PREVENTED

| ID | Failure | Concrete prevention check | Result |
|---|---|---|---|
| P01 | Frontend validation treated as backend enforcement | Inspect `WEAK_HINT` and frontend/server separation in CQ contract. | PREVENTED |
| P02 | OpenAPI hides schema bypass | Inspect `DECLARED` versus `SCHEMA_NOT_ENFORCED`. | PREVENTED |
| P03 | Undeployed framework default treated as limit | Inspect deployment-applicability requirement and `ENFORCEMENT_UNKNOWN`. | PREVENTED |
| P04 | Streaming upload limit generalized to buffered JSON | Inspect path/layer qualification and independent dimensions. | PREVENTED |
| P05 | Proxy limit protects direct app | Inspect qualified ingress/reachability rule. | PREVENTED |
| P06 | Product limits flattened | Inspect per-Project/baseline Product qualification. | PREVENTED |
| P07 | Provider mismatch becomes CQ/compatibility result | Inspect CC authority and CQ/TE separation. | PREVENTED |
| P08 | Gateway rejection implies app validation | Inspect expected stage versus observed execution. | PREVENTED |
| P09 | Unknown schema precision gets fabricated threshold | Inspect open assumptions and unknown-bound rule. | PREVENTED |
| P10 | Multipart/JSON limits conflated | Inspect separate categories and input paths. | PREVENTED |
| P11 | Deep GraphQL nesting unbounded | Inspect `NESTING_DEPTH` and parser-resource categories. | PREVENTED |
| P12 | Tiny items evade byte reasoning | Inspect collection count independent from body bytes. | PREVENTED |
| P13 | Compression expansion ignored | Inspect compressed/expanded evidence pair. | PREVENTED |
| P14 | Numeric input resource abuse ignored | Inspect numeric range plus contextual consequence. | PREVENTED |
| P15 | Chunked input bypasses body limit | Inspect aggregate streaming boundary requirement. | PREVENTED |
| P16 | Late deserialization unnoticed | Inspect validation-order CQ class. | PREVENTED |
| P17 | Accepted generated case becomes `TESTED` | Inspect state inequality and accepted-case rule. | PREVENTED |
| P18 | Expected 413 becomes observed | Inspect expected/observed separation. | PREVENTED |
| P19 | Exact planned payload creates pass/fail | Inspect execution evidence requirement. | PREVENTED |
| P20 | CI result lacks qualified environment/baseline | Inspect required execution bindings. | PREVENTED |
| P21 | Old revision proves new revision | Inspect revision/baseline binding and historical rule. | PREVENTED |
| P22 | One tested Project proves Product | Inspect Product member aggregation rule. | PREVENTED |

Final integrated result:

```text
fail_first: 8/8 CAPTURED
acceptance: 34/34 PASS
pressure: 22/22 PREVENTED
runtime_fuzzing: UNAVAILABLE
harness: DO_NOT_BUILD_HARNESS
migration: COMPATIBLE_EXTENSION
```
