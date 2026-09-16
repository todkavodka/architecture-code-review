# Final Editorial Review

This gate runs only after all requested endpoint artifacts have been technically accepted and the final package has been assembled.

Editorial Review **does not edit documents directly**. It produces an issue list. A separate correction pass applies the fixes, followed by a fresh-context re-review.

## 1. Purpose

Verify that final user-facing documents:

- are written as coherent professional technical prose in the selected user-facing language;
- explain material mechanisms to a human reader rather than copying terse working-artifact style;
- use terminology consistently;
- contain useful, actually validated diagrams when topology, lifecycle, ownership, or target behavior is difficult to understand from prose alone;
- contain no stale or superseded technical claims;
- agree with each other and with the authoritative ledger;
- have a coherent cross-link graph;
- do not distort severity, evidence, target, or roadmap semantics during editing;
- do not claim `REVIEW_COMPLETE` when Discovery Coverage is not in accepted `COVERAGE_ACCEPTED` state.

Editorial Review **is not a technical re-audit**. It does not need to rediscover omitted vulnerability or mechanism classes across the repository. Completeness of thematic discovery and absence-of-investigation gaps belong to the Independent Coverage Review defined in `discovery-coverage.md`.

Editorial Review also performs a targeted workflow-authority consistency check against accepted final artifact state and requires the coordinator's `FINAL_WORKFLOW_AUTHORITY_RECONCILED`. This does not turn editorial review into a technical re-audit.

## 2. Language contract

Narrative uses the selected user-facing language from the umbrella Skill language contract.

At first material use, an established English technical term may be paired with a natural-language equivalent when that improves understanding. Exact identifiers remain unchanged.

Do not translate exact:

- class/function/type identifiers;
- filenames and paths;
- API/IPC/protocol names;
- runtime states;
- verdict/status tokens;
- commands and code.

Flag accidental language drift: paragraphs, headings, or table explanations that unexpectedly switch away from the selected user-facing language.

Also flag mixed-language shorthand when an ordinary idea can be stated naturally without losing precision. For Russian output, examples of undesirable final prose include:

```text
error-boundary протекает credential-ами
prod-risks untestable
shutdown негрейсфул
designated owner отсутствует
runtime-drift
```

Do not require artificial translation of exact identifiers or established technical terms. The goal is professional, readable prose in the selected language, not linguistic purism.

## 3. Prose quality contract

Working notes, `HANDOFF SUMMARY`, ledger rows, and verification matrices may be dense. Final user-facing narrative must explain the system.

For every material conclusion, verify that the prose answers four questions:

1. what happens now;
2. why it happens;
3. what consequence follows;
4. what must change or be preserved.

Preferred causal structure:

```text
mechanism → evidence → consequence → correction direction
```

This is a reasoning structure, not a requirement to write literal arrows in final prose.

### 3.1 One primary mechanism per paragraph

A paragraph should have one dominant architectural mechanism or one causal chain. Related evidence and consequences may stay in the same paragraph, but several independent root mechanisms must not be compressed into one wall of text.

If answering “which single mechanism is explained here?” requires listing several independent answers, split or restructure the paragraph.

Do not impose a mechanical sentence- or paragraph-length quota. A short paragraph may still be overloaded, and a long paragraph may remain coherent when it develops one causal chain.

### 3.2 Explain before compressing

On first material use of a specialized English term, hybrid shorthand, or non-obvious architecture pattern, explain the mechanism naturally in the selected user-facing language. The exact term may then be retained in parentheses or reused as shorthand.

**Technical shorthand is not an explanation by itself.** A precise cluster of terms may name a solution correctly but does not replace a description of system behavior.

For Russian output, avoid explanatory layers such as:

```text
NATS получает eager startup + registered shutdown + drain.
in-flight KV puts дропаются при shutdown.
single-flight wrapper предотвращает thundering-herd на cold-cache miss.
```

Explain observable behavior first. For example:

```text
При запуске приложение заранее проверяет доступность NATS и не объявляет себя
готовым, если соединение установить невозможно. При остановке оно сначала
завершает уже начатые операции, а затем корректно закрывает соединение. Такой
подход можно дальше кратко называть fail-fast startup и graceful drain.
```

Or:

```text
При остановке приложения уже начатые операции записи в NATS KV могут быть
оборваны до завершения, если соединение закрывается без ожидания активной работы.
```

For `single-flight`, first explain that when a cache value is absent, several identical requests may hit the backing source concurrently, while the mechanism leaves one source request active and makes the others wait for its result. After that, `single-flight` may be used as a compact name for the already explained behavior.

The exact example wording is non-normative. The normative ordering is:

```text
natural-language mechanism explanation → specialized term as shorthand
```

