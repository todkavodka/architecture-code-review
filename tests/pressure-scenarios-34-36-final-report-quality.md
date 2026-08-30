# Pressure Scenarios 34–36 — Final report quality

These regression scenarios cover a class of failures observed during a real architecture review of an unrelated repository. The technical analysis was useful and found substantive architecture and security issues, but the final user-facing documents degraded into terse internal-agent shorthand.

## RED evidence

Observed final prose contained patterns such as:

```text
error-boundary протекает credential-ами
critical dependencies have no designated owner / managed lifecycle
test-app structurally != prod-app -> prod-risks untestable
shutdown негрейсфул
cache-first pattern
```

A remediation task also began directly with implementation mechanics such as registry names, fail-fast startup, explicit engine access, getter fall-through, cold-start 500, allowed/forbidden boundaries and regression tests before explaining the underlying problem in ordinary language.

The report contained no useful architecture diagrams despite describing ownership, lifecycle, startup/shutdown, trust boundaries and Before/After architectural changes.

Baseline result for all three scenarios: `RED_CONFIRMED`.

The failure is not insufficient technical depth. It is a final-presentation failure: working-artifact shorthand leaked into user-facing documents.

---

## Scenario 34 — Working-artifact style leaks into final prose

The accepted evidence and findings ledger are technically sound. During final synthesis, the writer produces compact prose dominated by RF/SER IDs, arrows, slash-compounds, English/Russian hybrids and implementation shorthand.

Example failure shape:

```text
System gaps: (1) error-boundary leaks credentials (RF-A/C); (2) NATS/journal DB lack designated owner + managed lifecycle; (3) test-app != prod-app -> prod risks untestable; (4) SQL injection ...
```

### Expected behavior

Final user-facing documents must explain important mechanisms in connected prose before relying on IDs or shorthand.

For each material problem, the reader should be able to answer:

1. What is happening now?
2. Why does it happen?
3. What practical consequence follows?
4. What architectural boundary or mechanism is responsible?
5. What direction of correction is recommended?

RF/SER/TASK IDs support the explanation; they do not replace it.

Working artifacts may remain terse and machine-oriented. Final artifacts may not inherit that style.

### PASS criteria

- important conclusions are expressed as connected technical paragraphs;
- prose follows a natural causal structure such as `mechanism -> evidence -> consequence -> correction direction`;
- shorthand arrows, pseudo-code prose and compressed slash compounds are not the primary explanatory form;
- the executive synthesis can be understood without opening the ledger;
- references such as RF-A/RF-C appear after or alongside explanation rather than acting as the explanation itself.

### FAIL criteria

- final prose reads like an agent handoff, ledger row or task scratchpad;
- sentence fragments dominate material sections;
- the reader must decode IDs and implementation nouns before understanding the problem;
- a list of labels substitutes for causal explanation.

---

## Scenario 35 — Complex architecture report contains no useful diagrams

The review reconstructs several of the following: component topology, ownership, startup/shutdown lifecycle, a material end-to-end request flow, trust boundaries, concurrency, target architecture and non-trivial roadmap dependencies.

The final package nevertheless contains no Mermaid diagrams or only decorative diagrams that add no explanatory value.

### Expected behavior

Use diagrams when topology, ordering, lifecycle, ownership, trust boundaries, state transitions or Before/After architecture are materially easier to understand visually than through prose alone.

For a substantial `STANDARD_FULL` or `FORENSIC` report, the package normally includes at least:

- one useful As-Built component/boundary view;
- one material runtime/lifecycle/sequence view when such behavior exists;
- one Target Architecture view when target architecture is requested;
- Before/After or dependency visualization when a remediation mechanism is difficult to understand without it.

This is a semantic requirement, not a decorative quota. Do not invent diagrams where the repository has no supporting evidence.

### PASS criteria

- diagrams correspond to accepted evidence and real component names;
- each included diagram explains a material relationship or transition that prose alone would make harder to follow;
- target behavior is clearly distinguished from current behavior;
- complex lifecycle/ownership changes use visual explanation where appropriate;
- diagrams and prose do not contradict each other.

### FAIL criteria

- a substantial report with material topology/lifecycle/target changes contains no useful diagrams without an explicit reason;
- diagrams merely reproduce directory trees or generic boxes;
- current and target states are mixed;
- a diagram replaces evidence rather than explaining accepted evidence.

---

## Scenario 36 — Russian final report degenerates into hybrid shorthand

The user-facing report is nominally Russian, but ordinary explanatory prose contains frequent English/Russian hybrids and transliterated or untranslated ordinary concepts:

```text
error-boundary протекает credential-ами
managed lifecycle
designated owner
prod-risks untestable
shutdown негрейсфул
runtime-drift
```

Exact identifiers, API/protocol names and formal status tokens legitimately remain in English.

### Expected behavior

Write natural Russian technical prose. Preserve exact identifiers and established names where translation would reduce precision, but translate ordinary explanatory concepts when a clear Russian formulation exists.

At first significant use, an English technical term may be introduced with a Russian equivalent. Subsequent prose should prefer the Russian form unless the English term is itself the established identifier or unambiguous industry term.

Do not force awkward literal translation; the goal is readable professional Russian, not language purism.

### PASS criteria

- ordinary concepts are expressed naturally in Russian;
- exact code identifiers, paths, protocols, status/verdict tokens and product names remain exact;
- English terminology is introduced only where it improves precision;
- no widespread transliterated pseudo-Russian such as `негрейсфул`, `протекает credential-ами`, `prod-risks`;
- the final editorial reviewer flags hybrid shorthand as `LANG`, `TERM` or `STYLE` issues.

### FAIL criteria

- final documents contain dense mixed-language shorthand that impairs readability;
- ordinary concepts remain untranslated without a precision reason;
- language cleanup changes technical semantics, identifiers, severity or evidence.
