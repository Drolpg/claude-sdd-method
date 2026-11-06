# Perfil de stack

| Campo | Valor |
|---|---|
| Status | Draft |
| Atualizado em | `<AAAA-MM-DD>` |
| Aprovado por / em | — |
| Decisões | `<ADR de estrutura, ADR de linguagem/framework, ADR de banco>` |

## Ferramentas

| Preocupação | Ferramenta | Versão | Comando | Observação |
|---|---|---|---|---|
| Build e execução | | | | |
| Regras de dependência (camadas e módulos) | | | | Roda em todo build |
| Checagem de tipos | | | | |
| Testes unitários | | | | |
| Integração com banco real | | | | |
| Testes HTTP | | | | |
| Cobertura | | | | Meta: `<80%>` |
| Migrations | | | | Pasta e convenção de nome abaixo |
| Contrato de API gerado | | | | Onde é servido |
| Validação na borda | | | | |
| Eventos in-process | | | | Publicação após commit? |
| Lint e formatação | | | | |
| SCA / SAST / DAST | | | | |

## Comandos do dia a dia

| Para | Comando |
|---|---|
| Rodar os testes | `<ex.: make test>` |
| Verificação completa (antes de PR) | `<ex.: make verify>` |
| Relatório de cobertura | `<ex.: make coverage>` |
| Subir localmente | `<ex.: docker compose up -d --build>` |

## Convenções

- Raiz de pacote / namespace: `<…>`.
- Migrations: pasta `<…>`, nome `<ex.: VyyyyMMddHHmmss__descricao_em_snake_case.sql, timestamp UTC>`.
- Estilo: `<indentação, tamanho máximo de linha, sem imports curinga, nomes>`.
- Injeção de dependência: `<por construtor; sem injeção em campo>`.

## Mapeamento de conceitos

| Conceito do método | Neste projeto |
|---|---|
| Módulo (bounded context) | |
| Aggregate root | |
| Value object | |
| Port | |
| Evento de domínio | |
| Transação do caso de uso | |
| Erro de negócio → código estável | |
