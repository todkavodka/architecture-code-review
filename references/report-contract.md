# Final Report Contract

Final documents are written in coherent Russian technical prose and are assembled **only from accepted authoritative state**, never directly from raw discovery notes.

Technical Documentation is a separate human-facing factual projection from accepted, fresh Shared Technical Model authority. Its scope, non-authority, source, and `PROJECTS_FROM` dependency rules are defined by [`technical-documentation.md`](technical-documentation.md). It is not an Architecture Review finding ledger or a developer how-to package.

## 1. Package

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md          # when requested
├── 04-remediation-roadmap.md          # when requested
└── working/
    ├── README.md
    ├── INDEX.md
    └── ... evidence/review artifacts ...
```

If the repository already has an established review directory, use it while preserving the internal roles of the files.

When composable capabilities are selected, keep their substantial detail in capability-owned artifacts registered in `working/INDEX.md`, for example:

```text
capabilities/test-review/01-test-assurance-map.md
capabilities/test-review/02-test-plan.md                 # optional
working/capabilities/test-review/...
```

The specialist artifact remains authoritative for its detailed evidence and assurance map. The umbrella report may synthesize and link an adjudicated cross-capability conclusion, but must not copy the complete specialist report.

For Test Engineering, preserve the compatible `00-test-assurance-summary.md`, `01-test-assurance-map.md`, and optional `02-test-plan.md` projections. Extended outputs are capability-owned projections `03` through `08`; authoritative `BC-*`, `CC-*`, `TM-*`, and `GAP-*` ledgers remain under capability `working/`. The numbered files do not become product-behavior authority merely because they are generated later.

## 2. Authority map

- Technical facts during investigation: accepted/fresh Shared Technical Model under `shared-technical-model.md` plus required coverage acceptance under `technical-model-coverage.md`.
- Human-readable As-Built: substantial projection of accepted/fresh STM plus architecture-oriented synthesis; it is not a competing factual authority.
- `01-architecture-review.md`: user-facing delivery projection. Its factual As-Built chapter is derived from STM, and it is never the sole persistence location for Architecture meaning.
- `02-authoritative-findings-ledger.md`: Architecture-owned semantic authority for final RF wording, evidence status, severity, projections, `SER-*`/open questions, supersessions, and the accepted architecture properties/invariants registry.
- `03-target-architecture.md`: authoritative source for target mechanisms, invariants, and feasibility when selected by the endpoint.
- `04-remediation-roadmap.md`: authoritative source for implementation sequence, tasks, and gates when selected by the endpoint.

### Product Architecture Review report boundary

When Product mode is selected, the Architecture Review ledger may contain Product-scoped existing `RF-*` records only after independent Product adjudication. Each record links the accepted Product revision and immutable baseline, affected Projects, qualified `WS-*`/`EV-*` evidence, accepted STM facts/relations, consequence, severity, lifecycle, dependencies, and provenance. A Project-local RF is not promoted by aggregation. The final report and any Product summary are projections/navigation assembled from the ledger; they cannot create, revise, resolve, or supersede RF semantics.

If the accepted STM revision, required factual coverage, or a projection selector changes, every dependent As-Built/final section is stale until synthesis and review are repeated. `PROJECTION_REPAIR` may repair presentation only against unchanged accepted authority; semantic drift is routed to technical revalidation rather than hidden through prose repair.

### 2.1 Stage B migration of composite Architecture authority

`01-architecture-review.md` remains the authoritative delivery surface for a reader, but that does not make its prose the sole semantic persistence authority. It may become a fully generated `PRJ-*` projection only after a migration inventory maps every persistent meaning that it renders to a current, accepted owning authority. The minimum map is:

| Meaning rendered by `01-architecture-review.md` | Upstream owning authority |
|---|---|
| factual As-Built architecture, scope, and factual limitations | accepted/fresh STM and required Technical Model Coverage acceptance |
| final `RF-*`, `SER-*`, open-question, and supersession semantics | `02-authoritative-findings-ledger.md` |
| accepted architectural properties and invariants | the explicit accepted properties/invariants registry in `02-authoritative-findings-ledger.md` |
| Target Architecture mechanisms, invariants, and feasibility | accepted `03-target-architecture.md`, when selected |
| Roadmap tasks, sequence, dependencies, gates, and safe activation | accepted `04-remediation-roadmap.md`, when selected |
| presentation-only narrative, navigation, layout, and cross-links | no persistent semantic authority; generated assembly only |

The inventory must also name an owning authority for any other report section whose meaning must survive regeneration. If a section contains persistent meaning without that mapping, record:

```text
PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY
```

The final-report projection is then `BLOCKED`: do not overwrite its unmapped section, preserve it as a hidden human-owned island, or infer an owner from its current prose. Route the missing mapping to the Architecture owner and resume generation only after the authority is accepted and revision-bound.

After the inventory is complete, the final report is generated assembly from the exact accepted authorities above and permitted factual projections. Stage B may render, link, and verify the assembly, but it MUST NOT create, change, delete, resolve, strengthen, weaken, merge, suppress, or reinterpret `RF-*`, `SER-*`, properties/invariants, Target Architecture semantics, or Roadmap semantics. `V4 AUTHORITY CONSISTENCY` compares the candidate with those owners; it does not adjudicate or repair them.

### 2.2 Registration of a legacy Architecture report

An existing `01-architecture-review.md` without accepted `PRJ-*` lifecycle metadata is a legacy delivery artifact. It is not `CURRENT` merely because it is readable, complete-looking, old, committed, or previously accepted by a human. Register it only through the shared legacy path:

```text
legacy artifact
→ identify capability owner
→ assign PRJ identity
→ define contract
→ resolve dependencies
→ verify against accepted authority
→ establish fingerprint/revision
→ CURRENT
```

For this report, “identify capability owner” means the Architecture owner is recorded and the inventory in §2.1 is complete for every persistent section. The registration must bind the accepted/fresh STM and coverage records, the Architecture findings ledger, and the selected Target Architecture and Roadmap authorities when those endpoint outputs are in scope, including their exact revisions and selector/dependency resolutions. Presentation-only prose may remain generated assembly, but it cannot supply a missing semantic owner.

The report's existing human-edited wording is only a candidate or historical context during registration. It must not promote itself into `RF-*`, `SER-*`, property/invariant, Target, Roadmap, or factual STM authority, and it must not resolve a conflict among those owners. If any persistent meaning remains unmapped, record `PROJECTION_MIGRATION_BLOCKED_UNMAPPED_AUTHORITY`, leave the legacy report non-current, and route the missing mapping to the Architecture owner. Do not overwrite the unmapped content, infer an owner from its prose, or preserve it as a hidden human-owned authority island.

Only after the registration contract is complete and the candidate passes the applicable `V1`–`V4` gates may its canonical fingerprint and first accepted `PRJ-*@revN` be established and the report become `CURRENT`. Insufficient, stale, or conflicting authority blocks registration and requires semantic revalidation/migration; it never justifies weakening verification.

## 3. `01-architecture-review.md`

This is the primary human-readable document. After Stage B migration is complete, it is a fully generated assembly of accepted STM and Architecture semantic authorities, not a competing Architecture semantic ledger.

Recommended structure for a Russian-language final document:

```markdown
# Архитектурное и кодовое ревью

