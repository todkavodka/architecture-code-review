# Architecture Code Review — архитектура Review Suite

Этот документ объясняет **что именно строит Skill**, какие части системы являются фактами, какие — интерпретациями, как разделены ответственности и почему итоговые Markdown-документы не считаются источником истины сами по себе.

README остаётся короткой входной страницей. Здесь находится концептуальная модель Review Suite.

## 1. Review Suite

`architecture-code-review` — это не один линейный аудит. Это набор независимых capability, которые работают поверх общего слоя доказательств и общей фактической модели системы.

```text
Repository / external sources
          |
          v
   Shared Evidence
      WS-* / EV-*
          |
          v
Shared Technical Model
          STM
          |
   +------+------+----------------+
   |             |                |
   v             v                v
Architecture   Test            Code Quality
 Review      Engineering        Review
   |             |                |
  RF-*       BC/CC/MAT/...      CQ/CQRA
   |             |                |
   +-------------+----------------+
                 |
                 v
           Projections
          PRJ-* documents
```

Три top-level capability:

- **Architecture Review** — архитектурные свойства, ownership, lifecycle, boundaries, root causes, reliability/security implications;
- **Test Engineering** — проверяемое поведение, assurance coverage, contract consistency и проектирование тестовых артефактов;
- **Code Quality Review** — реализационные механизмы с существенными последствиями для maintainability, reliability, testability и других качеств.

Они выбираются независимо. Ни одна capability не является обязательным родителем другой.

Для `NEW` действует инвариант:

```text
AT_LEAST_ONE_TOP_LEVEL_CAPABILITY_SELECTED
```

Допустимы все семь непустых комбинаций Architecture / Test / Code Quality.

## 2. Почему общий factual layer отделён от findings

Одна из главных проблем больших review — разные агенты могут независимо реконструировать одну и ту же систему и получить несовместимые версии «фактов».

Поэтому в Review Suite фактическая модель выделена отдельно:

```text
Evidence observation
        |
        v
Accepted technical fact
        |
        +--> Architecture interpretation
        +--> Test interpretation
        +--> Code Quality interpretation
```

Например, факт:

```text
INT-014
worker publishes completion event after database commit
```

может одновременно использоваться:

- Architecture Review для анализа ownership/order guarantees;
- Test Engineering для формирования `BC-*` и `MAT-*`;
- Code Quality Review для анализа конкретного implementation mechanism.

Но сам факт не становится автоматически ни `RF-*`, ни `GAP-*`, ни `CQ-*`.

## 3. Shared Evidence: `WS-*` и `EV-*`

Shared Evidence хранит наблюдения, привязанные к baseline.

```text
WS-* = bounded workset / investigation
EV-* = addressable observation inside WS
```

Пример:

```text
WS-012-payment-retry
  scope: retry and publication path
  baseline: abc123

  EV-001
    source: src/payment/retry.py
    symbol: RetryCoordinator.complete
    observed: completion updates row before publishing event
```

Ссылка на observation выглядит концептуально так:

```text
WS-012-payment-retry#EV-001
```

`EV-*` фиксирует **что было замечено**, но не объясняет, хорошо это или плохо.

Историческое observation не переписывается под новый baseline. Если код изменился, создаётся новое evidence или проводится revalidation.

## 4. Shared Technical Model

STM — persistent semantic authority для принятых общих технических фактов.

Основные семейства:

```text
COMP-*    Component / Runtime Unit
IF-*      Interface
INT-*     Interaction
DS-*      Data Store
EVENT-*   Event / Message
FLOW-*    Material Flow
AUTH-*    Auth / Trust Boundary
CFG-*     Configuration Fact
ERR-*     Error / Failure Contract
```

Пример связей:

```text
COMP-API
  PROVIDES -> IF-REST
  WRITES_TO -> DS-POSTGRES
  PUBLISHES -> EVENT-ORDER-CREATED

COMP-WORKER
  SUBSCRIBES -> EVENT-ORDER-CREATED
  WRITES_TO -> DS-POSTGRES
```

STM отвечает на вопрос:

> **Что в системе материально существует или происходит?**

Он не отвечает:

- является ли это архитектурным defect;
- достаточно ли это покрыто тестами;
- плох ли implementation pattern;
- какой remediation приоритетнее.

Это уже authority соответствующих capability.

## 5. Technical Model Gate

Принятые STM facts может менять только Technical Model Gate.

Capability не должна напрямую переписывать STM. Она может создать запрос:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

Это предотвращает ситуацию, когда Architecture Review, Test Engineering и Code Quality одновременно редактируют один факт под собственные выводы.

## 6. Architecture Review authority

Architecture Review использует STM как фактический substrate, а затем создаёт собственную интерпретацию.

Основной final finding:

```text
RF-* = Architecture/root finding
```

Типичный путь:

