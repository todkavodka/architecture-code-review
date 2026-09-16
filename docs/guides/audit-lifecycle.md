# Жизненный цикл аудита

Этот документ объясняет, как `architecture-code-review` живёт вместе с проектом во времени: от первого запуска до повторной проверки после изменений кода, обновления Product baseline и пересборки человекочитаемых результатов.

Это пользовательское руководство. Нормативные правила остаются в `SKILL.md`, `references/` и capability-specific контрактах.

## 1. Главная идея

Аудит — не одноразовый отчёт и не снимок чата. Skill сохраняет доказательства, принятые технические факты, findings, тестовые результаты, состояние координации и производные документы так, чтобы работу можно было продолжать после изменений проекта.

Упрощённый цикл:

```text
проект
  ↓
обнаружение существующего audit state
  ↓
выбор работы
  ↓
сбор доказательств
  ↓
Shared Technical Model
  ↓
Architecture / Test Engineering / Code Quality
  ↓
принятые семантические записи
  ↓
проекции и итоговые документы
  ↓
изменение проекта
  ↓
CHANGE_REVIEW или REVALIDATE
  ↓
адресная повторная проверка
  ↓
новое принятое состояние
```

Ключевое правило: **изменение исходного кода не означает, что весь аудит надо запускать заново**. Сначала определяется, что именно изменилось и какие принятые записи от этого зависят.

## 2. Что сохраняется между сеансами

Skill опирается не на память агента, а на сохранённые артефакты.

В пакете аудита обычно присутствуют:

- `working/INDEX.md` — состояние координации;
- `WS-*` и `EV-*` — рабочие области исследования и доказательства;
- Shared Technical Model — принятые технические факты;
- `RF-*` — архитектурные findings;
- `BC-*`, `CC-*`, `MAT-*`, `TM-*`, `GAP-*`, `TASK-*` — Test Engineering;
- `CQ-*` и связанные действия — Code Quality;
- `PRJ-*` — производные человекочитаемые представления;
- Product context и Product baseline, если аудит охватывает несколько Projects.

Эти классы состояния имеют разных владельцев. Нельзя считать `INDEX.md`, отчёт или Product summary заменой соответствующего семантического источника истины.

Подробно: [Структура пакета аудита](audit-package-structure.md).

## 3. Первый запуск

При первом запуске нет гарантии, что нужен `NEW`. Skill сначала должен проверить, существует ли уже пригодное состояние.

Минимальный запрос:

```text
Используй architecture-code-review для этого проекта.
```

Далее skill определяет:

1. выбранный repository / Project / Product context;
2. точный source baseline;
3. наличие предыдущего пакета;
4. его завершённость и применимость;
5. requested work пользователя;
6. подходящий `Session Intent`.

Если пригодного состояния нет, выбирается `NEW`.

## 4. NEW: создание нового пакета

`NEW` означает новую содержательную работу по выбранному baseline.

Пользователь выбирает не «всё сразу», а нужную работу:

- Architecture Review;
- Test Engineering;
- Code Quality Review;
- допустимые standalone outputs / Technical Documentation;
- сочетание нескольких направлений.

Пустой Requested Work недопустим.

После подтверждения начинается исследование.

## 5. Исследование и доказательства

Исследование начинается с ограниченных рабочих областей и доказательств.

```text
source
  ↓
WS-*
  ↓
EV-*
  ↓
кандидаты технических фактов
  ↓
Technical Model Gate
  ↓
Shared Technical Model
```

`EV-*` — наблюдение, а не conclusion. Оно не становится finding только потому, что выглядит подозрительно.

Shared Technical Model содержит принятые технические факты, например:

- `COMP-*` — компоненты;
- `IF-*` — интерфейсные поверхности;
- `INT-*` — интеграции;
- `DS-*` — данные и хранилища;
- `EVENT-*` — события;
- `FLOW-*` — потоки;
- `AUTH-*` — доверие и авторизация;
- `CFG-*` — конфигурация;
- `ERR-*` — отказное поведение.

Это общий технический фундамент для capability-specific анализа.

## 6. Capability-specific authority

После принятия технических фактов разные направления отвечают за разные виды выводов.

### Architecture Review

Владеет архитектурными findings `RF-*`, их lifecycle, severity, disposition, resolution, reopening и supersession.

### Test Engineering