## 1. Резюме
## 2. Объём, baseline и ограничения
## 3. Методика
## 4. Фактическая архитектура
### 4.1 Назначение и ключевые сценарии
### 4.2 Процессы и runtime-компоненты
### 4.3 Ответственность и владение
### 4.4 Основные data/control flows
### 4.5 IPC/API/native/process boundaries
### 4.6 Жизненный цикл
### 4.7 Конкурентность и фоновые операции
### 4.8 Хранение и конфигурация
### 4.9 Trust boundaries и security model
### 4.10 Platform-specific behavior
### 4.11 Положительные механизмы
## 5. Архитектурные свойства и ключевые выводы
## 6. Наиболее существенные подтверждённые замечания
## 7. Положительные механизмы, которые следует сохранить
## 8. Приоритеты и зависимости исправления
## 9. Выполненные проверки
## 10. Открытые вопросы и product-intent decisions
## 11. Ограничения исследования
## 12. Итоговый статус
```

The factual architecture is a substantial first-class chapter traceable to accepted/fresh STM facts and required coverage. For a medium-size project, an information-density target roughly equivalent to 5–10 pages is usually appropriate, but the gate is semantic completeness rather than line count. It preserves material purpose/scenarios, topology, ownership, boundaries, flows, lifecycle, concurrency, failure behavior, trust, configuration, persistence, observability, and platform-specific details; architecture properties and findings remain separate Architecture authority.

The main report normally explains the 10–20 most important RFs in readable form and links to the complete ledger instead of duplicating every detail.

### 3.1 Human-readable synthesis contract

The final report explains architectural mechanisms to a human reader rather than replaying the internal ledger.

For every material conclusion, the reader must be able to understand without opening working files:

1. **What happens now.** How the current mechanism, flow, or ownership model works.
2. **Why it happens.** Which boundary, responsibility, or lifecycle model creates the behavior.
3. **What it leads to.** The concrete runtime, security, reliability, or testability effect.
4. **What should change.** The correction direction or target mechanism without prematurely turning the conclusion into a code patch.

Preferred narrative pattern:

```text
current mechanism
→ code/evidence basis
→ practical consequence
→ architectural correction direction
```

`RF-*`, `SER-*`, `PC-*`, `OQ-*`, and `TASK-*` provide navigation and traceability. They **do not replace explanation**.

The following form is not acceptable as final prose:

```text
error-boundary leaks credentials (RF-A/C);
test-app != prod-app -> risks untestable;
shutdown non-graceful;
cache-first pattern.
```

Such shorthand is acceptable inside internal registries and handoffs, but a user-facing document must explain the causal chain in normal sentences and paragraphs.

### 3.2 Executive synthesis is not a ledger dump

The Executive Summary and key-findings section must not become a long numbered sequence of shorthand labels.

Start with 3–7 connected paragraphs that group issues by system-level causes such as ownership/lifecycle, trust boundaries, data integrity, testability, or coupling. After that explanation, a compact table or RF link list is appropriate.

A reader should understand the overall architectural health, systemic causes, and priorities even without knowing the Skill's internal taxonomy.

## 4. `02-authoritative-findings-ledger.md`

For every root record:

```text
stable RF ID
final title
severity
confidence
exploitability where applicable
root mechanism
reachable scenario
code evidence
projections
SER links
open/product-intent status
superseded candidate/wording references
links to main report
target link when applicable
roadmap task links when applicable
```

Preserve separate registries for `SER-*`, `PC-*`, `OQ-*`, and explicit supersessions.

The same Architecture-owned semantic artifact also maintains an explicit registry of accepted architectural properties/invariants needed by the final report, target, or roadmap but not reducible to one `RF-*`. Each entry has stable identity/revision, accepted status, evidence/provenance, and links to affected `RF-*`/`SER-*`/target/roadmap records where applicable. `01-architecture-review.md` may only render this registry; generation does not change it.

The ledger may be dense and structured. That is not permission to carry its terse style into user-facing narrative sections.

### 4.1 Architecture RF lifecycle ownership

`Architecture Review` is the sole owner and writer of accepted `RF-*` lifecycle, severity, disposition, revision, resolution, reopening, and supersession. The exact semantic persistence boundary is the generated Architecture-owned `02-authoritative-findings-ledger.md`; this reference defines the contract that ledger must implement. No Product report, projection, index, Change Review candidate, remediation record, or developer assertion is an alternative RF authority.

Each accepted RF revision records:

```text
finding_id
owner_capability / qualified_project_or_product_scope
accepted_revision
lifecycle: ACTIVE | RESOLVED | SUPERSEDED
disposition: owner-qualified treatment decision
severity
evidence_refs
source_binding / analyzed_baseline
resolution_evidence (when RESOLVED)
supersedes / superseded_by (when SUPERSEDED)
reopened_from / resolution_invalidated_by (when reopened)
```

The same identity is retained when the root mechanism and correction boundary remain the same. A changed lifecycle, severity, or disposition creates a new immutable accepted owner revision, not a new ID. A materially different root gets a new identity with explicit replacement/supersession lineage.

Architecture accepts these transitions only through its owner gate:

| Transition | Required authority |
|---|---|
| `ACTIVE → RESOLVED` | accepted evidence, owner revalidation, owner adjudication, exact proving source/dependency binding, and a new accepted RF revision |
| `ACTIVE → SUPERSEDED` | owner adjudication, qualified replacement/merge authority, and replacement lineage in a new revision |
| `RESOLVED → ACTIVE` | owner adjudication of recurrence or invalidated resolution, a new ACTIVE revision, and `reopened_from` provenance |
| severity change | owner severity adjudication and a new revision with the same identity where the root remains the same |
| disposition change | Architecture owner/governance decision with rationale, scope, approver, and policy metadata |

The resolution gate is:

```text
accepted RF evidence
→ owner revalidation against exact source/evidence binding
→ owner adjudication
→ accepted Architecture RF revision
```

Developer assertions, commit messages, completed remediation alone, candidate Change Review, Product inference, report prose, projection omission, and a remediation status do not satisfy this gate. `REOPENED` is never persisted as a fourth lifecycle value: it is a derived baseline transition over a newer accepted `ACTIVE` revision with the prior resolution reference.

## 5. Cross-link contract

Use relative links inside the audit package.

Navigation chain:

```text
main report
→ authoritative RF
→ working evidence / verification
→ target mechanism
→ remediation task
```

Add reverse links where they are useful.

Stable headings should begin with the ID:

```markdown
## RF-012 — ...
```

Do not rely only on long translated headings as anchors.

Final verification must detect:

- orphan RF/SER/TASK records;
- broken or missing relative links;
- target mechanisms without motivating RF/SER/invariant records;
- roadmap tasks without target/RF links;
- superseded working claims that do not point to current authority.

## 6. Technical draft versus final assembly

After the authoritative findings ledger is accepted, a `MAIN REVIEW TECHNICAL DRAFT` may be created for `01-architecture-review.md`. This draft and the later generated assembly do not become semantic authority: persistent Architecture meaning is accepted first in the owning records from §2.1.

If the endpoint includes target or roadmap work, this draft **is not the final package**.

`FINAL PACKAGE ASSEMBLY` runs only after all requested endpoint artifacts are accepted:

```text
accepted audit
+ accepted target (if requested)
+ accepted roadmap (if requested)
→ inject final navigation/cross-links/status
→ editorial review
```

For `REVIEW_ONLY`, the technical draft and final assembly may naturally coincide.

## 7. Chunked writing

Do not write a large Markdown document in one giant write when there is a meaningful risk of truncation or tool limits.

Normal pattern:

```text
CREATE SKELETON
→ WRITE LOGICAL CHUNK A
→ VERIFY headings/content
→ WRITE CHUNK B
→ VERIFY previous content preserved
→ WRITE CHUNK C
→ VERIFY IDs/links
→ FINAL READ
```

A chunk is defined by a logical section, not an arbitrary character count.

On write failure or truncation:

```text
inspect existing file
→ identify last complete logical boundary
→ resume from there
→ do not blindly overwrite whole large artifact
→ final read
```

One final artifact has one active writer at a time.

## 8. Writing style and terminology

Narrative output is Russian. On first material use, `English term (Russian equivalent)` is acceptable; afterward prefer the Russian term when precision is not reduced.

Do not translate exact identifiers, class/function/type names, filenames, API/IPC/protocol names, runtime states, verdict/status tokens, commands, or code.

Write paragraphs in the causal order `mechanism → evidence → consequence → correction direction`. Tables and Mermaid diagrams supplement analysis; they do not replace it.

### 8.1 Working-artifact style must not leak into final prose

Working artifacts, candidate registries, `HANDOFF SUMMARY`, and verification notes may be terse and machine-oriented. User-facing final documents may not.

In final narrative, avoid using the following as the primary form:

- arrow shorthand such as `X -> Y -> broken`;
- long chains through `+`, `/`, `!=`, or parentheses;
- sentence fragments instead of sentences;
- English/Russian hybrids when a natural Russian formulation exists;
- lists of implementation identifiers before the problem is explained;
- RF/SER/TASK IDs as substitutes for subject, predicate, and consequence.

For example, instead of:

```text
test-app structurally != prod-app -> prod-risks untestable
```

explain that the test application is assembled differently from the production application, which runtime paths are therefore not reproduced, and why a green test suite does not prove the absence of those regressions.

### 8.2 Terminology quality

Prefer natural Russian technical language over literal translation or transliteration.

Poor:

```text
негрейсфул shutdown
credential-ами
prod-risks
designated owner отсутствует
runtime-drift
```

Better:

```text
некорректное/неполное завершение работы
учётные данные
риски production-конфигурации
явный владелец ресурса
расхождение поведения между версиями во время выполнения
```

If an English term is the exact name of a concept, API, or established term and a Russian equivalent reduces precision, keep the English term and briefly explain it on first use.

Avoid unexplained labels such as `god object`, `spaghetti`, or `bad practice`, and avoid rhetorical intensifiers not supported by adjudicated severity.

## 9. Diagram contract

A diagram is required when it materially improves understanding of topology, ordering, lifecycle, ownership, trust boundaries, state transitions, or Before/After architecture. There is no decorative quota.

For a substantial `STANDARD_FULL` or `FORENSIC` final package, useful visual coverage is expected when the corresponding mechanisms exist:

- **As-Built:** at least one component/boundary diagram when the system has several material runtime components, processes, or external dependencies;
- **Runtime/lifecycle:** a sequence, state, or flow diagram for at least one material flow or lifecycle mechanism when ordering or ownership affects correctness;
- **Target Architecture:** a target component/boundary diagram when the endpoint includes target work and the target materially changes ownership, boundaries, or flows;
- **Before → After:** for a material architectural change that is difficult to understand from prose alone;
- **Roadmap dependencies:** a dependency diagram when task ordering has non-trivial prerequisites or a safe-activation boundary.

If a substantial report contains no useful diagrams, the final writer/reviewer must explicitly explain why visualization would not add architectural information. The exception must be evidence-based, not the result of forgetting the diagrams.

Follow `lifecycle-and-mermaid.md` for syntax and evidence rules.

## 10. Executive summary

Within the first 1–2 pages, the reader should understand:

- overall architectural health;
- the top 3–7 risks;
- security and data-integrity blockers;
- lifecycle and resource-ownership quality;
- whether incremental remediation is viable;
- whether there is a reason to block feature development;
- which endpoint was completed and which documents are authoritative.

The Executive Summary explains the system-level picture in human language first; tables and IDs follow the narrative synthesis.

## 11. Verification table

For a Russian-language final document, use a human-readable table such as:

```markdown
| Команда/проверка | Результат | Ограничение/комментарий |
|---|---|---|
```

Do not hide unavailable checks.

## 12. Final status

### Finding lifecycle, derived views, and progress

The common reporting model applies to accepted `RF-*` and `CQ-*` owner revisions. It does not create a shared finding authority and does not coerce Test Engineering families into these states.

| Dimension | Values | Meaning |
|---|---|---|
| `lifecycle` | `ACTIVE | RESOLVED | SUPERSEDED` | Owner-controlled technical lifecycle; `REOPENED` is derived only. |
| `freshness` | `CURRENT | STALE | BLOCKED` | Strength/availability of current evidence. |
| `disposition` | owner-qualified treatment | Action required, accepted risk/exception, declined, or deferred only where the owner contract defines it. |
| `remediation_status` | owner-specific work state | Execution state such as `BLOCKED`; never a lifecycle or disposition decision. |

Always qualify `BLOCKED` as `freshness=BLOCKED` or `remediation_status=BLOCKED`. They may coexist and have different effects.

### Current Findings predicate

`Current Findings` is a derived view over one accepted owner-authority snapshot. It includes each qualified active finding with its owner, stable identity, accepted revision, lifecycle, disposition, severity, source/baseline binding, freshness, evidence, and lineage references.

| State | Current Findings | Additional result |
|---|---|---|
| `lifecycle=ACTIVE, freshness=CURRENT` | included | actionable or accepted residual risk by disposition |
| `lifecycle=ACTIVE, freshness=STALE` | included | revalidation limitation; not verified-current |
| `lifecycle=ACTIVE, freshness=BLOCKED` | included | freshness limitation; excluded from `VERIFIED_CURRENT` |
| `lifecycle=ACTIVE, remediation_status=BLOCKED` | included | remediation-blocked label; remains technical risk |
| `lifecycle=RESOLVED, freshness=CURRENT` | excluded | resolved flow/history |
| `lifecycle=RESOLVED` with stale proof after source/dependency advancement | excluded from verified absence | `RESOLUTION_REVALIDATION_REQUIRED`; historical resolution remains bound to old source |
| `lifecycle=SUPERSEDED` | excluded | supersession history and replacement lineage |
| `LEGACY_STATUS_UNKNOWN` | excluded from definitive lifecycle/severity counts | mandatory migration uncertainty |
| unavailable owner/member | no invented row | availability limitation; never zero or unchanged |

An active accepted-risk disposition remains in technical Current Findings and current stock, but is excluded from actionable/open requiring remediation. Its transition from `ACTION_REQUIRED` to accepted risk emits `ACCEPTED_RISK_ADDED`, leaves current stock and lifecycle counts unchanged, decreases actionable count, and increases residual accepted risk. The reverse emits `ACCEPTED_RISK_REMOVED`; neither transition is `NEW` or `RESOLVED`. `WONT_FIX` is not accepted risk unless its owner contract establishes exact equivalence.

### Historical Findings and progress

The derived Historical Findings view preserves every accepted identity and immutable revision, including active, resolved, superseded, reopened, and legacy/unknown records. Report these separately as `REGISTERED_RF`, `RESOLVED_RF_HISTORICALLY`, `SUPERSEDED_RF_HISTORICALLY`, `CURRENT_RF`, and `ACCEPTED_RISK_RF`; they are overlapping views, not an arithmetic partition.

Compare two exact accepted baselines for the same qualified scope and frozen member/source vector. Join by qualified stable identity, then compare accepted revisions. Derived labels are:

```text
NEW, RESOLVED, REOPENED, SUPERSEDED, UNCHANGED,
SEVERITY_INCREASED, SEVERITY_DECREASED,
ACCEPTED_RISK_ADDED, ACCEPTED_RISK_REMOVED
```

Each identity receives at most one lifecycle transition per baseline pair; severity and disposition changes attach as classification flows. Current stock and severity buckets are stocks; lifecycle labels are flows; severity and disposition labels are classification flows. A complete comparable pair may use:

```text
CURRENT(N+1) = CURRENT(N) + NEW + REOPENED - RESOLVED - SUPERSEDED
```

Never force this equation for unavailable, unknown, or otherwise incomparable scope. `RESOLVED` and `SUPERSEDED` are distinct and supersession receives no resolution credit. Severity changes preserve identity and lifecycle unless a separate accepted lifecycle revision changes it.

### Source-bound resolution freshness

Every resolved revision proves absence only for its exact accepted source/evidence/dependency snapshot. When that binding advances, retain the historical `RESOLVED` fact but do not report `RESOLVED + CURRENT` on the new source. Expose `RESOLUTION_REVALIDATION_REQUIRED`, do not synthesize `ACTIVE`, and route owner revalidation. Active stale findings remain visible with a limitation and are not asserted definitely applicable to the advanced source.

### Legacy qualification

Legacy records are registered under their existing owner and stable identity without rewriting the old package. Evidence tiers are:

1. explicit accepted owner lifecycle/status with complete identity and owner binding — mechanical;
2. complete accepted resolution/supersession with identity, owner, and exact source binding — mechanical when complete;
3. finding-tied accepted remediation verification without lifecycle authority — owner adjudication required;
4. report/projection prose, including “fixed” — insufficient;
5. commit messages, code absence, timestamps, or inference — insufficient.

Only complete Tiers 1–2 mechanically migrate lifecycle. Otherwise derive `LEGACY_STATUS_UNKNOWN` as a migration/qualification condition. Unknown records are excluded from definitive lifecycle/severity and verified-current counts, shown as mandatory uncertainty, and cannot be treated as zero or verified resolved by Product. Existing projections use their current legacy registration and remain non-current until their own verification; Product baselines with unproven child bindings require bounded requalification.

`REVIEW_COMPLETE` is allowed only after the completion gates in `SKILL.md`, including independent verification/adjudication, cross-link checks, and editorial correction/re-review.

Otherwise return `REVIEW_PARTIALLY_COMPLETE` with the exact missing evidence and gates.