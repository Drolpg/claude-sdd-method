---
name: designing-strategic-model
description: Use quando for dividir um domínio em subdomínios e bounded contexts, desenhar ou revisar um context map, definir como os contextos se integram, ou consolidar a linguagem ubíqua (glossário, nomes definitivos, termos em conflito entre fontes).
---

# Desenho estratégico (trilhas DDD leve e DDD completo)

## Visão geral

Decide onde ficam as fronteiras de modelo e de linguagem e como os contextos conversam. É o rito que mais protege o
projeto de acoplamento acidental, e o que menos depende da stack.

## Modo leve (DDD leve)

Quando a avaliação de arquitetura indicou DDD leve, faça só os passos 3, 4 e 6: contextos (canvas resumido: propósito,
termos-chave, entrada e saída), context map e linguagem ubíqua. Sem princípios de aggregate, sem RFC de integração se
o projeto for de um módulo só. No nível 1, o glossário vai para a seção "Glossário" da spec.

No modo completo, siga todos os passos abaixo.

## Passos

1. **Domínio e subdomínios.** Nomeie o domínio e classifique os subdomínios em core, supporting e generic. Escreva o
   diferencial do core numa frase e as consequências de modelagem dele ("a execução de serviço é rica de propósito:
   a granularidade do status é o produto").
2. **Princípios de fronteira** que valem para todos os aggregates. Ponto de partida: uma transação altera um
   aggregate; referência entre aggregates só por ID; coordenação entre fronteiras por policy que reage a evento; dado
   de outro contexto entra como snapshot no momento do registro.
3. **Bounded contexts.** Proponha a partir dos eventos pivotais, das raias e das mudanças de vocabulário do Event
   Storming. Preencha um canvas por contexto (`templates/strategic-design.md`). Contexto, subdomínio e módulo são
   coisas diferentes: registre o mapeamento entre eles.
4. **Context map.** Para cada relação, defina direção (upstream/downstream) e padrão (`context-map-patterns.md`).
   Desenhe em Mermaid (`templates/context-map.md`).
5. **Contrato de integração.** Como as relações se materializam (chamada in-process por port do consumidor, eventos,
   HTTP, mensageria) é decisão de arquitetura: abra RFC ou ADR com `sdd-method:recording-decisions`.
6. **Linguagem ubíqua** em `templates/ubiquitous-language.md`: termo, definição, contexto, nome no código e termos que
   não devem ser usados. Registre as decisões de nomenclatura com o porquê ("Stock, não Inventory").
7. **Gate:** o usuário aprova contexts, context map e glossário. Preencha a seção "Bounded contexts" do `AGENTS.md`,
   espelhe no board se houver e atualize `docs/method.md`.

## Regras

- Um termo, uma definição por contexto. Conflito entre fontes vira entrada no registro de decisões, não duas linhas
  no glossário.
- O que não é bounded context também é registrado, com o lugar onde vive ("Notification é efeito outbound do módulo
  consumidor").
- Comece com poucos contextos. Dividir depois é mais barato do que fundir.
- Restrição de entrega (ex.: monólito) muda a materialização, não o desenho: os contextos continuam existindo como
  módulos.

## Erros comuns

- Um contexto por entidade ("Customer Context", "Vehicle Context").
- Seta de context map sem padrão: "conversa com" não é padrão.
- Linguagem ubíqua que só traduz o código. Ela nasce do negócio e o código obedece.
- Contexto definido pela estrutura do time e não pelo domínio, sem registrar isso como decisão.
