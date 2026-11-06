# Layout do board

Ordem dos frames, da esquerda para a direita, baseada no board do projeto de referência. Frames de workshop são
históricos: não são atualizados depois do rito. Frames de espelho reproduzem documentos do repositório depois de
aprovados e indicam a fonte e a data.

| # | Frame | Tipo | Rito | Espelha |
|---|---|---|---|---|
| 1 | Enunciados das fases | Espelho | 0 | `docs/challenge/` |
| 2 | Domain Storytelling | Workshop | 1 | `docs/domain/discovery/domain-storytelling.md` |
| 3 | Event Storming — Exploração | Workshop | 1 | `docs/domain/discovery/event-storming.md` |
| 4 | Event Storming — Linha do tempo | Workshop | 1 | idem |
| 5 | Hotspots | Workshop | 1 | `docs/domain/discovery/hotspots.md` |
| 6 | Eventos pivotais, atores, comandos e policies | Workshop | 1 | idem |
| 7 | Aggregates e bounded contexts (candidatos) | Workshop | 1–2 | idem |
| 8 | Context Map | Espelho vivo | 2 | `docs/domain/context-map.md` |
| 9 | DDD estratégico e tático (documentos) | Espelho | 2–3 | `docs/domain/` |
| 10 | Modelo de domínio | Espelho | 3 | `docs/domain/domain-model.md` |
| 11 | Requisitos e refinamento | Espelho | 4 | `docs/requirements/` |
| 12 | C4 e arquitetura | Espelho | 5 | `docs/architecture/overview.md` |
| 13 | RFC | Espelho | ∞ | `docs/rfc/` |
| 14 | ADR | Espelho | ∞ | `docs/adr/` |
| 15 | Dívida técnica | Espelho | ∞ | `docs/tech-debt/` |
| 16 | Segurança | Espelho | ∞ | `docs/security/vulnerability-report.md` |
| 17 | Arquitetura da fase `<n>` (entrega) | Espelho | entrega | `docs/architecture/overview.md` |

## Convenções

- Cada frame tem título e uma linha de descrição ("Proposta técnica para discussão e aprovação do time").
- Espelhos começam com "Fonte: `<caminho>` · atualizado em `<AAAA-MM-DD>`".
- Evolução do modelo depois dos workshops vai para o Context Map e o modelo de domínio, com uma nota ("No meio da
  implementação surgiram novos aggregates…"), nunca para os frames de workshop.
- Legenda de cores do Event Storming: `sdd-method:running-domain-discovery` › `event-storming-guide.md`.
- Registre o ID de cada frame no índice do `docs/method.md`.
