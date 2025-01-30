import pytest
from pymongo import MongoClient

from src.domain.base.nosql import NoSQLBaseDocument


@pytest.fixture
def nosql_base_document():
    return NoSQLBaseDocument()

@pytest.fixture(scope="function")
def mongo_database_collection():
    mongo_client = MongoClient(host="mongodb://localhost:27017/")
    test_database = mongo_client.get_database("test_database")
    test_database.create_collection("test_collection")
    test_collection = test_database.get_collection("test_collection")
    collection = test_database[test_collection]
    yield collection
    test_collection.drop()