# Perfis de stack

Ponto de partida, não verdade absoluta. Ao escolher, confirme versão atual, manutenção e licença de cada ferramenta
(algumas bibliotecas populares mudaram de licença recentemente, como MediatR e FluentAssertions no .NET).

## Ferramentas por preocupação

| Preocupação | Java / Kotlin (Spring) | TypeScript (Node / NestJS) | Python (FastAPI / Django) | Go | C# (.NET) |
|---|---|---|---|---|---|
| Build e execução | Maven Wrapper (`./mvnw`) ou Gradle Wrapper | pnpm ou npm scripts | uv ou Poetry | `go` + Makefile | `dotnet` CLI |
| Regras de dependência (camadas e módulos) | Spring Modulith (`ApplicationModules.verify()`), ArchUnit | dependency-cruiser, eslint-plugin-boundaries, Nx module boundaries | import-linter (contratos de camada e de independência), Tach | pacotes `internal/`, go-arch-lint, depguard | NetArchTest, ArchUnitNET, um projeto por módulo |
| Teste de módulo isolado | `@ApplicationModuleTest` | Testes por módulo com fakes dos ports | Idem | Idem | Idem |
| Testes unitários | JUnit 5, AssertJ, Mockito | Vitest ou Jest | pytest | `testing`, testify | xUnit, NSubstitute |
| Integração com banco real | Testcontainers | Testcontainers for Node | testcontainers-python | testcontainers-go | Testcontainers for .NET |
| Testes HTTP | MockMvc, RestAssured | supertest | TestClient / httpx, Django test client | `net/http/httptest` | `WebApplicationFactory` |
| Cobertura | JaCoCo | Vitest coverage (v8) ou c8 | coverage.py, pytest-cov | `go test -coverprofile` | coverlet + ReportGenerator |
| Migrations | Flyway ou Liquibase | Prisma Migrate, Drizzle Kit, Knex | Alembic, Django migrations | golang-migrate, goose, Atlas | EF Core migrations, DbUp |
| Contrato de API gerado | springdoc-openapi | @nestjs/swagger, tsoa, zod-openapi | FastAPI (nativo), drf-spectacular | swaggo, oapi-codegen, ogen | Microsoft.AspNetCore.OpenApi, Swashbuckle, NSwag |
| Validação na borda | Bean Validation (Jakarta) | zod, class-validator | Pydantic | go-playground/validator | DataAnnotations, FluentValidation |
| Eventos in-process | `ApplicationEventPublisher` + listener após commit (Spring Modulith events) | @nestjs/event-emitter, EventEmitter2, outbox próprio | blinker, signals do Django, outbox próprio | Implementação própria, outbox | Notificações in-process próprias, outbox |
| Injeção de dependência | Spring, por construtor | NestJS DI, tsyringe ou manual | Composição manual (padrão nos estilos leves), dependency-injector | Construtores, wire ou fx | DI nativo do ASP.NET Core |
| Gerenciador de pacotes e lockfile | Maven/Gradle com versões fixadas | pnpm/npm com lockfile | uv (`uv.lock`) ou Poetry | Go modules (`go.sum`) | NuGet com lock file |
| Checagem de tipos | Compilador | `tsc --noEmit` (strict) | mypy ou pyright | Compilador, `go vet` | Compilador, nullable habilitado |
| Evals de IA | — | Runner próprio ou promptfoo | Runner próprio com pytest fora da suíte padrão | Runner próprio | Runner próprio |
| Lint e formatação | Spotless, Checkstyle, Error Prone | ESLint + Prettier, ou Biome | Ruff (lint e format), mypy | gofmt, golangci-lint | `dotnet format`, analyzers |
| SCA (dependências) | OWASP Dependency-Check, OSV-Scanner | `npm audit`, OSV-Scanner | pip-audit, OSV-Scanner | govulncheck | `dotnet list package --vulnerable`, OSV-Scanner |
| SAST (código) | Semgrep, SpotBugs + FindSecBugs, CodeQL | Semgrep, CodeQL | Bandit, Semgrep | gosec, Semgrep | Semgrep, CodeQL |
| DAST (aplicação) | OWASP ZAP API scan guiado pelo contrato | Idem | Idem | Idem | Idem |
| Imagem de container | Multi-stage, JRE slim ou distroless | Node slim | Python slim | distroless/static | ASP.NET runtime |

## Mapeamento de conceitos do método

| Conceito | Java / Kotlin | TypeScript | Python | Go | C# |
|---|---|---|---|---|---|
| Módulo (bounded context) | Pacote de topo | Pasta de topo / workspace | Pacote de topo | Pacote de topo com `internal/` | Projeto ou namespace |
| Aggregate root | Classe com estado privado e métodos de negócio | Classe com campos `private` / `#` | Classe; atributos "privados" por convenção, garantidos por teste | Struct com campos não exportados e construtor | Classe com setters privados |
| Value object | `record` validado no construtor | Classe imutável / `readonly`, ou tipo marcado | `@dataclass(frozen=True)` validado em `__post_init__` | Struct imutável com construtor | `record` ou `readonly record struct` |
| Port (contrato) | `interface` | `interface` | `Protocol` ou classe abstrata | `interface` definida no consumidor | `interface` |
| Dinheiro | `BigDecimal` + moeda | Biblioteca decimal (ex.: decimal.js) + moeda | `Decimal` + moeda | Inteiro em centavos ou biblioteca decimal | `decimal` + moeda |
| Transação do caso de uso | `@Transactional` no caso de uso | Unit of work no caso de uso | Sessão/UoW no caso de uso | Transação explícita no caso de uso | Unit of work / `DbContext` no caso de uso |

## Adicionar uma linguagem

1. Uma coluna nova nas duas tabelas.
2. Para cada linha, a ferramenta mais madura e mantida, com link da documentação no perfil do projeto.
3. Se não houver ferramenta de fronteira, defina a alternativa (teste que lê imports, projeto por módulo) e registre
   numa ADR.
4. Registre a mudança no `CHANGELOG.md` do método.
