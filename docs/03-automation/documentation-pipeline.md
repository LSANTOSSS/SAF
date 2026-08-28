# Pipeline documental

## Visão

```text
Entrada
↓
Descoberta de arquivos
↓
Validação estrutural e referencial
↓
Composição
↓
Exportação
↓
Verificação do artefato
↓
Gate humano
```

## Entrada
A entrada é um conjunto explicitamente selecionado de arquivos Markdown pertencentes ao SAF ou a um case público independente. O pipeline não deve procurar conteúdo privado fora do escopo configurado.

## Descoberta
A automação identifica arquivos participantes e sua ordem lógica. A mesma entrada e configuração devem produzir o mesmo conjunto de fontes.

## Validação
O pipeline executa verificações estruturais e de referências. Validação não deve inventar conteúdo nem alterar decisões funcionais.

## Composição
Arquivos aprovados são ordenados e combinados. Composição não significa reinterpretar o conteúdo.

## Exportação
A fonte Markdown pode ser convertida para formatos de distribuição. Artefatos exportados são derivados e não substituem a fonte.

## Verificação
Após exportar, confirmar existência, formato esperado, ausência de falha reportada e relação conhecida com as fontes utilizadas.

## Gate humano
A existência de um artefato exportado não equivale a aprovação. Publicação ou entrega permanecem condicionadas à revisão humana.

## Propriedades desejadas
- determinismo;
- repetibilidade;
- rastreabilidade;
- falha explícita;
- mínima transformação semântica;
- independência entre conteúdo e ferramenta de exportação.
