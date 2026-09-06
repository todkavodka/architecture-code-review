# Обновление и откат

Этот документ описывает безопасное обновление установленного Skill и восстановление предыдущей версии без потери audit packages в анализируемых repositories.

## Проверить текущую revision

```bash
cd ~/.agents/skills/architecture-code-review
git status --short
git branch --show-current
git rev-parse HEAD
```

Перед обновлением зафиксируйте текущий SHA, если потребуется rollback.

## Обычное обновление `main`

Если checkout чистый:

```bash
git fetch origin --prune
git switch main
git pull --ff-only
```

После обновления начните новую agent session.

## Почему `--ff-only`

Skill installation должна быть воспроизводимой. Автоматический merge local modifications с upstream может создать неизвестный contract state.

Если fast-forward невозможен, сначала разберитесь, почему history расходится.

## Pinned installation

Для стабильной командной среды рекомендуется фиксировать known-good commit:

```bash
git checkout <known-good-sha>
```

В документации команды храните exact SHA Skill рядом с audit baseline/release process, если результат должен быть строго воспроизводим.

## Rollback

Если новая версия Skill обнаружила regression или несовместимость с вашим workflow:

```bash
cd ~/.agents/skills/architecture-code-review
git fetch origin --prune
git checkout <previous-known-good-sha>
```

Начните новую agent session.

Rollback installation не переписывает существующие audit packages автоматически.

## Возврат с pinned SHA на `main`

```bash
git switch main
git pull --ff-only
```

## Локальные изменения

Если `git status --short` показывает tracked changes, не выполняйте update/reset вслепую.

Сначала определите происхождение изменений.

Рекомендуемые варианты:

1. сохранить patch в отдельной branch/fork;
2. удалить intentional local customization после его переноса в fork;
3. оставить pinned local branch и обновляться через controlled merge/review.

Не используйте `git reset --hard` или `git clean` как универсальный способ «починить установку», если не подтверждено, что локальные файлы не нужны.

## Audit packages и версия Skill

Audit package живёт в анализируемом repository и может пережить обновление Skill.

Новая версия не должна молча переписывать legacy state. При `RESUME`, `REVALIDATE` или `EXTEND` применяется conservative reconciliation/backfill согласно compatibility contracts.

Подробнее: [Совместимость и миграция](compatibility-and-migration.md).

## Проверка после update

1. `git rev-parse HEAD` — expected revision.
2. новая agent session обнаруживает Skill.
3. для существующего package сначала используйте normal startup discovery; не запускайте `NEW` только из-за upgrade самого Skill.
4. если package требует reconciliation, Skill должен явно сообщить об этом.

## Когда rollback недостаточен

Rollback Skill не отменяет изменения, уже внесённые в audit package новой версией.

Если новая версия успела выполнить migration/reconciliation, нужно оценить package state отдельно по revision history и owning artifacts. Не делайте вид, что checkout старого Skill автоматически вернул package к старой семантике.
