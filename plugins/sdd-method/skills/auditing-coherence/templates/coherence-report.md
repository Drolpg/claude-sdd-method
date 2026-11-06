# Auditoria de coerência — <AAAA-MM-DD>

| Campo | Valor |
|---|---|
| Motivo | `<fim da fase N · antes da entrega · merge de X · migração de board>` |
| Repositório | `<branch>` @ `<commit>` |
| Board | `<URL>` (`<n>` itens, `<n>` frames lidos) |
| Auditado por | `<nome / Claude a pedido de nome>` |
| Não verificado | `<o que não foi possível acessar e por quê>` |

## Resumo

`<Duas ou três frases: o que está coerente, o que diverge, onde está a maior parte do drift.>`

| Classe | Quantidade |
|---|---|
| Igual | |
| Espelho desatualizado | |
| Ausente em um lado | |
| Conflito | |
| Inconsistência interna | |
| Referência quebrada | |
| Desvio doc × código | |

## Igual

- `<artefato>` — `<evidência: similaridade, cabeçalhos iguais>`

## Espelho desatualizado

| Artefato | Lado mais novo | Evidência (datas, commit) | Ação proposta | Dono |
|---|---|---|---|---|

## Ausente em um lado

| Artefato | Existe em | Falta em | Ação proposta | Dono |
|---|---|---|---|---|

## Conflitos (decisão necessária)

| Tema | Fonte A diz | Fonte B diz | Registro aberto | Dono |
|---|---|---|---|---|

## Inconsistências internas

| Fonte | Contradição | Ação proposta |
|---|---|---|

## Referências quebradas

| Onde | Referência | Problema | Ação proposta |
|---|---|---|---|

## Desvios documentação × código

| Documento | Afirma | Código faz | Ação proposta (TD, feature, correção do doc) |
|---|---|---|---|

## Não comparado

`<O que ficou fora e por quê (ex.: frames de workshop históricos, sem equivalente no repositório).>`

## Ações aprovadas

| Ação | Aprovado por / em | Feita em (commit) |
|---|---|---|
