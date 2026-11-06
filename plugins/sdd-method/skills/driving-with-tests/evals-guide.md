# Evals para comportamento de IA

Testes com LLM falso provam o encanamento (o loop chama a ferramenta certa, trata erro, monta o histórico). Só uma
avaliação contra o **provedor real** prova o comportamento: o modelo não inventa preço, não promete prazo, encaminha
para humano quando deve.

## Estrutura

```text
evals/
  scenarios.<ext>   cenários de referência
  runner.<ext>      executa contra o provedor real
  README.md         como rodar, custo, limites, resultado da última execução
```

Fora da suíte padrão de testes; roda só quando pedido (`make evals`).

## Cenário

| Campo | Exemplo |
|---|---|
| ID | `E-03` |
| Entrada | Conversa (uma ou mais mensagens do cliente) |
| Fatos esperados | "informa o prazo de 7 dias", "valor R$ 1.299,00" |
| Comportamentos proibidos | "não promete desconto", "não informa prazo de pedido não enviado" |
| Ferramentas esperadas | `buscar_pedido` chamada com o número informado |

## Avaliadores

1. **Determinísticos primeiro:** número exato, presença de fato, ferramenta chamada, negação explícita. Compare o fato
   numérico de forma que um valor diferente não passe; aceite sinônimos de status listados no cenário.
2. **Ancore na negação, não na palavra:** "não há desconto" deve passar e "há desconto" deve falhar, mesmo que ambos
   contenham "desconto".
3. **Juiz LLM** só para o que é subjetivo (tom, clareza), com rubrica escrita e nota mínima.

## Execução

- Código de saída: `0` todos passaram, `1` algum falhou, `2` não avaliado (sem chave de API, nenhum cenário
  selecionado).
- **Falhou ≠ não avaliado.** Limite de taxa ou indisponibilidade do provedor gera "não avaliado", com nova tentativa
  única; nunca conta como aprovado.
- Opções úteis: rodar só alguns cenários (`--only E-02,E-05`) e gravar o resultado bruto (`--json`).
- Registre custo (tokens por cenário) e tempo; respeite o limite de taxa do provedor com pausa entre cenários.

## Resultado

No README: data, modelo e versão, cenários passados/falhos, e a seção "O que a avaliação encontrou que os testes não
pegavam". Cada falha real vira correção com teste (quando for regra) ou ajuste de prompt/ferramenta com o cenário
como regressão.
