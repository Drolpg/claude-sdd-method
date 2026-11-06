# Padrões de context map

| Padrão | Quando usar | Sinal de alerta |
|---|---|---|
| Partnership | Dois contextos evoluem juntos e falham juntos; times coordenam entregas | Virou dependência mútua sem dono do contrato |
| Shared Kernel | Pequeno núcleo de modelo compartilhado de propósito, com mudança combinada | Cresceu e virou "módulo comum" de domínio |
| Customer/Supplier | Upstream atende necessidades do downstream, que pode negociar prioridades | Downstream bloqueado esperando o upstream |
| Conformist | Downstream aceita o modelo do upstream sem negociar | Termos do upstream vazando no domínio do downstream |
| Anticorruption Layer (ACL) | Proteger o modelo do downstream de um modelo externo ou legado | Tipos do sistema externo aparecendo no domínio |
| Open Host Service (OHS) | Upstream oferece uma API estável para vários consumidores | API espelha o modelo interno e quebra a cada mudança |
| Published Language (PL) | Formato documentado de troca (eventos, schema) entre contextos | Eventos com payload "tudo que existe" |
| Separate Ways | Integrar custa mais do que duplicar | Duplicação crescendo sem decisão registrada |
| Big Ball of Mud | Rotular um legado sem fronteiras claras | Ninguém sabe de onde vem um dado |

## Num monólito modular

O desenho continua o mesmo; muda a materialização. No projeto de referência (ADR-005):

- consultas síncronas: port no consumidor + API pública do módulo dono, chamada in-process;
- reações desacopladas: eventos publicados após o commit;
- REST interno entre módulos não é usado; OHS/REST descreve só uma possível extração futura para serviço.

Registre a materialização escolhida numa ADR e referencie-a no context map.

## Como desenhar

- Seta do upstream para o downstream, rótulo com `U/D` e padrão(ões), ex.: `U · OHS/PL → D · ACL`.
- Sistemas externos aparecem só se houver requisito ou decisão que os justifique.
- Uma nota no diagrama para cada mudança feita depois do workshop, com data.
