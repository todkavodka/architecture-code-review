# Доказательства, жизненный цикл кандидата и критичность

Этот файл является авторитетным источником для evidence contract (контракта доказательств), promotion lifecycle (жизненного цикла кандидата), security attack chain (цепочки эксплуатации), Safe Reproduction / Evidence Validation и severity adjudication (оценки критичности).

## 1. Evidence contract

Material finding должен разделять:

1. **Observation (наблюдение)** — что код демонстративно делает.
2. **Interpretation (интерпретация)** — почему механизм архитектурно значим.
3. **Risk/impact (риск/последствие)** — конкретный failure/security/consistency effect.
4. **Recommendation direction (направление исправления)** — без преждевременного To-Be design.

Для cross-layer claims приводи evidence с каждого существенного boundary. Одна строка с именем класса не доказывает архитектурную проблему.

Формат evidence:

```text
src/module/file.py:120-168
src/other/file.ts:41-77
```

## 2. Candidate lifecycle

Discovery не создаёт authoritative finding напрямую.

Нормальная цепочка:

```text
CANDIDATE
→ independent verification
→ CONFIRMED | CORRECTED | REFUTED | UNVERIFIED
→ root-boundary adjudication
→ authoritative RF / projection / SER / open question
→ severity adjudication
→ authoritative ledger
```

`REFUTED` и superseded formulations должны сохраняться в working evidence trail, чтобы не воскреснуть позже.

Discovery Coverage Review не заменяет эту цепочку: он проверяет полноту исследования mechanism classes, а не correctness уже найденного candidate.

## 3. Evidence strength

Используй confidence отдельно от severity:

- `HIGH` — mechanism и reachable flow доказаны кодом; желательно подтверждены проверкой/runtime evidence.
- `MEDIUM` — сильное static evidence, но ключевой runtime condition не воспроизведён.
- `LOW` — plausible, но evidence неполный; обычно open question/UNVERIFIED, не headline finding.

Не поднимай severity только из-за высокой уверенности: уверенность отвечает «правда ли», severity — «насколько плохо».

Для clarity допускаются evidence descriptions:

```text
STATICALLY_CONFIRMED
RUNTIME_REPRODUCED
RUNTIME_VALIDATION_UNAVAILABLE
```

Это **не новые lifecycle statuses и не severity levels**. Они только описывают тип фактического evidence.

`RUNTIME_REPRODUCED` можно указывать только когда runtime check реально выполнялся и его результат зафиксирован. Если проверка не выполнялась, не используй wording, создающее впечатление фактического воспроизведения.

## 4. Safe Reproduction / Evidence Validation

Runtime reproduction может повысить confidence и подтвердить reachability/semantics, но архитектурный audit Skill не является penetration-testing или exploitation framework.

Safe Reproduction — **опциональный** способ усилить evidence. Он не является prerequisite для каждого finding.

### Разрешённая цель

Проверить минимальный harmless effect, достаточный чтобы различить:

```text
mechanism реально существует
vs
static interpretation была ошибочной
```

Предпочитай в таком порядке:

1. существующий non-destructive test;
2. existing local fixture/harness;
3. isolated test environment;
4. synthetic input / local semantic reproduction.

### Authorization boundary

Выполняй runtime reproduction только на системе/environment/repository, которую пользователь авторизован проверять.

Не используй audit как повод probing unrelated external targets или third-party infrastructure.

### Hard safety boundary

Safe Reproduction не включает:

- destructive actions;
- persistence;
- privilege escalation;
- credential theft;
- lateral movement;
- data exfiltration;
- modification/corruption of real production data;
- unrelated external target probing;
- reusable offensive payload packs.

Demonstrate the **minimum effect necessary**. Не расширяй reproduction только потому, что уже доказан первый exploit primitive.

### Injection-like mechanisms

Для injection-like candidate предпочитай доказать:

```text
construction semantics
или
harmless local/test predicate manipulation
```

Не извлекай реальные данные и не цепляй privileges только ради демонстрации severity.

### Когда reproduction недоступна

Если безопасный runtime check невозможен, не forcing PoC.

Вместо этого:

```text
preserve static evidence
→ state runtime limitation
→ keep confidence proportional to actual evidence
```

`RUNTIME_VALIDATION_UNAVAILABLE` не означает, что static finding автоматически false или low severity; он описывает limitation evidence channel.

### Связь с candidate lifecycle и severity

Успешная safe reproduction может:

- повысить confidence;
- подтвердить reachable condition;
- falsify неверную static interpretation.

