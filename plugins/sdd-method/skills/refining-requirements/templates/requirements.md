# Requisitos

| Campo | Valor |
|---|---|
| Status | Draft |
| Atualizado em | `<AAAA-MM-DD>` |
| Aprovado por / em | — |
| Fontes | `docs/challenge/`, `docs/domain/` |

Este é o único registro de IDs de requisito. Board, tracker e specs citam estes IDs; nenhum deles cria IDs.

## Atores

| Ator | Papel | Tipo |
|---|---|---|
| `<Customer>` | `<dono do veículo; aprova ou reprova linhas do orçamento>` | `<humano · técnico · sistema externo>` |

## Requisitos funcionais

| ID | Requisito | Contexto | Origem | Fase | Status | Feature |
|---|---|---|---|---|---|---|
| RF01 | `<ação verificável, no tamanho de um comando>` | `<contexto>` | `<E2 · evento "X">` | 1 | Proposto | — |

Status: `Proposto`, `Aprovado`, `Em implementação`, `Implementado`, `Removido (<motivo>)`.

## Requisitos não funcionais

| ID | Requisito | Categoria | Origem | Como verificar |
|---|---|---|---|---|
| RNF01 | `<ex.: entrega como monólito com módulos por bounded context>` | `<arquitetura · segurança · desempenho · operação · entrega>` | `<E5>` | `<teste de fronteira no CI>` |

## Casos de borda fechados

### CB-01 — `<pergunta>`

**Decisão:** `<o que foi decidido>`
**Data / quem decidiu:** `<AAAA-MM-DD>` / `<nome>`
**Afeta:** `<RF, aggregate, feature>`

## Riscos técnicos

| # | Risco | Status | Referência |
|---|---|---|---|
| 1 | `<risco>` | `<Pendente de análise · Mitigado · Resolvido · Adiado>` | `<ADR, feature, TD>` |
