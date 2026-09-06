# Проекции и пакеты результатов

Человекочитаемые документы в Review Suite отделены от semantic authority. Это позволяет пересобирать presentation без потери provenance и повторного изобретения технического смысла.

## Projection

Projection — производное представление accepted authority.

Она имеет stable `PRJ-*` identity и собственный lifecycle record.

Пример:

```text
CQ-* authority
  -> PRJ-CQ-00 Findings View
  -> PRJ-CQ-01 Summary
  -> PRJ-CQ-02 Hotspots
```

Projection может быть Markdown report, summary, navigation view или другой controlled deliverable.

## Что хранит projection record

Conceptually:

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
- какой accepted revision он отображает;
- изменилось ли его содержимое;
- нужно ли его revalidate/regenerate;
- является ли новый файл новой revision той же projection.

## Почему filename недостаточно

Файл `summary.md` сам по себе не доказывает:

- что это тот же логический document;
- что dependencies не изменились;
- что content прошёл verification;
- что файл current.

Stable identity и lifecycle делают document addressable независимо от path.

## Projection Impact Analysis

После stabilized semantic delta выполняется отдельный accounting pass:

```text
accepted semantic delta
  -> Projection Impact Analysis
  -> direct impact
  -> reverse dependency propagation
  -> CURRENT / STALE / BLOCKED updates
  -> PROJECTION_IMPACT_ACCOUNTED
```

`PROJECTION_IMPACT_ACCOUNTED` означает, что влияние учтено. Это не означает, что все projections regenerated или `CURRENT`.

## Regeneration

Если пользователь требует fresh deliverable, запускается отдельная `RG-*` session.

```text
requested PRJ
  -> resolve stale prerequisites
  -> frozen RG plan
  -> generate
  -> V1..V4 verification
  -> fingerprint/revision decision
```

Если generated content идентичен current verified revision, новая revision не создаётся только ради факта запуска regeneration.

## Package

Projection package — именованный deliverable scope. Он не является semantic model и не превращает его members в authority.

Package declaration содержит finite membership rules:

```text
package_id
owner
gate
freshness_policy
required_members
optional_members
conditional_members
```

Membership не вычисляется arbitrary filename globs или prose queries.

Перед closeout создаётся resolved membership snapshot конкретной package instance.

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
