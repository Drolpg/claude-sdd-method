---
name: reviewing-security
description: Use quando um plano de implementação chegar ao checkpoint de segurança, quando for rodar ou registrar scans de vulnerabilidade (SCA, SAST, DAST) de uma fase, modelar ameaças, ou decidir o que fazer com um achado de segurança que não será corrigido agora.
---

# Revisão de segurança

## Visão geral

Segurança entra em dois ritmos: um checkpoint em toda feature ("o que esta mudança expõe?") e um relatório por fase
("o que o sistema inteiro expõe?"). Achado real nunca é suprimido para o scan sair limpo.

## Checkpoint por feature

Percorra `templates/security-checklist.md` e registre no plano da feature cada item com achado e mitigação, ou `N/A`
com motivo curto. A feature não vira `Implemented` com achado crítico ou alto em aberto.

## Relatório por fase

1. Defina as frentes e ferramentas pelo perfil de stack: SCA (dependências), SAST (código) e DAST (aplicação rodando,
   guiada pelo contrato de API, autenticada).
2. Rode o baseline e guarde a evidência (execução de CI, artefato, data, versão da ferramenta).
3. Corrija críticos e altos. Para cada correção, rescan provando a ausência do identificador e rode a suíte de testes
   para provar que não houve regressão.
4. Achado que não será corrigido (sem correção publicada, risco aceito, escopo só de teste) vira TD com mitigação em
   vigor e gatilho de reavaliação (`sdd-method:recording-decisions`).
5. Escreva `docs/security/vulnerability-report.md` (`templates/vulnerability-report.md`): resultado inicial →
   correções → resultado final, achado a achado, com como reproduzir.

## Modelagem de ameaças

No nível 3, ou quando houver dado pessoal ou financeiro sensível: STRIDE por fronteira de confiança do diagrama de
containers (`templates/threat-model.md`). Ameaça sem mitigação vira TD ou requisito.

## Regras

- Segredos fora do repositório; arquivos de exemplo com placeholders.
- Logs sem dados pessoais, tokens ou segredos.
- Resposta de erro sem stack trace, SQL ou nome de tipo interno; código de erro estável.
- Dependência nova entra no SCA antes do merge.
- Severidade só muda com justificativa registrada.

## Erros comuns

- "Sem achados" sem dizer quais ferramentas, versões e escopo rodaram.
- Downgrade de dependência para "zerar" um CVE, trocando um risco medido por um não medido.
- Credencial de bootstrap em migration sem TD nem plano de troca.
- Autorização só por papel, sem checar posse do recurso, sem registrar isso como risco aceito.
