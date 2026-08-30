# Architecture Code Review Skill

A reusable agent skill for evidence-first architecture and code reviews of existing software systems.

Instead of producing a lint-style list of smells, the skill reconstructs how the system actually works, traces ownership and lifecycle, verifies candidate findings independently, separates root causes from projections, and only then assigns severity and recommends remediation.

The default final narrative is written in Russian technical prose, while exact code identifiers, protocol names, paths, API/IPC names, and formal status tokens remain unchanged.

## What it reviews

The skill is intended for whole-project or subsystem reviews where one or more of these areas matter:

- architecture and responsibility boundaries;
- state and resource ownership;
- startup, steady-state, recovery, reconnect, cancellation, and shutdown lifecycle;
- concurrency and background work;
- IPC/API/native boundary contracts;
- security and trust boundaries;
- configuration and persistence;
- error contracts and observability;
- maintainability and testability;
- target architecture and remediation planning when explicitly requested.

Technology-specific review lenses are included for:

- Tauri;
- Electron;
- React;
- Django;
- FastAPI;
- Litestar.

The common review method is technology-independent. Stack files add checks; they do not replace the core workflow.

## Key v0.2 capabilities

Version 0.2 introduces a gated multi-pass review workflow:

- explicit `STANDARD_FULL` and `FORENSIC` depth selection;
- independent selection of the requested endpoint;
- detailed As-Built Architecture reconstruction before thematic findings;
- mandatory independent As-Built review in both modes;
- ownership matrices, invariants, and adversarial scenarios;
- explicit IPC/API/native boundary-contract analysis;
- candidate findings that must be independently verified before becoming authoritative;
- root/projection/SER separation before severity assignment;
- evidence-backed security attack-chain requirements for serious security claims;
- persistent `working/INDEX.md` workflow state and resumable agent handoffs;
- architecture-correction and `REVALIDATION_REQUIRED` handling;
- optional Target Architecture with an independent feasibility review;
- optional dependency-driven remediation roadmap with execution-consistency review;
- fresh-context final editorial review that cannot silently change technical meaning;
- chunked document writing and recovery under context pressure.

## Installation

### OpenCode / Codex and other agents using `~/.agents/skills`

Clone the repository directly into your personal skills directory:

```bash
git clone \
  https://github.com/todkavodka/architecture-code-review.git \
  ~/.agents/skills/architecture-code-review
```

Then start a new agent session so the installed skill is discovered from disk.

If the directory already exists, update it instead of cloning again:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

Verify the installed revision:

```bash
cd ~/.agents/skills/architecture-code-review
git rev-parse HEAD
```

### Install a specific released version

After a release tag is available, pin the installation to that version:

```bash
cd ~/.agents/skills/architecture-code-review
git fetch --tags
git checkout v0.2.0
```

To return to the latest production version later:

```bash
git switch main
git pull --ff-only
```

## How to use

Start a new agent session in the repository you want to review and ask it to use the skill explicitly.

For example:

```text
Use architecture-code-review to perform a full architecture review of this repository.
```

Or in Russian:

```text
Используй architecture-code-review и проведи полный архитектурный аудит этого проекта.
```

You can also state the desired result immediately:

```text
Используй architecture-code-review.
Нужен полный аудит плюс целевая архитектура и план исправлений.
```

The skill should not immediately start a deep review. Its Start Gate first separates two decisions: review depth and requested final result.

## Review depth

### `STANDARD_FULL`

A complete architecture review with the full verification and adjudication chain, but with thematic investigation kept reasonably compact.

This is the normal default for most production repositories.

### `FORENSIC`

A deeper investigation with separate thematic passes, expanded evidence trails, adversarial scenario analysis, and more working artifacts.

Use it when architecture defects are subtle, cross-process, concurrency-heavy, security-sensitive, or difficult to reproduce from a conventional review.

The skill may recommend a depth, but it must not silently choose `FORENSIC` for the user.

## Requested endpoint

Depth and endpoint are independent choices.

### `REVIEW_ONLY`

Produces the architecture review and authoritative findings ledger.

### `REVIEW_PLUS_TARGET_ARCHITECTURE`

Adds a reviewed Target Architecture / To-Be design derived from verified findings, invariants, positive controls, and explicit product decisions.

### `REVIEW_PLUS_TARGET_AND_ROADMAP`

Adds both Target Architecture and a dependency-driven remediation roadmap with an execution-consistency review.

Choosing `FORENSIC` does not automatically request a target architecture or roadmap.

## What the workflow looks like

At a high level:

