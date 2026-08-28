# Automação documental

Esta etapa do SAF define o contrato de um pipeline documental reproduzível, mantendo o Markdown como fonte primária e separando conteúdo, validação e formatos de entrega.

## Objetivo

```text
Markdown fonte
→ descoberta dos artefatos
→ validações
→ composição
→ exportação
→ artefato de entrega
```

A v0.5.0 define como o pipeline deve funcionar. A implementação executável de referência fica reservada para uma etapa posterior.

## Conteúdo
- [Pipeline documental](documentation-pipeline.md)
- [Markdown como fonte](markdown-as-source.md)
- [Contrato de validações](validation-contract.md)
- [Contrato de exportação](export-contract.md)

## Princípios
- conteúdo funcional permanece controlado em Markdown;
- formatos de entrega são derivados;
- validações detectam problemas, mas não corrigem regras silenciosamente;
- falhas bloqueantes impedem uma entrega considerada válida;
- rastreabilidade e segurança de publicação devem ser preservadas;
- revisão humana continua sendo o gate final.
