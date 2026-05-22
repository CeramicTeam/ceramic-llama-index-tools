from unittest.mock import MagicMock, patch

from llama_index.tools.ceramic.base import CeramicToolSpec


def _make_mock_client(results):
    mock_result = MagicMock()
    mock_result.result.results = results
    mock_client = MagicMock()
    mock_client.search.return_value = mock_result
    return mock_client


def test_search_returns_documents():
    with patch("ceramic_ai.Ceramic") as MockCeramic:
        mock_item = MagicMock()
        mock_item.title = "Test Title"
        mock_item.url = "https://example.com"
        mock_item.description = "Test result"
        MockCeramic.return_value = _make_mock_client([mock_item])

        spec = CeramicToolSpec(api_key="test-key")
        docs = spec.search("California rental laws")

        assert len(docs) == 1
        assert docs[0].text == "Test result"
        assert docs[0].metadata["url"] == "https://example.com"
        assert docs[0].metadata["title"] == "Test Title"
        MockCeramic.return_value.search.assert_called_once_with(query="California rental laws")


def test_spec_functions():
    with patch("ceramic_ai.Ceramic"):
        spec = CeramicToolSpec(api_key="test-key")
        assert "search" in spec.spec_functions


def test_search_empty_results():
    with patch("ceramic_ai.Ceramic") as MockCeramic:
        MockCeramic.return_value = _make_mock_client([])

        spec = CeramicToolSpec(api_key="test-key")
        docs = spec.search("test query")

        assert docs == []
