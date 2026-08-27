# 05 — Critérios de Aceite

## CA-001 — Buscar salas por horário
**Dado** um intervalo válido  
**Quando** o colaborador consulta disponibilidade  
**Então** apenas salas sem conflito e sem indisponibilidade são apresentadas.

## CA-002 — Filtrar por capacidade
**Dado** 8 participantes  
**Quando** consulta disponibilidade  
**Então** salas com capacidade inferior a 8 não aparecem.

## CA-003 — Criar reserva
**Dado** sala disponível e regras atendidas  
**Quando** confirma  
**Então** a reserva é registrada como confirmada.

## CA-004 — Rejeitar conflito
**Dado** reserva 10:00–11:00  
**Quando** solicita 10:30–11:30 na mesma sala  
**Então** a nova reserva é rejeitada.

## CA-005 — Permitir adjacência
**Dado** reserva 10:00–11:00  
**Quando** solicita 11:00–12:00  
**Então** pode prosseguir se as demais regras forem atendidas.

## CA-006 — Revalidar alteração
**Dado** reserva futura  
**Quando** o responsável altera horário ou sala  
**Então** todas as regras de criação são reaplicadas.

## CA-007 — Cancelar e liberar
**Dado** reserva futura  
**Quando** o responsável cancela  
**Então** o intervalo deixa de ser bloqueado por ela.

## CA-008 — Bloquear indisponibilidade
**Dado** sala indisponível 14:00–18:00  
**Quando** solicita 15:00–16:00  
**Então** a reserva é rejeitada.

## CA-009 — Cancelamento administrativo
**Dado** cancelamento de reserva de terceiro  
**Quando** administrador confirma  
**Então** um motivo é obrigatório e registrado.

## CA-010 — Consultar reservas
**Dado** que existem reservas do colaborador  
**Quando** consulta suas reservas  
**Então** distingue futuras de históricas.
