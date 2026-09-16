# Пример: проверка качества реализации

Этот пример показывает, как `Code Quality Review` отличает реальную инженерную проблему от обычного предупреждения анализатора.

Пути, идентификаторы и названия компонентов условны, но логика соответствует модели skill.

## Исходная ситуация

В приложении есть три точки входа:

- desktop client;
- web client;
- preview настроек.

В каждой отдельно реализован выбор резервного языка интерфейса. Команда замечает дублирование и хочет понять, является ли оно реальной проблемой качества или просто повторением кода.

Запрос:

```text
Используй architecture-code-review.
Нужен только Code Quality Review для locale resolution.
Подготовь Findings View, Summary и Maintainability Hotspots.
Architecture Review и Test Engineering не включай.
```

## Шаг 1. Начальная конфигурация

Skill фиксирует baseline `a1b2c3d` и запускает `NEW`.

```text
Architecture Review: OFF
Test Engineering: OFF
Code Quality Review: ON

Selected outputs:
  Code Quality Findings View
  Code Quality Summary
  Maintainability Hotspots
```

## Шаг 2. Наблюдения

В рабочей области сохраняются доказательства:

```text
WS-002-locale-resolution

EV-011
source: src/desktop/locale.ts
observed:
  неизвестный locale заменяется на en-US

EV-012
source: src/web/locale.ts
observed:
  неизвестный locale заменяется на locale операционной системы

EV-013
source: src/settings/preview-locale.ts
observed:
  preview использует третью таблицу fallback

EV-014
source: tests/locale-entrypoints.spec.ts
observed:
  один профиль пользователя с zz-ZZ получает разные языки
  в трёх точках входа
```

На этом этапе есть подтверждённое наблюдение: реализации различаются.

Но `CQ-*` ещё нет.

## Шаг 3. Фактический контекст

Для правильной интерпретации используется принятый срез Shared Technical Model:

```text
COMP-DESKTOP-CLIENT
COMP-WEB-CLIENT
COMP-SETTINGS-PREVIEW
IF-USER-PREFERENCES
CFG-LOCALE-FALLBACK
```

Это позволяет установить, что три реализации обрабатывают один и тот же пользовательский смысл — locale preference одного профиля.

## Шаг 4. От сигнала к finding

Статический анализатор сообщает о похожих функциях.

Само это предупреждение недостаточно.

Цепочка принятия finding выглядит так:

```text
анализатор заметил дублирование
    ↓
EV-011..EV-014 подтвердили разные реализации
    ↓
STM подтвердил общую семантическую границу
    ↓
установлено существенное последствие:
один пользователь получает разное поведение
    ↓
принимается CQ-014
```

## Шаг 5. Принятый Code Quality finding

```text
CQ-014
lifecycle: ACTIVE
applicability: APPLICABLE
severity: MEDIUM
confidence: HIGH

mechanism:
  три независимые реализации locale fallback

material consequence:
  один и тот же профиль пользователя может получить разный язык
  в зависимости от точки входа

provenance:
  WS-002-locale-resolution#EV-011..EV-014
  CFG-LOCALE-FALLBACK
```

Теперь finding основан не на эстетике кода, а на доказанном поведении.

## Почему большой файл не обязательно finding

В том же репозитории есть `src/session/coordinator.ts` на 2400 строк.

Анализатор считает его сложным.

Но если в выбранной области не доказано существенное последствие, skill не обязан создавать `CQ-*` только из-за размера.

Корректный результат:

```text
observation / candidate
```

а не автоматически:

```text
CQ-* HIGH
```

## Шаг 6. Remediation action

Для `CQ-014` создаётся отдельное действие:

```text
CQRA-006
relates_to: CQ-014
status: PLANNED

action:
  создать единый механизм locale fallback
  и использовать его во всех трёх точках входа
```

Это запись о работе по исправлению, а не изменение lifecycle finding.

## После реализации

Инженер выполняет refactoring и переводит `CQRA-006` в:

