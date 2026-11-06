# Mapa do método

## Eixo 1 — Nível de processo

| | 1 — Enxuto | 2 — Padrão | 3 — Completo |
|---|---|---|---|
| Para | Solo ou dupla, POC, desafio técnico, entrega a cliente de escopo fechado | Grupo, projeto acadêmico em fases, MVP | Produto contínuo, time maior, domínio regulado |
| SDD | De projeto: constituição → spec → plano → tarefas (`specifying-projects`) | Por feature, com gates (`refining-requirements` + `specifying-features`) | Igual ao 2 + regras por épico |
| Decisões | Tabelas no plano (decisões e débitos) | Registro AD + ADR, RFC e TD em arquivos | Igual ao 2 |
| Segurança | Checklist por tarefa | Checklist por feature + relatório por fase | + threat model (STRIDE) |
| Documentação | README completo; anexos de entrega se houver cliente | + índice Diátaxis, guias de setup e operação | + runbooks, SLOs, changelog |
| Auditoria | No fim, antes de entregar | No fim de cada fase | A cada merge relevante |

Sempre, em qualquer nível: TDD, `CONTRIBUTING.md`, README com diagramas Mermaid, avaliação de arquitetura.

## Eixo 2 — Estilo de arquitetura

Decidido em `choosing-architecture` (catálogo em `architecture-styles.md`). O estilo define quais ritos de domínio
entram:

| Estilo | Ritos de domínio |
|---|---|
| Código simples, camadas, camadas + ports, núcleo funcional, hexagonal, Clean, fatias verticais | Nenhum (glossário curto na spec) |
| Monólito modular sem DDD | Nenhum; contextos definidos como módulos na avaliação |
| DDD leve | `designing-strategic-model` em modo leve (glossário, contextos, context map) |
| DDD completo | `running-domain-discovery`, `designing-strategic-model`, `designing-aggregates` |

## Combinações típicas

| Projeto de referência | Nível | Estilo |
|---|---|---|
| `anticipation-engine` | 1 | Camadas |
| `customer_lookup` | 1 | Camadas + ports nas fronteiras |
| `whatsapp-ai-agent` | 1 | Hexagonal, sem DDD (decisão registrada) |
| `emporio-atendimento-agent` | 1 | Núcleo funcional (regras e ferramentas) + evals |
| plugin Flex para cliente (privado) | 1 + anexos de entrega | Núcleo funcional + casca |
| Workshop Management System | 2 (com elementos do 3) | Monólito modular + DDD completo |

## Situações

Combine as que se aplicarem e registre-as no `docs/method.md`.

| Situação | Ajuste |
|---|---|
| Solo | Aprovador é o próprio usuário, explícito. Event Storming vira entrevista guiada. PR com checklist de auto-revisão. |
| Time | Papéis e donos no `docs/method.md`; decisão que cruza donos é do time; PR com revisão. |
| Entrega para cliente | Anexos: plano de testes, evidências, release e rollback; ambientes nomeados; nada de dados reais sem avisar. |
| Agente de IA | Evals contra o provedor real como quality gate; regras de negócio fora do prompt. |
| Com board (Miro com MCP) | Workshops em frames; o repositório guarda a versão textual e é a fonte da verdade. |
| Com tracker | Um requisito ≈ uma história; o ID vem da spec ou do registro, nunca do tracker. |
| Brownfield | Comece por `auditing-coherence`; reconstrua a decisão de arquitetura a partir do código; depois siga o nível escolhido. |
| Sessões separadas (planejamento × implementação) | Prompt autocontido por tarefa em `03-tasks.md`; a sessão de implementação para no checkpoint. |
| Projeto em fases | Cada novo enunciado: `docs/challenge/phase-<n>.md` e delta na avaliação e na especificação. |

## Ritos em detalhe

| # | Rito | Entradas | Saídas |
|---|---|---|---|
| 0 | Fundação | Enunciado, prazo, equipe | `docs/method.md`, `docs/challenge/phase-<n>.md`, constituição (nível 1) ou charter (níveis 2–3), `AGENTS.md`, `CLAUDE.md`, `.gitignore` com `docs/_local/` |
| 1 | Git e colaboração | Tamanho do time, preferências | `CONTRIBUTING.md`, `.github/pull_request_template.md` |
| 2 | Avaliação de arquitetura | Enunciado, tipo de projeto (depois a spec) | Avaliação; decisão de estilo (plano ou ADR); regras "não adotar" no `AGENTS.md` |
| 3–5 | Domínio (se o estilo pedir) | Conhecimento do negócio | `docs/domain/` |
| 6 | Especificação | Enunciado, domínio | Nível 1: `docs/01-spec.md` → `02-plan.md` → `03-tasks.md`. Níveis 2–3: `docs/requirements/` |
| 7 | Arquitetura base | Decisão de estilo, stack | Estrutura de pastas, perfil de stack, teste de regras de dependência, CI, diagramas |
| 8 | Entrega incremental | Tarefa ou feature aprovada | Testes → código → commit por ciclo verde; matriz requisito → teste; relatório de tarefa |

## Layout de documentos

Nível 1:

```text
AGENTS.md  CLAUDE.md  CONTRIBUTING.md  README.md
docs/
  method.md
  challenge/phase-1.md
  00-constitution.md  01-spec.md  02-plan.md  03-tasks.md
  04-test-plan.md  05-evidence.md  06-release.md     (entrega para cliente)
  _local/                                            (fora do git)
evals/                                               (agentes de IA)
```

Níveis 2–3:

```text
AGENTS.md  CLAUDE.md  CONTRIBUTING.md  README.md
docs/
  method.md  README.md  project-charter.md  decision-register.md
  challenge/  domain/  requirements/  architecture/
  adr/  rfc/  tech-debt/  features/{_template/,<context>/<slug>/}
  security/  api/  setup/  operations/  learning/  audits/  _local/
.claude/rules/epic-<n>-<context>.md
```

Os caminhos podem mudar por projeto; o que vale é a tabela "Mapa de artefatos" do `docs/method.md`.
