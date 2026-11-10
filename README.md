# Minha Primeira IA — Tutor de Matemática

Meu primeiro projeto prático de desenvolvimento de agentes de inteligência artificial, utilizando Python, Google ADK e Gemini.

O projeto consiste em um agente tutor de matemática, desenvolvido para auxiliar estudantes na resolução de problemas matemáticos por meio de explicações detalhadas, cálculos e justificativas passo a passo.

## Sobre o projeto

A aplicação utiliza o **Google Agent Development Kit (ADK)** para estruturar e executar um agente de inteligência artificial, enquanto o **Gemini** é utilizado como modelo de linguagem (LLM).

O modelo de linguagem não foi desenvolvido por mim. Minha contribuição está na construção e configuração do agente, definição de suas instruções, comportamento e finalidade.

## Tecnologias utilizadas

- **Python:** linguagem de programação utilizada no desenvolvimento.
- **Google ADK:** framework responsável pela criação e execução do agente.
- **Gemini:** modelo de linguagem utilizado para interpretar perguntas e gerar respostas.
- **Google AI Studio:** plataforma utilizada para obter a chave de API.
- **python-dotenv:** biblioteca para carregamento de variáveis de ambiente.

## Como funciona?

O funcionamento do agente pode ser dividido em quatro etapas:

1. **Entrada:** o estudante envia uma pergunta ou problema matemático.
2. **Processamento:** o Google ADK recebe a solicitação e a encaminha ao modelo Gemini.
3. **Geração da resposta:** o Gemini interpreta o problema e produz uma resolução seguindo as instruções configuradas no agente.
4. **Saída:** o agente apresenta os cálculos, as explicações e a conclusão ao estudante.

## Exemplo de funcionamento

Um dos testes realizados utilizou um problema envolvendo o lançamento de uma cápsula, cuja altura era representada pela função:

\[
h(t)=-5t^2+60t+25
\]

O agente precisava calcular a altura máxima, determinar o intervalo em que a cápsula permanecia acima de 150 metros e verificar se um sistema de recuperação atendia às condições necessárias para funcionar.

O agente conseguiu:

- Calcular o instante e a altura máxima utilizando o vértice da função quadrática.
- Resolver uma inequação do segundo grau.
- Utilizar derivadas para calcular a velocidade instantânea.
- Verificar as condições de funcionamento do sistema.
- Apresentar uma resolução completa, com justificativas matemáticas.

Esse teste demonstrou a capacidade do agente de resolver problemas que exigem várias etapas de raciocínio matemático.

## Estrutura do projeto

A estrutura identificada no VS Code é:

```text
adk-workspace/
│
├── .venv/
│
└── my_first_agent/
    │
    ├── my_agent/
    │   ├── __init__.py
    │   ├── .env
    │   ├── .gitignore
    │   ├── agent.py
    │   └── root_agent.yaml
    │
    ├── my_config_agent/
    │   ├── .adk/
    │   ├── .env
    │   ├── .gitignore
    │   └── root_agent.yaml
    │
    ├── __init__.py
    ├── .env
    ├── .gitignore
    └── agent.py
```

### Arquivos e diretórios principais

- **`my_agent/`**: diretório do agente tutor de matemática.
- **`agent.py`**: contém a definição e as instruções do agente.
- **`__init__.py`**: permite que o Python reconheça o diretório como um pacote.
- **`root_agent.yaml`**: arquivo de configuração associado ao agente.
- **`.env`**: armazena variáveis de ambiente, incluindo a chave de API.
- **`.gitignore`**: define quais arquivos e diretórios devem ser ignorados pelo Git.
- **`.venv/`**: ambiente virtual utilizado pelo Python.
- **`my_config_agent/`**: diretório utilizado em um exercício de configuração do Google ADK, separado do projeto principal.

## Como executar

### 1. Pré-requisitos

- Python instalado.
- Google ADK instalado.
- Chave de API do Google AI Studio.

### 2. Ativar o ambiente virtual

Abra o terminal na pasta `adk-workspace` e execute:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Acessar o diretório dos agentes

```powershell
cd my_first_agent
```

### 4. Executar o agente tutor de matemática

```powershell
adk web my_agent
```

O servidor será iniciado localmente.

Acesse a interface pelo navegador:

```text
http://127.0.0.1:8000
```

### 5. Utilizar o agente

Após abrir a interface:

1. Selecione o agente disponível.
2. Envie um problema matemático.
3. Aguarde o processamento.
4. Analise a resolução apresentada.

Para encerrar o servidor, pressione `CTRL + C` no terminal.

### Executar o exercício de configuração

O diretório `my_config_agent` corresponde a um exercício separado do projeto principal.

Para executá-lo:

```powershell
adk web my_config_agent
```

Depois, acesse novamente:

```text
http://127.0.0.1:8000
```

## Configuração do agente

O arquivo `my_agent/agent.py` contém a definição do agente principal.

Exemplo da configuração atual:

```python
from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.8-flash',
    name='root_agent',
    description=(
        'Ajuda estudantes a aprender álgebra com orientação '
        'pelas etapas de solução de problemas.'
    ),
    instruction=(
        'Você é um orientador de matemática paciente. '
        'Ajude os estudantes a resolver problemas de álgebra.'
    ),
)
```

Nessa configuração:

- `model`: identifica o modelo de linguagem utilizado.
- `name`: define o nome interno do agente.
- `description`: descreve a finalidade do agente.
- `instruction`: estabelece como ele deve se comportar e auxiliar os estudantes.

## Segurança

A chave de API deve permanecer protegida.

- Não compartilhe sua chave de API.
- Não publique arquivos `.env` no GitHub.
- Verifique se os arquivos `.gitignore` ignoram os arquivos de credenciais.
- Nunca coloque sua chave diretamente no código-fonte.

## Objetivo do projeto

Este projeto representa meu primeiro contato prático com a criação e configuração de agentes de inteligência artificial.

O objetivo é desenvolver conhecimentos em Python, integração com modelos de linguagem, engenharia de prompts e construção de aplicações utilizando frameworks de IA.

**Desenvolvido como projeto de aprendizado em Inteligência Artificial.**
