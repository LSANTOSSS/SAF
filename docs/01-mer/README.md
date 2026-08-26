# MER — Método de Engenharia de Requisitos

O **MER** é o núcleo metodológico do SAF.

Seu objetivo é organizar a transformação de uma demanda inicial em uma especificação funcional clara, rastreável e validável.

## Problema que o MER busca resolver

Demandas raramente chegam como requisitos completos.

Elas podem chegar como:

- uma ideia;
- um incidente;
- uma necessidade de negócio;
- uma mudança regulatória;
- uma integração;
- uma solicitação de cliente;
- um comportamento observado em sistema legado;
- uma divergência entre documentação e implementação.

O risco é transformar essas entradas diretamente em solução sem compreender o contexto.

O MER introduz uma camada estruturada de descoberta e análise antes da especificação.

## Fluxo

```text
Demanda
  ↓
Fontes e Evidências
  ↓
Descoberta
  ↓
Análise
  ↓
Gaps
  ↓
Decisões
  ↓
Requisitos
  ↓
Cenários
  ↓
Validação
  ↓
Especificação
  ↓
Revisão
```

O fluxo é orientativo, não um processo rigidamente linear. Uma descoberta pode reabrir uma decisão; uma validação pode revelar um novo gap; uma evidência pode alterar requisitos já escritos.

## Conceitos fundamentais

### Fonte

Origem de informação utilizada na análise.

Exemplos:

- documentação pública;
- norma;
- contrato de API;
- código autorizado para análise;
- especialista;
- artefato aprovado do próprio projeto.

### Evidência

Informação observável que suporta uma conclusão.

### Inferência

Conclusão plausível obtida a partir de evidências incompletas. Deve ser explicitamente identificada.

### Hipótese

Possibilidade ainda não confirmada utilizada temporariamente para avançar uma análise.

### Gap

Informação ausente, conflitante ou insuficiente que precisa de decisão ou investigação.

### Decisão

Escolha validada que resolve uma questão relevante do domínio ou da solução funcional.

### Requisito

Comportamento, capacidade, restrição ou qualidade esperada do sistema.

## Artefatos esperados

Dependendo da complexidade da demanda, o MER pode produzir:

- registro de descoberta;
- mapa de fontes;
- lista de gaps;
- log de decisões;
- requisitos funcionais;
- regras de negócio;
- requisitos não funcionais;
- cenários;
- critérios de aceite;
- rastreabilidade;
- especificação funcional.

Nem toda demanda exige todos os artefatos.

## IA dentro do MER

IA pode apoiar:

- organização de fontes;
- comparação de informações;
- identificação de inconsistências;
- formulação de perguntas;
- revisão de requisitos;
- avaliação de duplicidades;
- produção textual;
- análise de impacto.

IA não deve:

- inventar regra ausente;
- transformar hipótese em decisão;
- substituir uma fonte oficial;
- aprovar requisito;
- ocultar incerteza;
- publicar informação confidencial.

## Evolução

As próximas versões deste diretório detalharão cada etapa do método individualmente.
