# 01 — Descoberta

## Identificação
- **Título:** Reserva de salas compartilhadas
- **Objetivo:** compreender a necessidade antes de definir a solução funcional
- **Versão:** v0.3.0
- **Responsável:** case demonstrativo SAF

## Demanda
> Colaboradores precisam conseguir reservar salas compartilhadas para reuniões e evitar conflitos de uso.

A demanda inicial não define regras de antecedência, duração, cancelamento, recorrência, permissões ou tratamento de conflitos.

## Resultado esperado
Permitir que pessoas autorizadas encontrem uma sala adequada e reservem um intervalo sem sobreposição com outra reserva confirmada.

## Atores
| Ator | Interesse |
|---|---|
| Colaborador | Consultar disponibilidade, criar e cancelar suas reservas |
| Administrador de espaços | Manter salas disponíveis ou indisponíveis |
| Participante | Consultar informações essenciais da reserva |

## Fontes
| ID | Fonte | Tipo | Referência | Observação |
|---|---|---|---|---|
| SRC-001 | Briefing fictício | Fonte primária | Demanda inicial | Define apenas objetivo geral |
| SRC-002 | Workshop fictício de descoberta | Fonte primária | Esta descoberta | Gera perguntas, não decisões automáticas |

## Evidências
| ID | Fonte | Evidência | Classificação | Observação |
|---|---|---|---|---|
| EVD-001 | SRC-001 | Existe necessidade de reservar salas compartilhadas | Fato do case | Sustenta o escopo principal |
| EVD-002 | SRC-001 | Conflitos de uso devem ser evitados | Fato do case | Não define a regra exata |
| EVD-003 | SRC-001 | O ator primário é o colaborador | Fato do case | Não define perfis administrativos |
| EVD-004 | SRC-002 | A demanda não define duração máxima | Fato da análise | Origina GAP-002 |
| EVD-005 | SRC-002 | A demanda não define antecedência | Fato da análise | Origina GAP-003 |
| EVD-006 | SRC-002 | A demanda não define política de cancelamento | Fato da análise | Origina GAP-004 |

## Inferências e hipóteses
| ID | Tipo | Descrição | Como validar |
|---|---|---|---|
| HYP-001 | Hipótese | Usuários podem precisar filtrar salas por capacidade | Decisão funcional no case |
| HYP-002 | Hipótese | Reservas recorrentes podem ser desejadas | Avaliar escopo da primeira versão |
| INF-001 | Inferência | Sala indisponível administrativamente não deve aceitar novas reservas | Submeter a decisão explícita |
| INF-002 | Inferência | Cancelar reserva deveria liberar o horário | Submeter a decisão explícita |

## Fluxo preliminar
1. Colaborador informa data/horário.
2. Sistema apresenta salas disponíveis.
3. Colaborador escolhe uma sala.
4. Sistema verifica disponibilidade.
5. Reserva é registrada.
6. Resultado é apresentado.

## Gaps identificados
GAP-001 conflito; GAP-002 duração; GAP-003 antecedência; GAP-004 cancelamento; GAP-005 recorrência; GAP-006 alteração; GAP-007 capacidade; GAP-008 indisponibilidade; GAP-009 cancelamento de terceiros.

## Próximos passos
Resolver gaps por decisões explícitas antes de consolidar requisitos.
