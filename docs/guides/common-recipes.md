# Практические рецепты

Этот документ собирает типовые рабочие ситуации и готовые формулировки запросов к `architecture-code-review`.

Это не формальный CLI. Фразы ниже — удобные пользовательские prompts. Skill должен нормализовать запрос в существующие `Session Intent`, capabilities, outputs и owner workflows.

## 1. Первый архитектурный аудит

Когда нужен полный первичный обзор фактической архитектуры:

```text
Используй architecture-code-review.
Нужен новый Architecture Review.
Depth: STANDARD_FULL.
Endpoint: REVIEW_ONLY.
Test Engineering и Code Quality Review пока не включай.
```

Если нужны целевая архитектура и план изменений:

```text
Используй architecture-code-review.
Нужен Architecture Review: STANDARD_FULL.
Endpoint: REVIEW_PLUS_TARGET_AND_ROADMAP.
```

## 2. Глубокий forensic-аудит

Для спорной архитектуры, сложной конкурентности, security-sensitive paths или запутанного lifecycle:

```text
Используй architecture-code-review.
Нужен новый Architecture Review.
Depth: FORENSIC.
Endpoint: REVIEW_ONLY.
Особое внимание: lifecycle, concurrency, trust boundaries и failure recovery.
```

`FORENSIC` не означает автоматическое перечисление каждого endpoint. Полнота интерфейсного inventory имеет отдельные условия.

## 3. Проверить только Test Engineering

```text
Используй architecture-code-review.
Нужен Test Engineering: Test Assurance + Test Plan.
Architecture Review и Code Quality Review не выбирай как пользовательскую работу.
Переиспользуй существующий Shared Technical Model, если он пригоден.
```

Если нужен Contract Consistency Report:

```text
Добавь Contract Consistency Report и проверь declared, implemented, consumed и tested representations.
```

## 4. Проверить только Code Quality

```text
Используй architecture-code-review.
Нужен Code Quality Review: Findings View + Summary.
Architecture Review и Test Engineering не включай как requested work.
```

При анализе API можно добавить:

```text
Отдельно проверь transport/body limits, строки, коллекции, uploads, pagination и порядок parsing/validation.
```

## 5. Проверить pull request перед merge

```text
Используй architecture-code-review.
Сделай CHANGE_REVIEW accepted baseline против pull request #123.
Покажи candidate findings и impact на accepted Architecture, Test Engineering, Code Quality и projections.
Ничего не reconcile автоматически.
```

Это read-only review. Existing accepted findings не закрываются автоматически.

## 6. Проверить feature branch

```text
Используй architecture-code-review.
Сделай CHANGE_REVIEW принятого baseline против branch feature/auth-hardening.
Покажи structural delta и material authority impact.
```

## 7. Обновить аудит после merge

Если код уже находится в принятом `main` и считается текущим source:

```text
Используй существующий пакет architecture-code-review.
Код уже принят как новый current source.
Выполни REVALIDATE только затронутого accepted state.
Не запускай полный NEW.
После semantic revalidation покажи projection impact.
```

## 8. Переиспользовать готовый Change Review после merge

Только если доказана эквивалентность merged result и reviewed candidate:

```text
Используй завершённый CHANGE_REVIEW как evidence input.
Merged result эквивалентен reviewed candidate.
Запусти контекстный RECONCILE_CHANGE и направь затронутые записи существующим owners.
```

Если была conflict resolution или эквивалентность не доказана, сначала нужна дополнительная проверка.

## 9. Продолжить незавершённый аудит

Если baseline не изменился:

```text
Используй существующий пакет.
Продолжи незавершённую работу через RESUME.
Не создавай новый audit package.
```

Если baseline изменился, `RESUME` использовать нельзя как обход revalidation.

## 10. Получить уже готовый результат

```text
Используй существующий принятый пакет.
Нужен USE_EXISTING для текущего Architecture Review.
Не запускай новую техническую работу.
```

Если результат исторический и source уже изменился, его нельзя выдавать за current state.

## 11. Добавить Target Architecture позже

Предположим, Architecture Review уже принят с `REVIEW_ONLY`.

```text
Используй существующий Architecture Review.
Через EXTEND добавь Target Architecture.
Не пересобирай без необходимости существующий обзор.
```

Для дальнейшего расширения:

```text
Через EXTEND добавь Remediation Roadmap к уже принятой Target Architecture.
```

## 12. Добавить техническую документацию позже

```text
Используй существующий пакет.
Через EXTEND добавь Provided Interfaces и Failure Behavior для текущего baseline.
Переиспользуй пригодные STM facts и evidence.
```

Standalone output не превращается в новый capability.

## 13. Получить API Report

```text
Используй существующий audit context.
Нужен API Report по provided/consumed interfaces и integrations для выбранного Project и baseline.
Не объявляй полный API без доказанного operation inventory completeness.
```

## 14. Проверить граничные значения API

