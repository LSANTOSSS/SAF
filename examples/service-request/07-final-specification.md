# 07 — Especificação Funcional

## 1. Objetivo

Disponibilizar uma solução fictícia para registrar, acompanhar e tratar solicitações de serviço com ciclo de vida, responsabilidade, prioridade e histórico controlados.

## 2. Escopo

A primeira versão contempla:

- criação e consulta de solicitações;
- categoria obrigatória;
- prioridade;
- workflow de estados;
- atribuição de responsável;
- resolução e reabertura;
- cancelamento controlado;
- histórico funcional;
- intervenção administrativa;
- registro de notificação de resolução.

## 3. Fora do escopo

- integração com e-mail, SMS ou mensageria externa;
- catálogo comercial de serviços;
- faturamento;
- contratos;
- automação por IA;
- escalonamento técnico entre sistemas externos.

## 4. Atores

| Ator | Responsabilidade |
|---|---|
| Solicitante | Criar, acompanhar, cancelar quando permitido e reabrir quando permitido |
| Atendente | Assumir, analisar, atender e resolver |
| Administrador | Atuar em exceções autorizadas e configuração funcional |

## 5. Estados

`Aberta → Em análise → Em atendimento → Resolvida → Encerrada`

Caminhos adicionais controlados:

- `Aberta → Cancelada`
- `Em análise → Cancelada`
- `Resolvida → Em atendimento` quando houver reabertura válida

`Encerrada` e `Cancelada` são estados finais.

## 6. Prioridade e prazo alvo

| Prioridade | Prazo alvo |
|---|---|
| Baixa | 5 dias úteis |
| Normal | 3 dias úteis |
| Alta | 1 dia útil |
| Crítica | 4 horas úteis |

A prioridade padrão é `Normal`.

## 7. Regras principais

- categoria é obrigatória;
- transições fora do fluxo aprovado são rejeitadas;
- atendente só assume solicitação sem responsável;
- reabertura pelo solicitante ocorre até 5 dias corridos após resolução;
- cancelamento pelo solicitante ocorre apenas em `Aberta` ou `Em análise`;
- alterações de estado, prioridade e responsável entram no histórico;
- alterações administrativas de prioridade ou responsável exigem justificativa;
- entrada em `Resolvida` registra notificação funcional ao solicitante.

## 8. Rastreabilidade

Os requisitos e critérios desta especificação derivam das decisões registradas após a resolução dos gaps. A matriz completa está em `06-traceability.md`.

## 9. Qualidade

O sistema deve preservar consistência nas transições, permitir reconstrução do histórico funcional e produzir erros compreensíveis sem expor detalhes internos.

## 10. Revisão humana

Este documento é um artefato demonstrativo do SAF. Mesmo em um fluxo apoiado por automação, decisões e aprovação permanecem responsabilidade humana.
