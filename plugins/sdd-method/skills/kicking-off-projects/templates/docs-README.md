# Documentação

Índice de toda a documentação, organizado por quem está lendo. Cada documento responde a uma pergunta; se duas páginas
parecerem dizer a mesma coisa, a mais específica é a fonte da verdade e a outra só aponta para ela.

## Para avaliar o projeto

| Documento | Responde |
|---|---|
| [Charter](project-charter.md) | Que problema o projeto resolve e como saberemos que deu certo |
| [Visão geral da arquitetura](architecture/overview.md) | Como o sistema é dividido e onde ele roda |
| [Domínio](domain/) | Subdomínios, bounded contexts, context map, aggregates e linguagem ubíqua |
| [Requisitos](requirements/requirements.md) | O que o sistema faz, com IDs rastreáveis |
| [Decisões arquiteturais](adr/) | Por que cada escolha estrutural foi feita |
| [Segurança](security/) | Achados de segurança e o tratamento de cada um |

## Para rodar o sistema

| Documento | Tipo | Responde |
|---|---|---|
| `<setup/local.md>` | Tutorial | Como subir o sistema localmente |
| `<setup/configuration.md>` | Referência | Que variáveis existem e de onde vem cada valor |

## Para consumir a API

| Documento | Responde |
|---|---|
| `<api/README.md>` | Autenticação e recursos disponíveis |
| `<api/manual-testing.md>` | Como executar o fluxo completo manualmente |

## Para contribuir

| Documento | Responde |
|---|---|
| [AGENTS.md](../AGENTS.md) | Regras do projeto: arquitetura, SDD, testes, segurança, Git |
| [Método](method.md) | Nível, estado dos ritos e mapa de artefatos |
| [Features](features/README.md) | O fluxo SDD e as specs de cada feature |
| [Registro de decisões](decision-register.md) | Decisões em aberto e resolvidas (AD-NNN) |
| [RFCs](rfc/) | Propostas discutidas antes da implementação |
| [Dívida técnica](tech-debt/) | Desvios conhecidos, com motivo e encaminhamento |
| [Backlog](requirements/backlog.md) | Ideias deixadas fora do escopo atual |

## Como manter esta documentação

- **Um documento, uma pergunta.** Conteúdo novo entra no documento cuja pergunta ele responde; se nenhum servir, crie
  um arquivo novo e adicione uma linha aqui.
- **Apontar em vez de copiar.** O contrato da API é o gerado pela aplicação; variáveis vivem no documento de
  configuração; decisões vivem nas ADRs.
- **Comandos testados.** Todo comando de um guia foi executado; registre a saída esperada e como verificar.
- **Idioma:** texto em pt-BR; nomes de código, arquivos, endpoints e status na forma original.
