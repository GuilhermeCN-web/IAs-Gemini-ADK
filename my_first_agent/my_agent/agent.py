from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.8-flash',
    name='root_agent',
    description='Ajuda estudantes a aprender álgebra com orientação pelas etapas de solução de problemas.',
    instruction='Você é um orientador de matemática paciente. Ajude os estudantes a resolver problemas de álgebra.',
)
