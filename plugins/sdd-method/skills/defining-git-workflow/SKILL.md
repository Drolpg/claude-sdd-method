---
name: defining-git-workflow
description: Use quando um projeto começar ou ainda não tiver convenção escrita de branches, commits e pull requests; antes de criar branch, commit, merge ou PR num projeto do método; ou quando o histórico estiver com padrões misturados.
---

# Branches, commits e pull requests

## Visão geral

Todo projeto tem a convenção de Git escrita desde o primeiro commit, em `CONTRIBUTING.md`. O histórico conta a mesma
história que a spec: um ciclo verde por commit, cada um citando o requisito.

## Na fundação

1. **Modelo de branches** (o usuário escolhe):

   | Modelo | Para | Fluxo |
   |---|---|---|
   | Só `main` | Solo, POC curta | Commits pequenos direto na `main`, sempre verdes |
   | `main` + `dev` | Solo ou dupla, com demonstrações ou entregas | `feat/*` sai da `dev` atualizada → volta à `dev` depois do checkpoint → `main` só com autorização explícita do usuário |
   | `main` + `dev` com PR | Time | Igual ao anterior, sempre por PR com ao menos uma revisão |

2. **Commits** no padrão Conventional Commits, com estes parâmetros definidos no `CONTRIBUTING.md`:
   - tipos permitidos (lista fechada): `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`,
     `style`, `revert`;
   - escopos permitidos: módulos, contextos ou fases do projeto, mais `platform`, `deps`, `readme`;
   - idioma e forma do assunto (padrão: português, imperativo, minúsculo, sem ponto, até 72 caracteres);
   - corpo com o quê e por quê; rodapé `Refs: RF-NN` e `BREAKING CHANGE:` quando houver;
   - trailers de autoria de IA (padrão: **não usar**, nem `Co-Authored-By` de assistente).
3. **Pull requests:** `templates/pull_request_template.md` (time) ou `templates/pull_request_template-solo.md`
   (auto-revisão) em `.github/pull_request_template.md`. Sem PR, a checklist solo é conferida antes de cada merge.
4. **Versões:** tag SemVer (`v1.2.0`) na `main` a cada entrega.
5. **Opcional:** validação automática do assunto do commit (commitlint, gitlint ou checagem do título do PR no CI).
6. Gere `CONTRIBUTING.md` a partir de `templates/CONTRIBUTING.md` e aponte para ele no `AGENTS.md`.

## Regras para o agente

- Nunca fazer merge ou push para a `main` sem autorização explícita do usuário naquele momento.
- Antes de commitar: testes verdes, nenhum segredo, mensagem no padrão. Não inventar tipos (`merge:`, `update:`).
- Branch nova: `<tipo>/<escopo>-<descricao-curta>`, minúscula, a partir da branch de integração atualizada.
- Mudanças sem relação vão em commits separados; formatação nunca se mistura com comportamento.
- Respeite a regra de trailers do `CONTRIBUTING.md`, mesmo que a ferramenta adicione um por padrão.

## Erros comuns

- Escopo às vezes presente, às vezes ausente: defina se é obrigatório.
- Tipos fora da lista em commits de merge ou release.
- Idioma alternando entre português e inglês no mesmo histórico.
- Um commit gigante no fim da fase: perde-se a relação com os requisitos.
