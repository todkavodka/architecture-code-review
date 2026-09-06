# Установка

## Поддерживаемая модель установки

`architecture-code-review` — файловый Skill. Агент обнаруживает его в каталоге Skills и использует `SKILL.md` как точку входа.

Рекомендуемый путь для Codex, OpenCode и других совместимых агентов:

```text
~/.agents/skills/architecture-code-review
```

## Требования

Перед установкой нужны:

- Git;
- агент, поддерживающий файловые Skills;
- доступ агента к анализируемому репозиторию;
- возможность читать и записывать Markdown-файлы внутри проекта, если выбран процесс с сохраняемым пакетом аудита.

Сам Skill не требует отдельной базы данных или фонового сервиса.

## Установка последней версии `main`

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

После установки начните новый сеанс агента, чтобы он заново обнаружил каталог Skills.

## Проверка установки

```bash
cd ~/.agents/skills/architecture-code-review
git status --short
git branch --show-current
git rev-parse HEAD
```

Ожидается:

- каталог существует;
- текущая ветка обычно `main`;
- `git status --short` пуст, если вы не вносили локальных изменений;
- `git rev-parse HEAD` возвращает установленную ревизию.

После этого попросите агента использовать `architecture-code-review`. Если Skill не обнаруживается, см. [Диагностика проблем](../operations/troubleshooting.md).

## Установка фиксированной ревизии

Для воспроизводимой среды лучше закрепить конкретный commit:

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review

cd ~/.agents/skills/architecture-code-review
git checkout <commit-sha>
```

Такой checkout находится в состоянии detached HEAD. Это допустимо для закреплённой установки, но обновлять её нужно осознанно.

## Обновление

Для обычной установки на `main`:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git fetch origin --prune
git pull --ff-only
```

`--ff-only` защищает от случайного merge локальных изменений с upstream history.

После обновления начните новый сеанс агента.

## Локальные изменения

Не рекомендуется изменять установленный Skill напрямую. Локальные patch-изменения усложняют:

- воспроизводимость;
- сравнение пакетов аудита между командами;
- обновление;
- диагностику расхождений между документацией и нормативными контрактами.

Если локальная адаптация необходима, храните её в отдельной ветке или fork и фиксируйте точную ревизию в инженерной документации команды.

## Удаление

Если в каталоге нет нужных локальных изменений:

```bash
rm -rf ~/.agents/skills/architecture-code-review
```

Удаление Skill не удаляет пакеты аудита, уже созданные внутри анализируемых репозиториев.

## Следующий шаг

- [Быстрый старт](quick-start.md)
- [Первый полный запуск](first-review.md)
- [Обновление и откат](../operations/upgrade-and-rollback.md)
