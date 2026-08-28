# Contrato de validações

Validações automatizadas aumentam confiabilidade operacional, mas não substituem revisão funcional.

## Classes

### Estrutural
Pode verificar arquivo obrigatório ausente, documento vazio, título obrigatório ausente, identificadores duplicados e seção esperada ausente.

### Referencial
Pode verificar links locais quebrados, arquivo inexistente, identificador citado sem correspondente e caminhos inválidos.

### Consistência documental
Pode sinalizar requisitos sem critério de aceite quando exigido, gaps críticos abertos, rastreabilidade incompleta e versão ou status incompatível.

### Segurança de publicação
Pode procurar padrões de risco conhecidos, mas não garante ausência de informação sensível. Checklist de publicação e revisão humana continuam obrigatórios.

## Severidade

| Nível | Efeito |
|---|---|
| Erro | bloqueia entrega considerada válida |
| Aviso | exige revisão |
| Informação | registra observação |

## Não correção silenciosa
A automação pode detectar e reportar. Não deve modificar automaticamente regra, requisito, decisão ou evidência para fazer a validação passar.
