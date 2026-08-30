# Финальное редакционное ревью

Этот gate запускается только после технического принятия всех requested endpoint artifacts и финальной сборки пакета.

Editorial Review (редакционное ревью) **не редактирует документы напрямую**. Оно создаёт issue list. Исправление выполняет отдельный correction pass, затем новый fresh-context re-review.

## 1. Цель

Проверить, что финальные документы:

- написаны связным русским техническим языком;
- объясняют material mechanisms человеку, а не копируют terse working-artifact style;
- используют терминологию последовательно;
- содержат полезные диаграммы там, где topology/lifecycle/ownership/target behavior трудно понять только текстом;
- не содержат stale/superseded technical claims;
- согласованы между собой и с authoritative ledger;
- имеют целостный cross-link graph;
- не искажают severity/evidence/target/roadmap semantics при редактуре.

## 2. Language contract

Narrative — русский.

При первом существенном употреблении допустимо:

```text
English term (русский аналог)
```

Дальше предпочитай русский аналог, если точность не теряется.

Не переводи exact:

- class/function/type identifiers;
- filenames/paths;
- API/IPC/protocol names;
- runtime states;
- verdict/status tokens;
- commands/code.

Флагай случайные английские paragraphs/headings/table explanations.

Также флагай mixed-language shorthand, если обычную мысль можно естественно выразить по-русски без потери точности. Примеры нежелательной final prose:

```text
error-boundary протекает credential-ами
prod-risks untestable
shutdown негрейсфул
designated owner отсутствует
runtime-drift
```

Не требуй искусственного перевода exact identifiers или established technical terms. Цель — профессиональный читаемый русский, а не языковой пуризм.

## 3. Prose quality contract

Working notes, HANDOFF SUMMARY, ledger rows и verification matrices могут быть плотными. Final user-facing narrative должен быть объясняющим.

Для каждого material conclusion проверь, что текст отвечает на четыре вопроса:

1. что происходит сейчас;
2. почему это происходит;
3. к чему это приводит;
4. что нужно изменить или сохранить.

Предпочтительная структура абзаца:

```text
mechanism → evidence → consequence → correction direction
```

Флагай как `STYLE-*`, если:

- final prose выглядит как agent scratchpad/handoff;
- предложения заменены fragments/labels;
- стрелки `->`, `!=`, slash-compounds и скобочные IDs несут основную смысловую нагрузку;
- RF/SER/TASK IDs заменяют объяснение;
- implementation nouns появляются раньше объяснения самой проблемы;
- executive summary является ledger dump вместо synthesis.

## 4. Diagram coverage contract

Сверь final package с `lifecycle-and-mermaid.md` и `report-contract.md`.

Если в системе есть material topology, lifecycle, ownership, trust boundary, ordering или target transition, проверь наличие useful visual explanation.

Для substantial report особенно ожидаются, когда применимы:

- As-Built component/boundary diagram;
- runtime/lifecycle/sequence diagram;
- Target Architecture diagram;
- Before → After diagram для material correction;
- roadmap dependency diagram для нетривиального sequencing/safe activation.

Отсутствие диаграммы допустимо, если visual representation реально не добавляет архитектурной информации. В substantial package такое решение должно быть явно объяснимо.

Флагай как `DIAG-*`, если:

- material architecture трудно понять без visual aid, но его нет;
- диаграмма декоративна и не объясняет real mechanism;
- current/target behavior смешаны;
- Mermaid противоречит prose или accepted evidence;
- diagram uses generic fake components instead of real subsystem names.

## 5. Issue types

Рекомендуемые IDs:

```text
LANG-###   language drift / grammar / hybrid shorthand
TERM-###   inconsistent terminology
STYLE-###  machine-like / duplicate / telegraphic prose
DIAG-###   missing/useless/misleading diagram coverage
LINK-###   broken/missing cross-link
CONS-###   prose/table/diagram/document contradiction
STALE-###  superseded claim resurfaced
SEV-###    wording rhetorically exceeds adjudicated severity
```

## 6. Checks

Проверь:

- connected prose `mechanism → evidence → consequence → correction direction`;
- accidental English drift;
- mixed-language shorthand/transliteration;
- inconsistent translations/terms;
- grammar/readability;
- executive summary explains system-level causes before RF lists;
- roadmap tasks first explain problem/root cause/result, then implementation contract;
- useful diagram coverage where material complexity warrants it;
- duplicate paragraphs/findings;
- stale superseded statements;
- root titles/status/severity одинаковы во всех final artifacts;
- diagrams/state tables не противоречат prose;
- Mermaid structurally valid enough for available renderer;
- important relative links resolve conceptually;
- no orphan RF/SER/TASK/target references;
- target mechanisms link to motivating RF/SER/invariant;
- roadmap tasks link to target/RF;
- working superseded claims point forward to current authority where required;
- no unsupported intensifiers `catastrophic`, `RCE`, `data loss`, `critical` вне adjudicated context.

## 7. Semantic safety

Editorial reviewer **не имеет права молча менять**:

- evidence;
- root identity;
- severity;
- confidence/exploitability;
- product-intent status;
- target invariants/ownership;
- feasibility classification;
- roadmap dependencies/gates;
- security assumptions.

Если language/diagram cleanup обнаруживает реальное technical contradiction, issue получает `CONS-*` и возвращается в соответствующий technical gate.

## 8. Output

Review artifact содержит:

```text
reviewed final artifact refs
baseline / authoritative ledger ref
issue ID
location
category
observed problem
required correction boundary
technical-gate escalation? yes/no
```

Не переписывай полный документ в review artifact.

## 9. Correction loop

```text
FINAL PACKAGE ASSEMBLED
→ fresh-context editorial review
→ issue list
→ separate editorial correction writer
→ verify links/semantics
→ fresh-context editorial re-review
→ FINAL_PACKAGE_ACCEPTED | CORRECTION_REQUIRED | TECHNICAL_GATE_REQUIRED
```

Correction writer меняет только то, что разрешено issue list; новый technical content не добавляет без возврата в technical gate.

## 10. Final acceptance

Пакет нельзя объявлять финальным, пока:

- все editorial issues closed или explicitly blocked;
- re-review выполнен;
- cross-links проверены;
- no stale authoritative projection remains;
- language/prose quality contract соблюдён;
- diagram coverage contract соблюдён либо отсутствие диаграмм обосновано;
- requested target/roadmap artifacts уже accepted технически.
