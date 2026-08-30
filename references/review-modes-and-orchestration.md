# Режимы и управление процессом аудита

Этот файл является **авторитетным источником** для выбора режима, конечного результата, структуры рабочего пакета, `working/INDEX.md`, статусов процесса, возобновления, передачи между агентами и отображения прогресса.

## 1. Стартовый выбор

Перед существенным исследованием покажи пользователю рекомендацию и два независимых выбора.

### Глубина

`STANDARD_FULL (полный стандартный аудит)` — полный evidence-first аудит с подробной фактической архитектурой, тематическим исследованием, независимой проверкой кандидатов, проверкой корневых причин и отдельной оценкой критичности. Рабочие артефакты компактнее, чем в forensic-режиме.

`FORENSIC (углублённое архитектурное расследование)` — максимальная глубина для сложных, конкурентных, security-sensitive или спорных систем. Тематические области исследуются отдельными рабочими проходами, история исправлений/опровержений сохраняется подробнее, а gates разделены явно.

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
├── 02-independent-verification.md
├── 03-root-and-severity-adjudication.md
├── 04-target-consistency.md       # если нужно
├── 05-roadmap-consistency.md      # если нужно
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

Создавай условные файлы только когда соответствующий проход реально нужен.

## 3. Карта авторитетности

Не дублируй один нормативный контракт в нескольких местах.

| Концепт | Авторитетный источник |
|---|---|
| mode / endpoint / workflow state / resume / subagent handoff | `review-modes-and-orchestration.md` |
| общая evidence-first методика | `review-method.md` |
| ownership/invariants/adversarial scenarios | `ownership-and-scenarios.md` |
| IPC/API/native/process boundary dimensions | `boundary-contract-audit.md` |
| evidence / candidate lifecycle / severity / security attack chain | `evidence-and-severity.md` |
| независимая falsification | `independent-verification.md` |
| root/projection/SER split | `root-boundary-adjudication.md` |
| lifecycle diagrams | `lifecycle-and-mermaid.md` |
| финальный пакет / cross-links / writing | `report-contract.md` |
| target review | `target-architecture-review.md` |
| roadmap review | `remediation-roadmap-review.md` |
| editorial gate | `final-editorial-review.md` |

`SKILL.md` оркестрирует эти контракты и не должен переопределять их подробно.

## 4. `working/INDEX.md`

`INDEX.md` — постоянный источник состояния процесса. Он должен оставаться компактным.

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
10. supersessions/corrections;
11. authoritative-document registry.

Только coordinator редактирует `INDEX.md`. Тематические агенты пишут собственные файлы и persisted handoff.

## 5. Статусы

Используй закрытый набор:

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

После подтверждённой корректировки As-Built:

```text
COMPLETE
→ REVALIDATION_REQUIRED
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
- смена active top-level phase;
- завершение batch subagents после проверки их persisted handoffs и отражения результатов в `INDEX.md`;
- подтверждённая architecture correction и последующее выставление `REVALIDATION_REQUIRED` зависимым stages.

При initial setup, если native tool доступен, вызови его сразу после создания/заполнения `INDEX.md`.

При resume обязательный порядок:

```text
read INDEX
→ verify/reconcile persisted artifacts and handoffs
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
[!] Независимое ревью As-Built — REVIEW_REQUIRED
[ ] Владение и изоляция — PENDING
[?] Security — BLOCKED: нужен продуктовый ответ OQ-004
```

План динамический: подтверждённые architecture corrections могут добавить correction/impact/revalidation stages. Не перезапускай весь аудит, если impact scan показывает локальное влияние.

## 8. Subagents и стабильность

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

Один файл — один активный writer. Параллельные агенты не редактируют один файл.

Сначала Baseline → As-Built → независимое As-Built review. Только после принятия As-Built запускай зависимые thematic passes.

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

При подтверждении отдельный correction pass изменяет технический As-Built, затем выполняется impact scan и только затронутые завершённые этапы получают `REVALIDATION_REQUIRED`.

## 10. As-Built authority

Во время исследования контролируемый working As-Built (`00-...as-built.md`) — **технический источник истины** для фактов архитектуры.

`01-architecture-review.md` содержит производную пользовательскую проекцию. Если технический As-Built меняется после её сборки, зависимые разделы финального отчёта считаются stale до повторной synthesis/review.

Независимое As-Built review обязательно в обоих режимах; в `STANDARD_FULL` оно может быть компактнее.

## 11. Recovery

При новой сессии:

```text
read INDEX
→ verify baseline and referenced artifacts
→ reconcile any persisted handoff not reflected in INDEX
→ reconstruct true workflow state
→ call native todo/task/plan tool with reconstructed state, if available
→ identify first non-accepted required gate
→ continue
```

Не полагайся на память предыдущего чата и не используй stale native UI как authority.
