# Matriz de Rastreabilidade — CentralBeer

Esta matriz relaciona as funcionalidades previstas para o CentralBeer com os casos de uso, entidades do modelo de dados, componentes da arquitetura e endpoints previstos da API REST.

O objetivo é manter correspondência entre os principais artefatos produzidos na Fase 1 e facilitar a verificação das decisões de projeto.

## Matriz

| Funcionalidade | Caso de Uso | Entidades envolvidas | Componente da arquitetura | Endpoint previsto |
|---|---|---|---|---|
| Autenticação e controle de acesso | UC01 - Autenticar-se | USUARIO | `usuarios` | — |
| Cadastro, consulta e manutenção de produtos | UC02 - Gerenciar produtos | PRODUTO, CATEGORIA | `produtos` | `GET /api/v1/produtos/` e `GET /api/v1/produtos/{id}/` |
| Entrada de mercadorias | UC03 - Registrar entrada de mercadorias | PRODUTO, MOVIMENTACAO_ESTOQUE, USUARIO | `estoque`, `produtos` | `GET /api/v1/estoque/` e `GET /api/v1/movimentacoes/` |
| Ajustes e correções de estoque | UC04 - Ajustar estoque | PRODUTO, MOVIMENTACAO_ESTOQUE, USUARIO | `estoque` | `GET /api/v1/estoque/` e `GET /api/v1/movimentacoes/` |
| Abertura de caixa | UC05 - Abrir caixa | CAIXA, USUARIO | `caixa` | `GET /api/v1/caixas/{id}/resumo/` |
| Registro e finalização de venda | UC06 - Registrar venda | VENDA, ITEM_VENDA, PAGAMENTO, PRODUTO, MOVIMENTACAO_ESTOQUE, CAIXA, USUARIO | `vendas`, `estoque`, `caixa`, `produtos` | `GET /api/v1/vendas/`, `GET /api/v1/vendas/{id}/` e `GET /api/v1/caixas/{id}/resumo/` |
| Retirada ou reforço de caixa | UC07 - Registrar retirada ou reforço de caixa | CAIXA, MOVIMENTACAO_CAIXA, USUARIO | `caixa` | `GET /api/v1/caixas/{id}/resumo/` |
| Fechamento e conferência do caixa | UC08 - Fechar caixa | CAIXA, CONFERENCIA_CAIXA, MOVIMENTACAO_CAIXA, VENDA, PAGAMENTO, USUARIO | `caixa`, `vendas`, `relatorios` | `GET /api/v1/caixas/{id}/resumo/` |
| Cancelamento integral de venda | UC09 - Cancelar venda | VENDA, MOVIMENTACAO_ESTOQUE, PRODUTO, CAIXA, USUARIO | `vendas`, `estoque`, `caixa` | `GET /api/v1/vendas/{id}/` e `GET /api/v1/movimentacoes/` |
| Consulta de relatórios | UC10 - Consultar relatórios | PRODUTO, MOVIMENTACAO_ESTOQUE, VENDA, ITEM_VENDA, PAGAMENTO, CAIXA, MOVIMENTACAO_CAIXA, CONFERENCIA_CAIXA | `relatorios` | `/api/v1/produtos/`, `/api/v1/estoque/`, `/api/v1/movimentacoes/`, `/api/v1/vendas/` e `/api/v1/caixas/{id}/resumo/` |
| Gerenciamento de usuários e permissões | UC11 - Gerenciar usuários e permissões | USUARIO | `usuarios` | — |
| Consulta por consumidores externos | UC12 - Consultar API REST | PRODUTO, MOVIMENTACAO_ESTOQUE, VENDA, ITEM_VENDA, PAGAMENTO, CAIXA | `API REST` | Todos os endpoints `GET` previstos em `/api/v1/` |
| Consulta de produto por código de barras | UC13 - Consultar dados de produto no Open Food Facts | PRODUTO | `integracoes`, `produtos` | API externa `GET /api/v3/product/{codigo}` |

## Observações

A API REST própria do CentralBeer será inicialmente destinada somente a consultas. Operações que alteram o estado do sistema, como cadastro, entrada de mercadorias, ajuste de estoque, abertura e fechamento de caixa, vendas e cancelamentos, serão executadas pela interface web protegida por autenticação e sessão do Django.

Por esse motivo, algumas funcionalidades possuem relação com endpoints `GET` utilizados para consultar seus resultados, mas não possuem endpoints de escrita previstos no contrato inicial da API.

A integração com o Open Food Facts é auxiliar ao cadastro de produtos. Os dados externos serão utilizados apenas como sugestão para informações como nome, marca e apresentação, permanecendo preço, estoque e demais informações operacionais sob responsabilidade do CentralBeer.
