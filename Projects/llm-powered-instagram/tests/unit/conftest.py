import pytest

class ContextRetriver:
    def __init__(self, mock: bool = False) -> None:
        self._query_expander = QueryExpansion(mock=mock)
        self._metadata_extractor = SelfQuery(mock=mock)
        self._reranker = Reranker(mock=mock)

@pytest.fixture
def context_retriever_instance():
    return ContextRetriver()