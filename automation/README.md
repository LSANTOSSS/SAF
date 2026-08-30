# SAF Automation Reference Implementation

Esta implementação pública demonstra o contrato definido em `docs/03-automation/` sem depender de bibliotecas externas.

## Executar

```bash
python automation/saf_pipeline.py examples/room-booking
```

## O que faz

1. lê `pipeline.json`;
2. descobre as fontes na ordem configurada;
3. valida presença, conteúdo e referências estruturais;
4. compõe um Markdown consolidado;
5. exporta Markdown e HTML;
6. retorna um status explícito.

## Limites deliberados

- não corrige conteúdo funcional;
- não toma decisões;
- não usa IA para validar regras;
- não acessa fontes externas;
- não depende de material privado;
- o HTML é propositalmente básico e dependency-free.

A implementação é uma prova de reprodutibilidade do processo documental, não um substituto da revisão humana.