Владеет собственными семантическими семействами: поведением, согласованностью контрактов, целями тестирования, доказательствами и gaps.

### Code Quality Review

Владеет `CQ-*` и собственным lifecycle findings и remediation actions.

Один capability не переписывает authority другого. Если Code Quality видит архитектурную проблему, он может создать наблюдение или запрос на adjudication, но не должен сам принимать `RF-*`.

## 7. Findings: история и текущий риск

Исторический реестр и текущий риск — разные представления.

Для `RF-*` и `CQ-*` lifecycle включает:

```text
ACTIVE
RESOLVED
SUPERSEDED
```

`REOPENED` — производный переход между двумя принятыми baseline, а не отдельное постоянное состояние.

Пример:

```text
Baseline A:
RF-017 ACTIVE HIGH

Baseline B:
RF-017 RESOLVED

Baseline C:
RF-017 ACTIVE HIGH
```

История сохраняет все принятые revisions. На сравнении B → C будет показано `REOPENED`, но finding ID остаётся тем же, если корневая проблема действительно та же.

### Принятый риск

Принятый риск — disposition, а не resolution.

Finding может быть:

```text
lifecycle = ACTIVE
disposition = ACCEPTED_RISK
```

Он остаётся техническим риском, но исключается из actionable subset при наличии действительного owner decision.

## 8. Проекции и человекочитаемые документы

Итоговые Markdown-документы — производные представления.

```text
semantic authority
    ↓
projection impact
    ↓
PRJ-*
    ↓
human-readable report
```

Проекция может стать устаревшей, даже если underlying semantic state остаётся принятым. И наоборот, новый красиво сформированный Markdown не делает семантическое состояние актуальным.

Поэтому существуют отдельные понятия:

- semantic lifecycle;
- semantic freshness;
- process state;
- projection freshness.

## 9. Завершение первичного аудита

Когда выбранная работа выполнена:

- доказательства сохранены;
- необходимые technical facts приняты;
- capability-specific authority принята;
- ограничения и неполнота явно зафиксированы;
- итоговые документы построены или помечены как не выбранные;
- состояние пакета позволяет определить, что можно переиспользовать позже.

После этого аудит становится базой для будущих изменений.

## 10. Что происходит, когда код меняется

После изменения кода сначала определяется статус изменения.

### Изменение ещё не принято

Branch, commit или pull request оцениваются через `CHANGE_REVIEW`.

`CHANGE_REVIEW` отвечает на вопрос:

> Что изменится, если candidate будет принят?

Он не меняет accepted authority.

### Изменение уже принято как новый source

Используется `REVALIDATE`.

Он отвечает на вопрос:

> Какие принятые знания больше нельзя считать проверенными для нового source и что нужно перепроверить?

Подробный маршрут: [Что делать после изменения кода](after-code-changes.md).

## 11. CHANGE_REVIEW

`CHANGE_REVIEW` сравнивает immutable `BASE` и `CANDIDATE`.

Результаты review-local:

- структурный delta;
- candidate findings/effects;
- impact on accepted authority;
- прогноз влияния на projections.

Он может сказать, что candidate `POTENTIALLY_RESOLVES` существующий finding, но сам finding остаётся в accepted state до owner adjudication.

### После CHANGE_REVIEW

Если candidate принят пользователем и review пригоден для повторного использования, может быть подтверждён контекстный `RECONCILE_CHANGE`.

Это не новый startup intent. Он лишь маршрутизирует candidate evidence к существующим владельцам:

```text
candidate evidence
  ↓
owner revalidation
  ↓
owner adjudication
  ↓
accepted semantic revision
```

Только после этого возможно продвижение accepted baseline.

## 12. REVALIDATE

`REVALIDATE` выполняется для source state, который уже считается текущим.

Он не должен механически переанализировать весь репозиторий.

Сначала определяется impact:

```text
изменившийся source
  ↓
затронутые evidence / STM facts / findings / test records / CQ records
  ↓
минимальный revalidation slice
  ↓
повторная проверка
```

Не затронутые записи переиспользуются.

## 13. Freshness после изменений

Изменение source не означает автоматическое изменение lifecycle.

Пример:

```text
RF-010 ACTIVE на source B
source изменился до C
```

До revalidation finding может оставаться `ACTIVE`, но его применимость к C требует подтверждения. Риск не исчезает только потому, что доказательство устарело.

