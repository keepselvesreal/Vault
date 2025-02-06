from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer


# 태수가 구현했던 클래스
class ContextRetriever:
    def __init__(self, client: QdrantClient, vectorizer):
        self.client = client #! 커플링
        self.vectorizer = vectorizer
        # self.vectorizer = SentenceTransformer(
        #      model_name_or_path = "sentence-transformers/all-MiniLM-L6-v2",
        #      device = "cpu",
        #      cache_folder = None,
        # )

    def search(self, query: str, k: int =3):
        query_embedding = self.vectorizer.from_query_to_vector(query)
        search_result = self.client.query_points( #! 커플링
            collection_name="test_collection",
            query=query_embedding,
            limit=k,
        )

        return search_result

