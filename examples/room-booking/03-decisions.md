# 03 — Log de Decisões

Todas as decisões são fictícias e exclusivas deste case.

## DEC-001 — Sobreposição
- **Decisão:** existe conflito quando `inicio_solicitado < fim_existente` e `fim_solicitado > inicio_existente`.
- **Racional:** permite horários adjacentes.
- **Relacionados:** GAP-001, RF-003, RN-001

## DEC-002 — Duração máxima
- **Decisão:** reserva individual limitada a 4 horas.
- **Relacionados:** GAP-002, RN-002

## DEC-003 — Antecedência
- **Decisão:** reservas podem ser criadas com até 90 dias de antecedência.
- **Relacionados:** GAP-003, RN-003

## DEC-004 — Cancelamento
- **Decisão:** o responsável pode cancelar enquanto a reserva ainda não iniciou.
- **Relacionados:** GAP-004, RF-005, RN-004

## DEC-005 — Recorrência
- **Decisão:** recorrência fica fora da primeira versão.
- **Relacionados:** GAP-005

## DEC-006 — Alteração
- **Decisão:** reserva futura pode ser alterada pelo responsável; todas as validações são reaplicadas.
- **Relacionados:** GAP-006, RF-004

## DEC-007 — Capacidade
- **Decisão:** se a quantidade de participantes for informada, somente salas com capacidade suficiente aparecem.
- **Relacionados:** GAP-007, RF-001, RN-005

## DEC-008 — Indisponibilidade
- **Decisão:** período administrativo de indisponibilidade bloqueia novas reservas; reservas já existentes são sinalizadas para tratamento, sem cancelamento automático.
- **Relacionados:** GAP-008, RF-006, RN-006

## DEC-009 — Cancelamento administrativo
- **Decisão:** apenas administrador de espaços pode cancelar reserva de terceiro, com motivo obrigatório.
- **Relacionados:** GAP-009, RF-007, RN-007
