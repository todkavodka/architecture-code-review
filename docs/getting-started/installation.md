# Установка

## Поддерживаемая модель установки

`architecture-code-review` — файловый Skill. Агент обнаруживает его по каталогу skills и читает `SKILL.md` как entrypoint.

Рекомендуемый путь для Codex, OpenCode и других совместимых агентов:

```text
~/.agents/skills/architecture-code-review
```

## Требования

Перед установкой нужны:

- Git;
- агент, поддерживающий файловые Skills;
- доступ агента к анализируемому repository;
- возможность читать и записывать Markdown-файлы внутри проекта, если выбран workflow с persisted audit package.

Сам Skill не требует отдельной базы данных или фонового сервиса.

## Установка последней версии `main`

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

После установки начните новую agent session, чтобы discovery перечитал каталог skills.

## Проверка установки

```bash
cd ~/.agents/skills/architecture-code-review
git status --short
git branch --show-current
git rev-parse HEAD
```

Ожидается:

- checkout существует;
- branch обычно `main`;
- `git status --short` пуст, если вы не вносили локальных изменений;
- `git rev-parse HEAD` возвращает установленную revision.

Далее попросите агента использовать `architecture-code-review`. Если Skill не обнаруживается, см. [Диагностика проблем](../operations/troubleshooting.md).

## Установка фиксированной revision

Для воспроизводимой среды лучше закрепить конкретный commit:

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review

cd ~/.agents/skills/architecture-code-review
git checkout <commit-sha>
```

Такой checkout находится в detached HEAD. Это нормально для pinned installation, но обновлять его нужно осознанно.

## Обновление

Для обычной установки на `main`:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git fetch origin --prune
git pull --ff-only
```

`--ff-only` защищает от случайного merge локальных изменений с upstream.

После обновления начните новую agent session.

## Локальные изменения

Не рекомендуется изменять установленный Skill напрямую. Локальный patch усложняет:

- воспроизводимость;
- сравнение audit packages между командами;
- обновление;
- диагностику drift между документацией и contracts.

Если локальная адаптация необходима, храните её в отдельной branch/fork и фиксируйте точную revision в инженерной документации команды.

## Удаление

Если в каталоге нет нужных локальных изменений:

```bash
rm -rf ~/.agents/skills/architecture-code-review
```

Удаление Skill не удаляет audit packages, уже созданные внутри анализируемых repositories.

## Следующий шаг

- [Быстрый старт](quick-start.md)
- [Первый полный запуск](first-review.md)
- [Обновление и откат](../operations/upgrade-and-rollback.md)
