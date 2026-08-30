# 03 — Decisões

| ID | Gap | Decisão | Racional |
|---|---|---|---|
| DEC-001 | GAP-001 | Prioridade será `Baixa`, `Normal`, `Alta` ou `Crítica`; `Normal` é padrão | Cria escala simples e verificável |
| DEC-002 | GAP-002 | Estados: `Aberta`, `Em análise`, `Em atendimento`, `Resolvida`, `Encerrada`, `Cancelada` | Torna o ciclo explícito |
| DEC-003 | GAP-003 | Prazo alvo: Baixa 5 dias úteis, Normal 3, Alta 1, Crítica 4 horas úteis | Demonstra SLA funcional por prioridade |
| DEC-004 | GAP-004 | Solicitação `Resolvida` pode ser reaberta pelo solicitante em até 5 dias corridos; depois deve ser `Encerrada` | Evita reabertura indefinida |
| DEC-005 | GAP-005 | Solicitante pode cancelar enquanto estiver `Aberta` ou `Em análise` | Evita cancelamento durante execução |
| DEC-006 | GAP-006 | Administrador pode alterar prioridade e responsável de qualquer solicitação, com justificativa obrigatória | Trata exceção administrativa com auditabilidade |
| DEC-007 | GAP-007 | Categoria é obrigatória; cada categoria pode ter fila responsável | Apoia direcionamento sem amarrar implementação |
| DEC-008 | GAP-008 | Toda mudança de estado, prioridade e responsável deve entrar no histórico funcional | Mantém rastreabilidade do ciclo |
| DEC-009 | GAP-009 | Um atendente pode assumir solicitação sem responsável; após assumir, torna-se responsável atual | Define ownership |
| DEC-010 | GAP-010 | Ao entrar em `Resolvida`, o sistema registra uma notificação funcional ao solicitante | Garante ciência do resultado |

## Transições aprovadas

| Origem | Destino permitido |
|---|---|
| Aberta | Em análise, Cancelada |
| Em análise | Em atendimento, Cancelada |
| Em atendimento | Resolvida |
| Resolvida | Encerrada, Em atendimento |
| Encerrada | — |
| Cancelada | — |

A transição `Resolvida → Em atendimento` representa reabertura válida conforme DEC-004.
