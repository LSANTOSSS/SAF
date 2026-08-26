# Manifesto SAF

O SAF nasce da ideia de que Análise de Sistemas não deve ser invisível.

Grande parte do trabalho de um analista acontece antes do código: entender um problema, localizar fontes, confrontar informações, identificar lacunas, organizar decisões e transformar tudo isso em uma especificação que negócio e tecnologia consigam compreender.

O SAF busca tornar esse processo explícito, reproduzível e demonstrável.

## Princípios

### 1. Entender antes de especificar

Um requisito bem escrito não corrige uma descoberta mal executada.

Antes de documentar uma solução, é necessário compreender problema, contexto, atores, restrições, fontes e comportamento existente.

### 2. Evidência antes de inferência

Conhecimento confirmado e interpretação provável não são a mesma coisa.

O método deve deixar visível quando algo é:

- fato;
- evidência;
- inferência;
- hipótese;
- gap;
- decisão.

### 3. Gaps são informação

Uma lacuna conhecida é melhor do que uma certeza inventada.

Quando algo ainda não foi decidido ou comprovado, o processo deve registrar a pendência em vez de escondê-la dentro de um requisito.

### 4. Requisitos devem ser rastreáveis

Uma decisão relevante deve conseguir explicar quais requisitos foram impactados.

Um requisito importante deve conseguir apontar de onde surgiu.

### 5. Funcional não é implementação

A especificação funcional deve explicar comportamento, resultado esperado e restrições.

Detalhes de implementação entram quando são necessários para compreensão, contrato de integração ou decisão arquitetural — não para substituir a análise funcional.

### 6. IA é apoio, não autoridade

IA pode acelerar investigação, organização, revisão e escrita.

Ela não substitui:

- fonte oficial;
- evidência;
- especialista;
- validação;
- aprovação;
- responsabilidade humana.

### 7. Documentação deve permanecer útil

Documentação existe para reduzir ambiguidade e preservar entendimento.

Quantidade de páginas não é sinônimo de qualidade.

### 8. Conhecimento deve sobreviver à demanda

Ao final de uma entrega, parte do aprendizado deve continuar reutilizável em novas análises, sem depender exclusivamente da memória de quem participou do projeto.

## Resultado esperado

O SAF pretende conectar:

```text
Problema
   ↓
Conhecimento
   ↓
Evidência
   ↓
Análise
   ↓
Decisão
   ↓
Requisito
   ↓
Validação
   ↓
Entrega
```

O objetivo não é criar burocracia.

É tornar decisões melhores, requisitos mais claros e sistemas mais compreensíveis.
