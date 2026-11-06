# 00 — Constituição do projeto

Princípios que valem para todas as decisões. Em caso de dúvida, volte aqui.

## 1. Objetivo

`<O que o sistema faz, para quem, e o nível de qualidade esperado (ex.: "rigor de código de produção financeira").>`

## 2. Método: SDD + TDD

| Fase | Artefato |
|---|---|
| Especificar | `docs/01-spec.md` |
| Planejar | `docs/02-plan.md` |
| Quebrar em tarefas | `docs/03-tasks.md` |
| RED — testes que falham | `tests/**` |
| GREEN — implementação mínima | `src/**` |
| REFACTOR | `src/**`, com testes verdes |
| Validar | revisão do diff contra a spec |

Regras:

1. Mudou o comportamento? Mude a spec primeiro, depois o teste, depois o código.
2. Teste é critério de aceite: não se altera teste para "fazer passar".
3. Um ciclo verde = um commit pequeno.
4. Todo requisito tem pelo menos um teste (matriz na spec).
5. Todo teste precisa poder falhar por um bug real; teste que só repete a implementação não entra.

## 3. Princípios de engenharia

<!-- Nasçam dos riscos deste projeto. Exemplos de projetos anteriores; mantenha só os que se aplicam: -->

- `<Não bloquear: a API responde na hora; trabalho lento vai para o worker.>`
- `<Falhar de forma previsível: todo erro tem código estável, status correto e log com contexto.>`
- `<Idempotência: processar a mesma mensagem duas vezes não corrompe nada; estados finais não são sobrescritos.>`
- `<Proteger o serviço externo: timeout explícito, retry limitado com backoff e jitter.>`
- `<Nenhuma transação aberta durante chamada de rede.>`
- `<Observabilidade desde o início: logs estruturados, ID de correlação de ponta a ponta.>`
- `<Dados pessoais nunca em claro nos logs; segredos fora do código e do git.>`
- `<Dinheiro sempre em decimal, nunca ponto flutuante.>`

## 4. Arquitetura

Estilo: `<estilo>` — decisão e justificativa em `docs/02-plan.md` § Decisão de arquitetura.

Simplicidade deliberada: `<o que não será adotado e por quê, ex.: "sem repository, sem container de DI, ports só nas
fronteiras com o serviço externo e a fila">`.

## 5. Definition of Done

- [ ] Testes da tarefa verdes e suíte completa verde (`<comando>`).
- [ ] Lint, formatação e checagem de tipos sem erros (`<comandos>`).
- [ ] Nenhum segredo, dado pessoal em claro ou stack trace em log ou resposta.
- [ ] Spec e matriz requisito → teste atualizadas se o comportamento mudou.
- [ ] Commit no padrão do `CONTRIBUTING.md`.

## 6. Convenções

- `<Linguagem e versão, gerenciador de pacotes, type hints/strict mode.>`
- `<Idioma dos nomes: domínio em português (Consulta, documento), infraestrutura em inglês; status e códigos de erro
  como no contrato.>`
- `<Direção das dependências, ex.: api → services → models; services não importa framework web nem fila.>`
- Branches, commits e PRs: `CONTRIBUTING.md`.
