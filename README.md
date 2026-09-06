# Architecture Code Review

`architecture-code-review` — evidence-first Skill для глубокого review существующих программных систем.

Он объединяет три независимые capability:

- **Architecture Review** — фактическая архитектура, ownership, lifecycle, boundaries, root causes, reliability/security implications;
- **Test Engineering** — какие существенные поведения действительно доказаны тестами, где есть gaps и какие test artifacts нужны;
- **Code Quality Review** — реализационные механизмы с существенными последствиями для maintainability, reliability, testability, lifecycle, resources, concurrency, dependencies и localization.

Capability можно использовать отдельно или вместе в одном Review Suite.

Главный принцип:

> **Ширина утверждения не должна превышать ширину доказательств.**

---

## Что делает Skill

Вместо lint-style списка подозрений Skill строит проверяемую цепочку:

```text
source code / contracts / tests
        |
        v
Shared Evidence
        |
        v
Shared Technical Model
        |
        +--> Architecture Review
        +--> Test Engineering
        +--> Code Quality Review
        |
        v
human-readable outputs
```

Это позволяет:

- сохранять provenance;
- переиспользовать уже принятые факты;
- продолжать незавершённый review;
- перепроверять только затронутую изменениями область;
- добавлять новые outputs без полного повторного аудита;
- отделять technical authority от человекочитаемых Markdown reports.

Подробно модель описана в [Architecture Guide](docs/architecture.md).

---

# Установка

## Codex, OpenCode и другие агенты с `~/.agents/skills`

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

После установки начните новую session агента, чтобы Skill был обнаружен заново.

### Обновление

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

Проверить установленную revision:

```bash
git rev-parse HEAD
```

---

# Быстрый старт

Самый простой запрос:

```text
Используй architecture-code-review для этого проекта.
```

Skill сначала определит repository/baseline, найдёт предыдущие audit packages и предложит подходящий Session Intent.

Для нового review показывается Review Suite:

```text
Review Suite

[ ] Architecture Review
[ ] Test Engineering
[ ] Code Quality Review
```

Нужно выбрать хотя бы одну capability.

---

# Примеры использования

## Только Architecture Review

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review:
- depth: STANDARD_FULL
- result: REVIEW_ONLY

Test Engineering: OFF
Code Quality Review: OFF
```

Для более глубокого расследования замените `STANDARD_FULL` на `FORENSIC`.

## Architecture + Target Architecture + Roadmap

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review:
- depth: STANDARD_FULL
- result: REVIEW_PLUS_TARGET_AND_ROADMAP

Test Engineering: OFF
Code Quality Review: OFF
```

## Только Test Engineering

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review: OFF

Test Engineering:
- Test Assurance
- Test Plan

Code Quality Review: OFF
```

## Только Code Quality Review

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review: OFF
Test Engineering: OFF

Code Quality Review:
- Findings View/Report
- Summary
```

## Полный Review Suite

```text
Используй architecture-code-review.

Session Intent: NEW

Architecture Review:
- depth: STANDARD_FULL
- result: REVIEW_ONLY

Test Engineering:
- Test Assurance
- Test Plan
- Contract Consistency Report

Code Quality Review:
- Findings View/Report
- Summary
- Maintainability Hotspots
```

Skill подключает внутренние dependencies минимально необходимым slice и не должен автоматически включать все возможные outputs.

---

# Повторное использование audit

```text
NEW
```

Новый review package.

```text
RESUME
```

Продолжить незавершённый workflow из persisted state.

```text
REVALIDATE
```

Проверить изменения через impact analysis и переоткрыть только затронутую semantic slice.

```text
EXTEND
```

Добавить capability/output к уже принятому package без повторного запуска несвязанных этапов.

```text
USE_EXISTING
```

Использовать уже принятый и актуальный результат.

```text
PROJECTION_REPAIR
```

Исправить только presentation: Markdown, Mermaid, links, navigation, wording — без изменения accepted technical semantics.

Подробно эти flows описаны в [Workflow Guide](docs/workflows.md).

---

# Что создаётся

Во время review Skill может создавать:

```text
working/INDEX.md
working/evidence/WS-*.md
working/technical-model/...
RF-* Architecture findings
BC-* / CC-* / MAT-* / TM-* / GAP-* Test Engineering records
CQ-* / CQRA-* Code Quality records
PRJ-* derived projections
RG-* regeneration sessions
```

`working/INDEX.md` хранит coordinator state, но не заменяет technical authority.

`WS-*` / `EV-*` — evidence.

Shared Technical Model хранит принятые общие технические факты.

`RF-*`, Test Engineering records и `CQ-*` принадлежат своим capability.

`PRJ-*` — человекочитаемые projections, а не новый источник технической истины.

Полное описание структуры файлов, индексов, IDs и их использования: [Artifacts and State](docs/artifacts-and-state.md).

---

# Какие итоговые документы можно получить

В зависимости от выбранных capability и outputs Review Suite может сформировать:

- Architecture Review;
- Authoritative Findings Ledger;
- Target Architecture;
- Remediation Roadmap;
- Test Assurance;
- Test Plan;
- Contract Consistency Report;
- Test Environment Design;
- Service Simulator Design;
- Service Simulator Implementation Plan;
- E2E Test Plan;
- Code Quality Findings View;
- Code Quality Summary;
- Maintainability Hotspots;
- Code Quality Roadmap Contribution.

Что означает каждый документ и когда его выбирать: [Output Guide](docs/output-guide.md).

---

# Документация

| Документ | О чём |
|---|---|
| [Architecture](docs/architecture.md) | Review Suite, Shared Evidence, STM, authority boundaries, semantic state vs projections |
| [Artifacts and State](docs/artifacts-and-state.md) | files, `INDEX.md`, IDs, indexes, registries, persistence и provenance |
| [Workflows](docs/workflows.md) | `NEW`, `RESUME`, `REVALIDATE`, `EXTEND`, `USE_EXISTING`, `PROJECTION_REPAIR`, regeneration |
| [Output Guide](docs/output-guide.md) | какие user-facing documents создаются и зачем |
| [Roadmap](docs/roadmap.md) | дальнейшее развитие Skill |

Нормативные agent contracts находятся в `SKILL.md`, `references/` и `capabilities/*/references/`. Документы выше предназначены для человека и объясняют эту модель, не создавая параллельную authority.

---

# Язык итоговых документов

Язык user-facing документов следует языку текущего запроса, если пользователь явно не выбрал другой.

Точные IDs, status tokens, file paths, API/protocol names и code symbols не переводятся без необходимости.

---

# Лицензия

См. [`LICENSE`](LICENSE).
