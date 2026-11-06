# Épicos

| Campo | Valor |
|---|---|
| Status | Draft |
| Atualizado em | `<AAAA-MM-DD>` |
| Aprovado por / em | — |

## Épicos

| Épico | Objetivo | RFs | Contextos / aggregates | Dono |
|---|---|---|---|---|
| `<1 — Cadastros>` | `<dados mestres para abrir uma ordem>` | `<RF01–RF08>` | `<Registrations: Customer, Vehicle>` | `<nome>` |

### Épico `<n>` — `<nome>`

`<Dois ou três parágrafos: o que cobre, onde estão as regras mais críticas, o que fica fora.>`

## Mapa de dependências

| Épico dependente | Depende de | Natureza | Como destravar sem esperar |
|---|---|---|---|
| `<2>` | `<1>` | `<precisa de IDs e dados para o snapshot>` | `<fake do repositório/port com objetos fixos; combinar os atributos antes>` |

## Contratos a combinar primeiro

Para que todos trabalhem em paralelo, combine no início:

- atributos dos aggregates que outros épicos consomem;
- assinatura dos eventos de domínio publicados entre contextos;
- métodos dos ports entre módulos.

| Contrato | Dono | Consumidores | Combinado em |
|---|---|---|---|
