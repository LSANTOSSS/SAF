# 06 — Matriz de Rastreabilidade

| Origem | Evidência/Inferência | Gap | Decisão | Requisito | Critério |
|---|---|---|---|---|---|
| SRC-001 | EVD-001 | — | — | RF-001 | CA-001 |
| SRC-002 | EVD-004, HYP-001 | GAP-002 | DEC-002 | RF-003, RN-001 | CA-002, CA-003, CA-004 |
| SRC-002 | EVD-005 | GAP-003 | DEC-003 | RF-004, RN-002 | CA-005 |
| SRC-002 | EVD-006 | GAP-004 | DEC-004 | RF-005, RN-003 | CA-006 |
| SRC-002 | EVD-007 | GAP-005 | DEC-005 | RF-005, RN-004 | CA-007 |
| SRC-002 | EVD-008 | GAP-006 | DEC-006 | RF-007, RN-005 | CA-009 |
| SRC-002 | EVD-009, INF-001 | GAP-007 | DEC-007 | RF-008, RN-009 | CA-010 |
| SRC-002 | INF-002 | GAP-008 | DEC-008 | RF-006, RN-006 | CA-008 |
| SRC-002 | HYP-002 | GAP-009 | DEC-009 | RF-010, RN-008 | CA-013, CA-014 |
| SRC-002 | — | GAP-010 | DEC-010 | RF-009, RN-007 | CA-011, CA-012 |

## Exemplo

`CA-014 → RF-010 → RN-008 → DEC-009 → GAP-009 → HYP-002 → SRC-002`

A hipótese de múltiplas alçadas não virou requisito diretamente.
