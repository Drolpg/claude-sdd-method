# Método do projeto

> Lido pelo Claude no início de cada sessão (`sdd-method:guiding-projects`). Mantenha atualizado: é o estado do
> projeto.

## Configuração

| Campo | Valor |
|---|---|
| Projeto | `<nome>` |
| Tipo de projeto | `<API síncrona · serviço assíncrono · integração · agente de IA · plugin/front-end · domínio rico · script/ETL>` |
| Nível de processo | `<1 — Enxuto · 2 — Padrão · 3 — Completo>` |
| Estilo de arquitetura | Definido no rito 2 — `<estilo>` (`<link da decisão>`) |
| Trilha de domínio | `<nenhuma · DDD leve · DDD completo>` |
| Situações | `<solo · time>`, `<entrega para cliente>`, `<com board · sem board>`, `<com tracker>`, `<brownfield>`, `<em fases>` |
| Idioma da documentação | pt-BR |
| Idioma dos nomes no código | `<domínio na língua do negócio, infraestrutura em inglês · tudo em inglês>` |
| Stack | Definida no rito 7 — `<resumo ou link do perfil>` |
| Comando de verificação completa | `<ex.: make verify · uv run pytest && uv run ruff check .>` |
| Meta de cobertura | `<80%>` |
| Git | `CONTRIBUTING.md` — modelo `<só main · main + dev · main + dev com PR>` |
| Board / tracker | `<URL ou "não usa">` |
| Aprovado por / em | `<nome>` / `<AAAA-MM-DD>` |

## Equipe

| Pessoa | Papel | Escopo | Aprova |
|---|---|---|---|

## Mapa de artefatos

| Artefato | Caminho |
|---|---|
| Enunciados e entregáveis | `docs/challenge/` |
| Constituição (nível 1) / charter (níveis 2–3) | `docs/00-constitution.md` / `docs/project-charter.md` |
| Avaliação e decisão de arquitetura | `<docs/02-plan.md § 1 · docs/adr/ADR-NNN-…>` |
| Spec / requisitos | `<docs/01-spec.md · docs/requirements/>` |
| Plano e tarefas | `<docs/02-plan.md, docs/03-tasks.md · docs/features/>` |
| Domínio (se houver) | `docs/domain/` |
| Decisões e débitos | `<tabelas no plano · docs/decision-register.md, docs/adr/, docs/rfc/, docs/tech-debt/>` |
| Testes e evals | `tests/`, `<evals/>` |
| Anexos de entrega (se houver) | `docs/04-test-plan.md`, `docs/05-evidence.md`, `docs/06-release.md` |
| Notas fora do git | `docs/_local/` |

## Estado dos ritos

| # | Rito | Aplica-se? | Status | Concluído em | Aprovado por | Artefatos |
|---|---|---|---|---|---|---|
| 0 | Fundação | Sim | Pendente | | | |
| 1 | Git e colaboração | Sim | Pendente | | | `CONTRIBUTING.md` |
| 2 | Avaliação de arquitetura | Sim | Pendente | | | |
| 3 | Descoberta do domínio | `<só DDD completo>` | | | | |
| 4 | Desenho estratégico | `<DDD leve ou completo>` | | | | |
| 5 | Desenho tático | `<só DDD completo>` | | | | |
| 6 | Especificação | Sim | Pendente | | | |
| 7 | Arquitetura base | Sim | Pendente | | | |
| 8 | Entrega incremental | Contínuo | — | | | |

Status: `Pendente`, `Em andamento`, `Concluído`, `Não se aplica (estilo)`, `Simplificado (<motivo>)`,
`Pulado (<motivo>)`.

## Fases

| Fase | Enunciado | Entrega | Status | Auditoria |
|---|---|---|---|---|
| 1 | `docs/challenge/phase-1.md` | `<AAAA-MM-DD>` | Em andamento | — |

## Índice do board

Links para o board seguem sempre `<URL do board>/?moveToWidget=<ID>`; trocar de board é um único replace.

| Frame | ID | Espelha | Tipo |
|---|---|---|---|

## Desvios do método

| Data | Desvio | Motivo | Aprovado por |
|---|---|---|---|
