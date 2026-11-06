---
name: refining-requirements
description: Use quando, num projeto de nível 2 ou 3, for transformar enunciado, Event Storming e modelo de domínio em requisitos funcionais e não funcionais numerados, quebrar o trabalho em épicos com donos e dependências, fechar casos de borda, definir Definition of Ready e Done, ou registrar requisitos novos de uma nova fase.
---

# Requisitos e épicos (níveis 2–3)

## Visão geral

O registro de requisitos liga enunciado, domínio e features: cada RF tem um ID estável, uma origem rastreável e,
depois, a feature que o implementa.

No nível 1, os requisitos ficam na própria spec (`sdd-method:specifying-projects`), com as mesmas regras de ID desta
skill e a matriz requisito → teste.

## Passos

1. **Atores e papéis**, incluindo papéis técnicos (admin) e sistemas externos.
2. **RF por contexto**, cada um no tamanho de uma ação ou comando: `RF01`, `RF02`…, com origem (entregável `E<n>` do
   enunciado ou evento do Event Storming), contexto e fase (`templates/requirements.md`).
3. **RNF** (`RNF01`…) para restrições de arquitetura, segurança, desempenho, operação e entrega, cada um com a forma de
   verificar.
4. **Casos de borda fechados:** pergunta, decisão, data e quem decidiu. O que não puder ser decidido agora vira AD ou
   RFC.
5. **Riscos técnicos** com status (`Pendente de análise`, `Mitigado`, `Resolvido`, `Adiado`) e referência. Atualize
   quando uma feature resolver o risco.
6. **Épicos** (`templates/epics.md`): faixa de RFs, contextos e aggregates, dono, e mapa de dependências com a
   estratégia para trabalhar em paralelo (que port ou evento mockar e que contrato combinar antes).
7. **DoR e DoD** (`templates/definition-of-ready-done.md`).
8. **Backlog** (`templates/backlog.md`) para o que ficou fora, com motivo e gatilho para retomar.
9. **Gate:** o usuário aprova registro, épicos e DoR/DoD. Com tracker, exporte depois da aprovação (um RF ≈ uma
   história) e anote no registro o ID da história.

## Regras de ID

- O próximo ID é o maior existente + 1. IDs nunca são reutilizados e nunca mudam de significado; requisito descartado
  fica com status `Removido`.
- Requisito novo entra no registro **antes** de ser citado em spec, ADR, board ou tracker.
- O ID vem do registro, nunca do tracker.
- Nova fase continua a numeração; a coluna "Fase" diz de onde o requisito veio.

## Erros comuns

- RF que descreve tela ou tabela em vez de comportamento.
- RF grande demais ("gerenciar ordens de serviço"): quebre por comando.
- Requisito que só existe no board ou no tracker.
- Risco que continua "pendente" depois que a feature o resolveu.