```text
baseline
  -> As-Built Architecture
  -> independent As-Built review
  -> thematic discovery
  -> candidate verification
  -> root-boundary adjudication
  -> severity adjudication
  -> authoritative findings ledger
  -> optional Target Architecture + independent review
  -> optional remediation roadmap + execution-consistency review
  -> final package assembly
  -> fresh editorial review / correction / re-review
```

The important distinction is that discovery does not directly create final findings. A candidate must survive independent verification, root-boundary adjudication, and severity adjudication first.

## Output

The default output package is created under:

```text
docs/reviews/architecture-review/
```

Depending on the selected endpoint, the final package contains:

```text
docs/reviews/architecture-review/
├── 01-architecture-review.md
├── 02-authoritative-findings-ledger.md
├── 03-target-architecture.md       # when requested
├── 04-remediation-roadmap.md       # when requested
└── working/
    └── ... intermediate evidence and review artifacts
```

`working/` is intentional. It contains intermediate evidence, candidate analysis, independent reviews, corrections, and persisted handoffs. Intermediate claims may later be corrected or refuted, so the authoritative state is tracked through the workflow registry and final documents.

## Evidence rules

Material findings are expected to distinguish:

1. observation;
2. interpretation;
3. concrete mechanism;
4. impact;
5. recommendation.

Claims should cite concrete `path:line-range` evidence. Cross-layer findings should normally include evidence from every materially affected boundary.

The skill intentionally rejects common review shortcuts:

- directory names are not proof of architecture;
- file length is not automatically a defect;
- `unwrap`, `clone`, mocks, TODOs, or hardcoded values are not findings without demonstrated impact;
- missing tests do not prove production behavior is broken;
- broad privileged APIs do not automatically prove RCE;
- security severity is not promoted without a plausible attacker chain;
- a rewrite is not recommended merely because a cleaner design can be imagined.

## Persistent multi-agent workflow

For long reviews, `working/INDEX.md` is the persistent workflow authority.

Agent results are not considered complete merely because an agent said it finished. Independently consumable artifacts move through explicit states such as:

```text
PENDING
IN_PROGRESS
ARTIFACT_WRITTEN
REVIEW_REQUIRED
CORRECTION_REQUIRED
REVALIDATION_REQUIRED
BLOCKED
COMPLETE
NOT_APPLICABLE
```

A downstream stage must not consume `REVIEW_REQUIRED`, `CORRECTION_REQUIRED`, `REVALIDATION_REQUIRED`, or `BLOCKED` as accepted truth.

Important workflow state must be persisted to files; it must not exist only in chat history.

## Repository structure

```text
.
├── README.md
├── LICENSE
├── SKILL.md
├── references/
│   ├── review-modes-and-orchestration.md
│   ├── review-method.md
│   ├── evidence-and-severity.md
│   ├── ownership-and-scenarios.md
│   ├── boundary-contract-audit.md
│   ├── independent-verification.md
│   ├── root-boundary-adjudication.md
│   ├── lifecycle-and-mermaid.md
│   ├── report-contract.md
│   ├── target-architecture-review.md
│   ├── remediation-roadmap-review.md
│   ├── final-editorial-review.md
│   └── stacks/
└── tests/
    ├── pressure-scenarios.md
    └── pressure-validation-matrix.md
```

`SKILL.md` is intentionally a compact orchestrator. Heavy normative guidance lives in the authoritative reference files instead of being duplicated in the entry point.

## Validation

The v0.2 implementation was pressure-tested with fresh isolated agent contexts.

Runtime validation result:

```text
32 / 32 required scenarios PASS
0 failed
0 blocked
0 inconclusive
```

The independent implementation review reported:

```text
BLOCKER 0
HIGH    0
```

The development repository retains the internal benchmark, design, review, and raw validation evidence. This public repository intentionally contains only the distributable Skill package and its pressure-test contracts.

## Updating the Skill

For a normal installation tracking `main`:

```bash
cd ~/.agents/skills/architecture-code-review
git switch main
git pull --ff-only
```

Start a new agent session after updating so the runtime reloads the Skill from disk.

For production environments where reproducibility matters, prefer pinning a release tag rather than continuously following `main`.

## Development and contribution

Changes to the Skill should be treated like behavior changes, not ordinary prose edits. The project uses pressure scenarios and fresh-context validation to verify that new guidance changes agent behavior without introducing contradictory authority or workflow regressions.

Before promoting a substantial change, preserve the sequence:

```text
design
-> implementation plan
-> isolated implementation
-> independent review
-> pressure validation
-> promotion readiness
-> public package
-> release
```

Do not treat a documentation-only appearance as evidence that a Skill change is behavior-neutral.

## License

This project is licensed under the MIT License. See `LICENSE` for the full text.
