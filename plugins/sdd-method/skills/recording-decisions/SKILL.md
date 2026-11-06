---
name: recording-decisions
description: Use quando surgir uma escolha arquitetural ou de processo, uma proposta que precisa de discussão antes de virar decisão, uma decisão tomada que precisa de registro, um desvio conhecido no código ou no desenho, ou quando for mudar o status de uma entrada AD, ADR, RFC ou dívida técnica (TD).
---

# Registro de decisões

## Visão geral

Decisões são o ativo mais durável do projeto: o código muda, o porquê precisa sobreviver. Cada tipo de registro
responde a uma pergunta diferente, e cada um tem dono, status e número que não se repete.

## Qual instrumento usar

| Situação | Instrumento | Onde |
|---|---|---|
| Escolha em aberto, com dono e escopo, que ainda não pode ser feita por quem a encontrou | AD (entrada no registro) | `docs/decision-register.md` |
| Proposta que precisa de discussão antes de virar decisão (estrutura, processo, desenho) | RFC | `docs/rfc/RFC-NNN-<slug>.md` |
| Decisão tomada, com contexto, opções e trade-offs | ADR | `docs/adr/ADR-NNN-<slug>.md` |
| Desvio que já existe entre o estado atual e o desejável | TD | `docs/tech-debt/TD-NNN-<slug>.md` |
| Ideia para depois, sem desvio atual | Backlog | `docs/requirements/backlog.md` |

Caminhos comuns: AD resolvida gera ADR; RFC aceita gera ADRs e specs; TD paga vira feature ou tarefa.

A decisão de estilo arquitetural tem template próprio: `sdd-method:choosing-architecture` ›
`templates/ADR-architecture-style.md`.

## Nível 1 (enxuto)

Decisões e débitos ficam em tabelas no `docs/02-plan.md` (§ "Decisões que afetam o código", `D01`…, e § "Débitos
técnicos intencionais"), com as mesmas regras de número, opções e aprovação. Uma decisão vira ADR em arquivo quando:

- cruza módulos ou donos;
- é revisitada ou substituída;
- o projeto sobe para o nível 2.

Ao promover, deixe na tabela a linha com "→ ADR-NNN".

## Ciclos de vida

- **AD:** `Pending` · `Team Decision Required` · `Not Blocking` · `Deferred` → `Resolved` ou `Superseded`.
- **RFC:** `Draft` → `Em discussão` (com prazo para comentários) → `Aceita` ou `Rejeitada` → `Implementada`.
- **ADR:** `Proposed` → `Accepted` ou `Rejected` → `Deprecated` ou `Superseded by ADR-NNN`.
- **TD:** `Open` → `In Progress` → `Resolved`; ou `Accepted` (assumida, sem plano); ou `Superseded by TD-NNN`.

## Procedimento

1. **Número:** liste a pasta (ou o registro) e use o maior número + 1. Nunca reutilize; nunca escreva "próximo
   número" em outro documento.
2. **Escreva** a partir de `templates/`. Datas ISO (`AAAA-MM-DD`; `AAAA-MM` só se o dia for desconhecido; nunca
   invente o dia).
3. **Opções reais:** pelo menos duas, com prós e contras honestos. A recomendação fica separada da decisão.
4. **Escopo de decisão:** quem pode decidir (dono do épico, arquitetura compartilhada, time todo). Mudança de
   fronteira de contexto, contrato público ou dado persistido compartilhado é sempre do time.
5. **Aprovação:** só uma pessoa muda para `Accepted`, `Resolved` ou `Aceita`; o documento registra nome e data.
6. **Propague** a mudança de status no mesmo commit (checklist abaixo).

## Checklist de propagação

- [ ] `docs/decision-register.md`
- [ ] ADR, RFC e TD relacionados (seção de relacionados e status repetido no rodapé)
- [ ] `.claude/rules/epic-<n>-<context>.md` e `AGENTS.md`, se uma regra mudou
- [ ] Specs afetadas (voltam a `Draft` se a mudança for material)
- [ ] Espelho no board, se existir
- [ ] `docs/method.md`, se a decisão fechar o gate de um rito

## Regras

- ADR registra decisão e racional. Código, YAML e estrutura de pastas ficam na technical-spec.
- Correções são aditivas: "Nota (AAAA-MM-DD): …" ou `Superseded by`.
- Ninguém marca como resolvida uma decisão que não é do seu escopo; reporte a lacuna e o dono.

## Erros comuns

- ADR com uma opção só: é anúncio, não decisão.
- RFC sem a seção "O que precisamos que o time decida".
- Mesmo número criado em duas branches: no merge, renumere o mais recente, atualize as referências e deixe uma nota.
- Decisão registrada só no board ou numa conversa de chat.