```text
Используй architecture-code-review.
Проверь API на oversized body, строки и коллекции, uploads, multipart, pagination, malformed payload и неверный Content-Type.
Если точная граница неизвестна, не придумывай число — зафиксируй gap.
```

## 15. Найти, какие findings действительно остались текущими

```text
Используй accepted finding authorities текущего package.
Покажи CURRENT STATE отдельно от HISTORICAL.
Отдельно покажи actionable findings, accepted residual risk, stale active и stale-resolution uncertainty.
Не используй cumulative historical count как current risk.
```

## 16. Проверить, исправлен ли конкретный finding

```text
Проверь RF-017 на текущем accepted source через owner revalidation.
Не закрывай finding по commit message или candidate diff.
Если evidence подтверждает устранение того же механизма, создай owner-controlled RESOLVED revision.
```

## 17. Проверить reopened finding

```text
Проверь RF-017, который ранее был RESOLVED, но снова проявился.
Если root identity та же, сохрани finding ID, создай новую ACTIVE revision и покажи REOPENED как baseline transition.
```

## 18. Разобраться со stale resolved finding

```text
RF-020 был RESOLVED на предыдущем source, после чего source изменился.
Покажи историческую resolution отдельно.
Не считай absence на новом source доказанной до owner revalidation.
```

## 19. Исправить только Markdown или Mermaid

```text
Используй PROJECTION_REPAIR.
Исправь Markdown/Mermaid/навигацию без изменения semantic authority.
Если для исправления требуется изменить технический смысл, остановись и вернись к semantic workflow.
```

## 20. Пересобрать устаревшую проекцию

```text
Проверь semantic authority и projection impact.
Если authority уже принято, а PRJ-* устарела, выполни explicit regeneration и verification.
Не меняй finding authority во время regeneration.
```

## 21. Обновить один child repository в Product

```text
Product состоит из нескольких Projects.
Изменился только backend.
Обнови или revalidate backend локально.
Переиспользуй пригодные accepted states остальных members.
После child acceptance выполни Product revalidation.
Не продвигай Product baseline автоматически.
```

## 22. Подключить уже готовый child audit к Product

```text
Найди существующий accepted child audit для backend.
Квалифицируй exact Project/repository/source/owner bindings.
Если он пригоден, переиспользуй его в Product вместо повторного локального аудита.
```

## 23. Child audit обновился независимо

```text
Backend audit был обновлён отдельно и имеет новую accepted semantic revision.
Определи semantic authority advancement относительно текущего Product baseline.
Product baseline не меняй автоматически.
```

## 24. Coordination Root не является Git repository

```text
Запусти Product coordination из /projects.
Обнаружь дочерние repositories ограниченно и детерминированно.
Не считай filesystem parent Product membership.
Попроси подтверждение membership перед Product work.
```

## 25. Проверить Project с грязным рабочим деревом

```text
Проверь текущее dirty working tree как явно выбранный noncanonical source.
Зафиксируй committed base и actual dirty bindings.
Не выдавай этот результат за canonical Git baseline.
```

## 26. Добавить Code Quality к существующему Architecture Review

```text
Используй существующий пакет и текущий согласованный baseline.
Через EXTEND добавь Code Quality Review: Findings View + Summary.
Architecture findings не переписывай.
```

## 27. Добавить Test Engineering к существующему пакету

```text
Используй существующий пакет.
Через EXTEND добавь Test Engineering: Test Assurance + Test Plan.
Переиспользуй пригодный Shared Technical Model и Architecture context без передачи ownership.
```

## 28. Проверить только один ограниченный участок

```text
Выполни адресную проверку только для auth/session lifecycle.
Не расширяй scope без доказанной зависимости.
```

Если задача действительно является revalidation, лучше явно назвать соответствующий `Session Intent`.

## 29. Обновить сам skill

Это не `REVALIDATE` анализируемого проекта.

```bash
cd ~/.agents/skills/architecture-code-review
git fetch origin --prune
git switch main
git pull --ff-only
```

После обновления начните новый сеанс агента.

Подробно: [Обновление самого skill и откат](../operations/upgrade-and-rollback.md).

## 30. Быстро понять, что делать после изменения кода

Если сомневаетесь:

```text
ещё candidate?            CHANGE_REVIEW
уже current source?       REVALIDATE
есть review и принимаем?  RECONCILE_CHANGE
тот же незавершённый run? RESUME
нужен новый output?       EXTEND
нужен готовый result?     USE_EXISTING
только presentation?      PROJECTION_REPAIR
```

Полное объяснение: [Что делать после изменения кода](after-code-changes.md).

## Связанные документы

- [Жизненный цикл аудита](audit-lifecycle.md)
- [Что делать после изменения кода](after-code-changes.md)
- [Структура пакета аудита](audit-package-structure.md)
- [Справочник процессов](../reference/workflows.md)
- [Быстрый старт](../getting-started/quick-start.md)
