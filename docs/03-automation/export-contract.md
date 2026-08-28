# Contrato de exportação

## Fluxo
```text
Fontes Markdown aprovadas
→ composição determinística
→ conversor
→ artefato derivado
→ verificação
```

## Formatos possíveis
- HTML;
- PDF;
- DOCX.

A primeira implementação não precisa suportar todos simultaneamente.

## Regras
1. O exportador não é fonte funcional.
2. A conversão não deve criar novas regras.
3. A ordem dos documentos deve ser conhecida.
4. Falhas devem ser explícitas.
5. O artefato deve ser regenerável.
6. O processo não deve depender de material privado ou ferramenta corporativa.
7. Arquivos temporários não são fonte.

## Identificação
Quando tecnicamente viável, a implementação deve relacionar o artefato à versão ou commit das fontes utilizadas.

## Fora da v0.5.0
A versão não fixa linguagem, biblioteca, CLI, formato de configuração ou ambiente de CI. Essas escolhas pertencem à implementação de referência.
