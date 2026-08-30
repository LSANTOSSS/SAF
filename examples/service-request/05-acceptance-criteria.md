# 05 — Critérios de Aceite

| ID | Critério | Requisito |
|---|---|---|
| CA-001 | Dado um solicitante autorizado, quando informar categoria, título e descrição válidos, então a solicitação deve ser criada em `Aberta` | RF-001, RN-006 |
| CA-002 | Dada criação sem categoria, quando tentar registrar, então a operação deve ser rejeitada | RF-001, RN-006 |
| CA-003 | Dada uma solicitação do usuário, quando consultada, então deve apresentar estado atual e dados essenciais | RF-002 |
| CA-004 | Dada uma transição não prevista, quando solicitada, então deve ser rejeitada | RF-003, RN-002 |
| CA-005 | Dada solicitação sem responsável, quando atendente assumir, então ele deve tornar-se responsável atual | RF-004, RN-008 |
| CA-006 | Dada solicitação em atendimento, quando atendente registrar resolução, então ela pode passar para `Resolvida` | RF-005 |
| CA-007 | Dada solicitação resolvida há até 5 dias, quando o solicitante reabrir, então deve retornar a `Em atendimento` | RF-006, RN-004 |
| CA-008 | Dada solicitação resolvida há mais de 5 dias, quando houver tentativa de reabertura, então deve ser rejeitada | RF-006, RN-004 |
| CA-009 | Dada solicitação em `Aberta`, quando solicitante cancelar, então deve passar para `Cancelada` | RF-007, RN-005 |
| CA-010 | Dada solicitação em `Em atendimento`, quando solicitante tentar cancelar, então a operação deve ser rejeitada | RF-007, RN-005 |
| CA-011 | Dada mudança de estado, prioridade ou responsável, quando concluída, então o histórico deve registrar a alteração | RF-008, RN-007 |
| CA-012 | Dada intervenção administrativa em prioridade ou responsável, quando não houver justificativa, então a operação deve ser rejeitada | RF-009, RN-009 |
| CA-013 | Dada solicitação que entra em `Resolvida`, então uma notificação funcional deve ser registrada para o solicitante | RF-010 |
| CA-014 | Dada prioridade `Crítica`, então o prazo alvo deve ser 4 horas úteis | RN-003 |
