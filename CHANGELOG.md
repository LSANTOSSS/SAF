# Changelog

## [1.0.0] — Stable Public Framework

- Consolidação do SAF como primeira versão pública estável.
- Inclusão de resultado final único para a validação dos três MER demonstrativos.
- Comparação transversal entre Room Booking, Service Request e Purchase Request.
- Formalização das capacidades estáveis e invariantes do framework.
- Hardening do pipeline para `pipeline.json` inválido ou estruturalmente incompatível.
- Bloqueio de fontes absolutas, parent traversal e caminhos fora do diretório do case.
- Inclusão de testes para configuração e fronteira de caminhos.
- Inclusão de `.gitignore` para artefatos derivados locais.
- Correção da alçada do terceiro case para explicitar N2 + N3 acima de R$ 20.000.
- Reposicionamento da experiência principal do portfólio para um único resultado consolidado.

## [0.10.0] — Third Case Study

- Inclusão do terceiro case demonstrativo do SAF: `purchase-request`.
- Demonstração do MER em um domínio fictício de aprovação de solicitações de compra.
- Inclusão de alçadas por valor, múltiplos níveis de aprovação e segregação de responsabilidade.
- Inclusão de devolução para ajuste, rejeição justificada, expiração, cancelamento e trilha de decisão.
- Demonstração de que hipóteses sobre alçadas passam por gaps e decisões antes de sustentar requisitos.
- Reutilização do mesmo pipeline documental para Markdown, HTML e DOCX.
- Atualização do GitHub Actions para validar os três cases públicos e seus DOCX.

## [0.9.0] — Second Case Study

- Inclusão do segundo case demonstrativo do SAF: `service-request`.
- Demonstração do MER em um domínio orientado a workflow e ciclo de vida.
- Inclusão de estados, prioridades, SLA, responsabilidade, reabertura, cancelamento e histórico funcional.
- Demonstração de rastreabilidade entre fontes, evidências, gaps, decisões, requisitos e critérios de aceite.
- Reutilização do mesmo pipeline documental para Markdown, HTML e DOCX, sem lógica específica para o domínio.
- Atualização do GitHub Actions para validar os dois cases públicos.

## [0.8.0] — Document Export

- Inclusão de DOCX como formato derivado do pipeline documental público.
- Criação de exporter DOCX clean-room usando somente Python standard library e Open XML.
- Suporte inicial a títulos, parágrafos, listas, blockquotes, tabelas, negrito e código inline.
- Inclusão de estilos, margens e rodapé de identificação do artefato gerado.
- Atualização do `room-booking` para gerar Markdown, HTML e DOCX.
- Inclusão de testes unitários para estrutura OOXML e tratamento de tabelas.
- Atualização do GitHub Actions para executar testes e validar a geração do DOCX.
- Preservação do Markdown versionado como fonte controlada e do gate de revisão humana.

## [0.7.0] — Portfolio Experience

- Reorganização do README para avaliação rápida por recrutadores, lideranças e profissionais técnicos.
- Inclusão de mapa visual do SAF em Mermaid.
- Inclusão de jornada recomendada de avaliação e quick start.
- Inclusão de GitHub Actions para executar o pipeline público do `room-booking`.
- Clarificação do Modelo de Confiança como status de sustentação de saídas de IA, sem competir com a taxonomia do MER.
- Reforço da narrativa profissional: Engenharia de Requisitos + Análise de Sistemas + IA responsável + automação.

## [0.6.0] — Automation Reference Implementation

- Primeira implementação executável do pipeline documental do SAF.
- Configuração explícita de fontes por `pipeline.json`.
- Descoberta determinística de artefatos.
- Validações estruturais e referenciais sem alteração de conteúdo funcional.
- Composição de Markdown consolidado.
- Exportação dependency-free para Markdown e HTML.
- Aplicação pública ao case fictício `room-booking`.
- Conclusão da Fase 5 — Automação.

## [0.5.0] — Documentation Pipeline

- Definição do pipeline documental do SAF.
- Formalização do Markdown como fonte primária controlada.
- Definição do contrato de validações automáticas.
- Definição da fronteira entre fonte e formatos de entrega.
- Estabelecimento da regra de não correção silenciosa.
- Preservação do gate humano.
- Preparação da implementação pública executável posterior.
- Correção da versão exibida na página inicial.

## [0.4.0] — AI Applied to Systems Analysis

- Conclusão da Fase 4 do roadmap.
- Governança pública para IA no MER.
- Estratégia de contexto mínimo, autorizado e rastreável.
- Regras de fontes e evidências.
- Modelo de confiança.
- Gate de revisão humana.
- Prompts seguros e genéricos.

## [0.3.1] — Templates & Checklists Completion

- Conclusão da Fase 2 do roadmap.
- Inclusão de template reutilizável para cases demonstrativos.
- Inclusão de template de especificação funcional.
- Inclusão de checklist de descoberta.
- Inclusão de checklist de revisão.
- Inclusão de checklist de publicação.
- Reforço da abordagem clean-room e do gate humano antes de publicação.

## [0.3.0] — First Case Study

- Primeiro case demonstrativo completo do SAF.
- Aplicação do MER a um domínio fictício de reserva de salas.
- Demonstração explícita da evolução de demanda, evidências, hipóteses e gaps até decisões e requisitos.
- Inclusão de requisitos funcionais, regras de negócio, requisitos não funcionais e critérios de aceite.
- Inclusão de rastreabilidade bidirecional no case.
- Consolidação de especificação funcional final.
- Atualização da página inicial para tornar a evolução do SAF imediatamente visível.
- Manutenção integral da abordagem pública e clean-room.

## [0.2.0] — MER Core

- Consolidação dos princípios públicos do Método de Engenharia de Requisitos.
- Detalhamento do fluxo operacional do MER.
- Introdução do modelo de evidências e classificação explícita de incerteza.
- Definição de rastreabilidade bidirecional.
- Definição do processo de revisão, validação e gate humano.
- Inclusão de templates para descoberta, gaps, decisões, requisitos, critérios de aceite e matriz de rastreabilidade.
- Reforço da IA como apoio sujeito a verificação, sem autoridade de decisão ou aprovação.
- Manutenção da abordagem pública e clean-room do SAF.

## [0.1.0] — Foundation

- Fundação do System Analysis Framework.
- MER definido como núcleo metodológico do SAF.
- Manifesto inicial do projeto.
- Política de segurança de publicação e abordagem clean-room.
- Governança inicial para agentes de IA.
- Roadmap de evolução.
- Estrutura inicial para casos demonstrativos.
