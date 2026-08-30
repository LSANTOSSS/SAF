# 04 — Requisitos

## Requisitos funcionais

| ID | Requisito |
|---|---|
| RF-001 | Permitir criar solicitação com itens, justificativa e valor estimado |
| RF-002 | Permitir submeter rascunho para aprovação |
| RF-003 | Determinar alçada conforme valor |
| RF-004 | Impedir autoaprovação |
| RF-005 | Permitir aprovar, rejeitar ou devolver conforme regras |
| RF-006 | Permitir nova submissão após ajuste |
| RF-007 | Expirar pendências conforme prazo |
| RF-008 | Preservar histórico funcional |
| RF-009 | Permitir cancelamento antes da autorização |
| RF-010 | Autorizar somente após todas as aprovações exigidas |

## Regras de negócio

| ID | Regra |
|---|---|
| RN-001 | Até R$ 5.000 requer N1; até R$ 20.000 requer N2; acima disso requer N2 e N3 |
| RN-002 | Solicitante não pode autoaprovar |
| RN-003 | Devolução exige comentário |
| RN-004 | Rejeição exige justificativa |
| RN-005 | Pendência expira após 10 dias corridos |
| RN-006 | Ajuste após devolução inicia novo ciclo |
| RN-007 | Cancelamento só ocorre antes da autorização |
| RN-008 | Autorização depende de todas as aprovações exigidas |
| RN-009 | Eventos relevantes entram no histórico |

## Requisitos não funcionais

| ID | Requisito |
|---|---|
| RNF-001 | A avaliação de alçada deve considerar o valor vigente |
| RNF-002 | O histórico deve permitir reconstruir decisões e responsáveis |
| RNF-003 | Rejeições funcionais não devem expor detalhes internos de implementação |
