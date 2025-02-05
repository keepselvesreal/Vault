from qdrant_client import QdrantClient

from src.infrastructure.db.qdrant import connection

def test_qdrant_connection():
    assert isinstance(connection, QdrantClient)