Do not re-explain terms that are already obvious to the target audience in every paragraph. The gate prevents clusters of shorthand from replacing explanation.

### 3.3 Roadmap presentation

A roadmap task first contains a human-readable problem/cause/consequence/target-result layer and then a visually separate implementation contract.

For every material roadmap task:

- the title must read as an engineering goal without `[prereq: ...]`, `[RF: ...]`, or other execution metadata;
- prerequisite, RF, SER, and target metadata belongs in the technical contract;
- after the explanatory layer, a dedicated heading meaning “Implementation Contract” in the selected user-facing language is mandatory;
- for Russian output, the exact heading remains `### Технический контракт реализации`;
- prerequisites, allowed/forbidden scope, regression tests, verification, exit criteria, rollback, and safe activation appear after that heading, preferably in a table or another clearly reference-oriented format.

Labels such as `Prerequisites`, `Allowed boundary`, and `Verification` must not blend into explanatory prose.

Flag `STYLE-*` or `TERM-*` when:

- final prose reads like an agent scratchpad or handoff;
- sentences are replaced with fragments or labels;
- arrows such as `->`, `!=`, slash-compounds, or parenthesized IDs carry the primary semantic load;
- RF/SER/TASK IDs replace explanation;
- implementation nouns appear before the problem itself is explained;
- the executive summary is a ledger dump rather than synthesis;
- one paragraph forces the reader to track several independent root mechanisms;
- specialized shorthand appears before its mechanics are explained;
- technical shorthand itself is used as the explanatory layer;
- a material roadmap title contains bracketed execution metadata;
- a material roadmap task lacks the dedicated Implementation Contract heading in the selected user-facing language;
- the roadmap human-readable layer and execution contract are not visually separated.

## 4. Diagram coverage and renderability contract

Compare the final package with `lifecycle-and-mermaid.md` and `report-contract.md`.

When the system contains material topology, lifecycle, ownership, trust boundaries, ordering, or target transitions, verify that useful visual explanation exists.

For a substantial report, the following are especially expected when applicable:

- an As-Built component/boundary diagram;
- a runtime, lifecycle, or sequence diagram;
- a Target Architecture diagram;
- a Before → After diagram for a material correction;
- a roadmap dependency diagram for non-trivial sequencing or safe activation.

A missing diagram is acceptable when visualization genuinely adds no architectural information. In a substantial package, that decision should be explicitly defensible.

Every Mermaid block in final user-facing artifacts must be enumerated. If a compatible parser or renderer is available, the reviewer/correction workflow must retain evidence of actual tool invocation for every block. Any known parser/render failure blocks acceptance.

If no renderer is available, record `MERMAID_RENDER_VALIDATION_UNAVAILABLE` and do not claim Mermaid render validation passed.

Flag `DIAG-*` when:

- material architecture is difficult to understand without a visual aid and none is provided;
- a diagram is decorative and does not explain a real mechanism;
- current and target behavior are mixed;
- Mermaid contradicts prose or accepted evidence;
- a diagram uses generic fake components instead of real subsystem names;
- a Mermaid block fails the available parser/renderer;
- some final Mermaid blocks were not actually validated despite an available renderer;
- render-validation `PASS` is claimed without evidence of tool invocation.

## 5. Issue types

Recommended IDs:

```text
LANG-###   language drift / grammar / hybrid shorthand
TERM-###   inconsistent or unexplained terminology
STYLE-###  machine-like / duplicate / telegraphic / overloaded prose
DIAG-###   missing/useless/misleading/unrenderable diagram
LINK-###   broken/missing cross-link
CONS-###   prose/table/diagram/document contradiction
STALE-###  superseded claim resurfaced
SEV-###    wording rhetorically exceeds adjudicated severity
STATUS-### final status contradicts accepted technical/coverage gate state
```

## 6. Checks

Verify:

