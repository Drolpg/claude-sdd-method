# Tipos de projeto

| Tipo | Exemplos de referência | Estilo de partida | Riscos típicos | Quality gates essenciais | Diagramas do README |
|---|---|---|---|---|---|
| API síncrona | — | Camadas | Regra vazando para o controller; contrato sem versionamento | Testes de contrato HTTP, erros com código estável, contrato gerado | Arquitetura, sequência do fluxo principal, dados |
| Serviço assíncrono (fila + worker) | `customer_lookup`, `anticipation-engine` | Camadas + ports na fila e no externo | Processamento duplicado, transação aberta durante chamada de rede, retry sem limite | Idempotência testada, retry com backoff e limite, teste ponta a ponta com containers, logs com ID de correlação | Arquitetura, sequência API → fila → worker → externo, estados do processamento |
| Integração / ACL / BFF | — | Camadas + ports | Modelo externo vazando para o domínio; timeouts ausentes | Fake determinístico do externo, timeout explícito, mapeamento de erros externos | Componentes, sequência com o externo |
| Agente de IA (LLM, ferramentas, RAG) | `emporio-atendimento-agent`, `whatsapp-ai-agent` | Núcleo funcional (regras e ferramentas) + port do provedor; hexagonal se o provedor ou o canal forem trocáveis | Modelo inventando valor ou prazo; custo e limite de taxa; regressão de comportamento sem quebra de teste | Testes com LLM falso para o encanamento, **evals contra o provedor real** para o comportamento, limites de custo | Componentes, sequência de uma mensagem com ferramenta, fluxo de decisão, dados |
| Plugin ou front-end embutido | plugin Flex para cliente (privado) | Núcleo funcional + casca | Quebrar a plataforma ou outros plugins; degradar desempenho | Testes das regras puras, teste de desempenho, configuração por ambiente, rollback documentado | Componentes, sequência de eventos da plataforma, estados da UI |
| Sistema de domínio rico | Workshop | Monólito modular + DDD completo no core | Acoplamento entre áreas; status inconsistente | Invariantes testadas, teste de fronteira de módulos, contrato, auditoria de coerência por fase | C4 (contexto e containers), context map, estados, modelo de domínio |
| Script, automação, ETL | — | Código simples | Execução repetida corrompendo dados; falha silenciosa | Testes do núcleo de transformação, idempotência, modo `--dry-run` | Fluxo dos dados |

## Combinações frequentes

- **Serviço assíncrono com regra financeira:** camadas + ports, dinheiro em decimal, estados finais imutáveis.
- **Agente de IA com regra de negócio:** regras de domínio puras e testadas (preço, frete, devolução) fora do prompt;
  o modelo decide quando chamar, a regra decide o resultado.
- **Plugin para cliente:** anexos de entrega (plano de testes, evidências, release e rollback) obrigatórios.
