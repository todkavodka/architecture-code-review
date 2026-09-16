# Структура пакета аудита

Этот документ объясняет, какие данные сохраняет `architecture-code-review`, кто отвечает за их смысл и что можно безопасно переиспользовать, обновлять или пересобирать.

Цель — помочь человеку быстро понять пакет аудита без необходимости сначала читать нормативные контракты.

## 1. Пакет аудита — это не один отчёт

Итоговый Markdown — только одна часть результата.

Полный пакет обычно содержит:

- состояние координации;
- доказательства;
- Shared Technical Model;
- capability-specific semantic authority;
- findings и test records;
- projections;
- Product state, если используется многорепозиторный режим.

Именно поэтому старый отчёт нельзя просто отредактировать вручную и считать аудит обновлённым.

## 2. Упрощённая схема

```text
working/INDEX.md
    ↓
координация процесса

WS-* / EV-*
    ↓
наблюдения и доказательства

Shared Technical Model
    ↓
COMP-* IF-* INT-* DS-* EVENT-* FLOW-* AUTH-* CFG-* ERR-*

Architecture Review
    ↓
RF-*

Test Engineering
    ↓
BC-* CC-* MAT-* TM-* GAP-* TASK-*

Code Quality Review
    ↓
CQ-* и связанные remediation records

Projection layer
    ↓
PRJ-* / человекочитаемые документы
```

Структура конкретного пакета может отличаться физически. Важно не имя каталога, а ownership и semantic role артефакта.

## 3. `working/INDEX.md`

`working/INDEX.md` хранит состояние координации.

Обычно он отвечает на вопросы:

- какой baseline выбран;
- какая работа запрошена;
- какие capabilities включены;
- что завершено;
- что заблокировано;
- какие маршруты продолжения доступны;
- где находятся связанные артефакты.

### Что это за authority

`working/INDEX.md` — источник истины для координации процесса.

Он **не является**:

- Shared Technical Model;
- authoritative findings ledger;
- Test Engineering authority;
- Code Quality authority;
- projection authority;
- заменой соответствующим owner records.

Если индекс расходится с owner artifact, это не повод переписывать owner artifact по индексу.

## 4. `WS-*`: рабочие области исследования

`WS-*` — ограниченная область исследования.

Она связывает:

- выбранный scope;
- source baseline;
- исследованные источники;
- ограничения;
- набор `EV-*`;
- состояние передачи результата следующему этапу.

`WS-*` не является архитектурным finding или technical fact.

## 5. `EV-*`: доказательства и наблюдения

`EV-*` — логически адресуемое наблюдение, привязанное к конкретному источнику и baseline.

Примерно это может быть:

- строка или фрагмент кода;
- конфигурация;
- API schema;
- dependency metadata;
- test result;
- runtime observation;
- внешний contract source.

### Что важно

`EV-*` само по себе не означает:

- finding;
- root cause;
- severity;
- recommendation;
- accepted technical fact.

Оно является доказательным входом для дальнейшей adjudication.

## 6. Shared Technical Model

Shared Technical Model хранит принятые общие технические факты.

Основные семейства:

| Семейство | Что описывает |
|---|---|
| `COMP-*` | компоненты и их границы |
| `IF-*` | интерфейсные поверхности |
| `INT-*` | интеграции |
| `DS-*` | данные и хранилища |
| `EVENT-*` | события |
| `FLOW-*` | потоки выполнения и данных |
| `AUTH-*` | доверие, идентичность и авторизация |
| `CFG-*` | конфигурация |
| `ERR-*` | отказное поведение |

Единственная сторона, принимающая общий technical fact, — Technical Model Gate.

Capability может предложить candidate или запросить revalidation, но не должен самостоятельно переписывать общий факт.

## 7. Architecture Review и `RF-*`

`RF-*` — подтверждённый архитектурный finding.

Он должен иметь:

- устойчивую identity;
- owner scope;
- evidence / STM provenance;
- severity;
- lifecycle;
- source binding;
- revision history;
- при необходимости disposition, resolution или supersession links.

Architecture Review остаётся владельцем `RF-*`.

### Lifecycle

```text
ACTIVE
RESOLVED
SUPERSEDED
```

`REOPENED` — производный переход между baseline, а не постоянный lifecycle state.

### Что нельзя делать

Нельзя закрыть `RF-*` только потому, что:

- разработчик написал «fixed»;
- commit выглядит правильным;
- Change Review говорит `POTENTIALLY_RESOLVES`;
- finding исчез из Markdown;
- remediation action завершена.

Нужна owner-controlled revalidation и adjudication.

## 8. Test Engineering

Test Engineering хранит несколько самостоятельных семантических семейств.

### `BC-*`

Behavior Contract — существенное поведение, которое можно независимо проверить.

### `CC-*`

Contract Consistency — согласованность разных представлений контракта.

### `MAT-*`

Material Assurance Target — существенная цель подтверждения.

### `TM-*`

Test Mapping — связь цели с исполнимым доказательством.

### `GAP-*`

Пробел или недостаточность доказательства.

### `TASK-*`

Test Engineering-owned work item там, где это предусмотрено контрактом.

Эти семейства не должны автоматически получать lifecycle `RF-*` или `CQ-*` только ради общей таблицы.

## 9. Code Quality Review и `CQ-*`

`CQ-*` — подтверждённый finding качества реализации.

Code Quality Review владеет:

