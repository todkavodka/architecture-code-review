# Диагностика проблем

Этот документ объясняет типовые причины, по которым Skill может остановиться или отказаться продолжать автоматически.

## Skill не обнаруживается агентом

Проверьте:

```bash
ls ~/.agents/skills/architecture-code-review
git -C ~/.agents/skills/architecture-code-review rev-parse HEAD
```

Убедитесь, что существует `SKILL.md` и agent session была перезапущена после установки/обновления.

Если ваш агент использует другой skills directory, установите repository туда согласно документации конкретного host.

---

## Dirty working tree

### Симптом

Skill не хочет молча анализировать незакоммиченные изменения как обычный Git baseline.

### Почему

Evidence должна быть воспроизводимой и baseline-bound.

### Возможные решения

1. анализировать committed HEAD;
2. явно использовать EPHEMERAL working-tree snapshot;
3. остановиться и сначала привести repository в понятное состояние.

Не представляйте ephemeral snapshot как Git commit.

---

## Неоднозначный baseline

### Симптом

Несколько refs/packages подходят к запросу, либо текущий branch state не даёт однозначного source baseline.

### Действие

Выберите baseline явно. Skill должен показать ambiguity вместо случайного выбора по timestamp.

---

## Найдено несколько предыдущих audit packages

### Симптом

Startup discovery обнаружил несколько потенциально пригодных packages.

### Действие

Сравните:

- repository identity;
- lineage;
- previous/current baseline;
- authority state;
- package completeness;
- revision/freshness bindings.

Recency сама по себе не определяет правильный package.

---

## `AUTHORITY_RECONCILIATION_REQUIRED`

### Значение

Compact state (`INDEX.md`, handoff, generated view) не совпадает или не может быть подтверждён current owning artifact.

### Действие

Прочитать minimum necessary owning authority, согласовать revision/status binding, обновить/invalidate compact state и только затем продолжить downstream work.

Не выбирайте compact record только потому, что его файл новее.

---

## `REVALIDATION_REQUIRED`

### Значение

Semantic fact/record больше нельзя считать fresh для требуемого решения без targeted verification.

### Действие

Использовать `REVALIDATE` или owning capability revalidation path. Не заменять это regeneration Markdown.

---

## Projection `STALE`

### Значение

Semantic authority может оставаться accepted, но человекочитаемый document не подтверждён как current representation.

### Действие

Если fresh output действительно нужен, запросить targeted `RG-*` regeneration. Если projection не входит в required scope текущего package, она может не блокировать unrelated closeout.

---

## Projection `BLOCKED`

### Значение

Projection нельзя безопасно сделать current из-за blocked prerequisite, missing authority, contract issue или другой owning action.

### Действие

Следовать required action owning lifecycle/semantic gate. Не обходить block исключением projection из package, если она required member.

---

## `SEMANTIC_DRIFT_DETECTED`

### Значение

Во время `PROJECTION_REPAIR` выяснилось, что requested correction меняет technical meaning.

### Действие

Workflow должен вернуть:

```text
TECHNICAL_REVALIDATION_REQUIRED
```

Перенесите изменение в owning technical workflow. Не меняйте severity/owner/finding/STM через presentation edit.

---

## `FULL_REAUDIT_RECOMMENDED`

### Значение

Impact классифицирован как `SYSTEMIC`: targeted revalidation больше не даёт достаточной уверенности.

### Действие

Оцените reason/systemic scope и явно решите, запускать ли полный audit.

Skill не должен начинать full reaudit без user decision.

---

## Missing or stale evidence

### Симптом

Semantic decision требует факт, но available evidence отсутствует, привязана к старому baseline или имеет insufficient scope.

### Действие

Создать targeted fresh workset/observations. Не расширять claim шире фактически исследованной области.

---

## Unknown dependency linkage

### Симптом

Impact analysis не может доказать, затронут ли dependent record.

### Действие

Записать context expansion / targeted investigation и проверить linkage. Unknown нельзя автоматически считать unaffected.

---

## Legacy package не проходит modern gate

### Значение

Старый file/package может быть valid historical context, но ему не хватает modern ownership, registration, revision или verification metadata.

### Действие

Использовать bounded reconciliation/registration. Не объявлять legacy Markdown `CURRENT` только потому, что он существует.

Подробнее: [Compatibility and Migration](compatibility-and-migration.md).

---

## Не работает Mermaid validation

Если compatible Mermaid validator/renderer недоступен, validation должна вернуть явное состояние вроде:

```text
MERMAID_RENDER_VALIDATION_UNAVAILABLE
```

Не утверждайте, что render validation прошла, если она не выполнялась.

---

## Новый output пытаются добавить через `RESUME` или `REVALIDATE`

Это routing error.

New capability/output/Architecture endpoint addition → `EXTEND`.

`RESUME` продолжает existing work. `REVALIDATE` пересматривает affected existing semantics.

---

## FORENSIC показывает только REVIEW_ONLY

Это неверное отображение. Depth и endpoint независимы.

Valid combinations:

```text
STANDARD_FULL × 3 endpoints
FORENSIC × 3 endpoints
```

Если UI host flattening снова скрывает два FORENSIC endpoints, это display regression menu contract.

---

## Когда остановиться, а не чинить автоматически

Остановка предпочтительнее guessing, если:

- baseline неясен;
- required authority конфликтует;
- source unavailable;
- migration meaning ambiguous;
- dirty changes могут быть потеряны;
- semantic drift обнаружен в projection-only task;
- user decision требуется contractually.

Хороший stop должен объяснять причину, required action и сохранённое состояние, чтобы работу можно было продолжить позже.
