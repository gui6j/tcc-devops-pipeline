# DevSecOps Automation Pipeline

Projeto desenvolvido para demonstrar a automação e a padronização de uma pipeline de Integração Contínua (CI), aplicando conceitos e práticas de DevSecOps em um ambiente baseado em containers.

A solução utiliza uma API desenvolvida com FastAPI, containerização com Docker e automação da pipeline por meio do GitHub Actions, estabelecendo uma base para evolução contínua da aplicação e adoção de boas práticas de engenharia de software.

Este projeto foi desenvolvido como Trabalho de Conclusão do MBA em Engenharia de Software da USP e continua em evolução como laboratório prático para estudos de automação, infraestrutura moderna e DevSecOps.


# Overview

O projeto tem como objetivo demonstrar a implementação de uma pipeline automatizada para validação e entrega de aplicações, utilizando ferramentas amplamente empregadas em ambientes corporativos.

A proposta é disponibilizar uma estrutura simples, organizada e reproduzível, permitindo a evolução gradual da solução com novas funcionalidades relacionadas à integração contínua, segurança, infraestrutura como código e observabilidade.

Além de atender aos requisitos acadêmicos do trabalho de conclusão de curso, o projeto também serve como portfólio técnico para aplicação prática de conceitos utilizados em ambientes DevOps.


# Objectives

Os principais objetivos deste projeto são:

- Demonstrar a criação de uma API utilizando FastAPI.
- Containerizar a aplicação utilizando Docker.
- Automatizar a validação da aplicação utilizando GitHub Actions.
- Padronizar o processo de integração contínua.
- Aplicar conceitos fundamentais de DevSecOps em uma aplicação real.
- Disponibilizar uma base para futuras implementações envolvendo segurança, infraestrutura como código e monitoramento.
- Consolidar conhecimentos adquiridos durante o MBA em Engenharia de Software da USP.


# Architecture

A arquitetura foi projetada para demonstrar uma pipeline de Integração Contínua (CI) simples, modular e reproduzível, utilizando ferramentas amplamente empregadas em ambientes corporativos.

Atualmente, a solução é composta pelos seguintes componentes:

- API REST desenvolvida com FastAPI;
- Containerização da aplicação utilizando Docker;
- Pipeline automatizada utilizando GitHub Actions;
- Repositório GitHub para versionamento do código.

Essa estrutura estabelece uma base sólida para futuras implementações envolvendo análise automatizada de vulnerabilidades, Infraestrutura como Código (IaC), observabilidade e implantação em ambientes Cloud.


## Architecture Diagram

```text
                     Developer
                         │
                         ▼
                GitHub Repository
                         │
                         ▼
               GitHub Actions (CI)
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
 Code Validation                  Docker Build
        │                                 │
        └────────────────┬────────────────┘
                         ▼
                 FastAPI Application
                         │
                         ▼
                  REST API Endpoints
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
        /health       /status       /info
```


## Continuous Integration Workflow

O fluxo atual da pipeline segue as seguintes etapas:

1. O desenvolvedor realiza alterações no código.
2. As alterações são enviadas para o repositório GitHub.
3. O GitHub Actions inicia automaticamente a pipeline de Integração Contínua.
4. A aplicação é validada durante o processo de execução da pipeline.
5. Em caso de sucesso, a aplicação permanece pronta para evolução e futuras etapas de entrega contínua.


# Technologies

O projeto foi desenvolvido utilizando tecnologias amplamente adotadas em ambientes modernos de desenvolvimento, infraestrutura e automação.

| Tecnologia | Finalidade |
|------------|------------|
| Python | Linguagem utilizada no desenvolvimento da aplicação |
| FastAPI | Framework para construção da API REST |
| Docker | Containerização da aplicação |
| GitHub Actions | Automação da pipeline de Integração Contínua (CI) |
| Git | Controle de versão do projeto |


# Features

Atualmente o projeto disponibiliza as seguintes funcionalidades:

- Desenvolvimento de uma API REST utilizando FastAPI;
- Containerização da aplicação com Docker;
- Pipeline automatizada de Integração Contínua (CI) utilizando GitHub Actions;
- Validação automática da aplicação durante o processo de integração;
- Endpoints para monitoramento e verificação da aplicação;
- Estrutura preparada para evolução contínua da solução.

As funcionalidades previstas para as próximas etapas estão descritas na seção **Roadmap**.


# Repository Structure

A organização do projeto foi definida para facilitar sua manutenção e evolução.

```text
tcc-devops-pipeline
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   └── main.py
│
├── docs/
│   ├── evidencias/
│   ├── referencias/
│   └── resultados-preliminares.md
│
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
└── .dockerignore
```

## Directory Structure

| Diretório | Descrição |
|------------|-----------|
| `.github/workflows` | Pipeline de Integração Contínua |
| `app` | Código-fonte da aplicação |
| `docs` | Documentação técnica e evidências |
| `Dockerfile` | Definição da imagem Docker |
| `requirements.txt` | Dependências da aplicação |
| `README.md` | Documentação principal |


# Getting Started

As instruções abaixo descrevem como configurar e executar o projeto em um ambiente local.


## Prerequisites

Antes de iniciar, certifique-se de possuir os seguintes softwares instalados:

| Software | Versão recomendada |
|-----------|-------------------|
| Git | 2.x ou superior |
| Python | 3.13 ou superior |
| Docker Desktop | versão mais recente |
| Visual Studio Code (opcional) | versão mais recente |


# Clone the Repository

Clone o repositório utilizando o comando abaixo:

```bash
git clone https://github.com/gui6j/tcc-devops-pipeline.git
```
Acesse o diretório do projeto:

```bash
cd tcc-devops-pipeline
```

# Running with Docker

Construa a imagem Docker:

```bash
docker build -t devsecops-pipeline .
```

Execute o container:

```bash
docker run -d -p 8000:8000 --name devsecops-pipeline devsecops-pipeline
```

Verifique se o container está em execução:

```bash
docker ps
```

# Running Locally

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
uvicorn app.main:app --reload
```


# Verifying the Application

Após iniciar a aplicação, acesse:

| Recurso | URL |
|-----------|-------------------|
| API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| Health Check | http://localhost:8000/health |


# API Documentation

A aplicação disponibiliza uma API REST desenvolvida com FastAPI para validação da aplicação e monitoramento de seu estado de execução.

Após iniciar a aplicação, a documentação interativa poderá ser acessada através do Swagger UI.

| Recurso | URL |
|----------|-----|
| Swagger UI | http://localhost:8000/docs |
| OpenAPI JSON | http://localhost:8000/openapi.json |


## Available Endpoints

| Método | Endpoint | Descrição |
|---------|----------|-----------|
| GET | `/` | Retorna a mensagem inicial da aplicação. |
| GET | `/health` | Verifica se a aplicação está operacional. |
| GET | `/status` | Retorna informações sobre o estado da aplicação. |
| GET | `/info` | Exibe informações gerais da aplicação. |
| GET | `/versao` | Retorna a versão atual da aplicação. |
| GET | `/metricas` | Disponibiliza métricas básicas da aplicação para futuras integrações com ferramentas de monitoramento. |


## Example Response

### GET /health

```json
{
    "status": "UP"
}
```


## API Documentation Interface

A FastAPI gera automaticamente uma documentação interativa baseada na especificação OpenAPI.

Após executar a aplicação, basta acessar:

```text
http://localhost:8000/docs
```

A interface permite:

- visualizar todos os endpoints disponíveis;
- testar requisições diretamente pelo navegador;
- consultar parâmetros e respostas;
- validar rapidamente o funcionamento da API durante o desenvolvimento.


