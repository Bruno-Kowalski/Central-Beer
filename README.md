# CentralBeer

**Gestão de estoque, vendas e caixa para distribuidoras de bebidas.**

![Status](https://img.shields.io/badge/status-planejamento-F5B82E)
![Versão](https://img.shields.io/badge/versão-0.0.1-171717)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-5.2_LTS-darkgreen)
![Banco](https://img.shields.io/badge/banco-SQLite-blue)

**Instituição:** CEUB  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Disciplina:** Desenvolvimento Web  
**Turma / Semestre:** Turma A / 2026.2  
**Professor(a):** Felippe Pires Ferreira  
**Status do projeto:** Em planejamento — Fase 1: documentação e arquitetura  

> As funcionalidades e decisões técnicas descritas representam o planejamento do projeto. A aplicação, os testes e os workflows serão implementados na Fase 2.

---

## Sumário

- [1. Descrição do projeto](#1-descrição-do-projeto)
- [2. Funcionalidades](#2-funcionalidades)
- [3. Demonstração](#3-demonstração)
- [4. Tecnologias utilizadas](#4-tecnologias-utilizadas)
- [5. Arquitetura](#5-arquitetura)
- [6. Organização dos diretórios](#6-organização-dos-diretórios)
- [7. Participantes](#7-participantes)
- [8. Como executar](#8-como-executar)
- [9. Configuração](#9-configuração)
- [10. Testes](#10-testes)
- [11. Uso de inteligência artificial](#11-uso-de-inteligência-artificial)
- [12. Contribuição e fluxo de trabalho](#12-contribuição-e-fluxo-de-trabalho)
- [13. Histórico de versões](#13-histórico-de-versões)
- [14. Limitações e próximos passos](#14-limitações-e-próximos-passos)
- [15. Licença, referências e contato](#15-licença-referências-e-contato)

---

## 1. Descrição do projeto

O CentralBeer é um projeto de aplicação web para gestão de distribuidoras de bebidas. A proposta surgiu da dificuldade do cliente em controlar o estoque, acompanhar entradas e saídas de mercadorias e localizar produtos com rapidez durante o atendimento.

O sistema reunirá cadastro de produtos, recebimento de mercadorias, vendas e controle de caixa. Ao finalizar uma venda, registrará os pagamentos e descontará automaticamente as quantidades vendidas do estoque. Os recebimentos serão separados por dinheiro, PIX, débito e crédito, permitindo a conferência no fechamento do caixa.

O estoque será mantido em unidades. Entradas e vendas poderão utilizar caixas fechadas, convertidas conforme a quantidade de unidades por caixa informada no cadastro de cada produto. A primeira versão atenderá um estabelecimento com um caixa aberto por vez, sem emissão fiscal ou integração com serviços de pagamento.

### Objetivos

- **Objetivo geral:** desenvolver uma aplicação web para organizar o estoque, as vendas e o caixa de uma distribuidora de bebidas.
- **Objetivos específicos:**
  - Centralizar o cadastro e a busca de produtos.
  - Registrar entradas e saídas com histórico de movimentações.
  - Converter caixas em unidades automaticamente.
  - Atualizar o estoque ao finalizar ou cancelar vendas.
  - Registrar pagamentos em até duas formas por venda.
  - Controlar abertura, retiradas, reforços e fechamento de caixa.
  - Apresentar relatórios de estoque, vendas e fechamento.
  - Expor informações selecionadas por uma API REST autenticada.
  - Consultar dados de produtos em uma API externa para auxiliar o cadastro.

### Público-alvo

- Proprietários e administradores de distribuidoras de bebidas.
- Atendentes responsáveis pelas vendas e pela operação do caixa.

---

## 2. Funcionalidades

| Funcionalidade | Descrição | Status |
| --- | --- | --- |
| Autenticação | Login e logout com perfis de administrador e atendente. | Planejada |
| Cadastro de produtos | Cadastro, consulta, edição, exclusão de produtos sem histórico e inativação dos demais. | Planejada |
| Conversão de embalagens | Quantidade de unidades por caixa registrada no produto. | Planejada |
| Entrada de mercadorias | Entrada manual por unidade ou caixa, com conversão para unidades. | Planejada |
| Ajuste de estoque | Registro administrativo de perdas e correções, com motivo e histórico. | Planejada |
| Consulta de estoque | Saldo em unidades e identificação de produtos abaixo do estoque mínimo. | Planejada |
| Busca de produtos | Pesquisa por nome, código interno, código de barras e categoria. | Planejada |
| Venda no caixa | Inclusão de vários produtos por unidade ou caixa fechada. | Planejada |
| Baixa automática | Atualização do estoque na finalização da venda. | Planejada |
| Pagamento dividido | Dinheiro, PIX, débito e crédito, com até duas formas diferentes por venda. | Planejada |
| Abertura de caixa | Registro do valor inicial para troco. | Planejada |
| Retiradas e reforços | Movimentações de dinheiro com valor, responsável e motivo. | Planejada |
| Fechamento de caixa | Conferência por forma de pagamento e registro das diferenças. | Planejada |
| Cancelamento | Cancelamento integral com autorização do administrador, enquanto o caixa da venda estiver aberto. | Planejada |
| Relatórios | Estoque, vendas e fechamento, com filtros, exportação CSV e impressão. | Planejada |
| API REST própria | Consulta autenticada de produtos, saldos, movimentações, vendas e resumos de caixa. | Planejada |
| Integração externa | Consulta ao Open Food Facts pelo código de barras para auxiliar o cadastro. | Planejada |

### Requisitos não funcionais

- **Desempenho:** meta de resposta de até 3 segundos em 95% das consultas internas, com uma base de teste de 1.000 produtos e 10.000 vendas. Consultas à API externa serão medidas separadamente.
- **Segurança:** senhas protegidas pelo mecanismo de hash do Django, autorização no servidor, proteção CSRF na interface, HTTPS em produção e segredos fora do GitHub.
- **Usabilidade:** interface em português, responsiva a partir de 360 px de largura, campos identificados, navegação por teclado e mensagens claras.
- **Disponibilidade:** hospedagem gratuita no PythonAnywhere durante a avaliação, com acompanhamento da validade da aplicação e renovação pelo painel.
- **Integridade:** vendas, pagamentos e movimentações de estoque serão persistidos em uma única transação.
- **Rastreabilidade:** operações relevantes registrarão usuário, data, horário e motivo, quando aplicável.
- **Manutenibilidade:** módulos separados por responsabilidade, dependências fixadas, testes automatizados e revisão de alterações.
- **Recuperação:** cópia consistente do SQLite antes de implantações e após o fechamento diário, usando o mecanismo de backup do banco.

---

## 3. Demonstração

Os protótipos da Fase 1 representarão as telas abaixo. As capturas serão armazenadas em `images/`, e os arquivos editáveis em `docs/prototipos/`.

| Tela | Descrição |
| --- | --- |
| Login | Acesso com usuário e senha, acompanhado da logomarca CentralBeer. |
| Painel inicial | Resumo de vendas, situação do caixa e alertas de estoque mínimo. |
| Produtos | Listagem, busca, cadastro, edição e inativação. |
| Entrada de mercadorias | Seleção do produto, quantidade, unidade ou caixa e prévia da conversão. |
| Histórico de estoque | Entradas, saídas, estornos e ajustes por produto e período. |
| Ponto de venda | Busca de produtos, itens da venda, total, pagamentos e troco. |
| Abertura de caixa | Informação do valor inicial e identificação do operador. |
| Movimentações de caixa | Retiradas e reforços com justificativa. |
| Fechamento de caixa | Valores esperados, valores conferidos e diferenças por forma de pagamento. |
| Histórico de vendas | Consulta dos itens, pagamentos, situação e cancelamento autorizado. |
| Relatórios | Filtros por período e produto, exportação CSV e impressão. |
| Usuários | Gestão administrativa de usuários e permissões. |

**Vídeo / protótipo:** protótipos previstos na entrega da Fase 1; vídeo de demonstração previsto para a Fase 2. Ainda não há material publicado.

### Identidade visual

A identidade visual do CentralBeer será baseada na logomarca da abelha coroada, utilizando preto, grafite, dourado e tons claros. A interface terá aparência profissional, com organização simples para facilitar o atendimento e a leitura das informações.

#### Paleta de cores

| Cor | Código | Aplicação |
| --- | --- | --- |
| Preto profundo | `#0B0B0B` | Fundo principal e área de login. |
| Grafite | `#171717` | Menu lateral, cabeçalho e cartões. |
| Cinza escuro | `#232323` | Campos de formulário e áreas secundárias. |
| Cinza de borda | `#3A3A3A` | Separação entre campos, cartões e tabelas. |
| Dourado principal | `#F5B82E` | Botões principais, seleção e indicadores de foco. |
| Dourado claro | `#FFD875` | Destaques e interação sobre elementos dourados. |
| Branco quente | `#F5F2E9` | Textos principais, títulos e valores. |
| Cinza claro | `#B8B8B8` | Legendas e textos secundários. |
| Verde | `#4ADE80` | Confirmações e situações regulares. |
| Vermelho | `#F87171` | Erros, cancelamentos e diferenças negativas. |

As cores foram escolhidas para harmonizar com a logomarca. Verde e vermelho serão utilizados como cores funcionais, acompanhados de texto ou ícones.

#### Tipografia

- Fonte da interface: Arial, com Helvetica e sans-serif como alternativas.
- Títulos e totais: negrito.
- Textos e formulários: tamanho-base de 16 px.
- Valores monetários e quantidades: alinhamento à direita nas tabelas.
- A tipografia decorativa da logomarca ficará restrita à própria marca.

#### Estilo da interface

- Tema escuro com dourado aplicado aos elementos de maior importância.
- Botões dourados com texto preto para as ações principais.
- Botões secundários em grafite, com texto claro e borda visível.
- Cartões e campos com cantos arredondados de 8 px.
- Ícones simples, acompanhados de rótulos nas ações importantes.
- Espaçamento consistente e tabelas com linhas bem separadas.
- Destaque para total da venda, troco e diferença de fechamento.
- Estados de foco visíveis para navegação por teclado.
- Informações de erro ou sucesso comunicadas por texto, além da cor.
- Contraste mínimo de 4,5:1 para textos comuns, verificado nos protótipos.

#### Aplicação da logomarca

- Logomarca completa na tela de login e na apresentação do projeto.
- Símbolo da abelha coroada em espaços menores, utilizando uma versão própria e legível.
- Proporções originais preservadas, sem distorções ou alteração das cores.
- Espaço livre ao redor da marca para evitar competição com outros elementos.
- Efeitos metálicos concentrados na logomarca; formulários, tabelas e botões utilizarão cores sólidas.

#### Responsividade

- Computador: menu lateral e área de trabalho ampla.
- Celular: navegação recolhível e conteúdo organizado em uma coluna.
- Ponto de venda: total e botão de finalização fáceis de localizar.
- Controles de toque com área mínima de 44 × 44 px.

---

## 4. Tecnologias utilizadas

As séries abaixo constituem a base técnica do projeto. As versões exatas das dependências serão registradas nos arquivos de requisitos quando instaladas, adotando correções de segurança compatíveis.

| Camada | Tecnologia | Versão |
| --- | --- | --- |
| Linguagem | Python | 3.12.x |
| Frontend | HTML5, CSS3, JavaScript e Bootstrap | Bootstrap 5.3.x |
| Templates | Django Templates | 5.2.x |
| Backend | Django | 5.2 LTS |
| API REST | Django REST Framework | 3.16.x |
| Banco de dados | SQLite | 3.x, mínimo 3.31 |
| Testes | Django TestCase, TransactionTestCase e Client | Django 5.2.x |
| Integração HTTP | Requests | 2.x |
| Configuração local | python-dotenv | 1.x |
| Infraestrutura | PythonAnywhere e GitHub Actions | Serviços gerenciados |
| Segurança | Bandit, pip-audit e OWASP ZAP | Versões registradas em cada análise |
| Outras ferramentas | Git, GitHub, diagrams.net e Postman | Ferramentas de apoio |

O banco SQLite será acessado pelo ORM do Django. Não será necessário instalar um servidor de banco separado.

O Bootstrap será personalizado com a paleta do CentralBeer. Os arquivos de interface serão servidos pelo próprio projeto, evitando dependência de CDN durante o atendimento.

---

## 5. Arquitetura

O CentralBeer utilizará uma aplicação Django única, organizada em módulos de usuários, produtos, estoque, vendas, caixa, relatórios e integrações.

A interface será renderizada por templates do Django. JavaScript será utilizado para melhorar a interação no ponto de venda e apresentar prévias dos cálculos. Todos os valores e permissões serão novamente validados no servidor.

As views da interface e os endpoints da API compartilharão os serviços responsáveis pelas regras de negócio. Esses serviços utilizarão os models e o ORM do Django para acessar o SQLite.

A integração com o Open Food Facts ficará em um serviço separado. Ela será utilizada no cadastro, sem se tornar uma dependência para finalizar vendas.

**Decisões relevantes:**

- Aplicação monolítica para reduzir a complexidade de desenvolvimento e publicação.
- SQLite para o escopo de uma loja e um caixa aberto por vez.
- Sessões do Django para a interface e autenticação por token para consumidores externos da API.
- API própria inicialmente voltada à consulta; operações de venda serão executadas pela interface protegida por sessão e CSRF.
- Perfil administrador para produtos, estoque, usuários, relatórios gerenciais e autorização de cancelamentos.
- Perfil atendente para vendas e operação do caixa.
- Produtos com histórico serão inativados; somente produtos sem vínculos poderão ser excluídos.
- Valores monetários armazenados em centavos inteiros, evitando cálculos com ponto flutuante.
- Quantidades de produtos sempre inteiras e positivas nas entradas e vendas.
- Preço da caixa calculado pelo preço unitário multiplicado pelas unidades da caixa.
- Preço e fator de conversão copiados para o item da venda, preservando o histórico.
- Finalização transacional com baixa condicional de estoque, impedindo saldo negativo.
- Identificador único de operação para evitar duplicação em reenvios de uma finalização.
- Um único caixa aberto, com validação também no banco de dados.
- Cancelamento integral somente no caixa de origem ainda aberto, com identificação e senha de um administrador.
- Senha de autorização validada pelo Django, sem armazenamento em logs ou no histórico da venda.
- Cancelamento com estorno registrado no estoque e nos totais financeiros, preservando a venda original.
- Devoluções financeiras realizadas externamente e confirmadas pelo responsável.
- Fechamentos concluídos preservados, sem edição retroativa nesta versão.

### Endpoints principais (quando houver API)

Contrato inicial previsto; as rotas ainda serão implementadas.

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/v1/produtos/` | Listar produtos com busca e filtros. |
| `GET` | `/api/v1/produtos/{id}/` | Consultar um produto. |
| `GET` | `/api/v1/estoque/` | Consultar saldos em unidades. |
| `GET` | `/api/v1/movimentacoes/` | Consultar movimentações por produto e período. |
| `GET` | `/api/v1/vendas/` | Consultar vendas por período e situação. |
| `GET` | `/api/v1/vendas/{id}/` | Consultar itens e pagamentos de uma venda. |
| `GET` | `/api/v1/caixas/{id}/resumo/` | Consultar o resumo financeiro de uma sessão de caixa. |

- **Autenticação:** cabeçalho `Authorization: Token ...`, exclusivamente por HTTPS em produção.
- **Permissão:** consultas externas reservadas a contas administrativas autorizadas.
- **Tokens:** emitidos e revogados administrativamente; não serão publicados no repositório.
- **Paginação:** 20 registros por página.
- **Filtros:** `busca`, `categoria`, `ativo`, `produto`, `data_inicio`, `data_fim` e `status`, conforme o recurso.
- **Datas:** formato ISO 8601.
- **Valores monetários:** centavos inteiros, com nomes de campos terminados em `_centavos`.
- **Respostas:** JSON, com códigos `200`, `400`, `401`, `403`, `404` e `429`, conforme a situação.

Documentação completa da API: contrato em Markdown e coleção Postman previstos em `docs/api/`, com exemplos de requisições, respostas, parâmetros e erros.

### Integração com Open Food Facts

- **Finalidade:** sugerir nome, marca e apresentação do produto no cadastro.
- **Endpoint:** `GET https://world.openfoodfacts.org/api/v3/product/{codigo}`.
- **Identificação:** User-Agent contendo nome, versão do CentralBeer e endereço do repositório.
- **Dados enviados:** somente o código de barras; vendas, pagamentos e dados de usuários não serão enviados.
- **Conferência:** o administrador confirmará os dados antes de salvar.
- **Dados locais:** preço, estoque mínimo e unidades por caixa serão informados no CentralBeer.
- **Falhas:** timeout, erro de conexão, resposta inválida, limite de requisições e produto ausente permitirão continuar pelo cadastro manual.
- **Tempo limite:** 3 segundos para conexão e 5 segundos para leitura.
- **Limites:** cache de consultas bem-sucedidas por 24 horas, consulta somente por ação explícita e respeito às respostas de limitação do provedor.
- **Funcionamento do caixa:** pesquisa no banco local, sem consulta externa durante a venda.
- **Atribuição:** indicação da origem dos dados consultados e respeito às licenças do provedor.

A leitura do código de barras e a consulta externa são operações diferentes. O leitor preencherá o código no campo de busca; a API será utilizada somente para auxiliar o cadastro.

---

## 6. Organização dos diretórios

### Estrutura atual do repositório

```text
.
├── README.md                         # Documentação principal do projeto
├── docs/                             # Documentação técnica e modelagem
│   └── modelagem/
│       ├── casos-de-uso/
│       │   └── especificacoes-casos-de-uso.pdf
│       ├── classes/
│       │   └── diagrama-de-classes.pdf
│       └── banco-de-dados/
│           ├── diagrama-er.pdf
│           └── modelo-logico.pdf
└── images/                           # Imagens utilizadas na documentação
    └── semaforo.png                  # Referência visual da política de uso de IA
```

Os PDFs herdados do template do professor serão atualizados com a modelagem específica do CentralBeer durante a primeira etapa.

### Estrutura planejada para o projeto

A organização abaixo está definida para orientar a documentação e a implementação. As pastas e os arquivos serão adicionados conforme as atividades forem realizadas.

```text
.
├── README.md                         # Apresentação e instruções do projeto
├── LICENSE                           # Licença MIT do código desenvolvido pela equipe
├── .gitignore                        # Exclusão de segredos, banco local e arquivos temporários
├── .env.example                      # Modelo de configuração, sem credenciais reais
├── requirements.txt                  # Dependências da aplicação
├── requirements-dev.txt              # Dependências de desenvolvimento e análise
├── manage.py                         # Comandos administrativos do Django
├── config/                           # Configuração principal do projeto Django
│   ├── settings.py                   # Banco SQLite, aplicações, segurança e ambiente
│   ├── urls.py                       # Rotas principais da aplicação e da API
│   ├── asgi.py                        # Ponto de entrada para servidores ASGI
│   └── wsgi.py                        # Ponto de entrada para hospedagem WSGI
├── apps/                             # Código-fonte organizado por domínio de negócio
│   ├── usuarios/                     # Autenticação, perfis e permissões
│   ├── produtos/                     # Produtos, categorias, preços e unidades por caixa
│   ├── estoque/                      # Entradas, saídas, ajustes e histórico de movimentações
│   ├── vendas/                       # Vendas, itens, pagamentos e cancelamentos
│   ├── caixa/                        # Abertura, suprimentos, sangrias e fechamento
│   ├── relatorios/                   # Consultas, exportação CSV e impressão
│   └── integracoes/                  # Consulta de códigos de barras no Open Food Facts
├── templates/                        # Interface HTML renderizada pelo Django
│   ├── base.html                     # Estrutura visual compartilhada
│   ├── includes/                     # Menu, cabeçalho e mensagens
│   ├── usuarios/                     # Login e gerenciamento de usuários
│   ├── produtos/                     # Cadastro e consulta de produtos
│   ├── estoque/                      # Entradas, ajustes e movimentações
│   ├── vendas/                       # Ponto de venda e histórico
│   ├── caixa/                        # Operação e fechamento do caixa
│   └── relatorios/                   # Visualização e impressão de relatórios
├── static/                           # Arquivos estáticos da aplicação
│   ├── css/                          # Estilos e paleta visual do CentralBeer
│   ├── js/                           # Interações da interface
│   ├── images/                       # Logomarca e elementos visuais do sistema
│   └── vendor/                       # Bibliotecas utilizadas localmente, como Bootstrap
├── tests/                            # Testes automatizados com as ferramentas do Django
│   ├── test_usuarios.py              # Autenticação e permissões
│   ├── test_produtos.py              # Cadastro, pesquisa e unidades por caixa
│   ├── test_estoque.py               # Conversões, movimentações e saldo
│   ├── test_vendas.py                # Pagamentos, baixa automática e cancelamentos
│   ├── test_caixa.py                 # Abertura, movimentações e fechamento
│   ├── test_relatorios.py            # Filtros, totais e exportações
│   ├── test_integracoes.py           # Consulta externa e tratamento de falhas
│   └── test_api.py                   # Autenticação, permissões e respostas da API
├── scripts/                          # Rotinas auxiliares de manutenção
│   └── backup_sqlite.py              # Cópia consistente do banco de dados SQLite
├── .github/
│   └── workflows/
│       ├── ci.yml                    # Verificações, testes e análises automatizadas
│       └── cd.yml                    # Preparação do pacote aprovado para publicação
├── docs/                             # Documentação técnica e acadêmica
│   ├── README.md                     # Índice dos documentos
│   ├── visao/                        # Problema, objetivos, escopo e requisitos
│   ├── modelagem/                    # Modelos editáveis e suas exportações em PDF
│   │   ├── casos-de-uso/             # Diagrama e especificações dos casos de uso
│   │   ├── classes/                  # Diagrama de classes
│   │   └── banco-de-dados/           # Diagrama ER, modelo lógico e dicionário de dados
│   ├── arquitetura/                  # Componentes, implantação e decisões técnicas
│   ├── api/                          # Contrato REST, exemplos e coleção do Postman
│   ├── prototipos/                   # Telas e identidade visual
│   ├── planejamento/                 # Backlog, responsabilidades, cronograma e riscos
│   └── seguranca/                    # Relatórios e evidências de SAST e DAST
└── images/                           # Figuras utilizadas no README e na documentação geral
    └── semaforo.png                  # Referência visual da política de uso de IA
```

Cada módulo em `apps/` reunirá seus modelos, rotas, validações e regras de negócio. A interface utilizará Django Templates, com arquivos HTML em `templates/` e recursos visuais em `static/`.

Os diagramas permanecerão nas respectivas pastas de `docs/`, acompanhados dos arquivos editáveis e das versões exportadas em PDF.

O banco SQLite, os backups e o arquivo `.env` serão mantidos fora do controle de versão. O repositório conterá apenas o modelo de configuração `.env.example`, sem informações sensíveis.
---

## 7. Participantes

Todos os integrantes atuarão como desenvolvedores, com responsabilidade principal por módulos e revisão cruzada.

| Nome | Matrícula | Função no projeto |
| --- | --- | --- |
| Bruno dos Santos | 22501077 | Desenvolvedor — produtos, estoque, integração externa e coordenação da documentação. |
| Carlos Emanuel | 22509279 | Desenvolvedor — vendas, pagamentos, ponto de venda e integração da interface. |
| Gustavo Augusto | 22507421 | Desenvolvedor — caixa, relatórios, workflows e publicação. |

Cada desenvolvedor será responsável pelos testes dos módulos em que atuar. Modelagem, segurança, revisão e apresentação serão atividades compartilhadas.

**Professor(a) responsável:** Felippe Pires Ferreira.

---

## 8. Como executar

### Pré-requisitos

- Git.
- Python 3.12 com `pip` e suporte ao módulo `sqlite3`.
- Navegador atualizado.
- Acesso à internet para instalação de dependências e consulta externa de produtos.

### Instalação e execução

Na Fase 1, o repositório pode ser obtido com:

```bash
git clone https://github.com/Bruno-Kowalski/gestao-distribuidora.git
cd gestao-distribuidora
```

O procedimento abaixo será utilizado após a implementação da aplicação na Fase 2. Ainda não é executável sobre o repositório apenas documental.

```bash
# Criar o ambiente virtual
python -m venv .venv
```

Ativar no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Ativar no Linux ou macOS:

```bash
source .venv/bin/activate
```

Instalar as dependências:

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
```

Copiar `.env.example` para `.env` e preencher a chave secreta local.

Gerar uma chave:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Preparar o banco e iniciar a aplicação:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py check
python manage.py runserver
```

**Acesso local:** `http://127.0.0.1:8000/`, após iniciar o servidor na Fase 2.

### Implantação (quando houver)

- **Ambiente:** PythonAnywhere, plano gratuito.
- **Execução:** aplicação WSGI gerenciada pela plataforma.
- **Banco:** SQLite em arquivo persistente, fora do diretório substituído nas entregas.
- **Estáticos:** coletados com `collectstatic` e servidos pelo mapeamento da plataforma.
- **URL de produção:** será registrada após a primeira publicação na Fase 2; nenhum endereço está ativo neste momento.
- **Segurança:** HTTPS, `DEBUG=False`, hosts explícitos e segredos carregados no ambiente.
- **Disponibilidade:** renovação da aplicação gratuita pelo painel antes do vencimento.
- **Dados de avaliação:** produtos e vendas fictícios e contas de teste.
- **Backup:** cópia consistente do banco antes de migrations e atualizações.

---

## 9. Configuração

O projeto carregará as variáveis do ambiente e, no desenvolvimento local, do arquivo `.env`.

| Variável | Obrigatória | Descrição | Exemplo |
| --- | --- | --- | --- |
| `DJANGO_SECRET_KEY` | Sim | Chave secreta exclusiva do ambiente. | Gerar localmente |
| `DJANGO_DEBUG` | Sim | Habilita depuração apenas no desenvolvimento. | `True` |
| `DJANGO_ALLOWED_HOSTS` | Sim | Hosts permitidos, separados por vírgula. | `localhost,127.0.0.1` |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Em produção | Origens HTTPS confiáveis. | Origem real da aplicação publicada |
| `SQLITE_PATH` | Sim | Caminho do arquivo SQLite. | `db.sqlite3` |
| `DJANGO_SECURE_SSL_REDIRECT` | Sim | Redirecionamento para HTTPS em produção. | `False` no ambiente local |
| `DJANGO_SESSION_COOKIE_SECURE` | Sim | Restringe o cookie de sessão a HTTPS em produção. | `False` no ambiente local |
| `DJANGO_CSRF_COOKIE_SECURE` | Sim | Restringe o cookie CSRF a HTTPS em produção. | `False` no ambiente local |
| `OFF_USER_AGENT` | Sim | Identificação nas consultas ao Open Food Facts. | `CentralBeer/0.0.1 (https://github.com/Bruno-Kowalski/gestao-distribuidora)` |
| `OFF_CONNECT_TIMEOUT` | Não | Limite de conexão, em segundos. | `3` |
| `OFF_READ_TIMEOUT` | Não | Limite de leitura, em segundos. | `5` |

O idioma será `pt-br`, o fuso de apresentação será `America/Sao_Paulo` e os horários serão armazenados com suporte a timezone.

Credenciais reais ficarão fora do GitHub. O `.gitignore` excluirá `.env`, `.venv/`, `db.sqlite3`, arquivos auxiliares do SQLite e backups.

---

## 10. Testes

Os testes serão desenvolvidos com as ferramentas do próprio Django.

```bash
python manage.py test
```

| Tipo | Ferramenta | O que verifica |
| --- | --- | --- |
| Unitários | Django TestCase | Conversão de caixas, cálculo de totais, pagamentos, troco e diferenças de fechamento. |
| Integração | Django TestCase e Client | Autenticação, permissões, produtos, vendas, estoque, caixa e API. |
| Transacionais | Django TransactionTestCase | Reversão de operações incompletas, bloqueio de saldo negativo e prevenção de duplicidades. |
| Manuais | Roteiro com evidências | Uso por teclado, leitura de código de barras, responsividade, impressão e conferência de caixa. |

Os cenários principais incluirão:

- Entrada e venda por unidade e caixa.
- Alteração do fator de conversão sem modificar o histórico.
- Venda com estoque suficiente e insuficiente.
- Pagamento em uma ou duas formas.
- Pagamentos incompatíveis com o total da venda.
- Troco somente sobre o valor entregue em dinheiro.
- Reenvio da finalização sem duplicar a venda.
- Falha durante a venda sem baixar parcialmente o estoque.
- Cancelamento com senha válida, inválida e caixa já fechado.
- Impedimento de dois caixas abertos simultaneamente.
- Retirada superior ao dinheiro disponível.
- Fechamento com sobra, falta e valores corretos.
- Produto externo ausente, timeout, JSON inválido e limite de requisições.
- Acesso não autorizado à API e às funções administrativas.

As chamadas externas serão simuladas nos testes automatizados, evitando dependência da disponibilidade do Open Food Facts.

**Cobertura atual:** testes ainda não implementados. A cobertura funcional será acompanhada pelos cenários executados e pelas evidências registradas.

### CI/CD

O GitHub Actions executará os workflows em `.github/workflows/`.

**Integração contínua — CI:**

- Executar em pull requests e pushes destinados à `main`.
- Instalar Python e dependências.
- Executar `python manage.py check`.
- Verificar migrations com `python manage.py makemigrations --check --dry-run`.
- Executar os testes do Django com SQLite temporário.
- Executar Bandit e análise de dependências com pip-audit.
- Armazenar os relatórios como artefatos do workflow.

**Entrega contínua — CD:**

- Gerar um pacote versionado somente após sucesso da CI na `main`.
- Excluir segredos, ambiente virtual, banco e backups do pacote.
- Disponibilizar o artefato para implantação.
- Promover a versão pelo painel do PythonAnywhere, realizar backup, aplicar migrations e recarregar a aplicação.
- Conferir login, consulta de produtos e acesso à API após a publicação.

Nesta versão, CD significa entrega contínua do pacote; a promoção para a hospedagem terá uma etapa manual.

### Segurança

- **SAST:** Bandit.
- **Dependências:** pip-audit como análise complementar.
- **DAST:** OWASP ZAP, em execução controlada contra ambiente autorizado do grupo.

Os relatórios registrarão versão da ferramenta, data, commit, escopo, achados, severidade, falsos positivos, correções, riscos aceitos e nova verificação. Nenhuma análise foi executada nesta etapa documental.

---

## 11. Uso de inteligência artificial

A atividade possui orientações específicas sobre uso de IA, representadas também pelo semáforo pedagógico do template:

![Política de uso de IA — semáforo](images/semaforo.png)

| Situação | Significado |
| --- | --- |
| **Vermelho — uso proibido** | Atividades de autonomia intelectual em que o uso é vedado. |
| **Amarelo — uso limitado** | Apoio permitido dentro das condições estabelecidas, com declaração. |
| **Verde — uso permitido** | Uso permitido conforme as orientações da atividade. |

### Declaração de uso

- **Houve uso de IA neste projeto?** Sim.
- **Ferramentas utilizadas:** ChatGPT.
- **Finalidade:** interpretação do enunciado, discussão de possibilidades, pesquisa de tecnologias, propostas técnicas, divisão de responsabilidades, orientação visual e redação deste README.
- **O que NÃO foi delegado à IA:** relato da dificuldade do cliente e decisões informadas pelo aluno sobre estoque, vendas, pagamentos, caixa, cancelamento, banco de dados e nome do sistema.

Este README foi gerado com auxílio de IA e não representa redação exclusivamente humana. O enunciado restringe a produção da especificação por IA; declarar o uso não substitui a autorização do professor para utilizar este material na entrega.

---

## 12. Contribuição e fluxo de trabalho

### Branches

- `main` — versão estável e materiais destinados à avaliação.
- `feat/nome` — novas funcionalidades.
- `fix/nome` — correções.
- `docs/nome` — documentação.
- `ci/nome` — workflows e automação.

O grupo utilizará branches curtas a partir da `main`, sem uma branch permanente de integração.

### Commits

Mensagens seguirão o padrão Conventional Commits:

- `feat: adiciona cadastro de produtos`
- `fix: corrige cálculo do troco`
- `docs: atualiza README do CentralBeer`
- `test: adiciona testes de cancelamento`
- `ci: configura testes do Django`

### Passos sugeridos

1. Registrar a tarefa em uma issue.
2. Criar uma branch a partir da `main`.
3. Desenvolver e testar a alteração.
4. Registrar commits na conta do próprio integrante.
5. Abrir um pull request.
6. Solicitar revisão de outro desenvolvedor.
7. Corrigir os apontamentos e verificar a CI.
8. Integrar a alteração e encerrar a issue.

**Issues e quadro de tarefas:** [GitHub Issues](https://github.com/Bruno-Kowalski/gestao-distribuidora/issues), com responsável, marco e etiquetas `a-fazer`, `em-andamento`, `em-revisao` e `concluido`.

O quadro e as etiquetas serão configurados durante a organização do planejamento.

---

## 13. Histórico de versões

| Versão | Data | Descrição |
| --- | --- | --- |
| `0.0.1` | 2026-10-03 | Criação do repositório e início da documentação. |

As versões nesta tabela identificam marcos documentais; ainda não há versão executável.

A entrega da Fase 1 está prevista para **05/10/2026**. A tag `fase-1` será criada após a conclusão e revisão dos entregáveis, identificando o commit enviado ao professor.

---

## 14. Limitações e próximos passos

### Problemas conhecidos

- A aplicação ainda não está implementada ou publicada.
- Os PDFs herdados do template não representam a modelagem do CentralBeer.
- Os protótipos e diagramas específicos ainda precisam ser produzidos.
- A logomarca foi fornecida como referência visual; sua aplicação nas telas será realizada durante a prototipação e implementação.
- O Open Food Facts pode não possuir determinados produtos ou apresentar dados incompletos.
- A consulta externa não fornece os preços praticados pela distribuidora nem substitui a conferência do cadastro.
- O plano gratuito de hospedagem possui limites de recursos e renovação periódica.
- O SQLite e o escopo operacional estão dimensionados para uma loja e um caixa aberto por vez.
- Pagamentos e devoluções serão realizados externamente, com registro e confirmação no sistema.
- Emissão fiscal, integração com SEFAZ, múltiplas filiais, vendas fiadas, entregas e controle de vasilhames retornáveis estão fora desta versão.
- Cancelamentos parciais e alterações de caixas já fechados estão fora desta versão.

---

## 15. Licença, referências e contato

**Licença:** MIT para o código original desenvolvido pelo grupo, com inclusão do texto integral em `LICENSE` na implementação.

Materiais herdados do professor, logomarca e dados de terceiros mantêm suas condições próprias de uso. A licença MIT do código não altera as licenças da base Open Food Facts.

Os dados consultados no Open Food Facts serão identificados como provenientes desse serviço, respeitando ODbL e as condições aplicáveis ao conteúdo. A primeira versão não importará imagens de produtos desse serviço.

### Documentação complementar

Arquivos herdados do template:

- [Casos de uso](docs/modelagem/casos-de-uso/especificacoes-casos-de-uso.pdf)
- [Diagrama de classes](docs/modelagem/classes/diagrama-de-classes.pdf)
- [Modelo conceitual](docs/modelagem/banco-de-dados/diagrama-er.pdf)
- [Modelo lógico](docs/modelagem/banco-de-dados/modelo-logico.pdf)

Esses arquivos deverão ser substituídos pelos materiais específicos do CentralBeer. Visão, arquitetura, contrato da API, protótipos e planejamento serão entregues nos diretórios descritos na seção 6, com fontes editáveis quando aplicável.

### Referências

- Ferreira, Felippe Pires. Especificação do trabalho prático de Desenvolvimento Web com Python e Django.
- [Repositório-base do professor](https://github.com/Felippe-Pires/template_projects)
- [Documentação do Python](https://docs.python.org/3.12/)
- [Documentação do Django 5.2](https://docs.djangoproject.com/en/5.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/docs.html)
- [Bootstrap](https://getbootstrap.com/docs/5.3/)
- [Open Food Facts API](https://openfoodfacts.github.io/documentation/docs/Product-Opener/api/)
- [PythonAnywhere](https://help.pythonanywhere.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Bandit](https://bandit.readthedocs.io/)
- [OWASP ZAP](https://www.zaproxy.org/docs/)

O repositório foi criado como fork do material indicado pelo professor, pois o botão “Use this template” não estava disponível. Esse procedimento preserva a origem do material, mas sua aceitação como forma de entrega deve ser confirmada com o professor.

### Contato

Dúvidas, sugestões e problemas: [Issues do CentralBeer](https://github.com/Bruno-Kowalski/gestao-distribuidora/issues).

**Agradecimentos:** ao professor Felippe Pires Ferreira pelas orientações e pelo template disponibilizado à turma.
