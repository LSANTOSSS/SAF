# Segurança de Publicação

## Objetivo

Esta política define a fronteira entre experiência profissional e conteúdo público do SAF.

O projeto existe para demonstrar competências, métodos e raciocínio de análise de sistemas. Ele não existe para reproduzir ativos pertencentes a empregadores, clientes, fornecedores ou parceiros.

## Regra principal

**Experiência profissional pode gerar aprendizado.  
Aprendizado pode gerar método.  
Método pode gerar um exemplo público.  
O exemplo público não deve reproduzir o ativo corporativo que originou o aprendizado.**

## Conteúdo proibido

Não publicar:

- código-fonte proprietário;
- documentos internos;
- diagramas privados;
- credenciais;
- tokens;
- segredos;
- dados pessoais;
- dados de clientes;
- bases de dados reais;
- endpoints privados;
- nomes internos de sistemas quando não forem públicos;
- incidentes internos identificáveis;
- contratos privados;
- layouts confidenciais;
- regras de negócio não públicas;
- dumps ou trechos copiados de ambientes profissionais.

## Sanitização não é suficiente em todos os casos

Trocar nomes em um documento corporativo não transforma automaticamente esse documento em conteúdo público seguro.

Se estrutura, regras, integrações ou comportamento permitirem reconhecer ou reconstruir um sistema real, o artefato não deve ser publicado.

## Abordagem clean-room

Casos demonstrativos do SAF devem ser construídos de forma independente.

Um exemplo pode demonstrar competências aprendidas profissionalmente, mas deve utilizar:

- domínio fictício ou conteúdo público;
- entidades próprias;
- regras próprias;
- dados fictícios;
- integrações fictícias;
- decisões próprias;
- documentação escrita especificamente para o SAF.

## Conteúdo baseado em fontes públicas

É permitido produzir estudos de sistemas, normas, padrões ou domínios públicos quando:

- as fontes forem públicas;
- as fontes forem citadas quando necessário;
- nenhuma informação privada for adicionada;
- inferências forem identificadas como inferências.

## Checklist antes da publicação

Antes de publicar qualquer artefato, verificar:

- O conteúdo foi escrito especificamente para o SAF?
- Existe algum dado vindo diretamente de ambiente corporativo?
- Algum nome interno permaneceu no material?
- Alguma regra não pública está sendo exposta?
- O exemplo poderia permitir reconstruir um fluxo proprietário?
- Há credenciais, identificadores, URLs ou dados pessoais?
- As fontes utilizadas são públicas ou pertencem ao próprio SAF?
- Hipóteses e inferências estão identificadas?

Em caso de dúvida, o conteúdo não deve ser publicado até revisão.
