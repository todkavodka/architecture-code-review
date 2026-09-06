# Проекции и пакеты результатов

Это каноническое объяснение для пользователя проекций, пакетов результатов и
правил их актуальности.

Человекочитаемые документы `Review Suite` отделены от семантического источника
истины. Это позволяет пересобирать представление без потери происхождения
вывода и повторного изобретения технического смысла.

## Проекция

Проекция — производное представление принятого источника истины.

У неё есть устойчивый идентификатор `PRJ-*` и собственная запись жизненного цикла.

Пример:

```text
источник истины `CQ-*`
  -> PRJ-CQ-00 Findings View
  -> PRJ-CQ-01 Summary
  -> PRJ-CQ-02 Hotspots
```

Проекцией может быть Markdown-отчёт, краткое резюме, навигационное представление или другой управляемый итоговый документ.

## Что хранит запись проекции

Схематично:

```text
projection_id
owner
artifact_path
contract_revision
semantic_dependencies
projection_dependencies
verified_revision
fingerprint
freshness
```

Эти данные нужны, чтобы ответить:

- от чего зависит документ;
- какую принятую ревизию он отображает;
- изменилось ли его содержимое;
- нужна ли ему повторная проверка или пересборка;
- является ли новый файл новой ревизией той же проекции.

## Почему имени файла недостаточно

Файл `summary.md` сам по себе не доказывает:

- что это тот же логический документ;
- что зависимости не изменились;
- что содержимое прошло проверку;
- что файл актуален.

Устойчивый идентификатор и жизненный цикл позволяют адресовать документ независимо от пути.

## Projection Impact Analysis

После стабилизации семантических изменений выполняется отдельный учёт их влияния:

```text
принятое семантическое изменение
  -> Projection Impact Analysis
  -> прямое влияние
  -> распространение по обратным зависимостям
  -> обновление `CURRENT` / `STALE` / `BLOCKED`
  -> PROJECTION_IMPACT_ACCOUNTED
```

`PROJECTION_IMPACT_ACCOUNTED` означает, что влияние учтено. Это не означает, что все проекции пересобраны или имеют состояние `CURRENT`.

## Regeneration

Если пользователю нужен актуальный итоговый документ, запускается отдельный сеанс `RG-*`.

```text
requested PRJ
  -> resolve stale prerequisites
  -> frozen RG plan
  -> generate
  -> V1..V4 verification
  -> fingerprint/revision decision
```

Если созданное содержимое идентично текущей проверенной ревизии, новая ревизия не создаётся только ради факта запуска пересборки.

## Package

Пакет проекций — именованный набор итоговых документов. Он не является семантической моделью и не превращает своих участников в источник истины.

Описание пакета содержит конечные правила состава:

```text
package_id
owner
gate
freshness_policy
required_members
optional_members
conditional_members
```

Состав пакета не вычисляется по произвольным шаблонам имён файлов или поисковым запросам в тексте.

Перед завершением создаётся снимок состава конкретного экземпляра пакета.

## Freshness policies

### `PERMISSIVE`

Stale/blocked projections могут оставаться видимыми, если текущий gate их не потребляет. Semantic closeout не требует repository-wide zero-stale state.

### `REQUIRED_SCOPE_CURRENT`

Requested projection и обязательные upstream prerequisites должны быть `CURRENT`.

### `ALL_SCOPED_CURRENT`

Все resolved required members выбранного package должны быть `CURRENT`.

## Closeout chain

Projection-sensitive closeout следует последовательности:

```text
semantic gates accepted
  -> PROJECTION_IMPACT_ACCOUNTED
  -> package membership resolved
  -> required scoped projections CURRENT
  -> closeout/publication permitted
```

Если required projection `BLOCKED`, package gate блокируется с указанием owning action. Accepted semantic work при этом не откатывается.

## Unrelated stale projections

Допустим, пользователь делает Code Quality extension, а старый Architecture summary stale.

Если Architecture projection не входит в required scope текущего package, она остаётся видимой, но не обязана блокировать Code Quality closeout.

Это позволяет работать bounded scope без искусственного требования «сначала обновить вообще все документы repository».

## `PROJECTION_REPAIR`

Presentation-only correction использует существующие registered projections выбранного accepted package.

Пользователь выбирает не semantic object, а конкретную projection/document/section.

Разрешены:

- язык;
- Markdown structure;
- Mermaid syntax/layout без изменения mechanism;
- links/navigation;
- tables;
- terminology;
- representation уже accepted meaning.

Semantic change возвращает workflow в technical revalidation.

## Как читать package

Для обычного потребителя:

```text
package main report
  -> supporting projection
  -> semantic record when needed
```

Для проверки provenance:

```text
PRJ-* document
  -> owning semantic records
  -> STM/evidence
  -> source
```

## Что читать дальше

- [Output Reference](../reference/outputs.md)
- [Workflow Reference](../reference/workflows.md)
- [Artifacts Reference](../reference/artifacts.md)
