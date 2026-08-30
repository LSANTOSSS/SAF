# SAF Automation Reference Implementation

Esta implementação pública demonstra o contrato definido em `docs/03-automation/` com foco em reprodutibilidade e independência de ambientes privados.

## Executar

```bash
python automation/saf_pipeline.py examples/room-booking
```

## O que faz

1. lê `pipeline.json`;
2. descobre as fontes na ordem configurada;
3. valida presença, conteúdo e referências estruturais;
4. compõe um Markdown consolidado;
5. exporta os formatos derivados configurados;
6. retorna um status explícito por etapa e formato.

O case público `room-booking` demonstra exportação para **Markdown, HTML e DOCX**.

## DOCX público

O exporter DOCX foi criado especificamente para o SAF, em abordagem clean-room, usando apenas Python standard library e o formato Open XML.

O subconjunto suportado nesta versão inclui:

- títulos e subtítulos;
- parágrafos;
- listas simples;
- blockquotes;
- tabelas Markdown;
- negrito e código inline;
- estilos, margens e rodapé de identificação do artefato.

O DOCX é sempre um **artefato derivado**. O Markdown versionado permanece como fonte controlada.

## Limites deliberados

- não corrige conteúdo funcional;
- não toma decisões;
- não usa IA para validar regras;
- não acessa fontes externas;
- não depende de material ou templates privados;
- não integra armazenamento externo;
- não pretende implementar todo o Markdown nesta versão.

A implementação é uma prova de reprodutibilidade do processo documental, não um substituto da revisão humana.
