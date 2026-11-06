---
name: running-domain-discovery
description: Use quando for entender um domínio de negócio antes de modelar — conduzir ou registrar Domain Storytelling, Event Storming (big picture ou de processo), hotspots e perguntas em aberto — ou quando o usuário trouxer anotações, fotos ou um board de workshop para organizar.
---

# Descoberta do domínio (trilha DDD completo)

## Visão geral

Descoberta é ouvir o negócio contar como o trabalho acontece e transformar isso em eventos numa linha do tempo. O
Claude facilita e registra; o conhecimento vem do usuário ou do time. Nada de domínio é inventado: o que for
suposição vira hotspot.

Entra quando a avaliação de arquitetura (`sdd-method:choosing-architecture`) indicou DDD completo. Em outros estilos,
uma Domain Storytelling curta (passo 1) ainda ajuda a escrever a spec, sem os demais passos.

## Passos

1. **Domain Storytelling.** Peça um caso real, do começo ao fim ("o cliente chega com o carro…"). Registre como
   frases numeradas *ator → atividade → objeto de trabalho* em `templates/domain-storytelling.md`. Faça ao menos uma
   história do caminho feliz e uma da exceção que mais dói.
2. **Exploração caótica.** Liste eventos de domínio no passado ("Orçamento Enviado"), sem ordem e sem filtro.
3. **Linha do tempo.** Ordene, remova duplicados e una sinônimos. Anote o termo vencedor de cada grupo: ele vai para
   a linguagem ubíqua.
4. **Hotspots.** Marque dúvidas, conflitos, riscos e dores. Cada hotspot ganha um destino: pergunta ao negócio,
   decisão (AD/RFC), caso de borda de requisito ou fora de escopo (`templates/hotspots.md`).
5. **Eventos pivotais e raias.** Identifique os eventos que mudam a fase do processo. Eles sugerem as fronteiras de
   contexto do desenho estratégico (rito 4).
6. **Atores, comandos, policies, sistemas externos e read models.** Para cada evento: que comando o causa e quem o
   dispara; que policy reage a ele ("sempre que… então…"); que informação o ator precisa ver para decidir.
7. **Aggregates candidatos.** Agrupe comandos e eventos em torno do que precisa garantir uma regra. São candidatos; o
   desenho tático (rito 5) confirma.
8. **Gate:** o usuário (ou o time) revisa a linha do tempo e o destino de cada hotspot. Atualize `docs/method.md`.

Notação, cores e representação em Mermaid: `event-storming-guide.md`. Registro textual:
`templates/event-storming.md`.

## Com board

Se o MCP do Miro estiver conectado, siga as instruções do servidor antes de criar itens. Crie um frame por etapa
(passos 2, 3, 4, 6 e 7) e não reaproveite o frame de uma etapa anterior: frames de workshop são históricos. Ao fim de
cada etapa, gere a versão textual no repositório e registre o ID do frame no `docs/method.md`.

## Sem time disponível

Conduza como entrevista: uma pergunta aberta por vez ("o que acontece logo depois que o orçamento é enviado?"),
espere a resposta e só então registre. Se o usuário pedir que você proponha, marque cada evento proposto como
hipótese até ele confirmar.

## Erros comuns

- Evento no presente ou como ordem ("Enviar orçamento") → reescreva no passado ("Orçamento enviado").
- Modelar entidades e tabelas aqui. Descoberta trata de comportamento e tempo, não de dados.
- Resolver hotspot sozinho. Registre e leve a quem decide.
- Pular a história de exceção: é nela que aparecem as regras que dão profundidade ao modelo.
