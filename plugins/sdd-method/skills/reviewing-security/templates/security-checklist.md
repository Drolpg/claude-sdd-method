# Checklist de segurança por feature

Copie a tabela para a seção "Revisão de segurança" do `implementation-plan.md`.

| Item | Pergunta | Achado | Mitigação | Status |
|---|---|---|---|---|
| Validação de entrada | Todo campo de entrada é validado na borda (tipo, tamanho, formato, faixa)? | | | |
| Mass assignment | O request só aceita os campos que o caso de uso permite alterar? | | | |
| Autenticação | Todo endpoint novo exige o mecanismo certo (token de usuário, assinatura de sistema)? | | | |
| Autorização | O papel exigido está correto? Há checagem de posse do recurso, ou o risco está registrado? | | | |
| Exposição de dados | A resposta expõe só o necessário? Dados pessoais ou operacionais saem para quem não deveria? | | | |
| Segredos | Algum segredo novo? Está fora do repositório, com exemplo em placeholder? | | | |
| Logs | Algum log novo contém dado pessoal, token, segredo ou payload inteiro? | | | |
| Persistência | Consultas parametrizadas? Migration nova é segura de aplicar e reverter? | | | |
| Respostas de erro | Erros novos usam código estável, sem detalhes internos? | | | |
| Dependências | Dependência nova? Passou pelo SCA? Versão fixada? | | | |
| Abuso | Limites de tamanho, volume, repetição (replay), enumeração de IDs? | | | |
| Integrações externas | Assinatura ou autenticação verificada, timeouts, tratamento de resposta maliciosa? | | | |

Status: `OK`, `Mitigado`, `Aceito → TD-NNN`, `N/A (<motivo>)`.