```text
accepted STM
  -> thematic discovery
  -> coverage accounting
  -> candidate verification
  -> root-boundary adjudication
  -> severity
  -> RF-*
```

As-Built Architecture — человекочитаемая проекция принятой фактической модели плюс architecture-oriented synthesis. Она полезна для человека, но не заменяет STM.

Если заказан endpoint:

```text
REVIEW_ONLY
REVIEW_PLUS_TARGET_ARCHITECTURE
REVIEW_PLUS_TARGET_AND_ROADMAP
```

могут дополнительно появиться Target Architecture и Remediation Roadmap.

## 7. Test Engineering authority

Test Engineering разделяет несколько разных сущностей:

```text
BC-*    Behavior Contract
CC-*    Contract Consistency Record
MAT-*   Material Assurance Target
TM-*    Test Mapping
GAP-*   Assurance Gap
TASK-*  Test Engineering remediation task
```

Они не взаимозаменяемы.

```text
BC != MAT
BC != GAP
CC != GAP
TM != BC
TASK != CQRA
```

Пример:

```text
BC-042
Only the current generation may publish terminal state.

MAT-017
Publication uniqueness must be proven under retry and timeout.

TM-021
integration/test_publication_retry.py::test_timeout_retry

GAP-008
No executable evidence for concurrent retry publication.
```

`Behavior Model` — внутренний слой, а не пользовательский checkbox.

Если существует существенный formal contract, `Contract Verification` запускается автоматически и сравнивает:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

## 8. Code Quality authority

Code Quality Review отвечает за:

```text
CQ-*    accepted Code Quality finding
CQRA-*  Code Quality remediation action
```

При этом:

```text
tool warning != CQ finding
metric != CQ finding
smell != CQ finding
candidate != semantic authority
```

Finding появляется только при доказанном material consequence.

Например, «файл большой» сам по себе не finding. Но если конкретный механизм делает lifecycle неразделимым, усложняет тестирование и приводит к подтверждённым ошибкам ownership — это уже может стать `CQ-*`.

`CQRA COMPLETED` также не означает автоматического `CQ RESOLVED`: resolution требует evidence-backed revalidation.

## 9. Cross-capability boundaries

Review Suite специально не сводит всё к одному универсальному finding.

```text
RF-*  != CQ-*
CQ-*  != GAP-*
CQRA  != TASK-*
BC-*  != STM fact
```

Один и тот же механизм может иметь несколько связанных интерпретаций.

Например:

```text
EV / STM fact
   |
   +--> CQ-012 duplicated retry implementation
   |
   +--> RF-007 publication ownership ambiguity
   |
   +--> GAP-004 no concurrent retry proof
```

Эти записи могут быть связаны, но каждая остаётся authority своей capability.

## 10. Semantic state и projections

Review Suite разделяет:

```text
semantic authority
        !=
human-readable projection
```

Projection имеет stable identity `PRJ-*` и выводится из accepted authority.

Например:

```text
CQ-* authority
   |
   +--> PRJ-CQ-00 Findings View
   +--> PRJ-CQ-01 Summary
   +--> PRJ-CQ-02 Hotspots
```

Projection может быть stale, не делая semantic authority ложной.

И наоборот, красивый Markdown-файл не считается accepted authority только потому, что он существует.

## 11. Freshness

В системе есть несколько независимых типов актуальности.

У STM, capability semantic records и projections свои lifecycle/freshness правила.

Важно:

```text
semantic REVALIDATE
        !=
projection regeneration
```

После semantic change выполняется Projection Impact Analysis. Она определяет, какие projections теперь stale или blocked, но не регенерирует их автоматически.

Для regeneration используется отдельная `RG-*` session.

## 12. `working/INDEX.md`

`working/INDEX.md` — coordinator workflow authority.

Он нужен, чтобы после паузы восстановить:

- repository/baseline;
- Session Intent;
- выбранные capability;
- capability configuration/output selection;
- current phase;
- gates;
- artifact registry;
- handoffs;
- blockers;
- projection/package routing state.

Он **не хранит второй экземпляр semantic model**.

```text
INDEX -> owning artifact -> evidence -> source
```

Именно поэтому `INDEX.md` нельзя использовать как замену чтению owning artifact, если требуется substantive technical decision.

## 13. Что читать дальше

- [Artifacts and State](artifacts-and-state.md) — какие файлы, IDs и indexes создаются;
- [Workflows](workflows.md) — как работают `NEW`, `RESUME`, `REVALIDATE`, `EXTEND` и другие intents;
- [Output Guide](output-guide.md) — какие пользовательские документы можно получить и зачем;
- [Roadmap](roadmap.md) — направления развития Skill.

Нормативные contracts остаются в `references/` и `capabilities/*/references/`. Документы в `docs/` объясняют модель человеку, но не заменяют эти contracts.