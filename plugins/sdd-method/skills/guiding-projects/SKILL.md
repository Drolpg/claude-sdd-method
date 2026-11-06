---
name: guiding-projects
description: Use quando for iniciar, retomar ou planejar o próximo passo de um projeto de software conduzido com SDD e TDD (com ou sem DDD), em qualquer linguagem, ou quando o usuário perguntar "onde estamos", "qual o próximo passo", "que arquitetura usar" ou "o que falta para a entrega".
---

# Conduzindo projetos com o método

## Visão geral

Todo projeto tem a mesma espinha: **SDD + TDD**, convenção de Git escrita e README com diagramas. O resto é
proporcional ao problema, em dois eixos independentes:

- **Nível de processo** (quanta documentação e quantos gates): 1 Enxuto, 2 Padrão, 3 Completo.
- **Estilo de arquitetura** (quanta estrutura): de código simples a DDD completo, decidido pela avaliação de
  arquitetura. Os ritos de domínio (DDD) só entram quando o estilo pede.

## Ao começar qualquer sessão

1. Leia `docs/method.md`. Se não existir, o projeto não foi iniciado. **REQUIRED SUB-SKILL:** use
   `sdd-method:kicking-off-projects`.
2. Na tabela "Estado dos ritos", localize o primeiro rito pendente que se aplica ao nível e ao estilo do projeto.
3. Diga ao usuário em que ponto o projeto está e qual rito propõe a seguir. Comece só depois que ele confirmar.
4. Ao concluir um rito, atualize a tabela: data, artefatos e quem aprovou.

## Ritos

| # | Rito | Skill | Quando | Gate de saída |
|---|---|---|---|---|
| 0 | Fundação | `kicking-off-projects` | Sempre | Enunciado, tipo de projeto e nível aprovados |
| 1 | Git e colaboração | `defining-git-workflow` | Sempre | `CONTRIBUTING.md` aprovado |
| 2 | Avaliação de arquitetura | `choosing-architecture` | Sempre (preliminar e confirmação) | Estilo, o que não adotar e gatilhos aceitos |
| 3 | Descoberta do domínio | `running-domain-discovery` | DDD completo | Event Storming revisado |
| 4 | Desenho estratégico | `designing-strategic-model` | DDD leve ou completo | Contextos e glossário aprovados |
| 5 | Desenho tático | `designing-aggregates` | DDD completo | Aggregates e modelo aprovados |
| 6 | Especificação | `specifying-projects` (nível 1) · `refining-requirements` (níveis 2–3) | Sempre | Spec ou registro de requisitos aprovado |
| 7 | Arquitetura base | `establishing-architecture` | Sempre | Estrutura do estilo, regras de dependência e CI verdes |
| 8 | Entrega incremental | `driving-with-tests` (+ `specifying-features` nos níveis 2–3) | Contínuo | Definition of Done |
| ∞ | Decisões | `recording-decisions` | Sempre que houver escolha | Uma pessoa aceita |
| ∞ | Segurança | `reviewing-security` | Toda tarefa/feature e fim de fase | Nenhum achado crítico ou alto aberto |
| ∞ | Documentação e entrega | `documenting-delivery` | Ao mudar uso, arquitetura ou entregável | README e entregáveis com evidência |
| ∞ | Auditoria de coerência | `auditing-coherence` | Fim de fase, antes de entregar | Divergências resolvidas ou registradas |

Níveis, estilos, combinações típicas e layout de documentos: `method-map.md`. Regras válidas em todos os ritos:
`principles.md`. Projetos reais que exemplificam cada combinação: `reference-projects.md`.

## Regras que valem sempre

- O agente nunca aprova nada. Aprovação é explícita, de uma pessoa, registrada com nome e data.
- A spec manda no código; o teste é o critério de aceite. Divergência: pare e registre.
- Nenhuma estrutura sem motivo registrado; decidir não adotar também é decisão.
- Não invente conteúdo de board, tracker ou enunciado. Sem acesso, diga isso e peça o trecho.
- Rito pulado ou simplificado só por decisão registrada em `docs/method.md`.
- Novo enunciado (nova fase) reabre fundação, avaliação de arquitetura e especificação em modo delta.

## Erros comuns

| Erro | Correção |
|---|---|
| DDD completo num projeto com uma decisão de negócio | A avaliação de arquitetura decide; DDD é uma trilha, não o padrão |
| Pular a avaliação "porque é pequeno" | Ela é curta justamente para registrar o que não adotar |
| Escolher stack e pastas antes da spec | Stack e estrutura são o rito 7 |
| Auditar só depois da entrega | Auditoria curta no fim de cada fase |
