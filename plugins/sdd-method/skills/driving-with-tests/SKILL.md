---
name: driving-with-tests
description: Use quando for implementar uma tarefa, feature ou correção num projeto do método — escrever os testes de aceite antes do código, manter a matriz requisito → teste, decidir o que testar em cada camada, montar avaliações (evals) de comportamento de IA — ou quando um teste "precisar" mudar para o código passar.
---

# Implementação guiada por testes (TDD)

## Visão geral

O teste é o critério de aceite escrito em código. Ele nasce do requisito, falha pelo motivo certo, e só então o código
é escrito. Teste não muda para o código passar: se o teste parece errado, a conversa volta para a spec.

## Ciclo por tarefa

1. **Leia** o requisito e o critério de aceite (spec ou functional-spec) e as regras da constituição/`AGENTS.md`.
2. **RED:** escreva o(s) teste(s) a partir do critério de aceite. Rode e mostre a falha; ela precisa ser pelo motivo
   esperado (comportamento ausente), não por erro de import ou de fixture.
3. **GREEN:** o mínimo de código para passar. Rode o teste alvo.
4. **REFACTOR:** melhore nomes e estrutura com tudo verde, dentro do estilo arquitetural decidido.
5. **Verifique:** suíte completa, lint, formatação e tipos (comandos do perfil de stack ou da constituição).
6. **Commit:** um ciclo verde = um commit, no padrão do `CONTRIBUTING.md`, citando o requisito no rodapé.
7. **Atualize** a matriz requisito → teste, o status da tarefa e a evidência (comando e resultado).
8. **Relate** com `templates/task-report.md`.

Correção de bug começa com um teste que reproduz o bug e falha.

## Regras

- Nunca edite testes, configuração de testes ou a spec para fazer algo passar. Se um teste parece errado, pare,
  explique por quê e espere a decisão.
- Todo requisito tem pelo menos um teste; todo teste aponta para um requisito.
- Um teste precisa poder falhar por um bug real. Teste que repete a implementação ou só verifica mocks não entra.
- Fakes nas fronteiras (ports, cliente externo, LLM); banco real (container) nos testes de integração quando houver
  persistência; nenhuma chamada de rede real em teste unitário.
- Testes caros ou que dependem de serviço pago (evals, e2e na nuvem) ficam fora da suíte padrão e têm comando próprio.

## O que testar em cada camada

O tipo de projeto (`sdd-method:choosing-architecture` › `project-archetypes.md`) define os gates; o padrão é:

| Camada | Cobre | Tipo |
|---|---|---|
| Regras puras / domínio | Invariantes, cálculos, decisões | Unitário, rápido, sem infraestrutura |
| Orquestração | Fluxo do caso de uso com fakes das fronteiras | Unitário ou integração do módulo |
| Contrato | Rotas, validação, códigos de erro | Integração HTTP |
| Persistência | Migrations, consultas | Integração com banco real |
| Fronteiras de arquitetura | Regras de dependência entre camadas/módulos | Teste de arquitetura |
| Fluxo completo | Caminho feliz e uma falha relevante | Ponta a ponta (containers) |
| Comportamento de IA | Respostas do modelo real em cenários de referência | Evals (`evals-guide.md`) |
| Desempenho | Limites dos RNFs | Teste de carga ou harness de desempenho |

## Plano de testes

Projetos entregues a terceiros mantêm `docs/04-test-plan.md` (`templates/test-plan.md`): testes automatizados,
cenários de integração no ambiente real e situação de cada um.

## Erros comuns

- Escrever código e teste juntos e chamar de TDD: o teste nunca foi visto falhando.
- "Ajustar" a asserção porque o valor mudou, sem checar se a spec mudou.
- Teste de integração que sobe a rede real de um terceiro.
- Medir só cobertura: 100% de linhas com asserções fracas não prova o requisito.
