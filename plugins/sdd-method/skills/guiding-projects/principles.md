# Princípios

Valem em todos os ritos. Entre parênteses, o problema real que deu origem à regra.

## Proporcionalidade

1. **Abstração só onde há fronteira real**: sistema externo, fila, tecnologia com troca prevista, regra que precisa
   ser testada sem infraestrutura.
2. **Toda estrutura tem um motivo registrado.** Camada, port, módulo ou aggregate sem sinal que o justifique sai.
3. **Decidir não adotar também é decisão**, e vira regra no `AGENTS.md`, para nenhum agente "melhorar" a arquitetura
   por conta própria. (O `AGENTS.md` do `anticipation-engine` proíbe ports, repository e DI e manda simplificar o que
   já existisse.)
4. **Preparar o futuro é registrar o gatilho, não construir a estrutura.**

## Método

5. **A spec manda no código.** Comportamento muda primeiro na spec, depois no teste, depois no código.
6. **Teste é critério de aceite.** Não se altera teste nem spec para fazer algo passar; se o teste parece errado, a
   conversa volta para a spec.
7. **Um ciclo verde = um commit**, citando o requisito.
8. **Divergência para e registra.** Código × spec em conflito vai para "Pendências abertas"; ninguém decide sozinho.
9. **Ninguém aprova pelo outro.** O agente redige; a pessoa aprova; o documento registra nome e data.
10. **Gates são sequenciais.** Mudança material num documento aprovado o devolve a `Draft` e torna obsoletos os
    seguintes.

## Coerência

| Artefato | Fonte da verdade | Espelhos permitidos |
|---|---|---|
| Requisitos e seus IDs | `docs/01-spec.md` (nível 1) ou `docs/requirements/requirements.md` (níveis 2–3) | Board, tracker |
| Decisões | Plano (nível 1) ou registro + ADR/RFC/TD (níveis 2–3) | Board, depois da aceitação |
| Workshops de domínio | Board; sem board, `docs/domain/discovery/` | Resumo no repositório |
| Linguagem ubíqua | Glossário da spec ou `docs/domain/ubiquitous-language.md` | Board |
| Modelo implementado | Código | Diagramas, auditados contra o código |
| Contrato de API | Contrato gerado pela aplicação | Collection, guia manual |
| Estado do método | `docs/method.md` | — |

11. **Um lugar para cada fato.** Os outros apontam, não copiam.
12. **Números são calculados, nunca lembrados.** O próximo ID é o maior existente + 1; nenhum documento registra
    "próximo número livre". (Um `CLAUDE.md` continuou dizendo "próximo é 008" depois que a ADR-008 já existia.)
13. **Um número, um significado, para sempre.** (RF37 acabou com dois significados.)
14. **Registre antes de citar.** (Requisitos de uma fase nova foram citados em specs sem nunca entrar no registro.)
15. **Mudou o status, propague no mesmo commit.** (Uma RFC ficou `Draft` no repositório e `Aceita` no board.)
16. **Um termo, uma definição.** (Technician era "ator" e "aggregate" no mesmo glossário.)
17. **Histórico é aditivo**: nota datada ou `Superseded by`, sem reescrever o passado.
18. **Referências externas centralizadas** em `docs/method.md`. (61 links apontavam para um board que a cópia pessoal
    não abria.)
19. **Diagrama é código** (Mermaid no repositório) e só mostra o que tem requisito ou decisão por trás. (Um C4 mostrava
    um Payment Gateway que nunca existiu.)
20. **Comando documentado é comando executado**, com a saída esperada.
21. **Sem acesso, sem invenção**: board, tracker ou enunciado indisponível → diga e marque "não verificado".
22. **Histórico bruto fica fora do git** (`docs/_local/`); o que virar conhecimento permanente é promovido para os
    documentos versionados.
