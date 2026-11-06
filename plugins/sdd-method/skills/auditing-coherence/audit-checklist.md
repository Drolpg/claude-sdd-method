# Pares a auditar

Para cada par: o que comparar e o drift mais comum (visto no projeto de referência).

| Par | Comparar | Drift típico |
|---|---|---|
| ADR no repositório ↔ ADR no board | Status, datas, opções, decisão, referências cruzadas | Board parado numa versão anterior; ADR nova ausente no board |
| RFC no repositório ↔ RFC no board | Número, título, status | Mesmo número para RFCs diferentes; status divergente |
| TD no repositório ↔ TD no board | Existência, status, "Last Updated" | TDs novas só no repositório |
| Registro de requisitos ↔ board ↔ specs ↔ tracker | Todos os IDs citados existem no registro, com o mesmo significado | IDs de fases novas citados sem registro; um ID com dois significados |
| Linguagem ubíqua ↔ board ↔ código | Uma definição por termo; nomes no código | Termo com duas definições na mesma fonte |
| Modelo de domínio (diagrama) ↔ código | Classes, campos, nomes alternativos documentados | Classe renomeada ou aninhada sem nota |
| Canvases e policies ↔ código | Invariantes testadas; policies implementadas | Policy só no desenho |
| Context map ↔ ADR de integração ↔ código | Padrões e contratos vigentes | Seta OHS/REST quando o contrato é in-process |
| C4 e implantação ↔ configuração real | Versões, réplicas, serviços externos, ambientes | Sistema externo sem requisito; versão de banco antiga |
| Riscos técnicos ↔ features implementadas | Status do risco | Risco "pendente" já resolvido |
| Links para o board ↔ board atual | URL e IDs de widget existem | Links para um board antigo ou de outro dono |
| `AGENTS.md`, `CLAUDE.md`, regras de épico ↔ estado real | Afirmações sobre números, status, módulos | "Próximo número livre" desatualizado; decisão citada com status antigo |
| Checklist de entregáveis ↔ artefatos | Cada item com evidência que abre | Item marcado sem evidência |
| Collection e guia de teste manual ↔ contrato gerado | Endpoints, códigos de status, variáveis | Guia desatualizado |
| Branches abertas ↔ `main` | Números de ADR/RFC/TD criados em paralelo | Duas ADRs com o mesmo número em branches diferentes |
| Spec ↔ testes (matriz requisito → teste) | Todo requisito tem teste que existe; todo teste aponta para um requisito | Requisito novo sem teste; teste apagado sem atualizar a matriz |
| Decisão de estilo ↔ código | Elementos estruturais presentes ou ausentes conforme a decisão; gatilhos disparados | Port, repository ou camada criados sem decisão; gatilho disparado sem reavaliação |
| README e diagramas ↔ código e configuração | Componentes, fluxo, estados e dados do README batem com o código; diagramas renderizam | Diagrama de um fluxo que mudou; diagrama quebrado |
| `CONTRIBUTING.md` ↔ histórico do Git | Tipos, escopos, idioma, trailers | Tipos inventados; escopo inconsistente; trailer de IA contra a regra |
