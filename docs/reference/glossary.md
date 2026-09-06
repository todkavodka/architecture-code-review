# Глоссарий

Этот глоссарий задаёт human-facing терминологию документации. Canonical tokens, идентификаторы и значения enum не переводятся внутри конфигурации, файлов состояния и примеров кода.

## Общие термины

| Термин | Значение |
|---|---|
| **Baseline** | Зафиксированное состояние проекта, относительно которого собираются доказательства и принимаются выводы. Обычно это Git commit; для незакоммиченного дерева может использоваться явно обозначенный ephemeral snapshot. |
| **Capability** | Независимый функциональный модуль Review Suite: Architecture Review, Test Engineering или Code Quality Review. В русском тексте допустимо «модуль проверки (capability)» при первом упоминании. |
| **Scope** | Явно ограниченная область анализа: система, подсистема, граница, поток, capability или набор зависимостей. |
| **Evidence** | Наблюдение, привязанное к конкретному источнику и baseline. Доказательство фиксирует, что источник показал, но само по себе не является finding или техническим фактом. |
| **Workset** | Ограниченное исследование `WS-*`, объединяющее связанные observations и handoff. |
| **Observation** | Адресуемая запись `EV-*` внутри workset. |
| **Shared Technical Model (STM)** | Общая принятая модель материальных технических фактов системы. |
| **Authority** | Источник истины для конкретного вида смысла. Разные слои владеют разными типами данных. |
| **Semantic authority** | Авторитетное состояние, которое хранит технический смысл: STM facts, `RF-*`, `BC-*`, `CQ-*` и другие capability-owned records. |
| **Projection** | Человекочитаемое или операционное представление уже принятой authority. Projection не становится источником истины только потому, что это Markdown-файл. |
| **Provenance** | Цепочка происхождения вывода: semantic record → STM/evidence → source. |
| **Finding** | Принятое и доказанное замечание конкретной capability. Architecture использует `RF-*`, Code Quality — `CQ-*`. |
| **Candidate** | Предварительная гипотеза до принятия owning gate. Candidate не является authority. |
| **Coverage** | Насколько выбранная область действительно исследована и подтверждена достаточными доказательствами. |
| **Freshness** | Актуальность записи относительно текущих зависимостей и baseline. Semantic freshness и projection freshness проверяются отдельно. |
| **Dependency** | Явная зависимость одной semantic или projection записи от другой. Используется для bounded revalidation и package closure. |
| **Package** | Именованный набор итоговых проекций, который проверяется как единый deliverable scope. |
| **Revalidation** | Повторная проверка затронутой изменениями semantic области. Не равна полному повторному аудиту. |
| **Regeneration** | Пересборка проекций из уже принятой authority в отдельной `RG-*` session. |
| **Supersession** | Явная замена старой semantic identity/revision новой без переписывания истории. |
| **Owning artifact** | Артефакт, который действительно владеет соответствующей семантикой или процессным состоянием. |
| **Durable boundary** | Сохранённая граница workflow, после которой работу можно безопасно продолжить в другой session. |
| **Handoff** | Компактная передача состояния между агентами/этапами с точными ссылками на authority, baseline и незакрытые вопросы. |
| **Material consequence** | Существенное практическое последствие механизма: риск, дефект поведения, рост стоимости сопровождения, нарушение инварианта и т. п. |
| **Applicability** | Применима ли конкретная проверка или finding к выбранной области. |
| **Disposition** | Итоговое решение по finding, например accepted exception или false positive, если это предусмотрено owning contract. |

## Canonical tokens

Следующие значения сохраняются без перевода:

```text
NEW
RESUME
REVALIDATE
EXTEND
USE_EXISTING
PROJECTION_REPAIR

STANDARD_FULL
FORENSIC

REVIEW_ONLY
REVIEW_PLUS_TARGET_ARCHITECTURE
REVIEW_PLUS_TARGET_AND_ROADMAP

CURRENT
STALE
BLOCKED
VALID
REVALIDATION_REQUIRED
UNKNOWN

PERMISSIVE
REQUIRED_SCOPE_CURRENT
ALL_SCOPED_CURRENT
```

В prose рекомендуется сначала объяснить смысл по-русски, затем при необходимости указать token в обратных кавычках.

## Термины, которых следует избегать в русском тексте без необходимости

Не рекомендуется писать «ownership», «lifecycle», «gaps», «outputs», «persisted state», «semantic slice», «presentation» как обычные слова. Предпочтительные формы:

- ownership → владение / ответственность;
- lifecycle → жизненный цикл;
- gap → пробел в доказательствах;
- output → итоговый документ / выходной артефакт;
- persisted state → сохранённое состояние;
- semantic slice → затронутая семантическая область;
- presentation → представление / оформление.
