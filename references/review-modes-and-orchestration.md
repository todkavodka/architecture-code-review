# Режимы и управление процессом аудита

Этот файл является **авторитетным источником** для выбора режима, конечного результата, структуры рабочего пакета, `working/INDEX.md`, статусов процесса, возобновления, передачи между агентами и отображения прогресса.

Discovery Coverage semantics определены в `discovery-coverage.md`; здесь фиксируется только их место в workflow state, artifacts, resume и revalidation.

## 1. Стартовый выбор

Перед существенным исследованием покажи пользователю рекомендацию и два независимых выбора.

### Глубина

`STANDARD_FULL (полный стандартный аудит)` — полный evidence-first аудит с подробной фактической архитектурой, thematic discovery, Discovery Coverage closeout, независимой проверкой кандидатов, проверкой корневых причин и отдельной оценкой критичности. Рабочие артефакты компактнее, чем в forensic-режиме.

`FORENSIC (углублённое архитектурное расследование)` — максимальная глубина для сложных, конкурентных, security-sensitive или спорных систем. Тематические области исследуются отдельными рабочими проходами, Discovery Coverage имеет отдельный independent gate, история исправлений/опровержений сохраняется подробнее, а gates разделены явно.

Skill может рекомендовать режим, но не должен молча выбирать `FORENSIC`.

### Конечный результат

Глубина не определяет endpoint автоматически.

- `REVIEW_ONLY` — аудит и авторитетный реестр замечаний.
- `REVIEW_PLUS_TARGET_ARCHITECTURE` — аудит + целевая архитектура после принятия аудита.
- `REVIEW_PLUS_TARGET_AND_ROADMAP` — аудит + целевая архитектура + план исправлений после принятия предыдущих артефактов.

Не добавляй оценки времени или ярлыки «лёгкий/сложный/максимальный».

## 2. Пакет артефактов

Рекомендуемый корень:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md          # если заказано
├── 04-remediation-roadmap.md          # если заказано
└── working/
    ├── README.md
    ├── INDEX.md
    └── ...
```

Следуй локальной директории проекта, если у репозитория уже есть установленная convention.

### STANDARD_FULL

```text
working/
├── README.md
├── INDEX.md
├── 00-baseline-and-as-built.md
├── 00a-as-built-review.md
├── 01-discovery-and-scenarios.md
├── 01a-discovery-coverage-matrix.md
├── 01b-independent-coverage-review.md
├── 01c-coverage-correction.md       # conditional
├── 01d-coverage-re-review.md        # conditional
├── 02-independent-verification.md
├── 03-root-and-severity-adjudication.md
├── 04-target-consistency.md         # если нужно
├── 05-roadmap-consistency.md        # если нужно
└── 06-final-editorial-review.md
```

### FORENSIC

```text
working/
├── README.md
├── INDEX.md
├── 00-baseline-as-built.md
├── 00a-as-built-independent-review.md
├── 01-invariants-ownership-isolation.md
├── 02-lifecycle-cancellation-concurrency.md
├── 03-boundary-contracts.md
├── 04-frontend-state-events.md
├── 05-security-trust-boundaries.md
├── 06-maintainability-tests.md
├── 06a-discovery-coverage-matrix.md
├── 06b-independent-coverage-review.md
├── 06c-coverage-correction.md       # conditional
├── 06d-coverage-re-review.md        # conditional
├── 07-independent-verification.md
├── 08-root-boundary-adjudication.md
├── 09-severity-adjudication.md
├── 10-authoritative-compaction-check.md
├── 11-target-consistency-review.md
├── 11a-target-correction.md
├── 11b-target-re-review.md
├── 12-roadmap-execution-consistency.md
├── 12a-roadmap-correction.md
├── 12b-roadmap-re-review.md
├── 13-final-editorial-review.md
├── 13a-editorial-correction.md
└── 13b-final-editorial-re-review.md
```

Создавай conditional correction/re-review files только когда соответствующий pass реально нужен.

## 3. Карта авторитетности

Не дублируй один нормативный контракт в нескольких местах.

| Концепт | Авторитетный источник |
|---|---|
| mode / endpoint / workflow state / resume / subagent handoff | `review-modes-and-orchestration.md` |
| общая evidence-first методика | `review-method.md` |
| discovery coverage matrix / domains / coverage verdicts / coverage review | `discovery-coverage.md` |
| ownership/invariants/adversarial scenarios | `ownership-and-scenarios.md` |
| interaction/interpreter/resource/authority boundary dimensions | `boundary-contract-audit.md` |
| evidence / candidate lifecycle / severity / security attack chain | `evidence-and-severity.md` |
| независимая falsification кандидатов | `independent-verification.md` |
| root/projection/SER split | `root-boundary-adjudication.md` |
| lifecycle diagrams | `lifecycle-and-mermaid.md` |
| финальный пакет / cross-links / writing | `report-contract.md` |
| target review | `target-architecture-review.md` |
| roadmap review | `remediation-roadmap-review.md` |
| editorial gate | `final-editorial-review.md` |

`SKILL.md` оркестрирует эти контракты и не должен переопределять их подробно.

## 4. `working/INDEX.md`

`INDEX.md` — постоянный источник состояния процесса. Он должен оставаться компактным.

### Session Orchestration projection

Startup selection is owned by `references/session-orchestration.md`. Persist its
compact routing projection here, without turning it into substantive technical
authority:

```text
orchestrator_version: 0.3
session_intent
repository_identity
source_audit
source_audit_revision
previous_baseline
current_baseline
baseline_type
working_tree_snapshot
working_tree_snapshot_algorithm
review_suite
stack_addenda
project_profile:
  schema_version
  collector_version
  collected_for_revision
  status
  artifact_or_projection_ref
