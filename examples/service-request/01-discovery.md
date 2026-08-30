# 01 — Descoberta

## Identificação

- **Título:** Gestão de Solicitações de Serviço
- **Objetivo:** compreender a necessidade antes de definir o workflow funcional
- **Versão:** v0.9.0
- **Responsável:** case demonstrativo SAF

## Demanda

> Usuários precisam registrar solicitações de serviço, acompanhar o andamento e saber quando a demanda foi resolvida.

A demanda não define prioridade, responsáveis, estados, SLA, cancelamento, reabertura, histórico ou permissões administrativas.

## Resultado esperado

Permitir que uma solicitação tenha ciclo de vida rastreável desde a abertura até seu encerramento, com regras explícitas para responsabilidade, transições e comunicação de estado.

## Atores

| Ator | Interesse |
|---|---|
| Solicitante | Abrir e acompanhar suas solicitações |
| Atendente | Analisar, assumir e resolver solicitações |
| Administrador | Configurar categorias e atuar em exceções administrativas |

## Fontes

| ID | Fonte | Tipo | Referência | Observação |
|---|---|---|---|---|
| SRC-001 | Briefing fictício | Fonte primária | Demanda inicial | Define apenas objetivo geral |
| SRC-002 | Workshop fictício de descoberta | Fonte primária | Esta descoberta | Expõe dúvidas e necessidades de decisão |

## Evidências

| ID | Fonte | Evidência | Classificação | Observação |
|---|---|---|---|---|
| EVD-001 | SRC-001 | Usuários precisam registrar solicitações | Fato do case | Sustenta abertura |
| EVD-002 | SRC-001 | Usuários precisam acompanhar andamento | Fato do case | Sustenta consulta de status |
| EVD-003 | SRC-001 | O usuário deve saber quando a solicitação foi resolvida | Fato do case | Sustenta comunicação de resolução |
| EVD-004 | SRC-002 | A demanda não define prioridade | Fato da análise | Origina GAP-001 |
| EVD-005 | SRC-002 | A demanda não define estados nem transições | Fato da análise | Origina GAP-002 |
| EVD-006 | SRC-002 | A demanda não define prazo de atendimento | Fato da análise | Origina GAP-003 |
| EVD-007 | SRC-002 | A demanda não define reabertura | Fato da análise | Origina GAP-004 |
| EVD-008 | SRC-002 | A demanda não define cancelamento | Fato da análise | Origina GAP-005 |
| EVD-009 | SRC-002 | A demanda não define permissões administrativas | Fato da análise | Origina GAP-006 |

## Inferências e hipóteses

| ID | Tipo | Descrição | Como validar |
|---|---|---|---|
| HYP-001 | Hipótese | Categorias podem ajudar a direcionar solicitações | Submeter a decisão funcional |
| HYP-002 | Hipótese | Prioridade pode influenciar prazo alvo | Submeter a decisão funcional |
| INF-001 | Inferência | Mudanças de estado devem ficar registradas | Confirmar necessidade de auditoria |
| INF-002 | Inferência | Uma solicitação resolvida não deveria ser alterada livremente | Definir regra de reabertura |

## Fluxo preliminar

1. Solicitante informa categoria, título e descrição.
2. Sistema registra a solicitação.
3. Atendente analisa e assume o atendimento.
4. Solicitação percorre estados controlados.
5. Atendente registra a resolução.
6. Solicitante consulta o resultado.
7. Solicitação é encerrada ou reaberta conforme regra.

## Gaps identificados

GAP-001 prioridade; GAP-002 estados/transições; GAP-003 SLA; GAP-004 reabertura; GAP-005 cancelamento; GAP-006 permissões; GAP-007 categorias; GAP-008 histórico; GAP-009 atribuição de responsável; GAP-010 notificação de resolução.

## Próximos passos

Resolver os gaps por decisões explícitas antes de consolidar requisitos.
