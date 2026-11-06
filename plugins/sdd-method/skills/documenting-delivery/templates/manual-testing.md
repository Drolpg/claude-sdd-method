# Teste manual da API

Executa o fluxo completo pela collection `<caminho>`. Atualize este guia sempre que a collection mudar.

## Pré-requisitos

- Aplicação rodando: `<comando>`; saúde em `<URL>` responde `<resposta>`.
- Collection importada em `<ferramenta>`; ambiente `<nome>` selecionado.
- Dados iniciais: `<seed de demonstração habilitado · nenhum>`.

## Variáveis

| Variável | Valor inicial | Preenchida por |
|---|---|---|
| `baseUrl` | `<http://localhost:8080>` | Manual |
| `token` | — | Requisição "Login" |

## Fluxo

| # | Requisição | O que faz | Resultado esperado | Variáveis gravadas |
|---|---|---|---|---|
| 1 | `<POST /api/auth/login>` | `<autentica>` | `<200 e token>` | `token` |

## Cenários de erro

| Requisição | Alteração | Resultado esperado |
|---|---|---|
| `<…>` | `<sem token>` | `<401 com código <AUTH_REQUIRED>>` |

## Execução automatizada

`<comando para rodar a collection em linha de comando, se houver>`
