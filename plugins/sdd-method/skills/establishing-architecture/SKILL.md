---
name: establishing-architecture
description: Use quando for montar a base técnica de um projeto depois de decidido o estilo — escolher stack (linguagem, framework, banco), criar a estrutura de pastas do estilo, automatizar as regras de dependência entre camadas ou módulos, desenhar C4 e implantação, configurar CI e quality gates — inclusive numa linguagem que ainda não tem perfil de stack.
---

# Arquitetura base (rito 7)

## Visão geral

Materializa o estilo decidido em `sdd-method:choosing-architecture`: estrutura de pastas, stack, regras de dependência
verificadas por ferramenta desde o primeiro commit e um esqueleto que já roda no CI. Nada de feature ainda.

## Passos

1. **Confirme a decisão de estilo.** Se a spec ou a descoberta do domínio mudaram os sinais, reavalie antes de
   seguir.
2. **Stack.** Uma decisão por escolha estrutural (linguagem e framework, banco com justificativa, fila se houver):
   tabela de decisões no plano (nível 1) ou ADR (níveis 2–3). Critérios: aderência ao estilo, conhecimento de quem
   trabalha, ferramentas de teste e de regras de dependência, custo de operar.
3. **Perfil de stack** (`templates/stack-profile.md`), a partir de `stack-profiles.md`: uma ferramenta por
   preocupação, com versão e comando. Preencha as seções `STACK` do `AGENTS.md` e o comando de verificação completa no
   `docs/method.md`.
4. **Estrutura** do estilo escolhido (`sdd-method:choosing-architecture` › `architecture-styles.md`), registrada no
   plano (nível 1) ou em `templates/project-structure.md` (níveis 2–3).
5. **Regras de dependência automatizadas**, proporcionais ao estilo:
   - camadas: "`services` não importa o framework web nem a fila";
   - ports e hexagonal: "`core` não importa `adapters`";
   - monólito modular: fronteira de módulos verificada (ex.: Spring Modulith, import-linter, dependency-cruiser).
6. **Diagramas:** os do README conforme o tipo de projeto (`sdd-method:documenting-delivery` ›
   `diagram-catalog.md`); C4 e implantação em `templates/architecture-overview.md` nos níveis 2–3 ou quando houver
   infraestrutura a entregar.
7. **Esqueleto executável:** projeto criado, primeiro teste passando, lint, tipos, testes e regras de dependência no CI.
8. **Gate:** decisão de estilo `Accepted` (ou aprovada no plano), CI verde, seções `STYLE` e `STACK` do `AGENTS.md`
   preenchidas. Atualize `docs/method.md`.

## Regras

- Dependências apontam para dentro; regra de negócio não importa framework.
- Regra de dependência sem verificação automática vira só combinação verbal: automatize.
- Nada de pasta, camada ou interface que o estilo não pede.
- Toda dependência tem versão fixada (lockfile versionado) e entra no SCA.

## Linguagem sem perfil

Se a linguagem não estiver em `stack-profiles.md`, pesquise a ferramenta equivalente para cada linha, confirme versão,
manutenção e licença, preencha o perfil do projeto e proponha ao usuário acrescentar a coluna no método.

## Erros comuns

- Pastas por camada técnica no topo (`controllers/`, `services/`) num projeto com várias áreas de negócio.
- Esqueleto com a estrutura de um estilo mais pesado "para depois".
- Escolher a ferramenta de regras de dependência depois que o acoplamento já existe.
- C4 com sistema externo sem requisito.
