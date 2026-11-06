# Registro de decisões

## Propósito

Separa decisões de arquitetura e de processo de trabalho apenas não feito, para que cada pessoa avance dentro do seu
escopo sem transformar uma escolha local em decisão do time.

## Fontes e autoridade

| Fonte | Autoridade sobre |
|---|---|
| Enunciado (`docs/challenge/`) | Resultados obrigatórios; não define o desenho interno |
| Board (workshops) | Intenção de domínio do time, até que um artefato aceito mais novo a substitua |
| Repositório (`docs/`) | Decisões, requisitos e specs vigentes |
| Código | Apenas o que está implementado agora |

## Status

| Status | Significado |
|---|---|
| **Pending** | Há uma escolha real e o dono indicado pode fazê-la. |
| **Team Decision Required** | A escolha cruza escopos ou módulos e não pode ser feita por uma pessoa só. |
| **Not Blocking** | A pergunta é válida, mas nenhuma implementação atual depende da resposta. |
| **Deferred** | Adiada de propósito para outra fase ou até um gatilho. |
| **Resolved** | Há evidência de que foi decidida explicitamente e adotada. |
| **Superseded** | Substituída por uma decisão mais nova. |

Status descreve a decisão, não a implementação: uma decisão resolvida pode estar sem implementação.

## Escopos

| Escopo | Significado |
|---|---|
| **Dono do épico** | Afeta só o épico e pode ser decidida pelo dono sem redefinir outro épico. |
| **Arquitetura compartilhada** | Escolha técnica transversal usada por vários contextos. |
| **Outro épico** | Pertence a outro dono; quem encontrou não decide sozinho. |
| **Time todo** | Muda fronteiras do sistema, contratos compartilhados, escopo de entrega ou política de arquitetura. |

## Conflitos entre fontes

| Diferença | Classificação | Por que importa |
|---|---|---|
| `<fonte A diz X; fonte B diz Y>` | `<decisão necessária · inconsistência de documentação · implementação pendente · instrução desatualizada · diferença inofensiva>` | `<impacto>` |

## Resumo

| ID | Título | Status | Escopo | Dono | Bloqueia |
|---|---|---|---|---|---|
| AD-001 | `<título>` | Pending | `<escopo>` | `<nome>` | `<o que bloqueia>` |

---

### AD-NNN — [Pergunta a decidir]

**Status:** [Pending | Team Decision Required | Not Blocking | Deferred | Resolved | Superseded]

**Scope:** [escopo]

**Decision:** [preencha só quando resolvida: opção escolhida e resumo]

**Resolved on:** [AAAA-MM-DD, por quem / "ratificada pelo time"]

**Blocking:** [o que não pode avançar sem esta decisão]

**Related epic / responsibility:** [épico, dono]

**Problem:** [o que precisa ser decidido]

**Why this is a decision rather than an implementation gap:** [que fronteira, contrato ou política muda]

**Conflicting evidence:** [o que cada fonte diz]

**Options:**

Option A — [nome]

- Vantagens:
- Desvantagens:

Option B — [nome]

- Vantagens:
- Desvantagens:

**Recommended option:** [recomendação e motivo; deixe claro que não é aprovação]

**Impact of the decision:** [módulos, persistência, APIs, testes, board, AGENTS.md]

**Follow-up:** [ADR-NNN, TD-NNN ou feature criada a partir da decisão]
