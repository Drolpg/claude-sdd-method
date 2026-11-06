# Desenho estratégico

| Campo | Valor |
|---|---|
| Status | Draft |
| Atualizado em | `<AAAA-MM-DD>` |
| Aprovado por / em | — |
| Fontes | `docs/domain/discovery/`, `<frames do board>` |

## Domínio

`<nome do domínio>`

## Subdomínios

| Subdomínio | Tipo | Por quê | Estratégia |
|---|---|---|---|
| `<nome>` | `<core · supporting · generic>` | `<justificativa>` | `<construir · comprar · reutilizar>` |

### Core domain

`<O diferencial em uma frase.>`

Pilares: `<ex.: transparência operacional, rastreamento em tempo real, visibilidade para o cliente>`.

Consequência de modelagem: `<o que o core exige do modelo>`.

## Princípios de fronteira

1. Uma transação altera um aggregate.
2. Referência entre aggregates só por ID.
3. Coordenação entre fronteiras por policy que reage a evento de domínio.
4. Dado de outro contexto entra como snapshot no momento do registro.

## Mapeamento

| Subdomínio | Bounded context | Módulo (rito 7) |
|---|---|---|

## Canvas: <Bounded Context>

| Campo | Conteúdo |
|---|---|
| Propósito | `<por que este contexto existe, em linguagem de negócio>` |
| Classificação | `<core · supporting · generic>` |
| Papel | `<execução · análise · gateway · cadastro · …>` |
| Linguagem (termos-chave) | `<termos que só fazem sentido aqui>` |
| Regras de negócio centrais | `<regras que este contexto decide>` |
| Entrada | `<de quem · o quê (comando, consulta, evento)>` |
| Saída | `<para quem · o quê>` |
| Aggregates candidatos | `<lista>` |
| Premissas | `<o que está sendo assumido>` |
| Perguntas em aberto | `<hotspots ou ADs>` |

<!-- Repita o canvas para cada contexto. -->

## O que não é bounded context

| Conceito | Onde vive | Por quê |
|---|---|---|
| `<ex.: Notification>` | `<efeito outbound do módulo consumidor>` | `<sem modelo nem linguagem próprios>` |
