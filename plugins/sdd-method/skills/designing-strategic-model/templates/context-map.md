# Context map

| Campo | Valor |
|---|---|
| Status | Draft |
| Atualizado em | `<AAAA-MM-DD>` |
| Aprovado por / em | — |
| Materialização das integrações | `<ADR-NNN>` |
| Board | `<link do frame>` |

```mermaid
flowchart LR
  subgraph REG["Registrations"]
    customer[[Customer]]
    vehicle[[Vehicle]]
  end
  subgraph SL["Service Lifecycle (core)"]
    order[[Service Order]]
    estimate[[Estimate]]
  end
  subgraph SP["Stock & Procurement"]
    item[[Stock Item]]
  end
  supplier[/"Sistema do fornecedor (externo)"/]

  REG -->|"U · OHS → D · Customer/Supplier"| SL
  SL <-->|"Partnership · PL (eventos)"| SP
  supplier -->|"U → D · ACL"| SP
```

<!-- Substitua o exemplo pelos contextos do projeto. -->

## Relações

| Upstream | Downstream | Padrão | Contrato vigente | Decisão |
|---|---|---|---|---|
| `<contexto>` | `<contexto>` | `<OHS · PL · ACL · Partnership · …>` | `<API in-process · evento X · HTTP>` | `<ADR-NNN>` |

## Observações

- `<AAAA-MM-DD>`: `<mudança feita depois do workshop e por quê>`.
