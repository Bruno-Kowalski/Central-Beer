# Gestão Distribuidora

![Status](https://img.shields.io/badge/status-em_planejamento-yellow)
![Versão](https://img.shields.io/badge/versão-0.0.1-blue)

**Instituição:** CEUB  
**Curso:** Análise e Desenvolvimento de Sistemas  
**Disciplina:** Desenvolvimento Web  
**Turma / Semestre:** Turma A / 2026.2  
**Professor(a):** Felippe Pires Ferreira  
**Status do projeto:** Em planejamento — Fase 1: documentação e arquitetura  

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

O Gestão Distribuidora é uma proposta de sistema web voltado ao controle de estoque, vendas e caixa de uma distribuidora de bebidas. O projeto parte da dificuldade do cliente em acompanhar as entradas e saídas de mercadorias e localizar os produtos com facilidade durante o atendimento.

A solução pretende reunir o cadastro dos produtos, o registro das movimentações de estoque e a realização de vendas em um mesmo sistema. Ao finalizar uma venda, os produtos vendidos serão descontados automaticamente do estoque, e os pagamentos serão registrados para a conferência do caixa.

O estoque será mantido em unidades, permitindo entradas e vendas por unidade ou caixa fechada. A conversão utilizará a quantidade de unidades por caixa informada no cadastro de cada produto. O sistema também contemplará abertura de caixa, retiradas, reforços de troco e fechamento com identificação de sobras ou faltas.

### Objetivos

- **Objetivo geral:** desenvolver uma aplicação web para facilitar o controle de estoque, vendas e caixa de uma distribuidora de bebidas.
- **Objetivos específicos:**
  - Centralizar o cadastro e a consulta de produtos.
  - Registrar entradas e saídas de mercadorias.
  - Converter quantidades informadas em caixas para unidades.
  - Facilitar a busca de produtos durante a venda.
  - Atualizar automaticamente o estoque após a finalização das vendas.
  - Registrar pagamentos e permitir a conferência do caixa.
  - Disponibilizar relatórios, uma API REST própria e uma integração externa útil ao usuário.

### Público-alvo

- Proprietários e administradores de distribuidoras de bebidas.
- Atendentes responsáveis pelas vendas e pela operação do caixa.
- Funcionários responsáveis pelo recebimento e controle de mercadorias.

---

## 2. Funcionalidades

| Funcionalidade | Descrição | Status |
| --- | --- | --- |
| Autenticação | Identificação dos usuários para acesso ao sistema e às operações autorizadas. | Planejada |
| Cadastro de produtos | Inclusão, consulta, alteração e exclusão conforme as restrições de histórico a definir. | Planejada |
| Configuração de embalagens | Registro da quantidade de unidades por caixa no cadastro do produto. | Planejada |
| Entrada de mercadorias | Registro de entradas por unidade ou caixa, com conversão para unidades. | Planejada |
| Consulta de estoque | Visualização dos saldos dos produtos em unidades. | Planejada |
| Busca de produtos | Localização de produtos para consulta e atendimento no caixa. | Planejada |
| Registro de vendas | Inclusão de produtos vendidos por unidade ou caixa fechada. | Planejada |
| Baixa automática | Atualização do estoque após a finalização da venda. | Planejada |
| Registro de pagamentos | Registro de dinheiro, PIX, débito e crédito, com até duas formas por venda. | Planejada |
| Abertura de caixa | Registro do valor inicial para troco, com somente um caixa aberto por vez. | Planejada |
| Movimentações de caixa | Registro de retiradas e reforços de dinheiro durante a operação. | Planejada |
| Fechamento de caixa | Comparação entre valores esperados e conferidos, apresentando sobra ou falta. | Planejada |
| Cancelamento de vendas | Cancelamento mediante autorização com senha do administrador. | Planejada |
| Relatórios | Consulta de informações consolidadas, com filtros e opção de exportação ou impressão a definir. | Planejada |
| API REST própria | Disponibilização de dados selecionados em JSON, com documentação e controle de acesso. | Planejada |
| Integração externa | Consulta de informações de produtos por código de barras para auxiliar o cadastro; serviço ainda em avaliação. | Planejada |

### Requisitos não funcionais

- **Desempenho:** metas de tempo de resposta e volume de dados a definir.
- **Segurança:** validação de dados no servidor, controle de acesso, proteção das senhas e configurações sensíveis por variáveis de ambiente.
- **Usabilidade:** interface responsiva, com identificação clara dos produtos, quantidades, valores e mensagens das operações.
- **Disponibilidade:** publicação com HTTPS durante o período de avaliação; hospedagem ainda a definir, com armazenamento persistente para o SQLite.

---

## 3. Demonstração

Os protótipos ainda serão elaborados. As capturas de tela da documentação geral serão armazenadas em `images/` quando estiverem disponíveis.

| Tela | Descrição |
| --- | --- |
| A definir | As telas essenciais serão detalhadas durante a elaboração dos protótipos da Fase 1. |

**Vídeo / protótipo:** ainda não disponível.

---

## 4. Tecnologias utilizadas

O projeto está na fase de documentação. Python, Django e SQLite estão definidos para a implementação; as demais escolhas técnicas permanecem em avaliação.

| Camada | Tecnologia | Versão |
| --- | --- | --- |
| Linguagem | Python | A definir |
| Frontend | A definir | A definir |
| Backend | Django | A definir |
| Banco de dados | SQLite | A definir |
| Testes | A definir | A definir |
| Infraestrutura | Hospedagem a definir | — |
| Outras ferramentas | Git e GitHub | — |

---

## 5. Arquitetura

A arquitetura será documentada durante a Fase 1, incluindo a organização dos componentes, suas responsabilidades, a integração externa e o fluxo de dados.

O backend será desenvolvido em Python e Django, com persistência em SQLite. A tecnologia da interface e a organização interna da aplicação ainda serão definidas pelo grupo.

Os diagramas e suas explicações serão armazenados em `docs/`, acompanhados dos arquivos-fonte editáveis e das versões exportadas para consulta.

**Decisões relevantes:**

- Uso de Python e Django no backend, conforme a exigência da atividade.
- Uso de SQLite como banco de dados relacional.
- Controle do estoque em unidades, com conversão de caixas conforme o cadastro do produto.
- Registro dos pagamentos confirmados pelo atendente, com maquininha e aplicativo bancário operando separadamente.
- Disponibilização de API REST própria e consumo de serviço externo, conforme os requisitos do trabalho.

### Endpoints principais (quando houver API)

| Método | Rota | Descrição |
| --- | --- | --- |
| A definir | A definir | Os endpoints serão especificados no contrato inicial da API durante a Fase 1. |

Documentação completa da API: ainda não disponível.

A API externa para consulta de produtos por código de barras ainda está em avaliação. Sua escolha dependerá da cobertura dos produtos, documentação, condições de uso e tratamento de falhas.

---

## 6. Organização dos diretórios

Estrutura atual do repositório:

```text
.
├── README.md
├── docs/
│   └── modelagem/
│       ├── casos-de-uso/
│       │   └── especificacoes-casos-de-uso.pdf
│       ├── classes/
│       │   └── diagrama-de-classes.pdf
│       └── banco-de-dados/
│           ├── diagrama-er.pdf
│           └── modelo-logico.pdf
└── images/
    └── semaforo.png
```

| Diretório / arquivo | Função |
| --- | --- |
| `README.md` | Apresentação do projeto, objetivos, tecnologias, situação atual e orientações de uso. |
| `docs/` | Documentação técnica do projeto. |
| `docs/modelagem/` | Arquivos de casos de uso, classes e modelo de dados herdados do template. |
| `images/` | Figuras da documentação geral do repositório. |
| `images/semaforo.png` | Imagem da política de uso de IA disponibilizada no template. |

Os PDFs atuais foram recebidos com o template e ainda não representam a modelagem específica do Gestão Distribuidora. As pastas de código, testes e configuração serão adicionadas durante o desenvolvimento.

---

## 7. Participantes

| Nome | Matrícula | Função no projeto |
| --- | --- | --- |
| Bruno dos Santos | A informar | A definir pelo grupo |
| Carlos Emanuel | A informar | A definir pelo grupo |
| Gustavo Augusto | A informar | A definir pelo grupo |

**Professor(a) responsável:** Felippe Pires Ferreira.

---

## 8. Como executar

### Pré-requisitos

Para obter a documentação atual:

- Git.

Para executar a futura aplicação:

- Python, em versão a definir.
- Dependências do projeto, que serão registradas durante a implementação.

### Instalação e execução

O projeto ainda não possui uma aplicação executável. Para obter uma cópia do repositório:

```bash
git clone https://github.com/Bruno-Kowalski/gestao-distribuidora.git
cd gestao-distribuidora
```

As instruções de instalação das dependências, configuração do ambiente, execução das migrations e inicialização do Django serão adicionadas após a implementação.

**Acesso local:** ainda não disponível.

### Implantação (quando houver)

- **Ambiente:** a definir.
- **URL de produção:** ainda não disponível.
- **Observações:** a hospedagem deverá oferecer HTTPS e armazenamento persistente para o arquivo do banco SQLite.

---

## 9. Configuração

As variáveis de ambiente ainda serão definidas durante a configuração do projeto Django.

| Variável | Obrigatória | Descrição | Exemplo |
| --- | --- | --- | --- |
| A definir | A definir | As configurações serão documentadas após a implementação. | — |

O banco SQLite será criado pelas migrations do Django. O arquivo do banco local não será versionado no GitHub.

Credenciais reais deverão permanecer fora do repositório. Quando necessário, será disponibilizado um `.env.example` com os nomes das variáveis e exemplos sem segredos.

---

## 10. Testes

Os testes ainda não foram implementados. Os comandos de execução serão adicionados junto ao código da aplicação.

| Tipo | Ferramenta | O que verifica |
| --- | --- | --- |
| Unitários | A definir | Cálculos e regras isoladas, incluindo conversão de caixas e valores das vendas. |
| Integração | A definir | Relação entre vendas, estoque, caixa, API e banco de dados. |
| Manuais | Roteiro a elaborar | Fluxos principais de cadastro, entrada, venda, cancelamento e fechamento. |

**Cobertura atual:** não medida; implementação não iniciada.

Na Fase 2, também serão realizadas análises SAST e DAST, com registro das ferramentas, resultados, correções e verificações posteriores. O DAST será executado somente contra ambiente autorizado do grupo.

---

## 11. Uso de inteligência artificial

Este repositório segue a política de uso de IA da disciplina (semáforo pedagógico):

![Política de uso de IA — semáforo](images/semaforo.png)

| Situação | Significado |
| --- | --- |
| **Vermelho — uso proibido** | Atividades de autonomia intelectual, como provas presenciais sem consulta. |
| **Amarelo — uso limitado** | IA pode ser ferramenta auxiliar, desde que haja declaração de uso. |
| **Verde — uso permitido** | Uso livre ao longo da atividade acadêmica. |

### Declaração de uso

- **Houve uso de IA neste projeto?** Sim.
- **Ferramentas utilizadas:** ChatGPT.
- **Finalidade:** esclarecimento do enunciado, discussão de possibilidades, orientação sobre GitHub e geração deste rascunho de README com base nas informações fornecidas por Bruno dos Santos.
- **O que NÃO foi delegado à IA:** relato da dificuldade do cliente e confirmação das decisões operacionais pelo aluno. Arquitetura detalhada, modelagem e implementação ainda não foram concluídas.

A especificação da atividade contém restrições ao uso de IA na elaboração dos documentos. Este README é um rascunho gerado com IA; sua utilização na entrega deverá ser validada com o professor.

---

## 12. Contribuição e fluxo de trabalho

### Branches

- `main` — versão estável para avaliação.
- `develop` — integração do grupo, caso seja adotada.
- `feat/[nome]` — nova funcionalidade.
- `fix/[nome]` — correção de defeito.
- `docs/[nome]` — alterações de documentação.

### Commits

Utilizar mensagens curtas e claras, por exemplo:

- `feat: adiciona cadastro de produtos`
- `fix: corrige conversão de caixas`
- `docs: atualiza apresentação do projeto`

### Passos sugeridos

1. Criar uma branch a partir de `main`.
2. Implementar e verificar as alterações localmente.
3. Abrir um pull request para revisão do grupo.
4. Integrar as alterações à branch principal após a revisão.

Cada integrante deverá utilizar sua própria conta, mantendo contribuições identificáveis no histórico.

**Issues e quadro de tarefas:** ferramenta e organização a definir pelo grupo.

---

## 13. Histórico de versões

| Versão | Data | Descrição |
| --- | --- | --- |
| `0.0.1` | 2026-10-03 | Criação do repositório com a estrutura inicial disponibilizada pelo professor. |

A entrega da documentação da Fase 1 está prevista para **05/10/2026**. O commit ou a tag correspondente será registrado após a conclusão e revisão dos materiais.

---

## 14. Limitações e próximos passos

### Problemas conhecidos

- A aplicação ainda não foi implementada.
- Os PDFs herdados do template ainda não representam a modelagem do projeto.
- A API externa ainda não foi escolhida ou validada.
- A identidade visual, os protótipos e a arquitetura detalhada estão pendentes.
- As condições de cancelamento e seus efeitos no estoque e nos pagamentos precisam ser detalhados.
- A emissão fiscal e a integração com a SEFAZ não fazem parte do escopo inicial.
- Os pagamentos serão registrados manualmente após confirmação do atendente, sem integração bancária ou com maquininha.

### Roadmap

- [ ] Confirmar os colaboradores e distribuir as responsabilidades.
- [ ] Elaborar o Documento de Visão.
- [ ] Elaborar os casos de uso e suas especificações.
- [ ] Documentar a arquitetura.
- [ ] Elaborar os modelos de dados.
- [ ] Definir o contrato inicial da API REST.
- [ ] Validar e selecionar a API externa.
- [ ] Definir nome definitivo e identidade visual.
- [ ] Elaborar os protótipos das telas essenciais.
- [ ] Registrar backlog, responsáveis, marcos e riscos.
- [ ] Revisar a correspondência entre os documentos.
- [ ] Registrar a entrega da Fase 1.
- [ ] Implementar, testar e publicar a aplicação na Fase 2.
- [ ] Executar e documentar as análises SAST e DAST.

---

## 15. Licença, referências e contato

**Licença:** a definir pelo grupo, respeitando as condições dos materiais de terceiros utilizados.

Este material destina-se a fins educacionais. A disponibilidade pública do repositório não representa, por si só, autorização irrestrita de reutilização.

### Documentação complementar

Os arquivos abaixo foram herdados do template e ainda não constituem a documentação específica da distribuidora:

- Casos de uso: [`docs/modelagem/casos-de-uso/especificacoes-casos-de-uso.pdf`](docs/modelagem/casos-de-uso/especificacoes-casos-de-uso.pdf)
- Diagrama de classes: [`docs/modelagem/classes/diagrama-de-classes.pdf`](docs/modelagem/classes/diagrama-de-classes.pdf)
- Modelo conceitual: [`docs/modelagem/banco-de-dados/diagrama-er.pdf`](docs/modelagem/banco-de-dados/diagrama-er.pdf)
- Modelo lógico: [`docs/modelagem/banco-de-dados/modelo-logico.pdf`](docs/modelagem/banco-de-dados/modelo-logico.pdf)

O índice da documentação e a apresentação serão incluídos quando forem elaborados.

### Referências

- Ferreira, Felippe Pires. Especificação do trabalho prático de Desenvolvimento Web com Python e Django. Material disponibilizado na disciplina.
- [Template disponibilizado pelo professor](https://github.com/Felippe-Pires/template_projects)

O repositório foi criado por meio de fork do material indicado, pois a opção “Use this template” não estava disponível. A aceitação desse procedimento para a entrega deverá ser confirmada com o professor.

### Contato

Dúvidas sobre o projeto: entrar em contato com os integrantes do grupo.

**Agradecimentos:** ao professor Felippe Pires Ferreira pelas orientações e pelo material disponibilizado para a atividade.
