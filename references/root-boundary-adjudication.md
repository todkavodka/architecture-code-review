# Проверка границ корневых причин

Этот gate выполняется после независимой verification и до severity. Его задача — убедиться, что один authoritative root finding соответствует одному concrete correction boundary (границе исправления), а не красивой общей теме.

## 1. Normative root test

Для каждого proposed root спроси:

> Если исправить именно этот конкретный механизм, исчезнут ли все перечисленные projections (проявления)?

Если нет:

```text
SPLIT_REQUIRED
```

## 2. Valid root shape

Хороший root обычно имеет:

- один concrete runtime mechanism;
- один coherent owner/scope;
- одну plausible correction boundary;
- достижимый path/scenario;
- projections, которые действительно устраняются тем же исправлением.

Не группируй только потому, что findings относятся к одному классу, сервису, «state machine», IPC или concurrency.

## 3. Root vs projection vs SER

### Root finding (`RF-*`)

Concrete mechanism, который непосредственно создаёт material incorrect behavior/risk.

### Projection

Наблюдаемое проявление того же механизма в другом path/UI/event/файле. Projection не получает отдельный root ID, если correction boundary действительно одна.

### Supporting Engineering Risk (`SER-*`)

Структурный фактор повторения/необнаружения, например:

- semantic owner не закодирован;
- lifecycle spread across flags;
- event identity отбрасывается consumer;
- shared resource allocation ownerless;
- отсутствует deterministic local regression suite.

SER не должен автоматически наследовать severity продуктового root finding.

## 4. Split/merge decision

Перед merge двух verified candidates проверь:

```text
same mechanism?
same authoritative owner/scope?
same correction unit?
one fix removes both effects?
```

Любой существенный `no` — сильный сигнал к split.

Перед split проверь обратное: не создаёшь ли два ID для одного и того же mechanism только потому, что он виден в двух layers.

## 5. Arithmetic integrity

После adjudication посчитай:

```text
verified candidates
→ mapped projections
→ authoritative roots
→ SER/open questions
```

Каждый material verified candidate должен иметь одно основное место: root/projection/SER/open question/refuted. Не допускай двойного primary counting.

## 6. Output

Для каждого proposed root:

```text
root ID
source candidates
mechanism
owner/scope
correction boundary
projections
SER links
root test result
final action: ACCEPT_ROOT | SPLIT_REQUIRED | MERGE_WITH | DEMOTE_TO_SER | OPEN_QUESTION
```

## 7. Anti-patterns

Плохие root labels без concrete mechanism:

- «неявная FSM»;
- «плохое владение»;
- «слишком глобальное состояние»;
- «архитектура событий хрупкая».

Они могут быть полезными SER/theme, но root finding требует mechanism + reachable effect.
