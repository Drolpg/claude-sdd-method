---
name: auditing-coherence
description: Use quando for verificar se documentação, board, requisitos, decisões e código estão coerentes entre si — no fim de uma fase, antes de uma entrega, depois de merges grandes, ao copiar ou migrar um board, ao criar um fork de referência, ou ao adotar o método num projeto existente.
---

# Auditoria de coerência

## Visão geral

Drift é inevitável quando há mais de uma fonte; o que não pode é ser invisível. A auditoria pareia cada artefato com
seus espelhos, compara cabeçalho e conteúdo, e classifica cada diferença para que alguém decida.

## Passos

1. **Inventário.** Documentos do repositório (`git ls-tree -r --name-only HEAD docs`), frames e documentos do board
   (busca em modo visão geral, depois leitura por frame), IDs de requisito citados no repositório inteiro (`git grep`)
   e o código relevante. Registre o commit e a data auditados.
2. **Pareamento** conforme `audit-checklist.md`.
3. **Cabeçalhos primeiro:** status, datas, "Last Updated". Use `git log -- <arquivo>` para saber qual lado é mais
   novo; não assuma.
4. **Conteúdo depois**, com os scripts (só leem arquivos; `python -I scripts/<script>.py --help` mostra os argumentos):
   - `scripts/extract_miro_docs.py`: extrai docs e diagramas de uma leitura do board e acha o arquivo do repositório
     mais parecido;
   - `scripts/doc_diff.py`: diferença frase a frase entre dois documentos;
   - `scripts/model_vs_code.py`: compara o `classDiagram` com os tipos declarados no código;
   - convenção de commits: `git log --format=%s <desde>..HEAD` e compare com os tipos, escopos e idioma do
     `CONTRIBUTING.md` (commits de merge gerados pelo Git ficam de fora).
5. **Classifique** cada divergência:

   | Classe | Significado | Quem resolve |
   |---|---|---|
   | Igual | Conteúdo equivalente | — |
   | Espelho desatualizado | Um lado é mais novo (diga qual e por quê) | Atualização, com aprovação do usuário |
   | Ausente em um lado | Existe só no repositório ou só no board | Atualização, com aprovação do usuário |
   | Conflito | Dois lados afirmam coisas diferentes e nenhum é claramente o vigente | Registro de decisões |
   | Inconsistência interna | Uma mesma fonte se contradiz | Registro de decisões ou correção com nota |
   | Referência quebrada | Link ou ID que não abre ou não existe | Atualização |
   | Desvio doc × código | O documento descreve algo que o código não faz | TD, feature ou correção do documento |

6. **Relatório** em `docs/audits/<AAAA-MM-DD>-coherence.md` (`templates/coherence-report.md`), agrupado por classe,
   com recomendação e dono para cada item.
7. **Ações:** proponha as correções de espelho e de referência e aplique só com aprovação. Conflitos vão para o
   registro de decisões; nunca os resolva sozinho.

## Uso do board

Leia frames inteiros em vez de itens soltos (menos chamadas) e salve saídas grandes em arquivo antes de analisar.
Respeite a cota da integração. Sem acesso a um board, marque os itens como "não verificado" em vez de supor o
conteúdo.

## Erros comuns

- Comparar só pelo título ou número: números iguais com significados diferentes passam batido.
- Assumir que o board é mais novo, ou que o repositório é. Verifique datas e histórico.
- Corrigir um conflito "óbvio" sem decisão registrada.
- Tratar diferença de formatação (tabela do board × tabela Markdown) como divergência de conteúdo.
