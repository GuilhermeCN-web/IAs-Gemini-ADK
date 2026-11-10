# 🤖 Meus Agentes de IA com Google ADK

Este projeto reúne dois agentes de inteligência artificial desenvolvidos em Python utilizando o **Google Agent Development Kit (ADK)** e modelos Gemini.

O objetivo é explorar a criação, configuração e execução de agentes capazes de realizar tarefas diferentes por meio de instruções personalizadas.

## 🚀 Tecnologias utilizadas

- **Python** — linguagem de programação.
- **Google ADK** — framework para desenvolvimento e execução de agentes.
- **Google Gemini** — modelo de inteligência artificial utilizado pelos agentes.
- **Google AI Studio** — obtenção da chave de API para acessar os modelos Gemini.

## 📁 Estrutura do projeto

```text
adk-workspace/
│
├── .venv/
│
└── my_first_agent/
    │
    ├── agent.py
    ├── .env
    ├── .gitignore
    ├── __init__.py
    │
    ├── my_agent/
    │   ├── agent.py
    │   ├── __init__.py
    │   ├── .env
    │   └── .gitignore
    │
    └── my_config_agent/
        ├── root_agent.yaml
        ├── .env
        └── .gitignore
```

## 🧠 Agentes desenvolvidos

### 1. Tutor de Matemática

**Nome:** `math_tutor_agent`

Um agente desenvolvido para auxiliar estudantes no aprendizado de matemática, principalmente em problemas de álgebra.

**Principais características:**
- Explica problemas matemáticos passo a passo.
- Auxilia na resolução de equações.
- Apresenta cálculos e justificativas.
- Ajuda o estudante a compreender o raciocínio por trás das respostas.
- Utiliza uma abordagem paciente e educativa.

**Arquivo principal:** `my_agent/agent.py`

### 2. Especialista em Suporte Técnico

**Nome:** `support_specialist`

Um agente desenvolvido para atuar como especialista em atendimento e suporte técnico.

**Principais características:**
- Demonstra empatia diante dos problemas apresentados.
- Faz perguntas para compreender melhor a situação.
- Oferece soluções claras e organizadas.
- Evita inventar informações técnicas.
- Respeita limites de segurança e privacidade.
- Identifica situações que devem ser encaminhadas para equipes especializadas.

**Metodologia de atendimento:**

1. **Reconhecer:** demonstra compreensão do problema.
2. **Esclarecer:** faz perguntas para identificar a causa.
3. **Resolver:** apresenta possíveis soluções.
4. **Verificar:** confirma se o problema foi resolvido.

**Arquivo principal:** `agent.py` (na pasta raiz `my_first_agent`).

> Observação: o encaminhamento para outras equipes é uma orientação definida nas instruções do agente. Atualmente, ele não possui integração real para abrir chamados ou transferir atendimentos.

## ⚙️ Configuração do ambiente

### 1. Pré-requisitos

- Python instalado.
- Google ADK instalado.
- Uma chave de API do Google AI Studio.

### 2. Ativar o ambiente virtual

No terminal, acesse a pasta do projeto e ative o ambiente virtual:

```powershell
cd C:\Users\guias\adk-workspace
.\.venv\Scripts\Activate.ps1
```

Depois, entre na pasta dos agentes:

```powershell
cd my_first_agent
```

### 3. Configurar a chave de API

Crie ou edite o arquivo `.env` correspondente ao agente e configure:

```env
GOOGLE_GENAI_USE_ENTERPRISE=0
GOOGLE_API_KEY=SUA_CHAVE_DE_API
```

Substitua `SUA_CHAVE_DE_API` pela sua chave do Google AI Studio.

**Importante:** não compartilhe sua chave de API e não a envie para o GitHub. Verifique se os arquivos `.env` estão protegidos pelo `.gitignore`.

## ▶️ Como executar os agentes

Com o ambiente virtual ativado e dentro da pasta `my_first_agent`, execute:

**Tutor de Matemática:**

```powershell
adk web my_agent
```

**Especialista em Suporte Técnico:**

```powershell
adk web .
```

**Exercício de configuração do ADK:**

```powershell
adk web my_config_agent
```

Após iniciar o servidor, acesse:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

Para encerrar a execução, pressione `Ctrl + C` no terminal.

> Execute um agente por vez na porta padrão 8000. O comando `adk web .` utiliza a pasta atual como diretório do agente; caso apresente erro, confira a estrutura e a mensagem exibida pelo terminal.

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram explorados conceitos como:

- Criação e configuração de agentes com Google ADK.
- Utilização de modelos Gemini.
- Personalização de comportamento por meio de instruções.
- Definição de identidade, objetivos e limites de atuação.
- Organização de projetos Python.
- Configuração de variáveis de ambiente.
- Execução e testes de agentes por meio da interface web do ADK.

## 🎯 Objetivo do projeto

Este repositório representa uma etapa de aprendizado no desenvolvimento de aplicações com inteligência artificial, explorando como diferentes agentes podem ser configurados para desempenhar funções específicas.

O projeto poderá ser expandido futuramente com novas funcionalidades, ferramentas e integrações.
