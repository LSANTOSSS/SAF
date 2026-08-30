# SAF — System Analysis Framework

> Engenharia de Requisitos, Análise de Sistemas, IA responsável e automação documental em um framework público, rastreável e executável.

## Em 60 segundos

O **SAF** demonstra como uma demanda incompleta pode evoluir até uma especificação funcional revisável sem transformar suposições em requisitos. O **MER — Método de Engenharia de Requisitos** é seu núcleo metodológico.

### O que este projeto demonstra

| Capacidade | Evidência |
|---|---|
| Engenharia de Requisitos | [`docs/01-mer/`](docs/01-mer/) |
| Análise ponta a ponta | [`examples/room-booking/`](examples/room-booking/) |
| Rastreabilidade | [`examples/room-booking/06-traceability.md`](examples/room-booking/06-traceability.md) |
| IA com revisão humana | [`docs/02-ai-applied/`](docs/02-ai-applied/) |
| Automação documental | [`automation/`](automation/) |
| Exportação Markdown → DOCX | [`automation/docx_exporter.py`](automation/docx_exporter.py) |
| Segurança de publicação | [`docs/00-governance/publication-safety.md`](docs/00-governance/publication-safety.md) |

## Como o SAF se conecta

```mermaid
flowchart LR
    A[Demanda] --> B[MER]
    B --> C[Especificação rastreável]
    D[IA aplicada] -. apoio com governança .-> B
    C --> E[Pipeline documental]
    E --> F[Validação]
    F --> G[Markdown / HTML / DOCX]
    H[Revisão humana] --> C
    H --> F
```

## Comece por aqui

1. [`MER`](docs/01-mer/README.md)
2. [`Case room-booking`](examples/room-booking/README.md)
3. [`Rastreabilidade`](examples/room-booking/06-traceability.md)
4. [`Governança de IA`](docs/02-ai-applied/README.md)
5. [`Automação`](automation/README.md)

### Quick start

Requer Python 3 e não utiliza dependências externas.

```bash
python automation/saf_pipeline.py examples/room-booking
```

A execução gera os artefatos configurados pelo case. Na v0.8.0, o exemplo público produz Markdown, HTML e DOCX.

## Princípio central

O MER diferencia fato, evidência, inferência, hipótese, gap, decisão e requisito. IA pode apoiar a análise, mas não substitui fontes, decisões ou revisão humana. A automação valida e deriva artefatos sem alterar silenciosamente o conteúdo funcional.

## Current version

**v0.8.0 — Document Export**

Esta versão adiciona uma implementação pública e clean-room de exportação Markdown → DOCX, testes automatizados e validação em CI, mantendo Markdown como fonte controlada.

## Segurança de publicação

O SAF não representa o processo interno de nenhuma empresa. Seus exemplos são independentes e fictícios. Veja [`publication-safety.md`](docs/00-governance/publication-safety.md).

## Roadmap e histórico

Consulte [`ROADMAP.md`](ROADMAP.md) e [`CHANGELOG.md`](CHANGELOG.md).

## Licença

MIT — consulte [`LICENSE`](LICENSE).
