from qdrant_client import QdrantClient


def test_qdrant_database(qdrant_database):
    assert isinstance(qdrant_database, QdrantClient)