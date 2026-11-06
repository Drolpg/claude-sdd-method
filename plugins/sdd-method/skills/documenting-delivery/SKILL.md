---
name: documenting-delivery
description: Use quando for escrever ou reorganizar README (com diagramas Mermaid), guias de setup e operação, guia de teste manual da API, checklist de entregáveis de uma fase, roteiro do vídeo de demonstração, anexos de entrega para cliente (evidências, release, rollback), documentação de CI/CD e infraestrutura, ou um glossário de aprendizado.
---

# Entrega e documentação

## Visão geral

Documentação boa responde a uma pergunta por documento, aponta em vez de copiar e só contém comandos que foram
executados. O README é a porta de entrada: diz o que o sistema faz, mostra a arquitetura em diagramas Mermaid e leva a
todo o resto.

## README

Siga `templates/readme.md`. Seções fixas: o que é, arquitetura, como rodar, exemplos de uso, testes ("o que é testado e
por quê"), decisões técnicas, débitos e evolução, estrutura do repositório. Opcionais: resiliência e erros, avaliação
(evals), uso de assistentes de código, entregas da fase.

**Diagramas obrigatórios** conforme o tipo de projeto (`diagram-catalog.md`):

- sempre: arquitetura (componentes) e sequência do fluxo principal;
- se houver ciclo de vida: estados;
- se houver persistência: dados;
- se houver decisão não trivial (agente, roteamento): fluxo de decisão.

Antes de commitar um diagrama, confira as armadilhas de renderização em `diagram-catalog.md` e visualize o resultado
(prévia do GitHub ou `mermaid-cli`).

## Outros documentos (Diátaxis)

Classifique cada documento antes de escrever (`templates/guide.md`):

| Tipo | Serve para | Exemplo |
|---|---|---|
| Tutorial | Levar alguém do zero a um resultado | Subir o ambiente local |
| How-to | Resolver uma tarefa específica | Gerar carga e observar o autoscaling |
| Referência | Descrever, sem narrativa | Variáveis de configuração, workflows de CI |
| Explicação | Dar o porquê | O que liveness e readiness significam |

Nos níveis 2–3, todo documento entra no índice `docs/README.md`, agrupado por público.

## Entregáveis

1. A partir de `docs/challenge/phase-<n>.md`, mantenha `templates/deliverables-checklist.md`: cada entregável com
   artefato, link e evidência verificada.
2. Contrato de API mudou → guia de teste manual (`templates/manual-testing.md`).
3. Vídeo ou apresentação → `templates/demo-script.md`, cronometrado e mapeado aos entregáveis.
4. Entrega para cliente → `docs/05-evidence.md` (`templates/evidence.md`) com fatos comprovados no ambiente real e
   `docs/06-release.md` (`templates/release.md`) com deploy, configuração e rollback.
5. Antes de entregar, rode `sdd-method:auditing-coherence`.

Branches, commits e PRs: `sdd-method:defining-git-workflow`.

## Infraestrutura e operação

Ambientes, CI/CD e IaC são decisões registradas. Cada workflow tem uma referência; cada operação recorrente (subir,
implantar, destruir sem custo residual) tem um how-to com saída esperada.

## O que não vai para o git

`docs/_local/` guarda histórico bruto: idas e vindas, depuração, evidências com dados de ambiente, diário de
aprendizado. O que virar conhecimento permanente é promovido para a spec, o plano ou o README.

## Glossário de aprendizado

Opcional, quando se está aprendendo uma tecnologia: `templates/learning-glossary.md`, com explicação curta, analogia
com o domínio do projeto e link para onde o termo aparece.

## Erros comuns

- README que repete os guias: vira duas fontes que divergem.
- Diagrama que não renderiza no GitHub (palavra reservada como nome de participante).
- Comando no guia que nunca foi executado.
- Checklist de entrega marcada sem link de evidência.
