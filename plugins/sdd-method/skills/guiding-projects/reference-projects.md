# Projetos de referência

Use-os para calibrar profundidade e forma, não para copiar decisões de stack. Repositórios em
`https://github.com/Drolpg/<nome>` (alguns privados).

| Projeto | Tipo | Nível · estilo | Exemplo de quê |
|---|---|---|---|
| `anticipation-engine` | Serviço assíncrono (FastAPI, Celery, PostgreSQL) | 1 · camadas | `AGENTS.md` com "não criar hexagonal, repository nem DI"; formato de relatório ao fim de tarefa; constituição; Postman por ambiente |
| `customer_lookup` | Serviço assíncrono com externo instável | 1 · camadas + 2 ports | `ports.py` só com `ClienteExterno` e `PublicadorDeTarefas`; matriz requisito → teste; README com estados, arquitetura e sequência |
| `whatsapp-ai-agent` | Agente de IA (LLM, RAG, WhatsApp, Flex) | 1 · hexagonal | "Decisão de arquitetura: sem DDD" no `plan.md`; troca de provedor de LLM sem tocar o core; fases com critério de aceite; padrão de Git no `CLAUDE.md` |
| `emporio-atendimento-agent` | Agente de IA com regras de loja | 1 · núcleo funcional | Regras de preço, frete e devolução puras e testadas; evals contra o provedor real; README com 4 diagramas e "uso de assistentes de código" |
| plugin Flex para cliente (privado) | Plugin de front-end para cliente (Twilio Flex) | 1 + anexos · núcleo funcional + casca | `docs/sdd/00–07` (plano até entrega na esteira do cliente); evidências neutras com detalhe em `docs/_local/`; teste de desempenho |
| `17SOAT-workshop-management-system` | Sistema de domínio rico, time de 5 | 2 · monólito modular + DDD completo | Todos os ritos de domínio, registro de decisões, SDD por feature, relatório OWASP |

## Workshop Management System — onde está cada rito

- Repositório: https://github.com/Drolpg/17SOAT-workshop-management-system (branch `main`)
- Board (cópia pessoal, privada): https://miro.com/app/board/uXjVEQkpfrw=/ — os frames estão longe da origem do canvas:
  use o painel de frames ou Shift + 1.

| Rito | No board | No repositório |
|---|---|---|
| Fundação | "Enunciados das fases do Tech Challenge" | `AGENTS.md`, `CLAUDE.md`, `docs/README.md` |
| Descoberta | "Domain Storytelling e Event Storming", "Brainstorming", "Ordenação", "Hotspots", "Pivotal Events, Actors, Commands and Policies" | — |
| Estratégico | "DDD Estratégico e tático" (docs 1, 3 e 6); "Context Map" | `docs/Architecture.md`; ADR-005 |
| Tático | "Aggregates and Bounded Contexts", "Service Order", "Stock", "Modelo de domínio"; docs "4. Aggregates" e "5. Detalhes" | `docs/Architecture.md`; `.claude/rules/epic-3-service-lifecycle.md` |
| Requisitos | "Levantamento de Requisitos e Refinamento Técnico" | `docs/backlog.md` |
| Arquitetura | "RFC" (RFC-001), "C4 Model", "Arquitetura Fase 2" | `docs/architecture/overview.md`, `docs/PROJECT-STRUCTURE.md`, ADR-001, ADR-008 |
| Decisões | "ADR", "RFC", "Technical Debt" | `docs/Architecture-Decisions.md` (AD-006), `docs/adr/`, `docs/rfc/`, `docs/tech-debt/` |
| Features | — | `docs/features/servicelifecycle/external-status-update/` |
| Segurança | "Relatório de Vulnerabilidades OWASP" | `docs/security/vulnerability-report.md`, TD-003 |
| Entrega | "Arquitetura Fase 2" | `README.md`, `docs/setup/`, `docs/operations/`, `docs/api/manual-testing.md` |

O que o método corrigiu em relação a esse projeto: requisitos com registro próprio no repositório, domínio e
arquitetura separados em documentos menores, auditoria de coerência por fase e `docs/method.md` como estado do
projeto.
