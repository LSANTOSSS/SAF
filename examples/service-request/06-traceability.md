# 06 — Matriz de Rastreabilidade

| Origem | Evidência/Inferência | Gap | Decisão | Requisito | Critério |
|---|---|---|---|---|---|
| SRC-001 | EVD-001 | GAP-007 | DEC-007 | RF-001, RN-006 | CA-001, CA-002 |
| SRC-001 | EVD-002 | GAP-002 | DEC-002 | RF-002, RF-003, RN-002 | CA-003, CA-004 |
| SRC-001 | EVD-003 | GAP-010 | DEC-010 | RF-010 | CA-013 |
| SRC-002 | EVD-004, HYP-002 | GAP-001 | DEC-001 | RN-001 | criação/prioridade |
| SRC-002 | EVD-006 | GAP-003 | DEC-003 | RN-003 | CA-014 |
| SRC-002 | EVD-007, INF-002 | GAP-004 | DEC-004 | RF-006, RN-004 | CA-007, CA-008 |
| SRC-002 | EVD-008 | GAP-005 | DEC-005 | RF-007, RN-005 | CA-009, CA-010 |
| SRC-002 | EVD-009 | GAP-006 | DEC-006 | RF-009, RN-009 | CA-012 |
| SRC-002 | HYP-001 | GAP-007 | DEC-007 | RF-001, RN-006 | CA-001 |
| SRC-002 | INF-001 | GAP-008 | DEC-008 | RF-008, RN-007 | CA-011 |
| SRC-002 | — | GAP-009 | DEC-009 | RF-004, RN-008 | CA-005 |

## Leitura para trás

`CA-008 → RF-006 → RN-004 → DEC-004 → GAP-004 → EVD-007/INF-002 → SRC-002`

## Leitura para frente

`HYP-002 → GAP-001 → DEC-001/DEC-003 → RN-001/RN-003 → CA-014`

A hipótese de que prioridade poderia influenciar prazo não virou regra diretamente; ela passou por gap e decisões explícitas.
