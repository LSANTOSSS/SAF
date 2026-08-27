# 07 — Especificação Funcional Consolidada

## Objetivo
Disponibilizar solução funcional para consulta e reserva de salas compartilhadas, reduzindo conflitos de agenda.

## Escopo incluído
- consultar disponibilidade;
- filtrar por capacidade;
- criar reserva individual;
- impedir sobreposição;
- alterar reserva futura;
- cancelar própria reserva futura;
- consultar próprias reservas;
- registrar indisponibilidade;
- cancelamento administrativo com motivo.

## Fora do escopo
- recorrência;
- cobrança;
- calendários externos;
- controle de acesso físico;
- definição de arquitetura/tecnologia;
- regras de organização real.

## Atores
**Colaborador:** consulta, cria, altera e cancela próprias reservas.  
**Administrador:** gerencia indisponibilidade e pode cancelar reserva de terceiro com justificativa.

## Estados funcionais mínimos
- **CONFIRMADA:** bloqueia disponibilidade.
- **CANCELADA:** não bloqueia mais.
- **CONCLUÍDA:** período encerrado.

A forma de persistir ou calcular esses estados é decisão de implementação.

## Fluxo principal
1. Colaborador informa data, início, fim e participantes opcionais.
2. Sistema busca salas elegíveis.
3. Colaborador seleciona sala.
4. Sistema revalida disponibilidade.
5. Se regras forem atendidas, cria a reserva.
6. Sistema confirma o resultado.

## Exceções principais
- conflito;
- duração acima de 4 horas;
- antecedência acima de 90 dias;
- sala indisponível;
- concorrência simultânea.

## Validação do MER
- **Clareza:** comportamentos centrais possuem resultado observável.
- **Completude:** principais alternativas e exceções estão cobertas.
- **Consistência:** critérios não introduzem regras divergentes.
- **Verificabilidade:** requisitos centrais são testáveis.
- **Rastreabilidade:** decisões relevantes ligam gaps a requisitos.
- **Incerteza:** recorrência foi explicitamente excluída, não escondida.

## Revisão final
Nenhum gap crítico permanece aberto dentro do escopo definido.

O case demonstra:

```text
demanda incompleta → análise explícita → decisão humana → requisito verificável
```
