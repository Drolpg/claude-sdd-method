---
name: kicking-off-projects
description: Use quando um projeto de software novo for começar e só existir o enunciado, um briefing ou uma pasta vazia; quando chegar o enunciado de uma nova fase; ou ao adotar o método num projeto existente que ainda não tem `docs/method.md`.
---

# Fundação do projeto (rito 0)

## Visão geral

Antes de qualquer modelo ou código, fixe o que o projeto precisa entregar, como o trabalho vai acontecer e quanto de
processo ele merece. Tudo isso fica em `docs/method.md`, que os outros ritos leem.

## Passos

1. **Guarde o enunciado literal** em `docs/challenge/phase-<n>.md` (`templates/challenge-phase.md`) e extraia a
   checklist de entregáveis, cada item com ID (`E1`, `E2`…) e a evidência esperada. Restrições técnicas do enunciado
   ("monólito", "justificar o banco") viram itens a decidir, não decisões.
2. **Pergunte uma coisa por vez**, só o que o enunciado não diz: prazo, quem trabalha e quem aprova, se é entrega
   para cliente, board e tracker, idioma da documentação (padrão pt-BR), idioma dos nomes de domínio no código (padrão:
   o do negócio para domínio, inglês para infraestrutura), se a stack já é imposta.
3. **Tipo de projeto e nível.** Proponha o tipo (`sdd-method:choosing-architecture` › `project-archetypes.md`) e o
   nível de processo (`sdd-method:guiding-projects` › `method-map.md`). O usuário escolhe.
4. **Crie a fundação** a partir de `templates/`:
   - `docs/method.md`: configuração, mapa de artefatos, estado dos ritos;
   - nível 1: `docs/00-constitution.md` (template de `sdd-method:specifying-projects`); níveis 2–3:
     `docs/project-charter.md`, `docs/README.md`, registro de decisões e pastas de ADR, RFC e TD;
   - `AGENTS.md` e `CLAUDE.md`: as seções `STYLE` e `STACK` ficam marcadas até os ritos 2 e 7;
   - `.gitignore` com `docs/_local/`.
5. **Git:** **REQUIRED SUB-SKILL:** `sdd-method:defining-git-workflow` gera `CONTRIBUTING.md` e o template de PR.
6. **Registre as escolhas em aberto** (ex.: "escolher e justificar o banco") na tabela de decisões do plano (nível 1)
   ou no registro de decisões (níveis 2–3).
7. **Board, se houver:** proponha os frames de `templates/board-layout.md` e registre URL e IDs no `docs/method.md`.
8. **Gate:** o usuário aprova enunciado, tipo, nível e situações. Registre nome e data e siga para
   `sdd-method:choosing-architecture`.

## Nova fase

Crie `docs/challenge/phase-<n>.md` e liste o delta: novos entregáveis, requisitos novos (continuando a numeração),
mudanças de arquitetura. Rode a avaliação de arquitetura de novo antes de especificar.

## Projeto existente

Gere a fundação sem sobrescrever nada: se `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md` ou `README.md` já existirem,
proponha um diff e espere aprovação. Em seguida rode `sdd-method:auditing-coherence`.

## Erros comuns

- Escolher stack ou estilo aqui. Registre só as restrições; a escolha vem nos ritos 2 e 7.
- Parafrasear o enunciado. Guarde o texto literal; a interpretação vai para a spec ou o charter.
- Nível 2 por hábito num projeto solo de duas semanas.
- Fazer todas as perguntas de uma vez. Uma por mensagem, só o que falta.