- identity;
- lifecycle;
- severity;
- disposition;
- freshness;
- revisions;
- resolution/supersession.

Отдельные remediation actions не равны finding lifecycle.

Например:

```text
CQRA COMPLETED != CQ RESOLVED
```

Завершение действия означает наличие implementation evidence, но linked finding ещё требует отдельной revalidation.

## 10. Findings: current и historical views

Пакет может содержать десятки или сотни исторических findings. Это нормально.

Нужно различать:

- когда-либо зарегистрированные identities;
- текущие active findings;
- исторически resolved;
- superseded;
- reopened;
- accepted residual risk;
- stale / uncertain state.

История не удаляется ради уменьшения счётчика.

Пример:

```text
REGISTERED_RF = 120
CURRENT_RF = 35
RESOLVED_RF_HISTORICALLY = 70
```

Эти показатели не обязаны образовывать простую арифметическую partition, потому что finding может быть resolved, а затем reopened.

## 11. Freshness

Lifecycle и freshness — разные вещи.

Например:

```text
lifecycle = ACTIVE
freshness = STALE
```

означает: известная finding остаётся accepted, но её применимость к текущему source требует повторной проверки.

### `freshness=BLOCKED`

Не хватает evidence или dependency для проверки current interpretation.

### `remediation_status=BLOCKED`

Заблокировано исправление.

Это разные измерения.

## 12. Projections и `PRJ-*`

Проекции нужны человеку: отчёты, карты, таблицы, summaries и другие представления.

Они производны:

```text
semantic authority
  ↓
projection
```

Они не могут менять semantic authority в обратную сторону.

Если projection устарела:

- underlying owner record не становится автоматически stale;
- новый Markdown не становится authoritative;
- regeneration выполняется отдельно;
- после regeneration требуется предусмотренная verification.

## 13. Что можно пересобрать

Обычно можно пересобрать именно производные представления, если semantic inputs приняты и пригодны.

Например:

- summary;
- report;
- Mermaid representation;
- navigation view;
- API documentation projection.

Но нельзя «пересобрать» owner finding так, чтобы изменить его lifecycle без owner adjudication.

## 14. Что нельзя редактировать вручную как обычный текст

Нежелательно вручную менять semantic records ради красивого результата.

Особенно опасно:

- ставить `RESOLVED` в finding без revalidation;
- менять severity без owner decision;
- удалять historical record;
- заменять source binding;
- менять Product baseline vector;
- превращать candidate result в accepted;
- снимать limitation из summary, если underlying evidence её всё ещё содержит.

Если нужно исправить semantic state, используйте соответствующий workflow.

## 15. Product state

Product не копирует child findings как собственную authority.

Он хранит qualified references и exact baseline vector.

Минимально важны:

- Product identity/revision;
- member Project identity;
- repository/source binding;
- accepted child authority revision;
- availability/freshness/limitations;
- derived qualified-view fingerprint там, где он используется.

Child update не продвигает Product baseline автоматически.

## 16. Coordination Root

При federated audit можно начать из обычного каталога:

```text
/projects/
├── backend/
├── frontend/
└── gateway/
```

Этот каталог — Coordination Root.

Он не становится автоматически:

- Product;
- Project;
- repository;
- semantic authority.

Filesystem location используется для discovery, а membership подтверждается отдельно.

## 17. Как читать пакет человеку

Практичный порядок:

```text
1. основной summary / report
2. конкретная finding или test record
3. связанные STM facts
4. evidence refs
5. исходный source
```

Не нужно начинать с полного чтения всех `EV-*`, если требуется понять общий результат.

## 18. Как проверить происхождение конкретного вывода

Для важного claim должна существовать цепочка вида:

```text
report statement
  ↓
owner semantic record
  ↓
STM / related authority
  ↓
WS-* / EV-*
  ↓
source binding
```

Если цепочка обрывается, это limitation или defect provenance.

## 19. Что делать после source change

Не переписывайте пакет вручную.

Используйте:

- `CHANGE_REVIEW` для candidate;
- `REVALIDATE` для нового current source;
- `RECONCILE_CHANGE` для принятия проверенного candidate;
- `EXTEND` для новой работы;
- `PROJECTION_REPAIR` для presentation-only defects.

Подробно: [Что делать после изменения кода](after-code-changes.md).

## 20. Legacy package

Старый пакет может не содержать современных полей lifecycle/freshness.

Это не означает, что его надо удалять.

Но отсутствие поля нельзя молча трактовать как:

```text
ACTIVE
```

или:

```text
RESOLVED
```

Для неоднозначных записей используется conservative qualification, например `LEGACY_STATUS_UNKNOWN`, и при необходимости owner adjudication.

## 21. Что считать сохранённой ценностью пакета

Главная ценность — не количество Markdown-файлов, а воспроизводимость знания:

- откуда взялся вывод;
- к какому source он относится;
- кто владеет его смыслом;
- когда он был принят;
- что изменилось позже;
- можно ли его переиспользовать сейчас;
- что требует повторной проверки.

## 22. Связанные документы

- [Справочник артефактов](../reference/artifacts.md)
- [Источники истины и происхождение](../concepts/authority-and-provenance.md)
- [Доказательства и Shared Technical Model](../concepts/evidence-and-technical-model.md)
- [Проекции и пакеты](../concepts/projections-and-packages.md)
- [Жизненный цикл аудита](audit-lifecycle.md)
- [Что делать после изменения кода](after-code-changes.md)
