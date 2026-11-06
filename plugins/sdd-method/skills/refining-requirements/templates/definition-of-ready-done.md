# Definition of Ready e Definition of Done

## Definition of Ready

Uma história ou feature só começa quando:

- [ ] A regra de negócio está mapeada no domínio (aggregate, invariantes e eventos identificados).
- [ ] Os RFs estão no registro de requisitos.
- [ ] Os critérios de aceite estão escritos e são verificáveis.
- [ ] As dependências com outras histórias, épicos ou contextos foram identificadas e resolvidas, ou marcadas como
      bloqueio (ver mapa de dependências).
- [ ] Os casos de borda relevantes estão fechados ou explicitamente fora do escopo.
- [ ] O contrato de entrada e saída está definido, ao menos no nível conceitual.
- [ ] Não há decisão em aberto no registro que bloqueie este trabalho.
- [ ] O esforço foi estimado.

## Definition of Done

Uma história ou feature só termina quando:

- [ ] A regra de negócio está no domínio, não vazou para controller ou adapter.
- [ ] Toda invariante tocada tem teste unitário; o fluxo do caso de uso tem teste de integração quando aplicável.
- [ ] O comando de verificação completa passa e a meta de cobertura foi respeitada.
- [ ] O teste de fronteira de módulos continua verde.
- [ ] A revisão de segurança foi registrada no plano, sem achado crítico ou alto em aberto.
- [ ] Contrato, collection de testes e guia de teste manual foram atualizados, se o contrato mudou.
- [ ] Os eventos de domínio previstos são publicados e consumidos corretamente.
- [ ] Houve revisão aprovada por pelo menos uma pessoa.
- [ ] Os critérios de aceite foram validados, por teste automatizado ou manualmente com evidência.
- [ ] Registro de requisitos, riscos e decisões refletem o que foi feito.