revalidation:
  change_range
  impact_status
  impact_classification
  affected_domains
  affected_findings
  affected_capabilities
  preserved_domains
  context_expansions
```

Absent v0.3 fields in a legacy package indicate legacy state requiring additive
reconciliation/backfill, not automatic corruption. Validate owning-artifact
freshness before using any projection downstream.

Session integration rules:

```text
USE_EXISTING → no technical stage transition solely for startup; metadata actions may update projection.
RESUME → reconstruct true workflow state, reconcile changed baseline if required, then continue first non-accepted gate.
REVALIDATE → delegate project-change evidence semantics to revalidation-and-freshness.md.
EXTEND → reuse capability registry/minimal dependency slice; do not reopen unrelated accepted stages.
NEW → enter existing full review flow with selected mode/endpoints/capabilities.
```

Test Review methodology remains in `capabilities/test-review/SKILL.md`; startup
visibility and selection remain in Session Orchestration.

Минимальные разделы:

1. repository path/ref/commit и dirty-state на старте;
2. mode и endpoint;
3. current phase;
4. execution plan;
5. artifact registry;
6. candidate registry;
7. positive controls;
8. open questions;
9. architecture-correction candidates;
10. Discovery Coverage projection;
11. supersessions/corrections;
12. authoritative-document registry.

13. capability registry.

### Discovery Coverage projection

Полная matrix принадлежит `01a-...` / `06a-...` artifact. `INDEX.md` хранит только компактную projection:

```text
coverage_artifact: working/<coverage-matrix-file>
coverage_review: <verdict>
baseline: <commit/ref>

domains:
  total: <n>
  covered: <n>
  not_applicable: <n>
  partial: <n>
  blocked: <n>

high_risk:
  applicable: <n>
  accepted: <n>
```

Перед downstream use coordinator обязан проверить freshness/revision binding owning coverage artifact и independent coverage review.

Только coordinator редактирует `INDEX.md`. Тематические агенты пишут собственные файлы и persisted handoff.

### Capability registry

`INDEX.md` records capability ownership and dependency freshness in a compact
registry. The following statuses reuse the existing workflow state vocabulary:

```text
capabilities:
  - id: test-review
    status: PENDING | IN_PROGRESS | REVIEW_REQUIRED | REVALIDATION_REQUIRED | BLOCKED | COMPLETE | NOT_APPLICABLE
    endpoint: REVIEW_ONLY | REVIEW_PLUS_TEST_PLAN  # legacy Test Review input/projection
    outputs:
      test_assurance: true
      test_plan: false
      contract_consistency_report: false
      test_environment_design: false
      service_simulator_design: false
      service_simulator_implementation_plan: false
      e2e_test_plan: false
    owning_artifact: <path>
    owning_artifact_revision: <revision>
    dependencies:
      - <artifact/ref + revision>
