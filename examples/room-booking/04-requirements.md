# 04 — Requisitos

## RF-001 — Consultar disponibilidade
O sistema deve permitir consulta por data, horário inicial e final. Quando participantes forem informados, deve considerar capacidade mínima.

## RF-002 — Criar reserva
O sistema deve permitir criar reserva para sala disponível, registrando responsável, sala, início, fim e finalidade opcional.

## RF-003 — Impedir conflito
O sistema deve rejeitar reserva sobreposta a outra reserva confirmada da mesma sala.

## RF-004 — Alterar reserva
O responsável deve poder alterar sala, início ou fim antes do início, reaplicando validações de criação.

## RF-005 — Cancelar própria reserva
O responsável deve poder cancelar sua reserva antes do início, liberando o intervalo.

## RF-006 — Administrar indisponibilidade
Administrador deve poder registrar período de indisponibilidade; novas reservas devem ser bloqueadas nesse período.

## RF-007 — Cancelar reserva de terceiro
Administrador deve poder cancelar reserva de terceiro com motivo obrigatório.

## RF-008 — Consultar próprias reservas
Colaborador deve poder consultar reservas futuras e histórico.

## Regras de negócio

### RN-001 — Sobreposição
Conflito quando `inicio_solicitado < fim_existente` e `fim_solicitado > inicio_existente`. Horários adjacentes são permitidos.

### RN-002 — Duração máxima
Máximo de 4 horas.

### RN-003 — Horizonte
Máximo de 90 dias de antecedência.

### RN-004 — Cancelamento
Responsável só cancela antes do início.

### RN-005 — Capacidade
Se participantes forem informados, capacidade da sala deve ser igual ou superior.

### RN-006 — Indisponibilidade
Nova reserva não pode ocupar período de indisponibilidade administrativa.

### RN-007 — Cancelamento administrativo
Cancelamento de terceiro exige administrador e motivo.

## Requisitos não funcionais

### RNF-001 — Consistência concorrente
Solicitações simultâneas não podem resultar em duas reservas confirmadas conflitantes para a mesma sala.

### RNF-002 — Auditabilidade funcional
Criação, alteração e cancelamento devem preservar ação, responsável e momento.

### RNF-003 — Clareza de erro
Rejeições funcionais devem informar motivo compreensível sem expor detalhes internos.
