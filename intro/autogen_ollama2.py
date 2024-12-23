# python example for autogen and ollama
from autogen import ConversableAgent, UserProxyAgent

config_list = [
  {
    "model": "llama3",
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama",
  }
]


agent = ConversableAgent(
    name="ZenMaster",
    system_message="You are a zen master and provide insights and "
    "advice on achieving enlightenment",
    llm_config={"config_list": config_list},
    code_execution_config=False,
    human_input_mode="NEVER",
)

response = agent.generate_reply(
    messages=[{"role": "user", "content": "Give me some zen insights, master"}]
)
print(response)
