# 🩺 Consultório Bot – Sistema de automação de confirmação de consultas

Sistema web para cadastro de consultas médicas com envio automático de e-mails de confirmação. O sistema envia um e-mail imediatamente após o agendamento e dispara lembretes automáticos na véspera da consulta.

## 🚀 Funcionalidades

- Cadastro de pacientes e agendamento de consultas
- Envio automático de e-mail de confirmação no momento do cadastro
- Envio de lembretes por e-mail na véspera da consulta (agendamento diário)
- Front-end simples com HTML + Flask
- Agendamento via `schedule` para rodar em segundo plano

## 🛠 Tecnologias utilizadas

- **Python**
- **Flask** (backend e templates)
- **Flask-Mail** (envio de e-mails)
- **PostgreSQL** (armazenamento de dados)
- **schedule** (agendamento de tarefas)
- **HTML/CSS** básico para interface