- connected prose follows `mechanism → evidence → consequence → correction direction`;
- material explanatory prose has one primary mechanism per paragraph;
- specialized shorthand is explained before becoming compressed terminology;
- technical shorthand is not used as the explanation itself;
- no accidental drift away from the selected user-facing language;
- no awkward mixed-language shorthand or transliteration;
- terminology is consistent;
- grammar and readability are acceptable;
- the executive summary explains system-level causes before listing RFs;
- material roadmap titles are human-readable and do not carry bracketed execution metadata;
- roadmap tasks first explain problem, root cause, and result, then contain the mandatory localized Implementation Contract boundary;
- useful diagram coverage exists where material complexity warrants it;
- every final Mermaid block is enumerated;
- actual parser/render validation exists for every final Mermaid block when a compatible renderer is available;
- failed Mermaid blocks are corrected and revalidated before acceptance;
- `MERMAID_RENDER_VALIDATION_UNAVAILABLE` is explicit when executable validation cannot be performed;
- there are no duplicated paragraphs or findings;
- no stale superseded statements resurfaced;
- root titles, status, and severity are identical across all final artifacts;
- diagrams and state tables do not contradict prose;
- important relative links resolve conceptually;
- there are no orphan RF, SER, TASK, or target references;
- target mechanisms link to their motivating RF, SER, or invariant;
- roadmap tasks link to target state and RF as required;
- superseded working claims point forward to current authority where required;
- no unsupported intensifiers such as `catastrophic`, `RCE`, `data loss`, or `critical` appear outside adjudicated context;
- final status agrees with `working/INDEX.md` and accepted Discovery Coverage state;
- `FINAL_WORKFLOW_AUTHORITY_RECONCILED` is accepted only when final status agrees with all mandatory workflow/gate states, the `INDEX.md` artifact registry agrees with final registered deliverables, and candidate/finding mappings, Positive Controls aggregates, authoritative-document registry, and selected-package projection lifecycle states agree with their owning authorities;
- `project_profile.status: PENDING` is not by itself a contradiction because Project Profile is routing-only metadata; any other mandatory `PENDING` or `IN_PROGRESS` state, or an unresolved reconciliation mismatch, blocks the gate;
- the package does not claim `REVIEW_COMPLETE` while coverage is `PARTIALLY_COVERED`, `BLOCKED`, `COVERAGE_CORRECTION_REQUIRED`, `COVERAGE_BLOCKED`, `COVERAGE_AUTHORITY_DRIFT`, or material `REVALIDATION_REQUIRED`.

## 7. Semantic safety

The editorial reviewer **must not silently change**:

- evidence;
- root identity;
- severity;
- confidence or exploitability;
- product-intent status;
- target invariants or ownership;
- feasibility classification;
- roadmap dependencies or gates;
- security assumptions;
- the Discovery Coverage technical verdict.

The editorial reviewer also **does not perform a new repository-wide vulnerability/discovery search** to prove coverage. If the final package shows non-accepted or stale coverage state, flag a status/consistency issue and return the package to the appropriate technical coverage gate.

If language or diagram cleanup reveals a real technical contradiction, create a `CONS-*` issue and return it to the appropriate technical gate.

## 8. Output

The review artifact records:

```text
reviewed final artifact refs
baseline / authoritative ledger ref
coverage verdict / coverage artifact ref
issue ID
location
category
observed problem
required correction boundary
technical-gate escalation? yes/no
```

For Mermaid validation, also retain a compact record:

```text
diagram/document location
validator/renderer used
result: PASS | FAIL | UNAVAILABLE
correction/revalidation ref if failed
```

Do not reproduce the full reviewed document inside the review artifact.

## 9. Correction loop

```text
FINAL PACKAGE ASSEMBLED
→ fresh-context editorial review
→ issue list
→ separate editorial correction writer
→ verify links/semantics + Mermaid renderability + status consistency
→ fresh-context editorial re-review
→ FINAL_PACKAGE_ACCEPTED | CORRECTION_REQUIRED | TECHNICAL_GATE_REQUIRED
```

The correction writer changes only what is authorized by the issue list. Do not add new technical content without returning to the appropriate technical gate.

A coverage-related `STATUS-*` issue is not repaired by editorially changing a verdict. If coverage is not accepted, the correction boundary is the technical Coverage Review, correction, or revalidation process.

## 10. Final acceptance

The package cannot be declared final until:

- every editorial issue is closed or explicitly blocked;
- re-review has been completed;
- cross-links have been checked;
- no stale authoritative projection remains within the required scope of the selected endpoint/package; unrelated stale projections remain visible and deferred according to `PERMISSIVE`, `REQUIRED_SCOPE_CURRENT`, or `ALL_SCOPED_CURRENT` policy;
- `FINAL_WORKFLOW_AUTHORITY_RECONCILED` is accepted after the final correction/re-review, including final `INDEX.md` reconciliation against registered deliverables, owning authoritative artifacts, mandatory workflow/gate states, and selected-package projection lifecycle records;
- the language/prose quality contract is satisfied;
- material roadmap tasks have human-readable titles and an explicit localized Implementation Contract boundary;
- the diagram coverage contract is satisfied or the absence of diagrams is justified;
- there are no known Mermaid parser/render failures;
- when a renderer is available, every final Mermaid block has executable validation evidence;
- when no renderer is available, the limitation is explicit and render `PASS` is not claimed;
- requested target/roadmap artifacts have already been technically accepted;
- Discovery Coverage is in accepted `COVERAGE_ACCEPTED` state bound to the current accepted As-Built/baseline;
- final status does not hide a material coverage limitation.