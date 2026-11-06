# Estrutura do projeto

| Campo | Valor |
|---|---|
| Atualizado em | `<AAAA-MM-DD>` |
| Estilo | `<estilo>` — `<link da decisão>` |

## Árvore

```text
<árvore do estilo escolhido; uma linha de descrição por pasta>
```

<!-- Exemplos por estilo (use só o do projeto):

Camadas:
  src/<pkg>/api/ services/ models/ db/ worker/ core/(config, erros, logging)

Camadas + ports nas fronteiras:
  src/<pkg>/api/ services/ models/ db/ ports.py adapters/(uma por fronteira) worker/

Núcleo funcional + casca:
  src/rules/(funções puras) store/ sync/ ui/ (casca da plataforma)

Hexagonal:
  core/(regras + ports) adapters/<tecnologia>/ main.(composition root)

Monólito modular (por módulo, com o estilo interno do módulo):
  <module>/domain/ application/(usecase, api, port) infrastructure/(persistence, web, integration)
-->

## Módulos ou pacotes

| Módulo / pacote | Responsabilidade | Quem pode importar |
|---|---|---|

## Regras de dependência

| Regra | Como é verificada |
|---|---|
| `<ex.: services não importa fastapi nem celery>` | `<contrato do import-linter no CI>` |

## Placeholders

Partes documentadas mas ainda sem feature aprovada ficam vazias, com descrição; nada de código, entidade ou tabela
inventados.

| Placeholder | Onde | Tarefa ou feature que vai criá-lo |
|---|---|---|