```

For Test Engineering, `outputs` is the persisted configuration authority; the
legacy `endpoint` is retained only for backward-compatible Test Review packages
and must not be used as the sole output selection. When normalizing legacy state:

```text
REVIEW_ONLY
  → test_assurance=true; every optional output=false

REVIEW_PLUS_TEST_PLAN
  → test_assurance=true; test_plan=true; every other optional output=false
```

Normalization is additive and conservative: it never infers an extended output.
`test_assurance` is required when the capability is enabled. Behavior Model is
an internal dependency and materially applicable Contract Verification is an
automatic gate; neither is a persisted user-selected output.

Test Review may be selected initially, recommended from a discovered material test
surface, or attached to an existing audit. Later attachment resumes from `INDEX`:

```text
resume INDEX
→ verify baseline/freshness
→ register capability
→ determine minimal accepted dependency slice
→ execute capability-owned pass
→ capability review/adjudication
→ reconcile cross-capability findings/corrections
→ targeted revalidation only for affected dependencies
```

Adding a capability does not restart unrelated accepted stages by default. A stale
or disputed dependency blocks downstream use under the freshness contract.

For the Test Engineering extension, the capability registry may project these
separate outputs and their owning artifacts:

```text
00-test-assurance-summary.md
01-test-assurance-map.md
02-test-plan.md                              # optional compatibility output
03-behavior-contract-model.md                # when extended model is required
04-contract-consistency-report.md            # optional projection
05-test-environment-design.md                # optional
06-service-simulator-spec.md                 # optional
07-service-simulator-implementation-plan.md  # optional
08-e2e-test-plan.md                          # optional
working/                                     # authoritative BC/CC/TM/GAP ledgers
```

The registry stores output selection as the independent `outputs` fields above.
An E2E Test Plan
requires Test Assurance, the internal Behavior Model, applicable Contract
Verification, and E2E Design; Service Simulator Design is added only when the
selected topology requires it. A Service Simulator Implementation Plan requires
an accepted and fresh simulator specification. `EXTEND` reuses the accepted
upstream slice instead of replaying the full review.

Capability-owned artifacts may use project-local paths, for example:

```text
capabilities/test-review/01-test-assurance-map.md
capabilities/test-review/02-test-plan.md
working/capabilities/test-review/...
```

The `INDEX` ownership and revision binding are the invariant, not the exact paths.

## 5. Статусы

Общие artifact/stage statuses:

```text
PENDING
IN_PROGRESS
ARTIFACT_WRITTEN
REVIEW_REQUIRED
CORRECTION_REQUIRED
REVALIDATION_REQUIRED
BLOCKED
COMPLETE
NOT_APPLICABLE
```

Coverage-row states и coverage-review verdicts принадлежат `discovery-coverage.md` и не заменяют общий lifecycle status.

`ARTIFACT_WRITTEN` означает только факт записи. Для артефакта с обязательным review следующий статус — `REVIEW_REQUIRED`, а не `COMPLETE`.

Типовой цикл:

```text
PENDING
→ IN_PROGRESS
→ ARTIFACT_WRITTEN
→ REVIEW_REQUIRED
→ COMPLETE
```

При замечаниях:

```text
REVIEW_REQUIRED
→ CORRECTION_REQUIRED
→ IN_PROGRESS
→ ARTIFACT_WRITTEN
→ REVIEW_REQUIRED
→ COMPLETE | BLOCKED
```

Coverage-specific semantic loop:

```text
Discovery artifacts COMPLETE
→ Coverage Matrix closeout
→ Independent Coverage Review
→ COVERAGE_ACCEPTED
```

При coverage gap:

```text
COVERAGE_CORRECTION_REQUIRED
→ targeted coverage correction
→ matrix update
→ impacted-domain coverage re-review
→ COVERAGE_ACCEPTED | COVERAGE_BLOCKED
```

`COVERAGE_BLOCKED`, `COVERAGE_AUTHORITY_DRIFT` и `COVERAGE_CORRECTION_REQUIRED` нельзя project как `COMPLETE` для downstream candidate verification.

После подтверждённой корректировки As-Built:

```text
COMPLETE
→ impact scan
→ affected technical/coverage stages REVALIDATION_REQUIRED
→ IN_PROGRESS
→ ARTIFACT_WRITTEN/REVIEW_REQUIRED
→ COMPLETE | CORRECTION_REQUIRED | BLOCKED
```

`REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED` и `BLOCKED` **не являются принятым авторитетным входом** для зависимых downstream-этапов.

## 6. Persisted handoff

Никакое состояние, необходимое для resume, не должно существовать только в чате.

Каждый agent-owned working artifact заканчивается жёстко структурированным разделом:

```markdown
## HANDOFF SUMMARY

