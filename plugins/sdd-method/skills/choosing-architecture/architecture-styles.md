# Catálogo de estilos

Do mais simples ao mais estruturado. Os estilos se combinam: um monólito modular pode ter DDD no módulo core e
camadas nos módulos de cadastro.

## Resumo

| Estilo | Vale quando | Custo | Exemplo de referência |
|---|---|---|---|
| Código simples | Script, automação, POC de dias | Mínimo | — |
| Camadas | API ou serviço com regras moderadas e poucas integrações | Baixo | `anticipation-engine` |
| Camadas + ports nas fronteiras | 1 a 3 fronteiras externas que precisam de fake ou podem mudar | Baixo | `customer_lookup` |
| Núcleo funcional + casca | Regras puras cercadas por estado, UI ou eventos de uma plataforma | Baixo | plugin Flex para cliente (privado), `emporio-atendimento-agent` |
| Hexagonal | Núcleo de decisão que precisa rodar sem nenhuma tecnologia; várias tecnologias trocáveis | Médio | `whatsapp-ai-agent` |
| Clean Architecture | Muitos casos de uso com fronteiras de entrada/saída explícitas; time que já pratica | Médio-alto | — |
| Fatias verticais | Muitas features independentes, pouca regra compartilhada | Baixo-médio | — |
| Monólito modular | Várias áreas de negócio ou várias pessoas em paralelo | Médio | Workshop (módulos) |
| DDD leve | Vocabulário de negócio rico ou ambíguo, regras simples | Baixo | — |
| DDD completo | Regras e estados ricos, consistência importante, várias áreas, vida longa | Alto | Workshop |

## Heurística por sinais

| Se… | Comece por… |
|---|---|
| Todos os sinais baixos | Código simples ou camadas |
| Integrações médias (precisam de fake determinístico ou têm falha previsível) | Camadas + ports nessas fronteiras |
| Troca de tecnologia alta (LLM, canal, provedor) ou integrações altas | Hexagonal |
| Regras puras dentro de uma plataforma que você não controla (plugin, UI, agente) | Núcleo funcional + casca |
| Equipe ou número de áreas médio/alto | Monólito modular, com o estilo interno decidido por módulo |
| Vocabulário ambíguo e regras baixas | DDD leve |
| Regras e estados altos, e equipe ou vida útil médias/altas | DDD completo no core; o resto pode ficar em camadas |
| Muitas features CRUD independentes | Fatias verticais |

## Estilos em detalhe

### Código simples

- **Estrutura:** um módulo (ou poucos arquivos) + testes.
- **Regras:** funções pequenas; efeitos colaterais nas bordas; configuração por variável de ambiente.
- **Subir quando:** surgir persistência, uma segunda responsabilidade ou uma integração instável.

### Camadas

- **Estrutura:** `api/` (transporte) → `services/` (regras e orquestração) → `models/` e `db/` (persistência);
  `worker/` → `services/` quando houver fila.
- **Regras:** `api` não tem regra de negócio; `services` não importa framework web nem biblioteca de fila; integrações
  são funções simples em `services/`.
- **Não adotar:** ports, repository, interfaces, pasta `adapters/`, container de DI.
- **Subir quando:** uma integração precisar de fake determinístico nos testes, ou tiver falha que exige tratamento
  próprio (retry, classificação de erro) → ports nessa fronteira.

### Camadas + ports nas fronteiras ("hexagonal leve")

- **Estrutura:** camadas + `ports.py` (ou equivalente) com as interfaces das fronteiras reais + `adapters/` só para
  elas. Ex.: `ClienteExterno` e `PublicadorDeTarefas`.
- **Regras:** `services` depende das ports, nunca dos adapters; o adapter traduz erros técnicos em exceções da port.
- **Não adotar:** repository (a sessão do banco basta), container de DI, ports para o que não é fronteira.
- **Subir quando:** a maior parte do núcleo precisar rodar sem infraestrutura, ou as fronteiras passarem de três →
  hexagonal.
- **Excesso:** port com uma implementação, sem fake nos testes e sem troca prevista.

### Núcleo funcional + casca

- **Estrutura:** `rules/` ou `domain/` com funções puras (cálculo, normalização, decisão) + casca com estado, UI,
  eventos ou ferramentas da plataforma. Ex.: `rules/computeBadge.ts` + `store/`, `sync/`, `ui/`.
- **Regras:** as regras não conhecem a plataforma; a casca não decide nada, só traduz e chama. Testes concentrados no
  núcleo; poucos testes de integração na casca.
- **Subir quando:** a casca começar a acumular decisão, ou a plataforma precisar ser trocada → hexagonal.

### Hexagonal (ports & adapters)

- **Estrutura:** `core/` (regras puras + `ports`) · `adapters/` (uma implementação por tecnologia) · composition root
  (`main`) que monta os adapters e injeta no core.
- **Regras:** `core` nunca importa `adapters`; cada port tem ao menos um fake usado nos testes; trocar tecnologia é
  trocar o adapter no composition root.
- **Excesso:** ports para tudo, inclusive o que nunca vai mudar; camada `application/` separada num fluxo pequeno.
- **Subir quando:** surgirem invariantes e estados ricos → aggregates no core (DDD tático).

### Clean Architecture

- **Estrutura:** entities → use cases (com input/output boundaries) → interface adapters (controllers, presenters,
  gateways) → frameworks.
- **Diferença prática para o hexagonal:** a mesma regra de dependência (tudo aponta para dentro); Clean acrescenta uma
  camada explícita de casos de uso e presenters. Prefira hexagonal, que tem menos cerimônia, salvo se o time já pratica
  Clean ou se muitos casos de uso precisam de fronteiras de entrada e saída formais.

### Fatias verticais

- **Estrutura:** uma pasta por feature (handler, validação, acesso a dados, testes); código compartilhado mínimo.
- **Regras:** uma feature não importa outra; o que for comum de verdade sobe para um módulo compartilhado pequeno.
- **Subir quando:** regras começarem a se repetir entre fatias → extrair domínio.

### Monólito modular

- **Estrutura:** um módulo de topo por área de negócio, com API pública e fronteira verificada por ferramenta; dentro
  de cada módulo, o estilo que o módulo precisar.
- **Regras:** módulos conversam por API pública, IDs ou eventos; dependências acíclicas; teste de fronteira no CI.
- **Subir quando:** a extração para serviço tiver motivo operacional real (escala, deploy independente), registrado em
  decisão.

### DDD leve

- **O que entra:** linguagem ubíqua, contextos e context map (`sdd-method:designing-strategic-model` em modo leve).
- **O que não entra:** aggregates formais, value objects por regra, eventos de domínio, policies.
- **Subir quando:** invariantes e estados começarem a se espalhar por services → DDD tático no contexto afetado.

### DDD completo

- **O que entra:** descoberta (Domain Storytelling, Event Storming), desenho estratégico e tático, aggregates com
  invariantes testadas, eventos e policies.
- **Custo:** ritos 3–5 do método (descoberta, estratégico e tático) e disciplina de fronteira em todo o código.
- **Excesso:** contextos supporting e generic modelados com aggregates sem regra que justifique.

## Decisões complementares (não são estilos)

CQRS com read models, event sourcing, mensageria entre módulos e microsserviços são decisões próprias, cada uma com
ADR. O padrão é **não** adotar sem um sinal forte (volume de leitura muito diferente da escrita, auditoria completa de
mudanças, deploy independente necessário).
