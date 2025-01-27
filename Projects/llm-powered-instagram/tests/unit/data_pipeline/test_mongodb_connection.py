import pytest
from pymongo import MongoClient

from src.infrastructure.db.mongo import connection

class TestMongoDatabaseConnector:
    @pytest.mark.usefixtures("mongo_client")
    def test_new(self, mongo_client):
        print("greeting: ", "welcome test world!")
        assert isinstance(connection, MongoClient)
        assert connection.host == mongo_client.host