```text
COMPLETED
```

Но:

```text
CQRA-006 COMPLETED != CQ-014 RESOLVED
```

Нужно получить новые доказательства для всех трёх точек входа.

Например:

```text
EV-021
все три entrypoint используют shared locale resolver

EV-022
один профиль с zz-ZZ даёт одинаковый результат во всех трёх entrypoint
```

После `REVALIDATE` владелец Code Quality Review может принять:

```text
CQ-014 ACTIVE → RESOLVED
```

История `CQ-014` сохраняется.

## Что будет в прогрессе

Если это единственный finding:

```text
Current CQ:
1 → 0

Resolved:
1

Historical registered CQ:
1
```

Историческая запись остаётся, но текущий технический риск уменьшается.

## Accepted exception

Допустим, команда не исправляет различие сейчас, а формально принимает его как допустимое исключение.

Тогда возможна запись вида:

```text
CQ-014
lifecycle: ACTIVE
disposition: ACCEPTED_EXCEPTION
```

Это всё ещё текущая реальная проблема.

Она может быть исключена из actionable remediation, но не из технического Current Findings.

Нельзя показывать её как `RESOLVED`.

## WONT_FIX

Другой вариант:

```text
CQ-014
lifecycle: ACTIVE
disposition: WONT_FIX
```

Это означает, что исправление не планируется.

Сам по себе `WONT_FIX` не означает, что риск формально принят как accepted risk, и тем более не означает `RESOLVED`.

## Пример с API input limits

Рассмотрим другой candidate.

В OpenAPI:

```text
name:
  type: string
  maxLength: 255
```

В серверном коде:

```text
request body читается полностью
    ↓
JSON парсится
    ↓
после этого применяется schema validation
```

Skill не должен делать слишком сильный вывод.

Подтверждено:

```text
field limit: 255
```

Но не доказано:

```text
ранний request body limit
```

Корректная интерпретация:

```text
field constraint: EVIDENCED
transport/body boundary: UNRESOLVED
resource-exhaustion protection: NOT ESTABLISHED
```

Если дальнейшее исследование подтверждает отсутствие лимита и существенный риск материализации больших payload, тогда может быть принят отдельный `CQ-*`.

## Maintainability Hotspot

После анализа нескольких областей может оказаться, что `src/settings/` содержит несколько связанных findings:

```text
CQ-014 locale fallback divergence
CQ-019 duplicated validation policy
CQ-023 global mutable configuration
```

Тогда область может быть показана как maintainability hotspot.

Причина — совокупность принятых проблем, а не количество строк в каталоге.

## Как выглядит итоговый пакет

```text
baseline: a1b2c3d

STM:
  COMP-DESKTOP-CLIENT
  COMP-WEB-CLIENT
  COMP-SETTINGS-PREVIEW
  IF-USER-PREFERENCES
  CFG-LOCALE-FALLBACK

Code Quality authority:
  CQ-014 ACTIVE
  CQRA-006 PLANNED

outputs:
  Code Quality Findings View
  Code Quality Summary
  Maintainability Hotspots
```

Проверяемая цепочка:

```text
Code Quality Findings View
    ↓
CQ-014
    ↓
CFG-LOCALE-FALLBACK
    ↓
WS-002#EV-011..EV-014
    ↓
исходный код @ a1b2c3d
```

## После следующего изменения

Если код ещё в pull request:

```text
CHANGE_REVIEW
```

может показать:

```text
CQ-014 → POTENTIALLY_RESOLVES
```

Но accepted finding остаётся `ACTIVE`.

После принятия кода используется `REVALIDATE`, и только owner revalidation может изменить lifecycle.

## Что читать дальше

- [Code Quality Review](../guides/code-quality-review.md)
- [Что делать после изменения кода](../guides/after-code-changes.md)
- [Структура пакета аудита](../guides/audit-package-structure.md)
- [Жизненный цикл и актуальность](../concepts/lifecycle-and-freshness.md)
