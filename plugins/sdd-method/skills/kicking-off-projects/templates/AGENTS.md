# AGENTS.md — <Project name>

Project instructions for humans and coding agents. This project follows the `sdd-method` plugin; its level,
architecture style and rite status live in `docs/method.md`.

<!--
How to fill this file:
- STYLE sections come from the architecture assessment (rite 2). STACK sections come from rite 7.
- Keep this file about rules. Epic-specific facts go to .claude/rules/epic-<n>-<context>.md (levels 2–3).
- Write it in the documentation language of the project if the team prefers; English is the default.
-->

## Before anything

1. Read `docs/method.md`, then the spec (`docs/01-spec.md` or `docs/requirements/`) and the current task or feature.
2. **The spec is the source of truth.** If code and spec diverge, stop and report it; do not fix it silently.

## Project context

- <One paragraph: what the system does and for whom.>
- <Hard constraints from the challenge statement.>
- Documentation language: <pt-BR>. Names in code: <domain in the business language, infrastructure in English>.
- <!-- STACK: language, framework, package manager and how to invoke it. Do not add dependencies outside the stack
  without asking. -->

## Architecture rules

Style: <!-- STYLE: e.g. "layered (api → services → models)" --> — decision in <!-- link -->.

<!-- STYLE: the dependency rules of the chosen style, e.g.
- `api` has no business rules; `services` does not import the web framework or the queue library at import time.
- `core/` never imports `adapters/`; the composition root wires adapters into the core.
- Modules talk only through public module APIs, stable IDs or events; the boundary check runs on every build. -->

**Do not add** (decided against; adding any of these requires a new decision):

<!-- STYLE: e.g.
- ports/interfaces, repositories, an `adapters/` folder or a DI container;
- aggregates, value objects or domain events beyond the ones listed in the spec. -->

Always:

- Change state through intention-revealing functions or methods, not ad-hoc field updates spread across layers.
- Use a decimal type for money; never floating point.
- Never expose persistence entities as API contracts; validate input at the boundary.

## Spec-driven workflow

<!-- Level 1 -->
- Work on **one task at a time**, in the order of `docs/03-tasks.md`.
- Behavior change: spec first, then test, then code.
- Divergence or doubt: record it under "Pendências abertas" in `docs/03-tasks.md` and move to the next independent
  task.

<!-- Levels 2–3 (replace the block above) -->
<!-- Every non-trivial feature starts in docs/features/<context>/<slug>/: functional-spec → human approval →
technical-spec → human approval → implementation-plan → implementation with evidence. An agent never infers or grants
approval. Material change to an approved spec returns it to Draft. -->

## Test-driven development

- Tests in `tests/` are the acceptance criteria. Write them first and see them fail for the right reason.
- **Never edit tests, test configuration or the spec to make something pass.** If a test looks wrong, explain why and
  wait for a decision.
- Every requirement has at least one test; the requirement → test matrix in the spec stays current.
- Fakes at real boundaries only; a real database in integration tests when there is persistence; no real network in
  unit tests.
- Run the target test, then the full suite and the linters before saying a task is done:
  <!-- STACK: commands -->
- Coverage target: <80%>. Do not reduce coverage of changed code.

## Persistent data

- Versioned migrations are the only schema mechanism. <!-- STACK: tool, folder, naming. -->
- Production never lets the ORM create or update the schema.
- Seeds: demonstration data only behind an explicit development flag; tests use their own fixtures.

## Errors, logs and security

- Client-facing errors use a stable envelope and code; never stack traces, SQL or internal messages.
- Logs are structured, carry a correlation ID and never contain personal data, tokens or secrets.
- Secrets only through environment variables; `.env` and `docs/_local/` never go to git.
- Every task or feature records a security review (`sdd-method:reviewing-security`).

## Decisions

- Level 1: decisions and intentional debts are tables in `docs/02-plan.md`.
- Levels 2–3: `docs/decision-register.md`, `docs/adr/`, `docs/rfc/`, `docs/tech-debt/`.
- The next number is always the highest existing one + 1. A decision that crosses module boundaries or public
  contracts is a team decision.

## Code style

- Small cohesive functions, explicit names, early validation instead of nested conditionals.
- Comments explain non-obvious decisions, not what the code says.
- No speculative abstractions, unused interfaces or generic utility packages.
- <!-- STACK: formatter, linter, type checker, line length. -->

## Git

Branches, commits and pull requests follow `CONTRIBUTING.md`. One green cycle = one commit. Never push or merge to
`main` without explicit authorization.

## When you finish a task, reply with

1. Files created or changed.
2. Commands run and their results.
3. Non-obvious decisions, in up to five lines, with the why.
4. Any divergence from the spec.
