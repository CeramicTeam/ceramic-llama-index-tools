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
        """Search the web using Ceramic.
        Use for accurate current information — news, prices, recent events, documentation, general fact checking.
        Returns up to 10 ranked results with titles, URLs, and descriptions.
        Ceramic matches exact keywords — it does not interpret natural language or synonyms automatically.
        Query rules:
        - Queries must be 2-8 words
        - Include specific entities, topics, locations, and dates
        - Do not include uninformative words such as articles (the, a, an). Avoid prepositions (on, about, in, for, of, at, by, with) unless they are within established phrases or names (United States of America, Into the Wild).
        - Keep word order meaningful (`house cat` and `cat house` return different results)
        - Good keyword query examples:
            - "2026 Super Bowl halftime performer"
            - "climate change effects global warming impact"
            - "beginner investing strategies stocks bonds basics"
        If the search returns no useful results, retry with a more specific keyword query.

        Args:
            query: keyword search query with 2–8 words
        """
        response = self.client.search(query=query)
        return [
            Document(
                text=result.description,
                metadata={"title": result.title, "url": result.url},
            )
            for result in response.result.results
        ]
