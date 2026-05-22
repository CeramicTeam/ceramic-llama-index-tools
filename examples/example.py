import os

from llama_index.agent.openai import OpenAIAgent

from llama_index.tools.ceramic import CeramicToolSpec

ceramic_tool = CeramicToolSpec(api_key=os.environ["CERAMIC_API_KEY"])

agent = OpenAIAgent.from_tools(
    ceramic_tool.to_tool_list(),
    verbose=True,
)

response = agent.chat("What are the latest California tenant protection laws?")
print(response)
