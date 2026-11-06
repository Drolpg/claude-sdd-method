# Especificação Técnica: <nome da feature>

| Campo | Valor |
|---|---|
| Feature | `<feature-slug>` |
| Status | Draft |
| Responsável | `<responsável>` |
| Atualizado em | `<AAAA-MM-DD>` |
| Aprovado por | — |
| Aprovado em | — |
| Especificação funcional | `./functional-spec.md` (aprovada em `<AAAA-MM-DD>`) |
| Decisões aplicadas | `<ADR-NNN, AD-NNN>` |

## Contexto e desenho

Contextos e módulos afetados, responsabilidades, comunicação entre módulos (API pública, port, evento) e por quê.

## Modelo de domínio

Aggregates, entidades e value objects tocados; novos estados ou transições; invariantes novas (com ID).

## Interfaces e fluxo de dados

Contratos de API (método, caminho, request, response, códigos de status), interfaces de aplicação, eventos publicados
e consumidos, e tradução de falhas em códigos de erro estáveis.

| Situação | Código HTTP | Código de erro |
|---|---|---|

## Persistência e dados

Mudanças de schema (migration nova; nenhuma migration existente é alterada) e classificação dos dados:
`nenhum seed` · `referência obrigatória` · `demonstração local` · `fixture de teste`.

## Segurança e operação

Autenticação e autorização, dados sensíveis, validação, segredos, logs, configuração nova, rollout e recuperação.

## Estratégia de testes

| Camada | O que cobre | Tipo de teste |
|---|---|---|
| Domínio | `<INV-NN>` | Unitário |
| Aplicação | `<fluxo do caso de uso>` | Unitário ou integração do módulo |
| Contrato | `<endpoints>` | Integração HTTP |
| Persistência | `<migration, consultas>` | Integração com banco real |
| Fronteiras | `<módulos>` | Teste de fronteira |

## Documentação a atualizar

- [ ] Contrato gerado (anotações)
- [ ] Collection de testes
- [ ] Guia de teste manual
- [ ] Índice de documentação, se houver documento novo

## Adendos

<!-- Mesmo formato da functional-spec. -->
