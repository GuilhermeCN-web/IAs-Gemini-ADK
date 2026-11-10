from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.8-flash',
    name='math_tutor_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge.',
)
