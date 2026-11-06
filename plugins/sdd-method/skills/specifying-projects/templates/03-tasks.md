# 03 — Tarefas

| Campo | Valor |
|---|---|
| Plano | `docs/02-plan.md` (aprovado em `<AAAA-MM-DD>`) |
| Atualizado em | `<AAAA-MM-DD>` |

Uma tarefa por vez, na ordem. Status: `Pendente`, `Em andamento`, `Concluída`, `Bloqueada (<motivo>)`.

## M0 — Esqueleto

**Checkpoint:** `<projeto roda, CI verde, primeiro teste passando>`

| ID | Tarefa | Requisitos | Testes (RED) | Critério de aceite | Status | Evidência |
|---|---|---|---|---|---|---|
| M0-T1 | `<tarefa>` | `<RF-01>` | `<arquivo de teste>` | `<verificável>` | Pendente | `<commit, comando e resultado>` |

## M1 — `<nome>`

**Checkpoint:** `<critério da fase>`

| ID | Tarefa | Requisitos | Testes (RED) | Critério de aceite | Status | Evidência |
|---|---|---|---|---|---|---|

## Pendências abertas

Divergências entre spec, teste e código, e dúvidas que bloqueiam uma tarefa. Ninguém decide sozinho.

| Data | Tarefa | Divergência | Decisão | Por quem |
|---|---|---|---|---|

## Prompt de implementação

<!-- Opcional: quando uma sessão planeja e outra implementa. Um bloco por tarefa entregue. -->

```text
Implemente somente a tarefa <ID> de docs/03-tasks.md.
Leia antes: docs/00-constitution.md, docs/01-spec.md (<seções>), docs/02-plan.md (<seções>).
Testes que definem o aceite: <arquivos>. Não altere tests/ nem a spec para fazer algo passar.
Rode: <teste alvo>, depois <suíte completa> e <lint>.
Ao terminar, responda com o relatório de tarefa (arquivos, comandos e resultados, decisões não óbvias,
divergências da spec).
```
