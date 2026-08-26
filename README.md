# SAF — System Analysis Framework

> Um framework pessoal e público para demonstrar como problemas de negócio podem ser transformados em requisitos claros, rastreáveis e validáveis.

## Sobre o projeto

O **SAF (System Analysis Framework)** organiza práticas de Análise de Sistemas, Engenharia de Requisitos, uso responsável de Inteligência Artificial e automação documental em um fluxo único e reutilizável.

O projeto tem dois objetivos principais:

1. servir como portfólio público de competências em análise de sistemas e engenharia de requisitos;
2. evoluir como referência prática para condução de descoberta, análise, decisão, especificação, validação e revisão.

O SAF não representa o processo interno de nenhuma empresa. Seu conteúdo público é desenvolvido de forma independente, com exemplos fictícios e materiais próprios.

## Núcleo metodológico: MER

O **MER — Método de Engenharia de Requisitos** é o núcleo metodológico do SAF.

Fluxo conceitual:

```text
Demanda
  ↓
Fontes e Evidências
  ↓
Descoberta
  ↓
Análise
  ↓
Gaps
  ↓
Decisões
  ↓
Requisitos
  ↓
Cenários
  ↓
Validação
  ↓
Especificação
  ↓
Revisão
```

O método busca manter explícita a diferença entre:

- fato;
- evidência;
- inferência;
- hipótese;
- gap;
- decisão;
- requisito.

A premissa central é simples: **IA pode apoiar a análise, mas não substitui fontes, evidências, validação humana ou responsabilidade profissional.**

## Estrutura do SAF

```text
SAF
├── MER
│   └── metodologia de Engenharia de Requisitos
├── Casos demonstrativos
│   └── aplicação prática em cenários fictícios
├── Governança de IA
│   └── uso de IA com fontes, evidências e revisão humana
├── Templates e checklists
│   └── artefatos reutilizáveis
└── Automação
    └── ferramentas para reduzir trabalho operacional
```

## O que este repositório pretende demonstrar

O SAF foi desenhado para tornar observáveis competências que normalmente ficam restritas ao trabalho cotidiano de um analista:

- descoberta e entendimento de problemas;
- levantamento e organização de requisitos;
- análise de sistemas existentes;
- identificação de gaps e conflitos;
- modelagem de regras de negócio;
- critérios e cenários de aceite;
- rastreabilidade entre decisões e requisitos;
- comunicação entre negócio e tecnologia;
- documentação funcional;
- uso responsável de IA em atividades técnicas;
- automação de tarefas documentais.

## Segurança de publicação

Este projeto adota uma política explícita de separação entre experiência profissional e propriedade das organizações.

Não são publicados:

- código proprietário;
- documentação interna;
- arquitetura privada;
- credenciais ou segredos;
- dados de clientes;
- incidentes internos;
- nomes de serviços privados;
- regras de negócio confidenciais;
- artefatos copiados de ambientes corporativos.

Os exemplos públicos são criados de forma independente e fictícia.

Veja [`docs/00-governance/publication-safety.md`](docs/00-governance/publication-safety.md).

## Estado atual

**Fase:** Fundação

O repositório está sendo construído de forma incremental. A primeira etapa estabelece identidade, governança, segurança de publicação e apresentação inicial do MER.

Consulte o [`ROADMAP.md`](ROADMAP.md) para acompanhar as próximas etapas.

## Licença

Este projeto é disponibilizado sob a licença MIT. Consulte [`LICENSE`](LICENSE).
