# 04 — Requisitos

## Requisitos funcionais

| ID | Requisito | Sustentação |
|---|---|---|
| RF-001 | O sistema deve permitir ao solicitante criar uma solicitação com categoria, título e descrição | EVD-001, DEC-007 |
| RF-002 | O sistema deve permitir ao solicitante consultar suas solicitações e o estado atual | EVD-002, DEC-002 |
| RF-003 | O sistema deve controlar transições de estado conforme fluxo aprovado | DEC-002 |
| RF-004 | O sistema deve permitir que atendente assuma uma solicitação sem responsável | DEC-009 |
| RF-005 | O sistema deve permitir registrar resolução antes da mudança para `Resolvida` | EVD-003, DEC-002 |
| RF-006 | O sistema deve permitir reabertura válida de solicitação resolvida | DEC-004 |
| RF-007 | O sistema deve permitir cancelamento pelo solicitante somente nos estados aprovados | DEC-005 |
| RF-008 | O sistema deve preservar histórico funcional das mudanças relevantes | DEC-008 |
| RF-009 | O sistema deve permitir intervenção administrativa com justificativa | DEC-006 |
| RF-010 | O sistema deve registrar notificação funcional ao entrar em `Resolvida` | DEC-010 |

## Regras de negócio

| ID | Regra | Sustentação |
|---|---|---|
| RN-001 | Prioridade válida é Baixa, Normal, Alta ou Crítica; padrão Normal | DEC-001 |
| RN-002 | Apenas transições previstas em DEC-002 são aceitas | DEC-002 |
| RN-003 | Prazo alvo depende da prioridade conforme DEC-003 | DEC-003 |
| RN-004 | Reabertura pelo solicitante é permitida até 5 dias corridos após resolução | DEC-004 |
| RN-005 | Cancelamento pelo solicitante só é permitido em `Aberta` ou `Em análise` | DEC-005 |
| RN-006 | Categoria é obrigatória na criação | DEC-007 |
| RN-007 | Mudanças de estado, prioridade e responsável geram histórico | DEC-008 |
| RN-008 | Solicitação só pode ser assumida por atendente quando não houver responsável atual | DEC-009 |
| RN-009 | Alteração administrativa de prioridade ou responsável exige justificativa | DEC-006 |

## Requisitos não funcionais

| ID | Requisito |
|---|---|
| RNF-001 | Operações de transição devem preservar consistência para impedir estados conflitantes |
| RNF-002 | O histórico funcional deve permitir reconstruir a sequência de mudanças relevantes |
| RNF-003 | Mensagens de rejeição devem explicar a regra funcional violada sem expor detalhes internos de implementação |
