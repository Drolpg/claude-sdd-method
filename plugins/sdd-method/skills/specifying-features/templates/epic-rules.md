# Épico <n> — regras específicas de `<context>`

Fonte: `<docs/domain/aggregates/…>`, `docs/decision-register.md`, `<ADRs relevantes>`. Não repita este conteúdo em
`CLAUDE.md` ou `AGENTS.md`. Carregado ao editar código ou documentos deste contexto.

## Invariantes implementados (fato, código atual)

- `<Entidade>` states: `<a → b → c>`, com `<x>` terminal.
- `<Regra já implementada e onde é garantida>`.

## Decisões — não tratar como diferentes do registrado

- **AD-NNN** (`<tema>`): **`<Status>`** em `<AAAA-MM-DD>` — `<opção escolhida e o que isso implica>`. `<O que não
  fazer sem nova decisão.>`
- **AD-NNN** (`<tema>`): **Team Decision Required** — `<não implementar nenhum dos lados até a decisão>`.

## Dívidas conhecidas neste contexto

- `TD-NNN` — `<resumo>`; `<suposição temporária a respeitar>`.

## Regras de fronteira que se aplicam aqui

- Nenhuma importação de pacote interno de outro módulo; use IDs, eventos ou port/adapter (`ADR-NNN`).
- O teste de fronteira de módulos continua verde após qualquer mudança estrutural.
