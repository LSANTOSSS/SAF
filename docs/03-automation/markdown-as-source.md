# Markdown como fonte

## Regra
No SAF, **Markdown é a fonte primária controlada do conteúdo documental**.

PDF, DOCX, HTML ou outros formatos gerados são derivados de uma versão conhecida dessa fonte.

## Benefícios
- versionamento em Git;
- revisão por diff;
- rastreabilidade;
- automação;
- portabilidade;
- leitura humana;
- separação entre conteúdo e apresentação.

## Fonte versus entrega
```text
Markdown versionado → transformação → formato de entrega
```

Alterações funcionais devem ocorrer primeiro no Markdown. Editar apenas o arquivo exportado cria divergência e não altera a fonte oficial.

## Metadados
Quando necessários, devem ser explícitos e estáveis, como título, versão, status, ordem de composição e identificador do case.

## Regra de sincronização
Se um artefato derivado divergir da fonte, prevalece o Markdown versionado e o artefato deve ser regenerado.
