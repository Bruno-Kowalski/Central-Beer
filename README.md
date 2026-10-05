<p align="center">
  <img src="images/logo.png" alt="Logo CentralBeer" width="220">
</p>

<h1 align="center">CentralBeer</h1>

<p align="center">
  <strong>Gestão de estoque, vendas e caixa para distribuidoras de bebidas.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-Fase_1-F5B82E" alt="Status">
  <img src="https://img.shields.io/badge/versão-0.0.1-171717" alt="Versão">
  <img src="https://img.shields.io/badge/Python-3.12-blue" alt="Python">
  <img src="https://img.shields.io/badge/Django-5.2_LTS-darkgreen" alt="Django">
  <img src="https://img.shields.io/badge/banco-SQLite-blue" alt="Banco">
</p>

---

**Instituição:** CEUB  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Disciplina:** Desenvolvimento Web  
**Turma / Semestre:** Turma A / 2026.2  
**Professor(a):** Felippe Pires Ferreira  
**Status do projeto:** Fase 1 — documentação e arquitetura  

> As funcionalidades e decisões técnicas apresentadas nesta etapa representam o planejamento do CentralBeer. A implementação da aplicação ocorrerá na Fase 2.

---

## Sumário

- [1. Descrição do projeto](#1-descrição-do-projeto)
- [2. Funcionalidades](#2-funcionalidades)
- [3. Protótipos e identidade visual](#3-protótipos-e-identidade-visual)
- [4. Tecnologias utilizadas](#4-tecnologias-utilizadas)
- [5. Arquitetura](#5-arquitetura)
- [6. Documentação da Fase 1](#6-documentação-da-fase-1)
- [7. Organização dos diretórios](#7-organização-dos-diretórios)
- [8. Participantes](#8-participantes)
- [9. Como executar](#9-como-executar)
- [10. Configuração](#10-configuração)
- [11. Testes](#11-testes)
- [12. Uso de inteligência artificial](#12-uso-de-inteligência-artificial)
- [13. Contribuição e fluxo de trabalho](#13-contribuição-e-fluxo-de-trabalho)
- [14. Histórico de versões](#14-histórico-de-versões)
- [15. Limitações e próximos passos](#15-limitações-e-próximos-passos)
- [16. Licença, referências e contato](#16-licença-referências-e-contato)

---

## 1. Descrição do projeto

O CentralBeer é uma aplicação web planejada para auxiliar a gestão de distribuidoras de bebidas. A proposta surgiu da necessidade de centralizar informações de estoque, vendas e caixa, reduzindo controles manuais e facilitando a consulta das informações durante o atendimento.

O sistema reunirá cadastro de produtos, entrada de mercadorias, controle de estoque, vendas e operação de caixa. Ao finalizar uma venda, os pagamentos serão registrados e as quantidades vendidas serão descontadas automaticamente do estoque.

Os recebimentos poderão ser registrados em dinheiro, PIX, débito e crédito, com possibilidade de utilização de até duas formas diferentes em uma mesma venda.

O estoque será controlado em unidades. Entradas e vendas também poderão utilizar caixas fechadas, sendo a conversão realizada de acordo com a quantidade de unidades por caixa definida no cadastro do produto.

A primeira versão do CentralBeer atenderá um único estabelecimento e permitirá apenas um caixa aberto por vez. Emissão fiscal, integração com SEFAZ e processamento direto de pagamentos não fazem parte do escopo inicial.

### Objetivos

**Objetivo geral:** desenvolver uma aplicação web para organizar o estoque, as vendas e o caixa de uma distribuidora de bebidas.

**Objetivos específicos:**

- centralizar o cadastro e a busca de produtos;
- registrar entradas e saídas com histórico de movimentações;
- permitir operações por unidade ou caixa fechada;
- converter caixas em unidades automaticamente;
- atualizar o estoque ao finalizar ou cancelar vendas;
- registrar pagamentos em até duas formas por venda;
- controlar abertura, retiradas, reforços e fechamento de caixa;
- apresentar relatórios de estoque, vendas e fechamento;
- disponibilizar informações selecionadas por uma API REST;
- consultar dados de produtos em uma API externa para auxiliar o cadastro.

### Público-alvo

- proprietários e administradores de distribuidoras de bebidas;
- atendentes responsáveis pelas vendas e pela operação do caixa.

---

## 2. Funcionalidades

| Funcionalidade | Descrição | Status |
| --- | --- | --- |
| Autenticação | Login e logout com perfis de administrador e atendente. | Planejada |
| Cadastro de produtos | Cadastro, consulta, edição, inativação e exclusão quando permitida. | Planejada |
| Conversão de embalagens | Registro da quantidade de unidades existentes em cada caixa. | Planejada |
| Entrada de mercadorias | Entrada manual por unidade ou caixa, com conversão para unidades. | Planejada |
| Ajuste de estoque | Registro de perdas e correções com motivo e histórico. | Planejada |
| Consulta de estoque | Consulta do saldo em unidades e identificação de estoque mínimo. | Planejada |
| Busca de produtos | Pesquisa por nome, código interno, código de barras e categoria. | Planejada |
| Venda no caixa | Inclusão de vários produtos por unidade ou caixa fechada. | Planejada |
| Baixa automática | Atualização do estoque após a finalização da venda. | Planejada |
| Pagamento dividido | Dinheiro, PIX, débito e crédito, com até duas formas diferentes por venda. | Planejada |
| Abertura de caixa | Registro do operador, horário e valor inicial. | Planejada |
| Retiradas e reforços | Movimentações de caixa com valor, responsável e motivo. | Planejada |
| Fechamento de caixa | Conferência dos valores esperados e informados por forma de pagamento. | Planejada |
| Cancelamento de venda | Cancelamento integral mediante autorização administrativa e regras definidas. | Planejada |
| Relatórios | Consultas de estoque, vendas e fechamento com filtros, impressão e exportação. | Planejada |
| API REST própria | Consulta autenticada de produtos, estoque, movimentações, vendas e caixa. | Planejada |
| Integração externa | Consulta ao Open Food Facts pelo código de barras para auxiliar o cadastro. | Planejada |

### Requisitos não funcionais

- **Desempenho:** consultas internas devem apresentar resposta adequada ao uso operacional da aplicação.
- **Segurança:** autenticação, autorização no servidor, proteção CSRF, HTTPS em produção e segredos fora do repositório.
- **Usabilidade:** interface em português, responsiva e com mensagens claras para o usuário.
- **Disponibilidade:** aplicação prevista para publicação em ambiente acessível pela Internet na Fase 2.
- **Integridade:** venda, pagamentos e movimentações relacionadas devem manter consistência durante a persistência.
- **Rastreabilidade:** operações relevantes registrarão responsável, data, horário e motivo quando aplicável.
- **Manutenibilidade:** módulos organizados por responsabilidade e regras de negócio centralizadas.
- **Recuperação:** o banco de produção deverá possuir estratégia de backup e recuperação.

---

## 3. Protótipos e identidade visual

A identidade visual do CentralBeer utiliza como principal elemento gráfico uma abelha coroada associada ao nome da aplicação.

A documentação completa dos protótipos e da identidade visual está disponível em:

- [Protótipos e Identidade Visual](docs/prototipos/README.md)

### Paleta de cores

| Cor | Código | Aplicação |
| --- | --- | --- |
| Preto profundo | `#0B0B0B` | Fundo principal e tela de login |
| Grafite | `#171717` | Menu, cabeçalho e cartões |
| Cinza escuro | `#232323` | Campos e áreas secundárias |
| Cinza de borda | `#3A3A3A` | Separadores e bordas |
| Dourado principal | `#F5B82E` | Botões e elementos de destaque |
| Dourado claro | `#FFD875` | Destaques secundários |
| Branco quente | `#F5F2E9` | Textos principais |
| Cinza claro | `#B8B8B8` | Textos secundários |
| Verde | `#4ADE80` | Confirmações e situações regulares |
| Vermelho | `#F87171` | Erros, cancelamentos e alertas |

### Tipografia

- Arial como fonte principal da interface;
- Helvetica e sans-serif como alternativas;
- títulos e valores importantes em negrito;
- tamanho-base aproximado de 16 px para textos e formulários.

### Estilo da interface

- tema escuro com elementos dourados;
- botões principais em destaque;
- cartões e campos com organização simples;
- tabelas com boa separação visual;
- destaque para total da venda, troco e diferenças de fechamento;
- mensagens de erro e sucesso acompanhadas de texto;
- interface planejada para computador e dispositivos móveis.

### Aplicação da logomarca

- logomarca completa na tela de login e apresentação do sistema;
- símbolo da abelha coroada em espaços menores;
- proporções e cores da marca preservadas;
- aplicação consistente nos materiais do projeto.

---

## 4. Tecnologias utilizadas

As tecnologias abaixo representam a base técnica planejada para a implementação do CentralBeer na Fase 2.

| Camada | Tecnologia | Versão prevista |
| --- | --- | --- |
| Linguagem | Python | 3.12.x |
| Backend | Django | 5.2 LTS |
| Frontend | HTML5, CSS3, JavaScript e Bootstrap | Bootstrap 5.3.x |
| Templates | Django Templates | 5.2.x |
| API REST | Django REST Framework | 3.16.x |
| Banco de dados | SQLite | 3.x |
| Persistência | Django ORM | Incluído no Django |
| Testes | Django TestCase, TransactionTestCase e Client | Django 5.2.x |
| Integração HTTP | Requests | 2.x |
| Configuração | python-dotenv | 1.x |
| Hospedagem | PythonAnywhere | Serviço gerenciado |
| Versionamento | Git e GitHub | — |
| Modelagem | diagrams.net / draw.io e MySQL Workbench | — |
| Segurança | Bandit, pip-audit e OWASP ZAP | Fase 2 |

O SQLite será acessado por meio do ORM do Django. A primeira versão foi planejada para o escopo de um estabelecimento e um caixa aberto por vez.

---

## 5. Arquitetura

O CentralBeer foi planejado como uma aplicação web monolítica modular desenvolvida com Django.

Embora seja implantada como uma única aplicação, sua estrutura será separada por responsabilidades de negócio, facilitando manutenção, testes e evolução do sistema.

Os principais módulos previstos são:

- usuários;
- produtos;
- estoque;
- vendas;
- caixa;
- relatórios;
- integrações.

A interface será renderizada utilizando Django Templates, HTML, CSS, Bootstrap e JavaScript.

As Views e os endpoints da API utilizarão serviços responsáveis pelas regras de negócio. Esses serviços acessarão os Models e o banco de dados através do Django ORM.

A integração com o Open Food Facts será isolada em um serviço específico e utilizada apenas para auxiliar o cadastro de produtos.

### Decisões arquiteturais principais

- aplicação monolítica modular;
- Django como framework principal;
- SQLite na primeira versão;
- Django ORM para persistência;
- autenticação por sessão na interface web;
- autenticação por token para consumidores externos da API;
- API REST inicialmente somente para consulta;
- separação das funcionalidades por domínio;
- validação de regras críticas no servidor;
- operações de venda executadas de forma transacional;
- um único caixa aberto simultaneamente;
- preservação do histórico de vendas, movimentações e fechamentos;
- integração externa independente do funcionamento do ponto de venda.

### Endpoints previstos

| Método | Rota | Descrição |
| --- | --- | --- |
| `GET` | `/api/v1/produtos/` | Listar produtos com busca e filtros |
| `GET` | `/api/v1/produtos/{id}/` | Consultar um produto específico |
| `GET` | `/api/v1/estoque/` | Consultar saldos de estoque |
| `GET` | `/api/v1/movimentacoes/` | Consultar movimentações de estoque |
| `GET` | `/api/v1/vendas/` | Consultar vendas |
| `GET` | `/api/v1/vendas/{id}/` | Consultar itens e pagamentos de uma venda |
| `GET` | `/api/v1/caixas/{id}/resumo/` | Consultar resumo financeiro de um caixa |

### Características da API

- versionamento pelo caminho `/api/v1/`;
- respostas em JSON;
- autenticação obrigatória;
- paginação das coleções;
- filtros conforme o recurso;
- datas e horários em formato ISO 8601;
- valores monetários representados de forma inteira conforme o modelo de dados;
- códigos HTTP adequados para sucesso e erro.

A documentação detalhada está disponível em:

- [Contrato Inicial da API](docs/api/README.md)

### Integração com Open Food Facts

A integração externa será utilizada para auxiliar o cadastro de produtos a partir do código de barras.

**Endpoint externo previsto:**

```text
GET https://world.openfoodfacts.org/api/v3/product/{codigo}
```

A integração poderá sugerir informações como:

- nome;
- marca;
- apresentação do produto.

Preço, estoque, quantidade por caixa e demais informações operacionais continuarão sendo definidos dentro do CentralBeer.

A aplicação também deverá prever:

- timeout;
- erro de conexão;
- resposta inválida;
- indisponibilidade do serviço;
- limite de requisições;
- continuidade do cadastro manual em caso de falha.

A documentação da integração está disponível em:

- [Plano de Integração Externa](docs/integracao/README.md)

---

## 6. Documentação da Fase 1

Toda a documentação da Fase 1 está organizada na pasta [`docs/`](docs/README.md).

### Principais entregáveis

- [Documento de Visão](docs/visao/README.md)
- [Modelagem](docs/modelagem/README.md)
- [Casos de Uso](docs/modelagem/casos-de-uso/README.md)
- [Arquitetura](docs/modelagem/arquitetura/README.md)
- [Contrato Inicial da API](docs/api/README.md)
- [Plano de Integração Externa](docs/integracao/README.md)
- [Protótipos e Identidade Visual](docs/prototipos/README.md)
- [Planejamento](docs/planejamento/README.md)
- [Matriz de Rastreabilidade](docs/rastreabilidade/matriz-de-rastreabilidade.md)

### Modelagem

A pasta de modelagem contém os diagramas exportados e seus respectivos arquivos editáveis.

#### Arquitetura

- Documento de Arquitetura;
- Diagrama UML de Componentes em PDF;
- arquivo editável `.drawio`.

#### Banco de dados

- Documento de Modelo de Dados;
- Diagrama Entidade-Relacionamento;
- arquivo editável do DER;
- Modelo Lógico;
- arquivo editável `.mwb`.

#### Casos de uso

- especificação textual dos casos de uso;
- Diagrama UML de Casos de Uso;
- arquivo editável `.drawio`.

#### Classes

- documento do Diagrama de Classes;
- Diagrama UML de Classes;
- arquivo editável `.drawio`.

### Rastreabilidade

A matriz de rastreabilidade relaciona:

```text
Funcionalidades
      ↓
Casos de Uso
      ↓
Modelo de Dados
      ↓
Arquitetura
      ↓
Endpoints previstos
```

Arquivo:

- [Matriz de Rastreabilidade](docs/rastreabilidade/matriz-de-rastreabilidade.md)

---

## 7. Organização dos diretórios

### Estrutura atual da Fase 1

```text
.
├── README.md
├── docs/
│   ├── README.md
│   │
│   ├── api/
│   │   ├── README.md
│   │   └── Contrato Inicial API - CentralBeer.pdf
│   │
│   ├── integracao/
│   │   ├── README.md
│   │   └── Plano de Integracao Externa - CentralBeer.pdf
│   │
│   ├── modelagem/
│   │   ├── README.md
│   │   │
│   │   ├── arquitetura/
│   │   │   ├── README.md
│   │   │   ├── Documento de Arquitetura - CentralBeer.pdf
│   │   │   ├── diagrama UML de Componentes.drawio
│   │   │   └── diagrama UML de Componentes.pdf
│   │   │
│   │   ├── banco-de-dados/
│   │   │   ├── Modelo de Dados - CentralBeer.pdf
│   │   │   ├── Diagrama DER.drawio
│   │   │   ├── Diagrama DER.drawio.pdf
│   │   │   ├── MODELO LOGICO.pdf
│   │   │   └── modelo_logico.mwb
│   │   │
│   │   ├── casos-de-uso/
│   │   │   ├── README.md
│   │   │   ├── Casos de Uso - CentralBeer.pdf
│   │   │   ├── Diagrama UML - Casos de Uso.drawio
│   │   │   └── Diagrama UML - Casos de Uso.pdf
│   │   │
│   │   └── classes/
│   │       ├── README.md
│   │       ├── Diagrama de Classes - CentralBeer.pdf
│   │       ├── Diagrama de Classes.drawio
│   │       └── Diagrama de Classes.pdf
│   │
│   ├── planejamento/
│   │   ├── README.md
│   │   └── Planejamento - CentralBeer.pdf
│   │
│   ├── prototipos/
│   │   ├── README.md
│   │   └── Prototipos e Identidade - CentralBeer.pdf
│   │
│   ├── rastreabilidade/
│   │   ├── README.md
│   │   └── matriz-de-rastreabilidade.md
│   │
│   └── visao/
│       ├── README.md
│       └── Documento de Visao - CentralBeer.pdf
│
└── images/
    ├── logo.png
    └── semaforo.png
```

Os diagramas possuem versões para consulta e, quando aplicável, seus respectivos arquivos-fonte editáveis.

### Estrutura prevista para a Fase 2

Durante a implementação, o projeto Django deverá acrescentar estruturas como:

```text
.
├── manage.py
├── requirements.txt
├── .env.example
├── config/
├── apps/
│   ├── usuarios/
│   ├── produtos/
│   ├── estoque/
│   ├── vendas/
│   ├── caixa/
│   ├── relatorios/
│   └── integracoes/
├── templates/
├── static/
├── tests/
└── .github/
    └── workflows/
```

Essa estrutura poderá sofrer ajustes durante a implementação, desde que as alterações sejam registradas e permaneçam coerentes com a documentação do projeto.

---

## 8. Participantes

Todos os integrantes atuarão como desenvolvedores e possuirão contribuições identificáveis no histórico do repositório.

| Nome | Matrícula | Responsabilidade principal |
| --- | --- | --- |
| Bruno dos Santos | 22501077 | Produtos, estoque, integração externa e documentação |
| Carlos Emanuel | 22509279 | Vendas, pagamentos, ponto de venda e interface |
| Gustavo Augusto | 22507421 | Caixa, relatórios, workflows e publicação |

Modelagem, revisão, segurança, testes e apresentação serão atividades compartilhadas entre os integrantes.

**Professor responsável:** Felippe Pires Ferreira.

---

## 9. Como executar

### Situação atual

O repositório encontra-se na Fase 1, destinada à documentação e à arquitetura da solução. Portanto, ainda não existe uma aplicação Django executável nesta etapa.

O repositório pode ser obtido utilizando:

```bash
git clone https://github.com/Bruno-Kowalski/Central-Beer.git
cd Central-Beer
```

### Execução prevista para a Fase 2

Após a implementação, o processo previsto será:

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
source .venv/bin/activate
```

Instalação das dependências:

```bash
python -m pip install -r requirements.txt
```

Preparação do banco:

```bash
python manage.py migrate
```

Verificação do projeto:

```bash
python manage.py check
```

Execução local:

```bash
python manage.py runserver
```

O procedimento definitivo será atualizado durante a implementação da Fase 2.

---

## 10. Configuração

As configurações sensíveis serão fornecidas por variáveis de ambiente e não serão versionadas no GitHub.

Variáveis previstas:

| Variável | Descrição |
| --- | --- |
| `DJANGO_SECRET_KEY` | Chave secreta do ambiente |
| `DJANGO_DEBUG` | Controle do modo de depuração |
| `DJANGO_ALLOWED_HOSTS` | Hosts autorizados |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | Origens HTTPS confiáveis |
| `SQLITE_PATH` | Caminho do banco SQLite |
| `DJANGO_SECURE_SSL_REDIRECT` | Redirecionamento HTTPS em produção |
| `DJANGO_SESSION_COOKIE_SECURE` | Proteção do cookie de sessão |
| `DJANGO_CSRF_COOKIE_SECURE` | Proteção do cookie CSRF |
| `OFF_USER_AGENT` | Identificação utilizada nas consultas ao Open Food Facts |
| `OFF_CONNECT_TIMEOUT` | Tempo máximo para conexão com o serviço externo |
| `OFF_READ_TIMEOUT` | Tempo máximo para leitura da resposta externa |

Exemplo previsto para identificação no Open Food Facts:

```text
CentralBeer/0.0.1 (https://github.com/Bruno-Kowalski/Central-Beer)
```

Credenciais, senhas, tokens, arquivos `.env`, banco local e backups não deverão ser enviados ao repositório.

---

## 11. Testes

Os testes serão implementados durante a Fase 2 utilizando as ferramentas do Django.

Comando previsto:

```bash
python manage.py test
```

### Tipos de testes planejados

| Tipo | Ferramenta | Objetivo |
| --- | --- | --- |
| Unitários | Django TestCase | Validar regras e cálculos |
| Integração | Django TestCase e Client | Validar fluxos entre módulos |
| Transacionais | Django TransactionTestCase | Validar atomicidade e reversões |
| API | Django REST Framework / Client | Validar autenticação, endpoints e respostas |
| Manuais | Roteiro de testes | Validar interface e experiência de uso |

Entre os principais cenários previstos estão:

- entrada de mercadorias;
- venda por unidade;
- venda por caixa;
- estoque suficiente e insuficiente;
- pagamento em uma forma;
- pagamento dividido;
- cálculo de troco;
- prevenção de duplicidade de venda;
- cancelamento de venda;
- restauração do estoque;
- abertura e fechamento de caixa;
- retirada e reforço;
- diferenças de fechamento;
- indisponibilidade do Open Food Facts;
- acesso não autorizado.

### Segurança

Na Fase 2 estão previstas:

- **SAST:** Bandit;
- **análise de dependências:** pip-audit;
- **DAST:** OWASP ZAP.

Os resultados deverão ser documentados juntamente com achados, severidade, correções e nova verificação.

---

## 12. Uso de inteligência artificial

A atividade possui orientações específicas sobre o uso de inteligência artificial, representadas também pelo material disponibilizado no template:

![Política de uso de IA — semáforo](images/semaforo.png)

### Declaração de uso

Houve utilização do ChatGPT como ferramenta de apoio durante o projeto.

O uso envolveu principalmente:

- interpretação e discussão do enunciado;
- apoio na organização do repositório;
- discussão de alternativas técnicas;
- revisão de consistência entre artefatos;
- apoio na organização visual e documental;
- revisão do README.

As decisões relacionadas ao domínio do CentralBeer, incluindo estoque, vendas, caixa, pagamentos, regras de negócio e escopo, devem permanecer compreendidas e justificáveis pelos integrantes do grupo.

---

## 13. Contribuição e fluxo de trabalho

O histórico do projeto deverá permitir identificar as contribuições realizadas por cada integrante.

### Branches previstas

- `main` — versão destinada à avaliação;
- `feat/nome` — novas funcionalidades;
- `fix/nome` — correções;
- `docs/nome` — documentação;
- `test/nome` — testes;
- `ci/nome` — automação.

### Padrão de commits

O projeto utiliza mensagens de commit curtas e descritivas.

Exemplos:

```text
feat: adiciona cadastro de produtos
fix: corrige cálculo do troco
docs: atualiza README do CentralBeer
test: adiciona testes de cancelamento
ci: configura testes do Django
```

Durante a Fase 1, os commits de documentação também permitem identificar a participação dos integrantes na construção dos artefatos.

---

## 14. Histórico de versões

| Versão | Data | Descrição |
| --- | --- | --- |
| `0.0.1` | 03/10/2026 | Início da organização e documentação do CentralBeer |

As versões desta etapa representam marcos documentais. Ainda não existe uma versão executável da aplicação.

Ao concluir a revisão da Fase 1, o commit utilizado para a entrega poderá ser identificado por uma tag específica.

---

## 15. Limitações e próximos passos

### Situação atual

- a aplicação ainda não foi implementada;
- a aplicação ainda não possui URL pública;
- os testes automatizados ainda não foram implementados;
- as análises SAST e DAST serão realizadas na Fase 2;
- os artefatos da Fase 1 representam o comportamento e a arquitetura planejados para a implementação.

### Limitações da primeira versão

- um estabelecimento;
- um caixa aberto por vez;
- sem emissão fiscal;
- sem integração com SEFAZ;
- sem processamento direto de PIX ou cartão;
- sem múltiplas filiais;
- sem vendas fiadas;
- sem controle de entregas;
- sem controle de vasilhames retornáveis;
- sem cancelamento parcial de vendas;
- sem alteração retroativa de caixas já fechados.

### Próximos passos

Na Fase 2 deverão ser realizados:

- criação do projeto Django;
- implementação dos Models;
- criação das migrations;
- implementação das regras de negócio;
- desenvolvimento das interfaces;
- implementação da API REST;
- integração com Open Food Facts;
- criação dos relatórios;
- implementação dos testes;
- publicação da aplicação;
- execução das análises SAST e DAST;
- atualização da documentação conforme a implementação final.

---

## 16. Licença, referências e contato

### Licença

A licença do código desenvolvido pela equipe será definida e adicionada ao repositório durante a implementação.

Materiais de terceiros permanecem sujeitos às suas respectivas licenças e condições de uso.

### Documentação complementar

A documentação completa da Fase 1 pode ser acessada pelo índice:

- [Documentação do CentralBeer](docs/README.md)

Principais documentos:

- [Documento de Visão](docs/visao/README.md)
- [Modelagem](docs/modelagem/README.md)
- [Casos de Uso](docs/modelagem/casos-de-uso/README.md)
- [Arquitetura](docs/modelagem/arquitetura/README.md)
- [Contrato Inicial da API](docs/api/README.md)
- [Plano de Integração Externa](docs/integracao/README.md)
- [Protótipos e Identidade Visual](docs/prototipos/README.md)
- [Planejamento](docs/planejamento/README.md)
- [Matriz de Rastreabilidade](docs/rastreabilidade/matriz-de-rastreabilidade.md)

### Referências

- Ferreira, Felippe Pires. Especificação do trabalho prático de Desenvolvimento Web com Python e Django.
- [Repositório-base do professor](https://github.com/Felippe-Pires/template_projects)
- [Python](https://docs.python.org/3.12/)
- [Django](https://docs.djangoproject.com/en/5.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/docs.html)
- [Bootstrap](https://getbootstrap.com/docs/5.3/)
- [Open Food Facts API](https://openfoodfacts.github.io/documentation/docs/Product-Opener/api/)
- [PythonAnywhere](https://help.pythonanywhere.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Bandit](https://bandit.readthedocs.io/)
- [OWASP ZAP](https://www.zaproxy.org/docs/)

O repositório CentralBeer foi derivado do repositório-base disponibilizado pelo professor para a atividade, preservando a origem do material.

### Repositório

[CentralBeer no GitHub](https://github.com/Bruno-Kowalski/Central-Beer)
