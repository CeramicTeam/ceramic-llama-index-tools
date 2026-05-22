# llama-index-tools-ceramic

LlamaIndex tool integration for [Ceramic AI](https://ceramic.ai) search.

## Installation

```bash
pip install llama-index-tools-ceramic llama-index-agent-openai
```

## Usage

```python
import os
from llama_index.tools.ceramic import CeramicToolSpec
from llama_index.agent.openai import OpenAIAgent

ceramic_tool = CeramicToolSpec(api_key=os.environ["CERAMIC_API_KEY"])

agent = OpenAIAgent.from_tools(
    ceramic_tool.to_tool_list(),
    verbose=True,
)

response = agent.chat("What are the latest California tenant protection laws?")
print(response)
```

Get a Ceramic API key at [platform.ceramic.ai/keys](https://platform.ceramic.ai/keys).
