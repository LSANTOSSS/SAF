# 06 — Matriz de Rastreabilidade

| Origem | Evidência/Hipótese | Gap | Decisão | Requisito | Critério |
|---|---|---|---|---|---|
| SRC-001 | EVD-001 | — | — | RF-001, RF-002 | CA-001, CA-003 |
| SRC-001 | EVD-002 | GAP-001 | DEC-001 | RF-003, RN-001 | CA-004, CA-005 |
| SRC-002 | EVD-004 | GAP-002 | DEC-002 | RN-002 | criação |
| SRC-002 | EVD-005 | GAP-003 | DEC-003 | RN-003 | criação |
| SRC-002 | EVD-006 | GAP-004 | DEC-004 | RF-005, RN-004 | CA-007 |
| SRC-002 | HYP-002 | GAP-005 | DEC-005 | fora do escopo | — |
| SRC-002 | — | GAP-006 | DEC-006 | RF-004 | CA-006 |
| SRC-002 | HYP-001 | GAP-007 | DEC-007 | RF-001, RN-005 | CA-002 |
| SRC-002 | INF-001 | GAP-008 | DEC-008 | RF-006, RN-006 | CA-008 |
| SRC-002 | — | GAP-009 | DEC-009 | RF-007, RN-007 | CA-009 |

## Leitura para trás
`CA-004 → RF-003 → RN-001 → DEC-001 → GAP-001 → EVD-002 → SRC-001`

## Leitura para frente
`HYP-001 → GAP-007 → DEC-007 → RF-001/RN-005 → CA-002`

A hipótese não virou requisito diretamente; passou por gap e decisão.
