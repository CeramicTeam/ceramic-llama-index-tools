# llama-index-tools-ceramic

LlamaIndex tool integration for [Ceramic AI](https://ceramic.ai) search.

## Installation

```bash
pip install llama-index-tools-ceramic llama-index-llms-openai
```

## Usage

```python
import asyncio
import os
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.tools.ceramic import CeramicToolSpec

ceramic_tool = CeramicToolSpec(api_key=os.environ["CERAMIC_API_KEY"])

agent = FunctionAgent(
    tools=ceramic_tool.to_tool_list(),
    llm=OpenAI(model="gpt-5.4"),
)

async def main():
    response = await agent.run("What are the latest California tenant protection laws?")
    print(response)

asyncio.run(main())
```

Get a Ceramic API key at [platform.ceramic.ai/keys](https://platform.ceramic.ai/keys).
