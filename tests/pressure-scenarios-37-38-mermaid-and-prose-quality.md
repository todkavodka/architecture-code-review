# Pressure Scenarios 37–38 — Mermaid Renderability and Final-Prose Density

These scenarios were added from field validation of the v0.2 final-report readability branch on a real completed architecture-review package.

The field run showed two remaining defects:

- several Mermaid diagrams were present but failed to render in VS Code Markdown Preview;
- final prose was substantially more readable than before, but some sections still packed multiple independent mechanisms into one dense paragraph and introduced specialist English shorthand faster than it was explained.

These are final-package quality defects. They do not reopen technical evidence unless correction exposes a real contradiction.

## Scenario 37 — Mermaid exists but does not render

### RED evidence

A real final package contained several Mermaid blocks added by the readability/diagram pass. At least one lifecycle diagram and additional Mermaid diagrams failed when viewed in VS Code Markdown Preview.

The existing Skill contract required simple syntax and said to check Mermaid structurally when a renderer was unavailable, but did not require an actual parser/render validation when a suitable renderer was available.

### Required behavior

For every Mermaid block in final user-facing artifacts:

1. Extract or otherwise identify each block independently.
2. If a Mermaid parser/renderer is available in the environment, actually invoke it against every block.
3. Record validation per diagram, preferably by stable diagram/document location.
4. A failed parse/render is a `DIAG-*` editorial issue and blocks final acceptance.
5. Correct failed diagrams without changing technical semantics.
6. Re-run the parser/renderer after correction.
7. Only diagrams that pass the available renderer may be considered render-validated.

If no Mermaid parser/renderer is available, do not claim render validation. Record the limitation explicitly as `MERMAID_RENDER_VALIDATION_UNAVAILABLE` and perform the strongest structural review available.

Do not require one specific vendor tool. `mmdc`, a project-provided Mermaid validator, or another compatible parser/renderer is acceptable. Prefer the renderer/toolchain actually used by the repository or documentation workflow when known.

### PASS

PASS requires evidence that:

- each final Mermaid block was enumerated;
- every block was actually parser/render validated when a renderer was available;
- all failed blocks were corrected and revalidated;
- final acceptance did not occur while a known Mermaid parse/render failure remained;
- when no renderer existed, the package clearly states that render validation was unavailable instead of implying PASS.

### FAIL

FAIL if any of the following occurs:

- the reviewer merely says Mermaid "looks structurally valid" despite an available renderer;
- only one sample diagram is validated while other final blocks are unchecked;
- a known render failure remains in an accepted final package;
- render validation is claimed without evidence of a parser/renderer invocation;
- correction changes architecture semantics merely to satisfy Mermaid syntax.

---

## Scenario 38 — Connected prose is still overloaded and terminology-dense

### RED evidence

A real rewritten final report improved from telegraphic shorthand to connected prose, but still produced paragraphs that combined several distinct mechanisms, for example NATS lifecycle, journal-engine ownership, synchronous audit writes, and shutdown cleanup in one paragraph.

Target/roadmap prose also retained dense clusters such as:

- `eager reachability-check`;
- `producer-miss`;
- `write-back`;
- `single-flight wrapper`;
- `cold-cache miss`;
- `thundering-herd`.

These terms may be technically appropriate, but a final user-facing document must explain an important specialist term or mechanism before relying on it as shorthand.

### Required behavior

Final user-facing prose follows these rules:

1. **One primary mechanism per paragraph.** A paragraph may mention related effects, but it must not make the reader track multiple independent root mechanisms simultaneously.
2. **Explain before compressing.** At the first material use of a specialist English term, hybrid expression, or architecture shorthand, explain the mechanism in natural Russian; the exact term may then be retained in parentheses or used afterward.
3. **Do not simplify exact identifiers.** Class names, methods, APIs, file paths, status tokens, protocol names, and precise code terms remain exact.
4. **Keep implementation precision.** The rule is readability, not loss of technical detail.
5. **Separate explanation from execution contract.** Roadmap tasks present human-readable problem/cause/result first, then a visually distinct implementation contract (table, subsection, or equivalent).
6. Editorial review should flag paragraph overload and unexplained specialist shorthand as `STYLE-*` / `TERM-*` issues.

A useful test is whether a technical reader unfamiliar with the code can answer, after one paragraph: "What single mechanism was this paragraph explaining?" If several independent answers are required, split it.

### PASS

PASS requires evidence that:

- dense multi-mechanism paragraphs are split or restructured;
- specialist shorthand is explained on first material use where its meaning is not obvious from surrounding prose;
- roadmap explanatory prose and implementation contract are visually separated;
- exact identifiers and technical semantics are preserved;
- fresh editorial re-review accepts the corrected package.

### FAIL

FAIL if:

- a paragraph still compresses several independent root mechanisms into one wall of text;
- English/hybrid terminology is merely translated mechanically without explaining the mechanism;
- technical precision is removed to make the prose shorter;
- execution-contract labels again become the primary explanation;
- the author self-accepts the correction without fresh editorial re-review.
