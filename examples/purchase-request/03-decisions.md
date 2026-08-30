# 03 — Decisões

| ID | Gap | Decisão |
|---|---|---|
| DEC-001 | GAP-001 | Apenas Aprovador com alçada compatível pode aprovar |
| DEC-002 | GAP-002 | Até R$ 5.000 exige N1; acima de R$ 5.000 até R$ 20.000 exige N2; acima de R$ 20.000 exige N3 |
| DEC-003 | GAP-003 | Solicitante nunca pode autoaprovar |
| DEC-004 | GAP-004 | Aprovador pode devolver para ajuste com comentário obrigatório |
| DEC-005 | GAP-005 | Rejeição exige justificativa |
| DEC-006 | GAP-006 | Pendência expira após 10 dias corridos sem decisão |
| DEC-007 | GAP-007 | Eventos de decisão e ciclo entram no histórico |
| DEC-008 | GAP-008 | Alteração após devolução exige nova submissão e invalida aprovações anteriores |
| DEC-009 | GAP-009 | Acima de R$ 20.000 exige N2 e N3 sequencialmente |
| DEC-010 | GAP-010 | Solicitante pode cancelar antes da autorização final |

## Estados

`Rascunho`, `Pendente de aprovação`, `Devolvida`, `Rejeitada`, `Autorizada`, `Cancelada`, `Expirada`.