Она **не**:

- обходит independent verification;
- обходит root-boundary adjudication;
- назначает severity сама по себе;
- автоматически поднимает severity;
- превращает conditional capability в direct exploit без evidence.

## 5. Security attack-chain gate

Серьёзный security finding (`HIGH`/`CRITICAL`) требует доказанной цепочки, где применимо:

```text
attacker capability
→ entry point
→ trust boundary crossed
→ failed/missing control
→ privileged effect
→ concrete impact
```

Отдельно классифицируй exploitability:

```text
DIRECT
CONDITIONAL
DEFENSE_IN_DEPTH
```

Отсутствие hardening control само по себе не является HIGH/CRITICAL vulnerability. Conditional post-compromise capability не наследует автоматически severity гипотетического prerequisite compromise.

Runtime reproduction не обязана доходить до полного offensive attack chain; chain может быть доказан combination static/runtime evidence, пока каждый material link обоснован.

## 6. Severity adjudication

Severity назначается **после** verification и root-boundary gate.

Оцени:

- impact;
- reachability;
- blast radius (масштаб воздействия);
- recoverability (восстановимость);
- frequency/exposure;
- prerequisites;
- attacker model для security;
- product-intent dependency.

Для material finding явно проверь:

```text
Почему не на один уровень выше?
Почему не на один уровень ниже?
```

### CRITICAL

Только для evidence-backed catastrophic/systemic outcomes, например practical RCE/elevated code execution, broad auth bypass, вероятная существенная потеря/коррупция данных, unrecoverable secret exposure или systemic outage без разумного containment. Не используй как риторический усилитель.

### HIGH

Serious realistic production impact: wrong-owner mutation, process-wide crash from reachable path, major auth/permission flaw, severe lifecycle/concurrency/data-consistency failure, security exploit с сильной цепочкой, но не уровня CRITICAL.

### MEDIUM

Material bounded reliability/security/maintainability/testability issue: lifecycle/resource leak, conditional security weakness, substantial fragility, local wrong behavior с ограниченным blast radius.

### LOW

Локальная проблема с небольшим practical impact.

### INFORMATIONAL

Defense-in-depth/architectural note без доказанного material incorrect behavior, но полезный для hardening/clarity.

### PENDING_PRODUCT_INTENT

Используй, когда correctness/severity зависит от неустановленного product intent. Не угадывай policy.

## 7. Supporting Engineering Risks

`SER-*` — recurrence/non-detection risk, не обязательный runtime defect. Примеры: owner identity не закодирован, lifecycle spread across flags, отсутствие deterministic local regression tests.

SER может иметь приоритет remediation, но не должен автоматически получать severity ближайшего RF.

## 8. Finding shape

```markdown
## RF-012 — Короткий русский заголовок

**Критичность:** HIGH
**Уверенность:** HIGH
**Exploitability:** DIRECT | CONDITIONAL | DEFENSE_IN_DEPTH | N/A

**Корневой механизм.** ...

**Доказательства:**
- `path/file.ext:10-40`
- `path/other.ext:80-120`

**Evidence validation:** STATICALLY_CONFIRMED | RUNTIME_REPRODUCED | RUNTIME_VALIDATION_UNAVAILABLE

**Достижимый сценарий.** ...

**Практическое последствие.** ...

**Почему не выше / не ниже.** ...

**Проявления:** ...

**Связанные SER / open questions:** ...
```

`Evidence validation` описывает фактический evidence mode и не обязано присутствовать, если существующее report contract уже выражает это яснее. Не создавай параллельную lifecycle state machine.

Recommendation direction может быть краткой, но detailed Target Architecture создаётся только если выбран соответствующий endpoint.

## 9. Anti-noise rules

Не продвигай в material finding без concrete impact:

- file length;
- `unwrap`/`clone`/mocks;
- TODO/comment;
- framework choice;
- lint warning count;
- hardcoded literal;
- отсутствие теста;
- broad API surface без reachable misuse path;
- raw-looking API name без provenance/effect;
- mere inability to produce a PoC.

Absence evidence ≠ defect evidence.

Runtime reproduction unavailable ≠ finding false.

Runtime reproduction successful ≠ severity automatically higher.

## 10. Stable identity

До adjudication используй `CAND-*`. После root-boundary — stable `RF-*` для roots, `SER-*` для supporting engineering risks, `OQ-*` для open questions. Не создавай разные root IDs для одного механизма только потому, что он виден в разных файлах/layers.
