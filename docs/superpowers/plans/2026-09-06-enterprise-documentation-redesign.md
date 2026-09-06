# Enterprise Documentation Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Перестроить пользовательскую документацию `architecture-code-review` в документационный комплект enterprise-класса с нормальным русским языком, последовательным раскрытием тем, справочными контрактами, эксплуатационными инструкциями и реалистичными сценариями.

**Architecture:** README становится короткой входной страницей. `docs/index.md` становится навигационным центром. Подробности разделяются на Getting Started, Concepts, Guides, Reference, Operations и Examples; нормативные agent-контракты в `SKILL.md`, `references/` и `capabilities/*/references/` остаются единственным источником исполняемой семантики.

**Tech Stack:** Markdown, GitHub-rendered diagrams/tables, existing Skill contracts.

**Spec:** `/mnt/data/architecture-code-review-documentation-review.md` + утверждённая в чате структура документации.

## Global Constraints

- Русский пользовательский текст пишется по-русски; английскими остаются canonical tokens, IDs, пути, протоколы, API и имена кода.
- Не менять семантику Skill и нормативные agent-контракты.
- Не создавать параллельный источник authority в `docs/`.
- Использовать progressive disclosure: README → docs hub → concepts/guides → reference/operations/examples.
- Сохранять совместимость старых ссылок на `docs/architecture.md`, `docs/artifacts-and-state.md`, `docs/workflows.md`, `docs/output-guide.md` через короткие навигационные страницы.

---

### Task 1: Documentation foundation

**Files:**
- Create: `docs/index.md`
- Create: `docs/reference/glossary.md`
- Create: `docs/reference/identifiers-and-statuses.md`

- [ ] Зафиксировать терминологическую политику и карту документации.
- [ ] Описать canonical identifiers/status tokens без перевода их значений в исполняемых контрактах.
- [ ] Проверить, что README может ссылаться на единый documentation hub.

### Task 2: Getting Started

**Files:**
- Create: `docs/getting-started/installation.md`
- Create: `docs/getting-started/quick-start.md`
- Create: `docs/getting-started/first-review.md`

- [ ] Описать установку, проверку установки, обновление и базовую диагностику discovery.
- [ ] Дать минимальный первый запуск без знания внутренних IDs.
- [ ] Показать полный путь первого review от запроса до пакета результатов.

### Task 3: Concepts

**Files:**
- Create: `docs/concepts/review-suite.md`
- Create: `docs/concepts/evidence-and-technical-model.md`
- Create: `docs/concepts/authority-and-provenance.md`
- Create: `docs/concepts/lifecycle-and-freshness.md`
- Create: `docs/concepts/projections-and-packages.md`

- [ ] Объяснить модель Review Suite и независимые capabilities.
- [ ] Раскрыть Shared Evidence и STM с правилами identity/revision/provenance.
- [ ] Объяснить ownership/authority и конфликтные ситуации.
- [ ] Объяснить semantic freshness, projection freshness, revalidation и supersession.
- [ ] Объяснить PRJ/RG, package membership и closeout policies.

### Task 4: Capability and lifecycle guides

**Files:**
- Create: `docs/guides/architecture-review.md`
- Create: `docs/guides/test-engineering.md`
- Create: `docs/guides/code-quality-review.md`
- Create: `docs/guides/reuse-and-change.md`

- [ ] Дать пользовательские guides для каждой capability.
- [ ] Описать NEW/RESUME/REVALIDATE/EXTEND/USE_EXISTING/PROJECTION_REPAIR как жизненный цикл использования продукта.
- [ ] Явно разделить пользовательские выборы и автоматические зависимости.

### Task 5: Human-facing reference

**Files:**
- Create: `docs/reference/artifacts.md`
- Create: `docs/reference/workflows.md`
- Create: `docs/reference/outputs.md`

- [ ] Для артефактов описать роль, владельца, writer/consumer, создание, обновление, freshness, provenance и пример.
- [ ] Для workflows использовать единую форму Purpose / Entry / Choices / Automatic / Reads / Writes / Gates / Stops / Postconditions.
- [ ] Для outputs описать audience, prerequisites, source authority, sections, freshness, dependencies и consumption.

### Task 6: Operations

**Files:**
- Create: `docs/operations/upgrade-and-rollback.md`
- Create: `docs/operations/compatibility-and-migration.md`
- Create: `docs/operations/troubleshooting.md`

- [ ] Описать upgrade, pinned revision, rollback, local-modification policy.
- [ ] Описать legacy package compatibility и migration/backfill boundaries.
- [ ] Описать типовые блокировки и действия пользователя.

### Task 7: End-to-end examples

**Files:**
- Create: `docs/examples/architecture-review.md`
- Create: `docs/examples/test-engineering.md`
- Create: `docs/examples/code-quality-review.md`
- Create: `docs/examples/revalidation.md`

- [ ] Показать реалистичный входной запрос, рекомендации, создаваемое состояние, итоговый пакет и последующее использование.
- [ ] Не представлять примеры как дополнительную semantic authority.

### Task 8: README and compatibility pages

**Files:**
- Modify: `README.md`
- Modify: `docs/architecture.md`
- Modify: `docs/artifacts-and-state.md`
- Modify: `docs/workflows.md`
- Modify: `docs/output-guide.md`

- [ ] Сжать README до landing-page формата: продукт, аудитория, задачи, capabilities, быстрый старт, установка, сценарии, карта документации, важные ограничения.
- [ ] Убрать подробные внутренние схемы из README.
- [ ] Превратить старые guide paths в короткие compatibility/navigation pages, ведущие в новую структуру.

### Task 9: Editorial consistency verification

- [ ] Проверить отсутствие суржика вне canonical terms.
- [ ] Проверить ссылки между README, docs hub, concepts, guides, reference, operations и examples.
- [ ] Проверить отсутствие семантического расхождения с `references/` и capability contracts.
- [ ] Проверить, что определения не дублируются без необходимости.
- [ ] Проверить, что старые ссылки продолжают вести пользователя к актуальной документации.
