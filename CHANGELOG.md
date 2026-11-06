# Changelog

Formato: [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/); versões em [SemVer](https://semver.org/lang/pt-BR/).

## [0.2.1] — 2026-11-06

### Mudado

- README: instruções de instalação em outras máquinas e no WSL, acesso a repositório privado, atualização e remoção,
  plugin ligado a um projeto por `.claude/settings.json` e instalação a partir de cópia local.
- Referência a um repositório privado de cliente trocada por uma descrição genérica nos exemplos.

## [0.2.0] — 2026-11-06

O método deixa de ser centrado em DDD: a espinha passa a ser SDD + TDD, e a arquitetura é escolhida por avaliação,
proporcional ao problema. Baseado nos projetos `anticipation-engine`, `customer_lookup`, `whatsapp-ai-agent`,
`emporio-atendimento-agent` e um plugin Twilio Flex entregue a um cliente (repositório privado).

### Mudado

- Plugin renomeado de `ddd-method` para `sdd-method`; pasta do repositório para `claude-sdd-method`; skill de entrada
  de `guiding-ddd-projects` para `guiding-projects`.
- Dois eixos independentes: nível de processo (1 Enxuto, 2 Padrão, 3 Completo) e estilo de arquitetura. Os ritos de
  DDD viraram trilhas (DDD leve e DDD completo), ativadas pela avaliação de arquitetura.
- `kicking-off-projects`: tipo de projeto, idioma dos nomes de domínio, constituição no nível 1, `docs/_local/` fora
  do git e Git definido sempre na fundação.
- `AGENTS.md` (template): regras de arquitetura vindas do estilo escolhido, seção "Do not add", TDD e formato de
  relatório ao fim de tarefa.
- `establishing-architecture`: materializa o estilo decidido; regras de dependência automatizadas mesmo em camadas.
- `documenting-delivery`: README padrão com diagramas Mermaid obrigatórios por tipo de projeto, armadilhas de
  renderização e anexos de entrega para cliente (evidências, release e rollback).
- `recording-decisions`: modo enxuto (tabelas de decisões e débitos no plano) com regra de promoção para ADR.
- `architecture-reviewer`: aponta também excesso e falta de estrutura em relação ao estilo decidido.
- Princípios: proporcionalidade ("abstração só onde há fronteira real", "decidir não adotar também é decisão").

### Adicionado

- `choosing-architecture`: avaliação por sinais, catálogo de 10 estilos com quando vale, custo, gatilhos para subir e
  sinais de excesso; tipos de projeto (API, serviço assíncrono, integração, agente de IA, plugin/front-end, domínio
  rico, script/ETL); template de ADR de estilo.
- `specifying-projects`: SDD de projeto (constituição, spec com matriz requisito → teste, plano, tarefas com
  checkpoints, pendências abertas e prompt para sessão de implementação).
- `driving-with-tests`: ciclo RED → GREEN → REFACTOR, um ciclo verde por commit, camadas de teste, plano de testes,
  guia de evals contra o provedor real para agentes de IA, relatório de tarefa.
- `defining-git-workflow`: modelos de branch, Conventional Commits com lista fechada de tipos, sem trailers de IA por
  padrão, `CONTRIBUTING.md` e templates de PR para time e para auto-revisão solo.
- Perfis de stack: linhas de lockfile, checagem de tipos e evals.
- Auditoria: pares spec ↔ testes, decisão de estilo ↔ código, README ↔ código e `CONTRIBUTING.md` ↔ histórico do Git.

### Removido

- Template de PR de `documenting-delivery` (movido para `defining-git-workflow`).

## [0.1.0] — 2026-11-06

### Adicionado

- Plugin `ddd-method` com 12 skills (guia de entrada; ritos 0 a 6; decisões, segurança, entrega e auditoria de
  coerência) e o agente `architecture-reviewer`.
- Templates extraídos do Workshop Management System e generalizados para qualquer linguagem.
- Perfis de stack iniciais: Java/Spring, TypeScript/Node, Python, Go e C#/.NET.
- Scripts da auditoria de coerência: `doc_diff.py`, `extract_miro_docs.py` e `model_vs_code.py`.
- Princípios de coerência derivados da auditoria do projeto de referência.
