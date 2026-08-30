# 07 — Especificação Funcional

## Objetivo

Registrar e aprovar solicitações de compra fictícias com alçadas, segregação de responsabilidades e histórico rastreável.

## Escopo

- criação e submissão;
- alçadas por valor;
- múltiplos níveis;
- bloqueio de autoaprovação;
- aprovação, rejeição e devolução;
- nova submissão;
- expiração;
- cancelamento;
- histórico;
- autorização final.

## Atores

| Ator | Responsabilidade |
|---|---|
| Solicitante | Criar, ajustar, submeter e acompanhar |
| Aprovador | Decidir dentro da alçada |
| Administrador | Configurar alçadas e exceções autorizadas |

## Alçadas fictícias

| Valor | Aprovação |
|---|---|
| Até R$ 5.000 | N1 |
| Acima de R$ 5.000 até R$ 20.000 | N2 |
| Acima de R$ 20.000 | N2 e N3 sequenciais |

## Regras centrais

- sem autoaprovação;
- devolução exige comentário;
- rejeição exige justificativa;
- pendência expira em 10 dias corridos;
- ajuste reinicia aprovação;
- cancelamento somente antes da autorização;
- autorização depende de todas as aprovações;
- eventos relevantes ficam no histórico.

## Fora do escopo

Execução da compra, fornecedores reais, pagamentos, contratos, estoque, contabilidade, integrações externas e decisão de aprovação por IA.

## Revisão humana

O case é demonstrativo. Automação e IA podem apoiar o SAF, mas decisões e aprovação permanecem humanas.
