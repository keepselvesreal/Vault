import pytest
from pymongo import MongoClient

from src.infrastructure.db.mongo import MongoDatabaseConnector

class TestMongoDatabaseConnector:
    @pytest.mark.usefixtures("mongo_client")
    def test_new(self, mongo_client):
        print("greeting: ", "welcome test world!")
        connection = MongoDatabaseConnector()
        assert isinstance(connection, MongoClient)
        assert connection.host == mongo_client.host
