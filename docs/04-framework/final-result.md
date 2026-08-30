# Resultado Final — Validação do SAF com três MER

## Objetivo

Esta é a conclusão única da prova pública de reutilização do SAF.

Os três cases permanecem disponíveis com seus artefatos completos, mas este documento consolida o resultado: **o mesmo método foi aplicado a três problemas funcionalmente distintos sem introduzir lógica de domínio no framework ou no pipeline**.

## Três demandas, um método

| Case | Problema central | Capacidades demonstradas |
|---|---|---|
| Room Booking | Reserva de recurso compartilhado | disponibilidade, conflito, intervalo temporal, capacidade e cancelamento |
| Service Request | Gestão do ciclo de uma solicitação | estados, transições, prioridade, SLA, responsabilidade, reabertura e histórico |
| Purchase Request | Aprovação de uma solicitação | alçadas, múltiplos níveis, segregação de responsabilidade, devolução, rejeição e trilha de decisão |

## O que permaneceu invariável

Nos três MER, o SAF preservou a mesma sequência de raciocínio:

1. a demanda foi tratada como ponto de partida, não como especificação;
2. fontes e evidências foram explicitadas;
3. incertezas permaneceram visíveis;
4. hipóteses não se tornaram requisitos diretamente;
5. gaps foram registrados antes das decisões;
6. decisões funcionais passaram a sustentar regras e requisitos;
7. critérios de aceite tornaram o comportamento verificável;
8. a rastreabilidade permitiu navegar da origem ao resultado e no sentido inverso;
9. a revisão humana permaneceu como gate;
10. o mesmo pipeline processou os três conjuntos documentais.

## O que mudou conforme o domínio

O método não impôs as regras dos cases.

No **Room Booking**, a análise precisou resolver sobreposição, adjacência, antecedência, duração e indisponibilidade.

No **Service Request**, o centro passou a ser ciclo de vida: estados, transições, prioridade, prazo-alvo, responsabilidade e reabertura.

No **Purchase Request**, a análise exigiu autoridade decisória: alçadas, segregação, múltiplos níveis, devolução, rejeição e expiração.

Essa variação é parte da evidência de reutilização: o SAF fornece estrutura para análise sem substituir a descoberta do domínio.

## Evidência metodológica

Exemplos dos três cases mostram a mesma propriedade:

```text
Hipótese → Gap → Decisão → Regra/Requisito → Critério de aceite
```

Uma hipótese pode orientar investigação, mas não recebe autoridade funcional por ter sido sugerida por uma pessoa, automação ou IA.

## Evidência de automação

Cada case declara suas fontes em `pipeline.json`. O pipeline:

- descobre apenas as fontes configuradas;
- executa validações;
- compõe o documento derivado;
- gera formatos solicitados;
- não corrige silenciosamente regras funcionais;
- não contém regras específicas de Room Booking, Service Request ou Purchase Request.

A v1.0 adiciona validação defensiva de configuração e caminhos para tornar esse contrato mais seguro.

## Conclusão

A prova demonstra três propriedades do SAF:

**Repetibilidade.** A mesma estrutura metodológica pode ser aplicada novamente.

**Adaptabilidade.** O conteúdo funcional muda de acordo com o problema, sem exigir que o método incorpore regras do domínio.

**Rastreabilidade.** O resultado pode ser relacionado às evidências, gaps e decisões que o sustentam.

### Resultado

> **Três demandas distintas. Um mesmo método. Três especificações rastreáveis. Um único resultado de validação do SAF.**

A v1.0.0 consolida essa evidência como a primeira versão pública estável do framework.
