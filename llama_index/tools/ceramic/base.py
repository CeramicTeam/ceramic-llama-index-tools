"""Ceramic Search tool spec."""

from typing import List

from llama_index.core.schema import Document
from llama_index.core.tools.tool_spec.base import BaseToolSpec


class CeramicToolSpec(BaseToolSpec):
    """Ceramic Search tool spec."""

    spec_functions = ["search"]

    def __init__(self, api_key: str) -> None:
        """Initialize with a Ceramic API key."""
        from ceramic_ai import Ceramic

        self.client = Ceramic(api_key=api_key)

    def search(self, query: str) -> List[Document]:
        """Search the Ceramic AI knowledge base. Returns ranked results with titles, URLs, and descriptions.

        Ceramic is a lexical (keyword-based) search engine — it matches exact words, not meaning or intent.

        Ideal Use Cases:
        - Keyword and entity lookups, technical terms, named people/products/events
        - Answering questions that require fresh or current information

        Not ideal for: Conversational or natural language questions.

        Query tips:
        - Use keywords, not full sentences. "2026 Super Bowl halftime performer" not "Who performed at the Super Bowl this year?"
        - Include explicit synonyms when terminology may vary.

        For best results, rewrite user queries into concise keyword-focused searches before calling this tool.
        Issuing multiple simpler keyword queries and aggregating the results often outperforms a single complex query.

        Args:
            query: A keyword-focused search query. Aim for 2–8 words for best results.
        """
        response = self.client.search(query=query)
        return [
            Document(
                text=result.description,
                metadata={"title": result.title, "url": result.url},
            )
            for result in response.result.results
        ]
