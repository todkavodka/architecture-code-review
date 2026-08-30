# Контракт итоговых документов

Финальные документы пишутся на русском связном техническом языке и собираются **только из принятого авторитетного состояния**, а не напрямую из raw discovery notes.

## 1. Пакет

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md          # если заказано
├── 04-remediation-roadmap.md          # если заказано
└── working/
    ├── README.md
    ├── INDEX.md
    └── ... evidence/review artifacts ...
```

Если в репозитории уже есть established review directory, используй её, сохраняя внутренние роли файлов.

## 2. Authority map

- Технические факты As-Built во время исследования: accepted `working/00-...as-built.md`.
- `01-architecture-review.md`: authoritative user-facing report, но As-Built section является производной проекцией технической базы.
- `02-authoritative-findings-ledger.md`: единственный авторитетный источник final RF wording, evidence status, severity, projections, SER/open questions и supersessions.
- `03-target-architecture.md`: авторитетный источник target mechanisms/invariants/feasibility, когда endpoint это включает.
- `04-remediation-roadmap.md`: авторитетный источник implementation sequence/tasks/gates, когда endpoint это включает.

Если технический As-Built меняется, все производные final sections, которые на него опираются, считаются stale до повторной synthesis/review.

## 3. `01-architecture-review.md`

Основной читаемый документ.

Рекомендуемая структура:

```markdown
# Архитектурное и кодовое ревью

## 1. Резюме
## 2. Объём, baseline и ограничения
## 3. Методика
## 4. Фактическая архитектура
### 4.1 Назначение и ключевые сценарии
### 4.2 Процессы и runtime-компоненты
### 4.3 Ответственность и владение
### 4.4 Основные data/control flows
### 4.5 IPC/API/native/process boundaries
### 4.6 Жизненный цикл
### 4.7 Конкурентность и фоновые операции
### 4.8 Хранение и конфигурация
### 4.9 Trust boundaries и security model
### 4.10 Platform-specific behavior
### 4.11 Положительные механизмы
## 5. Архитектурные свойства и ключевые выводы
## 6. Наиболее существенные подтверждённые замечания
## 7. Положительные механизмы, которые следует сохранить
## 8. Приоритеты и зависимости исправления
## 9. Выполненные проверки
## 10. Открытые вопросы и product-intent decisions
## 11. Ограничения исследования
## 12. Итоговый статус
```

Фактическая архитектура — substantial first-class chapter. Для medium project ориентир по информационной плотности примерно соответствует 5–10 страницам, но gate — semantic completeness, а не количество строк.

Основной отчёт обычно раскрывает 10–20 наиболее важных RF в читаемом виде и ссылается на полный ledger вместо копирования всех деталей.

## 4. `02-authoritative-findings-ledger.md`

Для каждого root:

```text
stable RF ID
final title
severity
confidence
exploitability where applicable
root mechanism
reachable scenario
code evidence
projections
SER links
open/product-intent status
superseded candidate/wording references
links to main report
target link when applicable
roadmap task links when applicable
```

Отдельно сохраняй registries `SER-*`, `PC-*`, `OQ-*` и explicit supersessions.

## 5. Cross-link contract

Используй относительные ссылки внутри audit package.

Навигационная цепочка:

```text
main report
→ authoritative RF
→ working evidence / verification
→ target mechanism
→ remediation task
```

Где полезно, добавляй обратные ссылки.

Stable headings начинай с ID:

```markdown
## RF-012 — ...
```

Не полагайся только на длинные translated headings как anchors.

Финальная проверка должна выявлять:

- orphan RF/SER/TASK;
- broken/missing relative links;
- target mechanism без motivating RF/SER/invariant;
- roadmap task без target/RF link;
- working claim, который superseded, но не ведёт к текущей authority.

## 6. Технический черновик vs финальная сборка

После authoritative findings ledger можно создать `MAIN REVIEW TECHNICAL DRAFT` для `01-architecture-review.md`.

Если endpoint включает target/roadmap, этот draft **не является финальным пакетом**.

`FINAL PACKAGE ASSEMBLY` выполняется после того, как все заказанные endpoint artifacts приняты:

```text
accepted audit
+ accepted target (если заказан)
+ accepted roadmap (если заказан)
→ inject final navigation/cross-links/status
→ editorial review
```

Для `REVIEW_ONLY` technical draft и final assembly могут естественно совпасть.

## 7. Chunked writing

Большой Markdown-документ не записывай одним giant write, если есть риск truncation/лимита.

Нормальный pattern:

```text
CREATE SKELETON
→ WRITE LOGICAL CHUNK A
→ VERIFY headings/content
→ WRITE CHUNK B
→ VERIFY previous content preserved
→ WRITE CHUNK C
→ VERIFY IDs/links
→ FINAL READ
```

Chunk определяется логическим разделом, не случайным количеством символов.

При write failure/truncation:

```text
inspect existing file
→ identify last complete logical boundary
→ resume from there
→ do not blindly overwrite whole large artifact
→ final read
```

Один final artifact имеет одного active writer за раз.

## 8. Writing style and terminology

Narrative — русский. На первом существенном употреблении допустимо `English term (русский аналог)`, дальше предпочитай русский термин, если точность не теряется.

Не переводи exact identifiers, class/function/type names, filenames, API/IPC/protocol names, runtime states, verdict/status tokens, commands/code.

Пиши абзацами «механизм → evidence → consequence». Таблицы и Mermaid дополняют анализ, а не заменяют его.

Избегай необъяснённых labels вроде `god object`, `spaghetti`, `bad practice`, а также риторических усилителей, не подтверждённых severity.

## 9. Executive summary

В начале за 1–2 страницы должно быть понятно:

- overall architectural health;
- top 3–7 risks;
- security/data-integrity blockers;
- lifecycle/resource ownership quality;
- incremental remediation viability;
- есть ли причины блокировать feature development;
- какой endpoint выполнен и какие документы являются authority.

## 10. Verification table

```markdown
| Команда/проверка | Результат | Ограничение/комментарий |
|---|---|---|
```

Не скрывай недоступные проверки.

## 11. Final status

`REVIEW_COMPLETE` допускается только после completion gates `SKILL.md`, включая independent verification/adjudication, cross-link check и editorial correction/re-review.

Иначе `REVIEW_PARTIALLY_COMPLETE` с точным перечислением missing evidence/gates.
