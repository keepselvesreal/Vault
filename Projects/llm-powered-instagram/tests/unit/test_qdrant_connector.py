from ...src.infrastructure.db.qdrant import QdrantDatabaseConnector


class TestQdrantDatabaseConnector:
    def setup_method(self):
        QdrantDatabaseConnector._instance = None

    def test_local_connection_success(self):
        pass