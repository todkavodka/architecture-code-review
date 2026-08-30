# Финальное редакционное ревью

Этот gate запускается только после технического принятия всех requested endpoint artifacts и финальной сборки пакета.

Editorial Review (редакционное ревью) **не редактирует документы напрямую**. Оно создаёт issue list. Исправление выполняет отдельный correction pass, затем новый fresh-context re-review.

## 1. Цель

Проверить, что финальные документы:

- написаны связным русским техническим языком;
- используют терминологию последовательно;
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

## 3. Issue types

Рекомендуемые IDs:

```text
LANG-###   language drift / grammar
TERM-###   inconsistent terminology
STYLE-###  machine-like / duplicate / telegraphic prose
LINK-###   broken/missing cross-link
CONS-###   prose/table/diagram/document contradiction
STALE-###  superseded claim resurfaced
SEV-###    wording rhetorically exceeds adjudicated severity
```

## 4. Checks

Проверь:

- connected prose «mechanism → evidence → consequence»;
- accidental English drift;
- inconsistent translations/terms;
- grammar/readability;
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

## 5. Semantic safety

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

Если language cleanup обнаруживает реальное technical contradiction, issue получает `CONS-*` и возвращается в соответствующий technical gate.

## 6. Output

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

## 7. Correction loop

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

## 8. Final acceptance

Пакет нельзя объявлять финальным, пока:

- все editorial issues closed или explicitly blocked;
- re-review выполнен;
- cross-links проверены;
- no stale authoritative projection remains;
- language contract соблюдён;
- requested target/roadmap artifacts уже accepted технически.
