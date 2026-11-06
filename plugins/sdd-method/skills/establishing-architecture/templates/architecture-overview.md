# Visão geral da arquitetura

| Campo | Valor |
|---|---|
| Atualizado em | `<AAAA-MM-DD>` |
| Decisões | `<ADRs de estrutura, stack, banco, ambientes>` |

## 1. Contexto (C4 nível 1)

```mermaid
flowchart LR
  customer(["Cliente"])
  staff(["Atendente / Técnico"])
  system["Sistema <nome><br/>API REST"]
  email[/"Servidor SMTP (externo)"/]

  customer -->|"acompanha o status, aprova orçamento"| system
  staff -->|"abre e executa ordens de serviço"| system
  system -->|"envia notificações"| email
```

Só entram pessoas e sistemas externos que têm requisito ou decisão por trás.

## 2. Containers (C4 nível 2)

```mermaid
flowchart LR
  user(["Usuários"])
  subgraph app["<nome do sistema>"]
    api["API<br/><linguagem / framework>"]
    db[("Banco <tecnologia e versão><br/>schema por migrations")]
  end
  user -->|"HTTPS + token"| api
  api -->|"<protocolo>"| db
```

| Container | Responsabilidade | Tecnologia | Decisão |
|---|---|---|---|

## 3. Componentes / módulos (C4 nível 3)

Nível 3 ou quando a divisão interna precisa ser explicada. Um bloco por módulo e as relações do context map.

```mermaid
flowchart TB
  subgraph api["API"]
    m1["<módulo 1>"]
    m2["<módulo 2>"]
  end
  m1 -->|"API pública in-process"| m2
  m2 -.->|"evento após commit"| m1
```

## 4. Implantação

```mermaid
flowchart LR
  subgraph env["<ambiente: local · nuvem>"]
    app["<workload> · <réplicas / escala>"]
    db[("<banco gerenciado ou em cluster>")]
  end
  registry[("Registro de imagens")]
  registry -->|"pull :<tag>"| app
  app --> db
```

| Ambiente | Para que serve | Como é criado | Guia |
|---|---|---|---|

## 5. Decisões

| ADR | Decide |
|---|---|
