# Avaliação de arquitetura

| Campo | Valor |
|---|---|
| Fase | `<preliminar (enunciado) · confirmação (após spec/descoberta) · reavaliação (gatilho X)>` |
| Data | `<AAAA-MM-DD>` |
| Tipo de projeto | `<ver project-archetypes.md>` |
| Responsável | `<nome>` |

## Sinais

| Sinal | Nível | Evidência |
|---|---|---|
| Regras e estados (invariantes, máquinas de estado, cálculos com regra) | `<baixo · médio · alto>` | `<trecho, requisito, fato>` |
| Integrações (quantas, quão instáveis, precisam de fake?) | | |
| Troca de tecnologia prevista (provedor, canal, banco, LLM) | | |
| Equipe e trabalho em paralelo | | |
| Vida útil e evolução (POC, MVP, produto) | | |
| Processamento assíncrono (filas, workers, idempotência) | | |
| Conformidade e auditoria (dinheiro, dados pessoais, regulação) | | |

Sinal sem evidência conta como baixo.

## Fronteiras reais

| Fronteira | Por que é real | Precisa de fake nos testes? | Troca prevista? |
|---|---|---|---|

## Recomendação

**Estilo:** `<estilo>` `<por módulo, se variar: módulo A → DDD completo; módulo B → camadas>`

| Elemento estrutural | Sinal que justifica | Custo |
|---|---|---|
| `<ex.: port ClienteExterno>` | `<integração instável, precisa de fake>` | `<1 interface + 1 adapter + 1 fake>` |

## O que não adotar

| Elemento | Por quê | Regra no AGENTS.md |
|---|---|---|
| `<ex.: repository>` | `<um banco, acesso simples pela sessão>` | `<"Não criar repository">` |

## Trilha de domínio

`<nenhuma · DDD leve · DDD completo>` — `<motivo em uma frase>`

## Gatilhos para subir de nível

- `<quando acontecer X → adotar Y>`

## Sinais de excesso (para descer de nível)

- `<quando Y não for usado por Z → remover>`

## Alternativas consideradas

| Estilo | Por que não |
|---|---|
| `<mais simples>` | |
| `<mais estruturado>` | |
