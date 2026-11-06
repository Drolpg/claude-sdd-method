---
name: choosing-architecture
description: Use quando for decidir o estilo de arquitetura de um projeto (código simples, camadas, ports só nas fronteiras, hexagonal, Clean Architecture, núcleo funcional, fatias verticais, monólito modular, DDD leve ou completo), avaliar se um investimento estrutural vale a pena, ou quando um projeto em andamento mostrar sinais de que a arquitetura ficou pequena ou grande demais.
---

# Avaliação de arquitetura

## Visão geral

Arquitetura é investimento: cada camada, port ou aggregate custa tempo agora para economizar depois. Este rito mede o
problema e recomenda o **menor estilo que resolve as fronteiras reais** do projeto, e registra o que não será adotado,
com o porquê. Decidir não usar DDD é tão importante quanto decidir usar.

## Quando rodar

- Sempre, logo depois da fundação: avaliação preliminar, a partir do enunciado.
- De novo ao fechar a especificação ou a descoberta do domínio: confirmação.
- Sempre que um gatilho de reavaliação registrado na decisão disparar.

## Passos

1. **Tipo de projeto.** Identifique-o em `project-archetypes.md`. O tipo traz o estilo de partida, os quality gates
   e os diagramas do README.
2. **Sinais.** Preencha `templates/architecture-assessment.md`, com evidência para cada sinal (trecho do enunciado,
   requisito, fato do negócio): regras e estados, integrações, troca de tecnologia prevista, equipe e paralelismo,
   vida útil, processamento assíncrono, conformidade. Sinal sem evidência conta como baixo.
3. **Fronteiras reais.** Liste cada fronteira (sistema externo, fila, provedor trocável, regra que precisa ser testada
   sem infraestrutura) e diga por que é real.
4. **Recomendação.** Cruze tipo e sinais com `architecture-styles.md`. Para cada elemento estrutural proposto
   (camada, port, módulo, aggregate), aponte o sinal que o justifica. Elemento sem sinal sai. O estilo pode variar por
   módulo (core com DDD, cadastro em camadas).
5. **O que não adotar.** Liste o que fica de fora e por quê ("sem repository: um banco só, acesso pela sessão").
   Essas linhas viram regras no `AGENTS.md`, para nenhum agente "melhorar" a arquitetura por conta própria.
6. **Gatilhos.** Quando subir de nível ("apareceu o segundo provedor de LLM → criar a port") e sinais de excesso
   ("port com uma implementação, sem fake nos testes → remover").
7. **Trilha de domínio:** nenhuma; DDD leve (só glossário, contextos e context map, em
   `sdd-method:designing-strategic-model`); ou DDD completo (`running-domain-discovery`, `designing-strategic-model`,
   `designing-aggregates`).
8. **Registro.** Nível 1: seção "Decisão de arquitetura" do `docs/02-plan.md`. Níveis 2–3: ADR a partir de
   `templates/ADR-architecture-style.md`, `Proposed` até o gate da arquitetura base. Atualize `docs/method.md`.
9. **Gate:** o usuário concorda com o estilo, com o que fica de fora e com os gatilhos.

## Regras

- Abstração só onde há fronteira real.
- Não existe estrutura "por precaução". Preparar o futuro é registrar o gatilho, não construir a estrutura.
- A recomendação segue o problema, não o tamanho: projeto pequeno com regras ricas pode precisar de aggregates; projeto
  grande e CRUD pode não precisar.
- Mudar de estilo no meio do projeto é uma nova decisão, que substitui a anterior.

## Erros comuns

| Erro | Correção |
|---|---|
| Hexagonal completo num CRUD sem integração | Camadas; ports só quando surgir fronteira |
| DDD tático num domínio com uma decisão só | DDD leve ou nenhum, com o porquê registrado |
| Camadas anêmicas num domínio com muitas regras e estados | Aggregates nos pontos de regra |
| Clean Architecture escolhida pelo nome | Escolha pelo problema; ver a comparação em `architecture-styles.md` |
| Decidir e não registrar | Sem registro, o próximo agente "corrige" a arquitetura |
