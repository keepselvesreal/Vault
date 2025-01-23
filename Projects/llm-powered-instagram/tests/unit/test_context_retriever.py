import pytest
from unittest.mock import Mock
from qdrant_client.http.models import QueryResponse

from src.application.rag.retriever import ContextRetriever


class TestContextRetriever:
    @pytest.mark.usefixtures("mock_qdrant_client")
    def test_search(self, mock_qdrant_client):

        mock_vectorizer = Mock()
        mock_vectorizer.from_query_to_vector.return_value = [0.1, 0.2, 0.3, 0.4]

        retriever = ContextRetriever(client=mock_qdrant_client, vectorizer=mock_vectorizer)
        search_result = retriever.search(query="test_query", k=3)
        
        assert isinstance(search_result, QueryResponse)  
        
        

