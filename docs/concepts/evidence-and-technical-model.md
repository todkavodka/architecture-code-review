# Shared Evidence и Shared Technical Model

Этот документ объясняет, как Skill превращает чтение repository и внешних источников в повторно используемые технические факты.

## Зачем разделять evidence и facts

Если сразу превращать наблюдение из кода в finding, теряется важная граница:

```text
что источник показал
!=
что это означает для архитектуры, тестов или качества кода
```

Поэтому factual pipeline состоит минимум из двух уровней:

```text
Source
  -> Shared Evidence
  -> Shared Technical Model
```

Только после этого capability создаёт собственную интерпретацию.

## Shared Evidence

### `WS-*`

`WS-*` — bounded investigation/workset. Он задаёт область одного исследовательского прохода и физически группирует observations.

Минимально workset фиксирует:

- stable ID;
- scope;
- baseline;
- status;
- investigated sources;
- limitations;
- `EV-*` observations;
- handoff summary.

Один workset имеет одного активного writer. Это снижает риск, что несколько агентов одновременно перепишут одно и то же evidence state.

### `EV-*`

`EV-*` — логически адресуемое observation внутри workset.

Пример:

```text
WS-012-payment-retry#EV-003

source: src/payment/retry.py
symbol: RetryCoordinator.complete
baseline: 7f3a1c2
observed: state is persisted before completion event is published
```

`EV-*` не назначает severity, не говорит «это ошибка» и не выбирает remediation. Он фиксирует только evidence-bounded observation.

## Baseline binding

Evidence всегда связано с baseline. Старое observation нельзя переписать так, чтобы оно выглядело актуальным для нового commit.

Если исходный код изменился:

1. старое observation сохраняется как historical evidence;
2. impact analysis определяет, нужна ли fresh evidence;
3. при необходимости создаётся новая observation/revision-bound evidence;
4. dependent semantics проходит revalidation.

Так сохраняется история того, почему был принят прошлый вывод.

## Shared Technical Model

STM хранит принятые общие технические факты.

Основные families:

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

Факт STM отвечает на вопрос «что материально существует или происходит в системе?».

Он не отвечает:

- является ли это defect;
- достаточно ли это протестировано;
- насколько это плохо реализовано;
- что исправлять первым.

## Identity и revision

Stable identity используется, пока речь идёт о той же семантической сущности.

Например:

```text
IF-021@rev1
IF-021@rev2
IF-021@rev3
```

означает ревизии одного интерфейса.

Если смысл сущности изменился настолько, что это уже другой object identity, старую запись не переписывают. Создаётся новая identity и явная связь supersession.

Это важно для revalidation: downstream records могут зависеть от конкретной identity/revision, а не просто от filename.

## Relations

STM использует controlled relation vocabulary, например:

```text
PROVIDES
CONSUMES
CALLS
PUBLISHES
SUBSCRIBES
READS_FROM
WRITES_TO
OWNS_STATE
PROTECTED_BY
CONFIGURED_BY
EMITS_ERROR
PARTICIPATES_IN
DEPLOYS_AS
DEPENDS_ON
```

Связи делают model пригодной для dependency traversal и impact analysis.

## Technical Model Gate

Accepted STM semantics меняет только Technical Model Gate.

Capability может сообщить:

```text
TECH_FACT_CANDIDATE
TECH_FACT_CONFLICT
TECH_FACT_REVALIDATION_REQUEST
```

но не должна напрямую переписывать accepted STM.

Это особенно важно, если Architecture Review и Test Engineering видят один факт по-разному: спор решается на уровне factual authority, а не победой «последнего writer».

## Multiple observed views

Один технический объект может иметь несколько representations:

```text
DECLARED
IMPLEMENTED
CONSUMED
TESTED
```

Например, OpenAPI говорит одно, backend реализует другое, frontend ожидает третье, а тесты проверяют четвёртое.

STM может сохранить эти observed views, но не выбирает автоматически «правильную» сторону. Когда требуется authority decision, его выполняет соответствующий specialist gate, например Contract Verification.

## Coverage

Создание persistent STM не означает полного описания repository.

```text
always create model
!=
always build complete model
```

Требуемая ширина зависит от downstream decision.

Полный Architecture Review требует принятой factual coverage достаточной для архитектурных утверждений. Узкий Code Quality Review может использовать bounded accepted slice.

Если coverage неполная, downstream claim должен быть ограничен этой реальностью. Skill не должен писать глобальный вывод, если evidence была локальной.

## Как читать факт до source

Типичный provenance path:

```text
semantic finding
  -> STM fact
  -> WS#EV
  -> raw source
```

Иногда semantic record может ссылаться прямо на evidence, если отдельный STM object не нужен. Главное — сохранить точную baseline-bound provenance.

## Что происходит при конфликте

Если dependent capability обнаруживает, что accepted fact больше не подходит:

```text
TECH_FACT_CONFLICT
or
TECH_FACT_REVALIDATION_REQUEST
```

До reconciliation нельзя использовать спорный required fact как accepted downstream truth.

При этом unrelated accepted work не обязано автоматически переоткрываться.

## Что читать дальше

- [Authority и provenance](authority-and-provenance.md)
- [Lifecycle и freshness](lifecycle-and-freshness.md)
- [Artifact Reference](../reference/artifacts.md)