Особенно важен случай resolved finding:

```text
RF-020 RESOLVED на B
source изменился до C
```

Исторический факт «resolved на B» остаётся. Но отсутствие проблемы на C ещё не доказано. Нельзя автоматически считать finding ни current-resolved на C, ни reopened-active. Сначала требуется owner revalidation.

## 14. Повторное использование после merge

Совпадение branch name или ancestry недостаточно для доказательства эквивалентности candidate и merged result.

Возможные варианты:

- fast-forward или эквивалентное дерево — review часто можно переиспользовать напрямую;
- no-ff merge — возможен reuse при доказанном tree equivalence;
- squash merge — возможен reuse при доказанном равенстве релевантного дерева;
- conflict resolution — обычно требует дополнительной проверки;
- partial cherry-pick — нельзя считать эквивалентным без доказательства выбранного slice.

Подробности: [Change Review](change-review.md).

## 15. EXTEND

`EXTEND` используется, когда source согласован, но пользователь хочет добавить новую работу:

- новый capability;
- Target Architecture;
- Remediation Roadmap;
- дополнительную Technical Documentation;
- более глубокий operation inventory;
- другой допустимый output.

`EXTEND` не должен пересобирать всё существующее без необходимости.

## 16. USE_EXISTING

`USE_EXISTING` подходит, когда уже принятый результат пригоден для текущего запроса.

Это режим чтения и переиспользования, а не новый технический анализ.

Если source изменился и old package больше не подтверждает current state, старый результат можно читать как исторический, но нельзя представлять его как актуальный.

## 17. PROJECTION_REPAIR

`PROJECTION_REPAIR` используется для проблем представления:

- Markdown;
- Mermaid;
- таблицы;
- навигация;
- формулировки;
- сломанные ссылки;
- другие presentation-only defects.

Если исправление требует изменить технический смысл, это уже не projection repair.

## 18. Product lifecycle

Для Product, состоящего из нескольких Projects, жизненный цикл двухуровневый.

```text
child Project audits
    ↓
qualified accepted child authority
    ↓
Product baseline
    ↓
Product-level cross-project analysis
```

Product baseline — точный immutable vector выбранных member/source/authority bindings.

### Top-down

Product coordinator обнаруживает stale/changed child и предлагает запустить соответствующий child workflow.

После завершения child audit Product повторно квалифицирует весь необходимый vector и только затем может принять новый Product baseline.

### Bottom-up

Child audit может независимо обновиться раньше Product.

Product позже обнаруживает semantic-authority advancement и решает, как его принять. Child update не продвигает Product baseline автоматически.

## 19. Текущий риск и прогресс Product

Product агрегирует qualified child views, а не raw local IDs.

Если два Projects имеют `RF-001`, это две разные findings, пока qualification различается.

Product может показывать:

- current technical risk;
- actionable findings;
- accepted residual risk;
- stale-resolution uncertainty;
- baseline-to-baseline progress;
- unavailable-member limitations.

Недоступный Project не превращается в «0 findings».

## 20. Когда начинать новый аудит

Новый полный `NEW` нужен не после каждого изменения, а когда действительно создаётся новый независимый audit scope либо прежнее состояние нельзя корректно продолжить или квалифицировать.

Обычно сначала стоит проверить возможность:

- `RESUME`;
- `USE_EXISTING`;
- `CHANGE_REVIEW`;
- `REVALIDATE`;
- `EXTEND`.

## 21. Практическая модель на каждый день

Для команды полезно мыслить так:

```text
до изменения:
  accepted audit state

во время разработки:
  CHANGE_REVIEW candidate

после принятия изменения:
  RECONCILE_CHANGE или REVALIDATE

после semantic acceptance:
  projection impact

если нужны свежие документы:
  explicit regeneration
```

Такой процесс сохраняет историю, избегает полного повторного аудита и не смешивает candidate evidence с accepted truth.

## 22. Связанные документы

- [Что делать после изменения кода](after-code-changes.md)
- [Практические рецепты](common-recipes.md)
- [Структура пакета аудита](audit-package-structure.md)
- [Повторное использование и изменения](reuse-and-change.md)
- [Change Review](change-review.md)
- [Жизненный цикл и актуальность](../concepts/lifecycle-and-freshness.md)
- [Справочник процессов](../reference/workflows.md)
