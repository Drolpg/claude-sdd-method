---
name: specifying-features
description: Use quando, num projeto de nível 2 ou 3, for começar, continuar, revisar ou concluir uma feature não trivial — escrever functional-spec, technical-spec ou implementation-plan, registrar uma aprovação, ajustar uma spec já aprovada, ou decidir se uma feature pode ser marcada como implementada.
---

# SDD por feature (níveis 2–3)

## Visão geral

Comportamento é aprovado antes do desenho, e desenho antes do código. O gate humano entre os documentos é o que dá
profundidade: cada documento é escrito sobre uma base já aprovada.

## Antes de começar

1. Identifique contexto, épico e RFs. RF que não está no registro → registre antes
   (`sdd-method:refining-requirements`).
2. Leia as regras do épico (`.claude/rules/epic-<n>-<context>.md`), se existirem, e reconfira no registro e nas ADRs
   o status das decisões citadas: ele pode ter mudado.
3. Confirme o slug com o usuário e copie `templates/` para `docs/features/<context>/<slug>/` (`platform` para
   mudanças transversais).

## Gates

1. Escreva **só** `functional-spec.md`: problema, atores e cenários, regras, fora de escopo, critérios de aceite
   verificáveis. Pare e peça aprovação explícita.
2. Com a funcional `Approved` (nome e data registrados), escreva `technical-spec.md`: impacto nos contextos,
   contratos, eventos, persistência e classificação dos dados, falhas e códigos de erro, segurança, estratégia de
   testes. Pare e peça aprovação.
3. Com a técnica `Approved`, escreva `implementation-plan.md`: checkpoints ordenados, cada um com o que muda, os
   testes e a evidência esperada; checkpoint de segurança; rollback.
4. Implemente checkpoint a checkpoint com `sdd-method:driving-with-tests` (testes de aceite antes do código), registrando
   evidências (comando, resultado, data) e mantendo o status do plano.
5. Marque `Implemented` só quando a Definition of Done do plano estiver completa.

Status permitidos: `Draft`, `Approved`, `In Progress`, `Implemented`.

No nível 1 não se usa spec por feature: o projeto inteiro é especificado com `sdd-method:specifying-projects`.

## Regras

- O agente nunca marca `Approved` nem infere aprovação de frases vagas ("parece bom", "ok, segue"). Pergunte:
  "Posso registrar a spec como aprovada por você hoje?".
- Mudança material numa spec aprovada a devolve a `Draft`; documentos seguintes ficam obsoletos até nova aprovação.
- Ajuste pontual numa spec aprovada, sem reabri-la → **adendo numerado** no fim da spec, com aprovação própria. O
  plano trata o adendo como checkpoint bloqueante.
- Dados persistidos são classificados como: nenhum seed, referência obrigatória, demonstração local ou fixture de
  teste.
- Contrato mudou → atualize na mesma feature o contrato gerado, a collection de testes e o guia de teste manual.
- Ao implementar, atualize o registro de requisitos (status e feature) e os riscos resolvidos.
- Mudança pequena (typo, documentação) pode usar um plano curto, mas passa pelas mesmas verificações.

## Regras por épico

Quando um épico acumula decisões em aberto ou invariantes que as specs repetem, crie
`.claude/rules/epic-<n>-<context>.md` a partir de `templates/epic-rules.md`. O arquivo lista fatos implementados e
decisões em aberto, e não repete o `AGENTS.md`.

## Erros comuns

- Escrever a technical-spec "para adiantar" antes da aprovação funcional.
- Critério de aceite que não dá para testar.
- Plano sem evidência: checkbox marcado não é prova.
- Marcar `Implemented` com achado de segurança alto aberto ou com o guia manual desatualizado.
