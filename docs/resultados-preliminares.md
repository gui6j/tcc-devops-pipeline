# Resultados Preliminares

## Desenvolvimento da API

Foi desenvolvida uma API REST utilizando FastAPI, contendo endpoints para monitoramento e validação da aplicação.

Os endpoints implementados foram:

- /
- /health
- /versao
- /info
- /status
- /metricas

## Containerização

A aplicação foi containerizada utilizando Docker, permitindo sua execução de forma padronizada em diferentes ambientes.

## Integração Continua

Foi implementada uma pipeline de integração continua utilizando GitHub Actions.

A pipeline executa automaticamente a validação da aplicação sempre que alterações são enviadas ao repositorio.

## Metricas

Foi criado um endpoint dedicado para exposição de metricas basicas da aplicação, permitindo futuras integrações com ferramentas de monitoramento.