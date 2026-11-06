# Eventos de domínio e policies

| Campo | Valor |
|---|---|
| Status | Draft |
| Atualizado em | `<AAAA-MM-DD>` |
| Aprovado por / em | — |

## Catálogo de eventos

| Evento (passado) | Emitido por | Payload mínimo | Consumidores | Alcance |
|---|---|---|---|---|
| `<EstimateLineApproved>` | `<Estimate>` | `<estimateId, lineId, serviceExecutionId>` | `<Service Order, Stock>` | `<interno ao contexto · publicado entre contextos>` |

Eventos publicados entre contextos são contrato (Published Language): mudar payload exige decisão.

## Policies

| Evento de origem | Policy ("sempre que… então…") | Comando | Aggregate alvo | Consistência | Falha e retry |
|---|---|---|---|---|---|
| `<EstimateLineApproved>` | `<sempre que uma linha for aprovada, reservar as peças da execução>` | `<ReserveStockItems>` | `<StockReservation>` | `<eventual, após commit>` | `<reserva indisponível → execução aguarda peça; retry no restock>` |

## Status derivado

Quando um status é calculado a partir de outros, escreva a regra aqui, em ordem de precedência (o primeiro que casar
vence), e diga quando ela é recalculada.

1. `<DELIVERED>` — `<condição>`
2. `<…>`

Recalculado em: `<todo comando que altera execuções · na leitura>` (registre a escolha como decisão).
