# Agentes de IA com Google ADK

Coleção de projetos de estudo em Python que explora diferentes padrões de agentes com o Google Agent Development Kit (ADK) e modelos Gemini. Cada pasta é um exemplo independente: há agentes conversacionais simples, extração estruturada, uso de ferramentas, estado de sessão, planejamento e integração com pesquisa ou MCP.

> Os agentes com bases de pedidos, voos, hotéis e capitais usam dados fixos de demonstração. Eles não consultam sistemas comerciais reais nem processam transações reais.

## Índice

- [Projetos](#projetos)
- [Requisitos e configuração](#requisitos-e-configuração)
- [Como executar](#como-executar)
- [Conceitos explorados](#conceitos-explorados)

## Projetos

### `my_first_agent` — agente básico de perguntas

Agente introdutório chamado `math_tutor_agent`, criado com `Agent`. Apesar do nome, suas instruções atuais são genéricas: ele responde às perguntas conforme seu conhecimento, sem ferramenta ou fluxo especializado.

**Arquivo:** `my_first_agent/agent.py`

### `my_agent` — tutor de álgebra

Agente simples voltado a ajudar estudantes com problemas de álgebra e orientar a resolução por etapas. É uma versão focada em matemática, embora suas instruções ainda sejam curtas.

**Arquivo:** `my_agent/agent.py`

### `customer_support_agent` — suporte técnico

Agente de suporte que segue quatro etapas: reconhecer o problema, esclarecer os detalhes, sugerir uma solução e confirmar o resultado. As instruções também definem limites de privacidade e encaminhamento para equipes apropriadas; não há integração real para criar chamados ou transferir casos.

**Arquivo:** `customer_support_agent/agent.py`

### `customer_support` — pedidos, reembolsos e escalonamento

Agente de e-commerce com três ferramentas Python:

- `check_order_status`: consulta uma pequena base de pedidos em memória.
- `process_refund`: simula reembolso apenas para pedidos entregues.
- `escalate_to_supervisor`: simula o encaminhamento e gera um identificador de tíquete.

Os dados e resultados são simulados; não há conexão com clientes, pagamentos ou atendimento humano real.

**Arquivo:** `customer_support/agent.py`

### `travel_agent` — planejamento de viagem

Pesquisa opções de voos e hotéis e estima o custo de passagem mais hospedagem. As ferramentas têm dados fixos para Paris e Tóquio; não consultam companhias aéreas, hotéis ou preços atuais.

**Arquivo:** `travel_agent/agent.py`

### `geography_assistant` — capitais de países

Responde perguntas sobre capitais usando a função `get_capital_city` e um dicionário local com alguns países. Não é uma base geográfica completa.

**Arquivo:** `geography_assistant/agent.py`

### `product_extractor` — extração estruturada de produtos

Extrai nome, preço, armazenamento e cor de uma mensagem. Define o formato de saída com Pydantic (`ProductInfo`) e guarda o resultado na chave `extracted_product` do estado da sessão.

**Arquivo:** `product_extractor/agent.py`

### `name_extractor` — extração de nomes

Extrai o nome de uma pessoa mencionado na mensagem e configura a resposta para ser salva em `user_name` no estado da sessão.

**Arquivo:** `name_extractor/agent.py`

### `personalized_greeter` — saudação com estado

Personaliza uma saudação usando variáveis de estado como nome, idioma preferido e nível de associação. Os valores padrão são usados quando não há dados no estado.

**Arquivo:** `personalized_greeter/agent.py`

### `namespace_demo` — demonstração de templating

Repete o exemplo de saudação personalizada para demonstrar substituição de valores e padrões em instruções. É um exemplo separado de `personalized_greeter`, não uma dependência dele.

**Arquivo:** `namespace_demo/agent.py`

### `research_assistant` — pesquisa na web

Assistente que usa a ferramenta `google_search` para perguntas que dependem de informação atual e orienta a citar fontes e reconhecer limitações dos resultados.

**Arquivo:** `research_assistant/agent.py`

### `file_reader_assistant` — leitura de arquivos via MCP

Usa o servidor de sistema de arquivos do MCP para listar e ler arquivos. O caminho permitido é `file_reader_assistant/my_files`, e o agente expõe somente as ferramentas de leitura `list_directory` e `read_file`.

**Arquivo:** `file_reader_assistant/agent.py`  
**Arquivos de exemplo:** `file_reader_assistant/my_files/`

### `problem_solver` — resolução estratégica de problemas

Agente orientado a decompor problemas, analisar abordagens, planejar e propor recomendações. Configura o `BuiltInPlanner` com parâmetros de pensamento do modelo.

**Arquivo:** `problem_solver/agent.py`

### `model_comparison` — comparação de configurações

Define dois agentes com objetivos e parâmetros distintos:

- `data_extractor`: prioriza extração factual consistente, com temperatura baixa e saída limitada.
- `creative_brainstormer`: prioriza geração de ideias variadas, com temperatura mais alta.

A pasta demonstra configurações contrastantes de geração; não contém, por si só, um mecanismo de avaliação automática entre os resultados.

**Arquivo:** `model_comparison/agent.py`

## Requisitos e configuração

- Python instalado.
- Google ADK e dependências dos exemplos instalados no ambiente Python.
- Chave de API do Google AI Studio para os modelos Gemini.
- Para `file_reader_assistant`, Node.js/npx disponível para iniciar o servidor MCP de sistema de arquivos.

Configure a variável `GOOGLE_API_KEY` no ambiente ou no arquivo `.env` reconhecido pelo ADK para o agente. Exemplo:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

Mantenha a chave privada e não a envie para o Git. Os arquivos `.env` não devem conter segredos versionados.

## Como executar

No PowerShell, a partir da raiz do repositório, ative o ambiente virtual (se já estiver configurado) e inicie um agente:

```powershell
.\.venv\Scripts\Activate.ps1
adk web customer_support
```

Troque `customer_support` pelo nome da pasta do agente que deseja abrir. Por exemplo:

```powershell
adk web travel_agent
adk web research_assistant
adk web file_reader_assistant
```

A interface web do ADK informa o endereço local ao iniciar. Para encerrar, pressione `Ctrl+C` no terminal. Execute um agente por vez na mesma porta padrão.

> `model_comparison` define dois agentes no mesmo arquivo e não declara um `root_agent`; pode exigir configuração adicional para seleção/execução pela interface web do ADK.

## Conceitos explorados

- Instruções e identidade de agentes com `Agent` e `LlmAgent`.
- Ferramentas Python chamadas pelo agente.
- Saídas estruturadas com Pydantic.
- Estado de sessão e templating de instruções.
- Parâmetros de geração e planejamento.
- Pesquisa web e integração com ferramentas MCP.

Os projetos são exemplos de aprendizado. As integrações simuladas devem ser conectadas a serviços reais e protegidas adequadamente antes de qualquer uso em produção.
