---
name: designing-aggregates
description: Use quando for definir ou revisar aggregates, entidades, value objects, invariantes, máquinas de estado, status derivado, eventos de domínio e policies, ou desenhar o modelo de domínio (diagrama de classes) de um ou mais bounded contexts.
---

# Desenho tático (trilha DDD completo)

## Visão geral

Cada aggregate é uma fronteira de consistência: protege invariantes numa única transação. O rito transforma os
aggregates candidatos do Event Storming em canvases verificáveis e num modelo de domínio que o código vai obedecer.

Entra quando a avaliação de arquitetura indicou DDD completo, e só nos contextos com regras e estados ricos. Contextos
de cadastro ou genéricos podem ficar em camadas; registre isso na decisão de estilo. Fora dessa trilha, o template de
máquina de estados e a seção de status derivado ainda servem para qualquer entidade com ciclo de vida.

## Passos

1. **Um canvas por aggregate** (`templates/aggregate-canvas.md`): propósito, comandos aceitos, eventos emitidos,
   invariantes, ciclo de vida, referências (só por ID), snapshots, volume e concorrência esperados.
2. **Invariantes testáveis.** Escreva cada uma como regra verificável, com ID (`INV-01`): "uma linha só pode ser
   decidida enquanto o orçamento está `SENT`". Na entrega incremental (rito 8), cada invariante vira teste de domínio.
3. **Máquina de estados** em Mermaid `stateDiagram-v2` para todo aggregate ou entidade com status. Status derivado de
   outros (o status da ordem a partir das execuções) tem uma regra de precedência explícita, escrita num lugar só.
4. **Eventos e policies** em `templates/domain-events.md`: evento → policy → comando → aggregate alvo, indicando se é
   na mesma transação ou com consistência eventual, e o que acontece se falhar.
5. **Value objects** para todo conceito com regra de formação (documento fiscal, placa, dinheiro com moeda).
   Validação na criação; imutáveis.
6. **Casos de borda.** Para cada hotspot ligado a um aggregate, feche a decisão no canvas (pergunta, decisão, data,
   quem decidiu) ou abra AD/RFC.
7. **Modelo de domínio** em Mermaid `classDiagram`, com `namespace` por contexto e estereótipos
   (`templates/domain-model.md`). Antes da implementação ele é o alvo; depois, o código é a fonte e o diagrama é
   auditado contra ele (`sdd-method:auditing-coherence`).
8. **Gate:** o usuário aprova canvases, máquinas de estado e modelo. Atualize `docs/method.md`.

## Regras

- Aggregate pequeno. Referência a outro aggregate só por ID.
- Nada de framework, ORM ou transporte no modelo de domínio.
- Estado muda por métodos com intenção de negócio (`approveLine`, `startExecution`), não por setters.
- Dinheiro com tipo decimal e moeda; nunca ponto flutuante.
- Dado copiado de outro contexto é snapshot com momento de congelamento definido.

## Erros comuns

- Aggregate espelhando tabela ou tela.
- Invariante que depende de dois aggregates na mesma transação: ou é policy com consistência eventual, ou a
  fronteira está errada.
- Status calculado de jeitos diferentes em lugares diferentes: uma regra de precedência, num lugar só.
- Policy desenhada no diagrama e nunca implementada nem registrada como dívida (no projeto de referência, "Estimate
  expirada → finalizar OS" ficou só no desenho e virou TD depois).
