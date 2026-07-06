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