status: ARTIFACT_WRITTEN
baseline: <commit/ref>
artifact: <relative path>
new_candidates:
- ...
positive_controls:
- ...
open_questions:
- ...
architecture_correction_candidates:
- ...
supersedes:
- ...
```

Coverage artifacts дополнительно должны явно ссылаться на owning matrix/review baseline и affected domains, если pass является correction/re-review.

Допускается `none`, но поля должны присутствовать.

Безопасный порядок:

```text
write complete artifact
→ verify required headings/content
→ persist HANDOFF SUMMARY inside artifact
→ coordinator validates baseline + artifact path
→ coordinator updates INDEX
→ stage may advance
```

Если файл существует, а `INDEX.md` не обновлён после потери ответа/контекста:

```text
read persisted HANDOFF SUMMARY
→ validate artifact identity and baseline
→ reconcile INDEX
→ continue
```

## 7. Видимый план выполнения

Пользователь должен видеть текущий план и статус длинного аудита.

`INDEX.md` всегда является persistent authority. Любой native Todo/task/plan UI — только **non-authoritative projection** этого состояния.

- Если host предоставляет native todo/task/plan **tool**, coordinator обязан **реально вызвать этот tool** для создания и последующих обновлений видимого плана. Само изменение `INDEX.md`, prose вроде «план синхронизирован» или внутреннее reasoning не считаются синхронизацией UI.
- Если native tool отсутствует — показывай компактный текстовый план в CLI/chat.

### Native Plan Projection Sync Contract

После каждого **material coordinator state transition** порядок обязателен:

```text
validate completed artifact / persisted handoff
→ update working/INDEX.md
→ call the native todo/task/plan tool with the current projection, if available
→ only then advance/dispatch the next visible phase
```

К material transition относятся:

- изменение tracked stage между `PENDING`, `IN_PROGRESS`, `ARTIFACT_WRITTEN`, `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED`, `BLOCKED`, `COMPLETE`, `NOT_APPLICABLE`;
- изменение coverage review verdict, которое открывает/закрывает downstream gate;
- смена active top-level phase;
- завершение batch subagents после проверки их persisted handoffs и отражения результатов в `INDEX.md`;
- подтверждённая architecture correction и последующее выставление `REVALIDATION_REQUIRED` зависимым stages/domains.

При initial setup, если native tool доступен, вызови его сразу после создания/заполнения `INDEX.md`.

При resume обязательный порядок:

```text
read INDEX
→ verify/reconcile persisted artifacts and handoffs
→ validate coverage matrix/review baseline binding
→ reconstruct true workflow state
→ call native todo/task/plan tool with that reconstructed state, if available
→ identify first non-accepted gate
→ continue
```

Если host tool имеет конкретное имя, например `todowrite`, используй именно доступный runtime tool. Не ограничивай Skill одним vendor name: требование — **фактический tool invocation**, а не конкретное название API.

Не обновляй native UI после каждого microscopic tool call, чтения файла, shell-команды или внутреннего reasoning step. Цель — точная coarse-grained projection, а не шумный progress ticker.

Если native plan расходится с `INDEX.md`, это `NATIVE_PLAN_DRIFT`. Не доверяй UI и не перезапускай accepted work. Восстанови projection из `INDEX.md` реальным вызовом native tool, затем продолжай с первого реально non-accepted gate.

Пример:

```text
[✓] Фактическая архитектура — COMPLETE
[✓] Тематическое discovery — COMPLETE
[!] Discovery Coverage — COVERAGE_CORRECTION_REQUIRED
[ ] Independent Candidate Verification — PENDING
```

План динамический: подтверждённые architecture corrections и coverage review gaps могут добавить targeted correction/impact/revalidation stages. Не перезапускай весь аудит, если impact scan показывает локальное влияние.

## 8. Subagents и стабильность

### Context Orchestration v0.3

Capability dispatch uses the minimum fresh authoritative context needed for the
current decision. Start with structure/inventory, then materiality and evidence
pointers, then targeted reads; deepen only for unresolved material questions.

The dispatch envelope contains exact baseline/revision, mission and narrow scope,
forbidden scope, accepted dependency artifact pointers with revisions, required
shared/reference contracts, output path, and the `HANDOFF SUMMARY` contract.
Routing projections select reads but cannot replace owning decision evidence.
Unrelated accepted artifacts are not preloaded. A material omission or boundary
discovered outside the initial slice is a recorded `CONTEXT_EXPANSION_REQUIRED`,
not a blindfold or an unbounded restart.

Субагенты — механизм изоляции контекста, а не только ускорение.

Каждый substantial agent получает:

- exact baseline;
- mode/endpoint;
- `INDEX.md`;
- принятую As-Built базу;
- узкий scope;
- forbidden scope;
- собственный output path;
- `HANDOFF SUMMARY` contract.

Coverage Reviewer дополнительно получает bounded factual packet по `discovery-coverage.md`: accepted As-Built, matrix, thematic artifact registry, candidate/PC/OQ registries и baseline binding. Он не получает predecessor reasoning как authority.

Один файл — один активный writer. Параллельные агенты не редактируют один файл.

Сначала Baseline → As-Built → независимое As-Built review. Только после принятия As-Built запускай зависимые thematic passes.

После thematic discovery обязательный порядок:

```text
discovery artifacts complete
→ coverage matrix closeout
→ Independent Coverage Review
→ targeted correction/re-review if needed
→ COVERAGE_ACCEPTED
→ candidate verification
```

Параллельность ограниченная и адаптивная. При сомнении выполняй последовательно. Stability-first.

## 9. Architecture correction

Тематический агент не исправляет As-Built напрямую. Он создаёт `ARCH-CORRECTION-CANDIDATE` с текущим утверждением, противоречием, evidence и предполагаемым влиянием.

Отдельный fresh-context reviewer выдаёт:

```text
CONFIRMED_CORRECTION
REFUTED_CORRECTION
PARTIALLY_CORRECT
INSUFFICIENT_EVIDENCE
```

При подтверждении отдельный correction pass изменяет технический As-Built, затем выполняется impact scan.

Impact scan обязан включать Discovery Coverage:

```text
confirmed As-Built change
→ determine affected coverage domains
→ only affected accepted rows/stages become REVALIDATION_REQUIRED
```

Не сбрасывай unrelated accepted coverage без concrete impact.

## 10. Candidate verification gate

Independent candidate verification разрешён только при:

```text
DISCOVERY_COMPLETE
AND
COVERAGE_ACCEPTED
```

Следующие состояния запрещают переход:

```text
PARTIALLY_COVERED
BLOCKED
COVERAGE_CORRECTION_REQUIRED
COVERAGE_BLOCKED
COVERAGE_AUTHORITY_DRIFT
REVALIDATION_REQUIRED on material affected coverage
```

Coverage Review не проверяет correctness каждого кандидата; candidate verification не используется как замена coverage review.

## 11. As-Built authority

Во время исследования контролируемый working As-Built (`00-...as-built.md`) — **технический источник истины** для фактов архитектуры.

`01-architecture-review.md` содержит производную пользовательскую проекцию. Если технический As-Built меняется после её сборки, зависимые разделы финального отчёта считаются stale до повторной synthesis/review.

Независимое As-Built review обязательно в обоих режимах; в `STANDARD_FULL` оно может быть компактнее.

## 12. Recovery

При новой сессии:

```text
read INDEX
→ verify baseline and referenced artifacts
→ reconcile any persisted handoff not reflected in INDEX
→ validate coverage_artifact and coverage_review baseline/revision binding
→ reconstruct true workflow state
→ call native todo/task/plan tool with reconstructed state, if available
→ identify first non-accepted required gate
→ continue
```

Если INDEX утверждает `COVERAGE_ACCEPTED`, но owning matrix/review stale, missing или bound to another accepted As-Built/baseline, не доверяй compact projection. Используй freshness/reconciliation contract и верни соответствующий coverage stage в non-accepted state.

Не полагайся на память предыдущего чата и не используй stale native UI как authority.
