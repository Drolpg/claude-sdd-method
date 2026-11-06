# Plano de Implementação: <nome da feature>

| Campo | Valor |
|---|---|
| Feature | `<feature-slug>` |
| Status | Draft |
| Responsável | `<responsável>` |
| Atualizado em | `<AAAA-MM-DD>` |
| Especificação técnica | `./technical-spec.md` (aprovada em `<AAAA-MM-DD>`) |

## Objetivo

Uma frase: o que estará verdadeiro quando o plano terminar.

## Checkpoint 1 — <nome>

- O que muda: `<arquivos, componentes>`.
- Testes: `<o que prova o checkpoint>`.
- Evidência esperada: `<comando e resultado>`.
- Gate: `<o que precisa estar aprovado antes, se houver (ex.: adendo da spec)>`.

## Checkpoint 2 — <nome>

…

## Checkpoint N — Validação final

- Comando de verificação completa.
- Teste manual do fluxo pelo guia (quando o contrato mudou).

## Revisão de segurança

| Item | Achado | Mitigação | Status |
|---|---|---|---|
| Validação de entrada e mass assignment | | | |
| Autenticação e autorização | | | |
| Exposição de dados | | | |
| Segredos e logs | | | |
| Persistência e migrations | | | |
| Respostas de erro | | | |
| Dependências novas | | | |
| Abuso do endpoint | | | |

Status: `OK`, `Mitigado`, `Aceito → TD-NNN`, `N/A (<motivo>)`. Checklist completo:
`sdd-method:reviewing-security`.

## Definition of Done

- [ ] Checkpoints concluídos, com evidência.
- [ ] Testes relevantes criados ou atualizados e passando.
- [ ] Comando de verificação completa passando; cobertura dentro da meta.
- [ ] Fronteiras de módulo verificadas.
- [ ] Revisão de segurança registrada, sem achado crítico ou alto aberto.
- [ ] Migration e classificação de dados presentes, se a persistência mudou.
- [ ] Contrato, collection e guia de teste manual atualizados, se o contrato mudou.
- [ ] Registro de requisitos e riscos atualizados.

## Evidências de verificação

### Checkpoint 1 — <nome> (<AAAA-MM-DD>)

```text
<comando executado>
<resultado relevante>
```

## Rollback ou recuperação

Como desfazer um deploy ou uma migration com problema, ou `N/A` com motivo.
