
from ...domain.embedded_chunks import EmbeddedChunk
from ...domain.queries import Query

class ContextRetriever:
    def __init__(self, mock: bool = False) -> None:
        self._query_expander = None
        self._metadata_extractor = None
        self._reranker = None

    def search(
            self,
            query: str,
            k: int = 3,
            exxpand_to_n_queries: int = 3
    ) -> list:
         query_model = Query.from_str(query)

    def _search(self, query: Query, k: int = 3) -> list[EmbeddedChunk]:
        pass

    def rerank():
        pass