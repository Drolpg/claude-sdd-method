# Catálogo de diagramas Mermaid

## Quais diagramas cada tipo de projeto pede

| Tipo de projeto | Obrigatórios | Quando houver |
|---|---|---|
| API síncrona | Componentes, sequência do fluxo principal | Estados, dados |
| Serviço assíncrono | Componentes, sequência API → fila → worker → externo, estados do processamento | Dados |
| Integração / ACL | Componentes, sequência com o externo | Estados |
| Agente de IA | Componentes, sequência de uma mensagem com ferramenta, fluxo de decisão | Dados |
| Plugin / front-end | Componentes, sequência de eventos da plataforma | Estados da UI |
| Domínio rico | C4 contexto e containers, context map, estados dos aggregates centrais | Modelo de domínio, implantação |
| Script / ETL | Fluxo dos dados | — |
| Qualquer projeto com infraestrutura | Implantação | Pipeline de CI/CD |

## Tipos

| Diagrama | Mermaid | Use para |
|---|---|---|
| Componentes / C4 | `flowchart LR` com `subgraph` | Partes do sistema e o que conversa com o quê |
| Sequência | `sequenceDiagram` | Um fluxo no tempo, com respostas e chamadas assíncronas |
| Estados | `stateDiagram-v2` | Ciclo de vida de uma entidade ou processamento |
| Dados | `erDiagram` | Tabelas, chaves e relações |
| Modelo de domínio | `classDiagram` com `namespace` | Aggregates, entidades e value objects |
| Decisão | `flowchart TD` com losangos `{}` | Roteamento, triagem, regras de encaminhamento |
| Implantação | `flowchart LR` com `subgraph` por ambiente | Onde cada container roda |
| Branches | `gitGraph` | Modelo de branches no `CONTRIBUTING.md` |

Formas no flowchart: `["processo"]`, `(["ator"])`, `[("banco")]`, `[["fila"]]`, `[/"externo"/]`, `{"decisão"}`.

## Armadilhas que impedem a renderização

- **Palavras reservadas como nome.** Em `sequenceDiagram`, não use `loop`, `alt`, `else`, `opt`, `par`, `and`,
  `critical`, `break`, `rect`, `note`, `end` como nome de participante; use um alias:
  `participant Agente as Loop do agente`. Em `flowchart`, não use `end` (minúsculo) como ID de nó.
- **Encadeamento com `&`** (`A & B --> C`) não renderiza em todas as versões; escreva uma aresta por linha.
- **Rótulos com parênteses, colchetes, chaves, `:` ou `;`** precisam de aspas: `api["API (FastAPI)"]`.
- **Quebra de linha** em rótulo: `<br/>`.
- **IDs** sem espaço nem acento; o texto com acento vai no rótulo.
- **`subgraph`** com ID e título: `subgraph aws["AWS Academy"]`.
- **Tamanho:** mais de ~15 nós vira dois diagramas.

## Como validar

1. Prévia do GitHub (abra o arquivo na branch antes do merge) ou extensão Mermaid do editor.
2. Com Node disponível: `npx -y @mermaid-js/mermaid-cli -i diagrama.mmd -o diagrama.svg` (falha com a linha do erro).
3. Diagrama que não renderiza é bug: corrija no mesmo PR.
