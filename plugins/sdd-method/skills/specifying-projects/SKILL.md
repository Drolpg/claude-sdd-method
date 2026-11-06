---
name: specifying-projects
description: Use quando um projeto pequeno ou médio (nível 1 do método) for especificado como um todo — constituição, spec, plano e tarefas —, quando uma mudança de comportamento precisar entrar na spec antes do código, ou quando o código divergir da spec.
---

# SDD de projeto (nível 1)

## Visão geral

Quatro documentos, escritos em ordem e revisados antes do código, são a fonte da verdade do projeto. **A spec manda
no código**: comportamento novo ou alterado entra primeiro na spec, depois no teste, depois no código.

| Documento | Responde | Template |
|---|---|---|
| `docs/00-constitution.md` | Princípios que valem para todas as decisões | `templates/00-constitution.md` |
| `docs/01-spec.md` | O quê e por quê: requisitos, contrato, erros, matriz requisito → teste | `templates/01-spec.md` |
| `docs/02-plan.md` | Como: arquitetura, decisões, testes, débitos | `templates/02-plan.md` |
| `docs/03-tasks.md` | Em que ordem: tarefas com critério de aceite, status, pendências | `templates/03-tasks.md` |

## Gates

1. Constituição e spec: escreva, revise com o usuário e só siga com a **spec aprovada** (registre nome e data).
2. Plano: a seção "Decisão de arquitetura" vem de `sdd-method:choosing-architecture`. Siga com o **plano aprovado**.
3. Tarefas: pequenas, ordenadas, cada uma com requisitos atendidos e critério de aceite verificável.
4. Execução: **uma tarefa por vez**, com `sdd-method:driving-with-tests`. Ao fim de cada tarefa, atualize status,
   evidência e a matriz requisito → teste.

## Regras

- Mudou o comportamento? Spec primeiro, depois teste, depois código.
- Divergência entre código e spec: pare, registre em `03-tasks.md` › "Pendências abertas" e siga para a próxima tarefa
  que não dependa dela. Nunca "conserte" a spec ou o teste em silêncio.
- Todo requisito tem pelo menos um teste, e todo teste aponta para um requisito (matriz na spec).
- Decisões pequenas e débitos intencionais ficam em tabelas no plano; viram ADR ou TD em arquivo só quando cruzarem
  módulos, forem revisitadas ou o projeto subir de nível (`sdd-method:recording-decisions`).
- Histórico bruto (idas e vindas, depuração, diário) vai para `docs/_local/`, fora do git. O que virar conhecimento
  permanente é promovido para os quatro documentos ou para o README.

## Fases ou marcos

Agrupe tarefas em fases (`Fase 1 — núcleo`) ou marcos (`M0`, `M1`) que terminam num **checkpoint**: o critério de
aceite da fase cumprido e verificado antes da próxima. Merge para a branch de integração só depois do checkpoint.

## Sessões separadas (opcional)

Quando uma sessão planeja e revisa e outra implementa, a de planejamento escreve, no fim da tarefa em `03-tasks.md`,
um prompt autocontido (seção "Prompt de implementação"). A sessão que implementa segue só aquele escopo e para no
checkpoint.

## Entrega para cliente

Projetos entregues a terceiros acrescentam anexos: plano de testes (`sdd-method:driving-with-tests`), evidências,
release e rollback (`sdd-method:documenting-delivery`).

## Erros comuns

- Plano escrito antes de a spec estar aprovada.
- Tarefa sem requisito nem critério de aceite.
- Spec que não muda quando o comportamento muda (a matriz denuncia).
- Constituição genérica: os princípios devem nascer dos riscos deste projeto (ex.: "nenhuma transação aberta durante
  chamada de rede").
