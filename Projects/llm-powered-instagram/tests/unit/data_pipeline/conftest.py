import pytest
from pymongo import MongoClient

from src.domain.base.nosql import NoSQLBaseDocument

@pytest.fixture
def mongo_client():
    return MongoClient(host="mongodb://localhost:27017/")


# @pytest.fixture(scope="module")
# def mongo_client():
#     # 실제 MongoDB 테스트 환경 연결
#     client = MongoClient("mongodb://localhost:27017/")
#     yield client
#     client.drop_database("test_db")  # 테스트가 끝나면 데이터베이스를 삭제
#     client.close()


@pytest.fixture(scope="function")
def mongo_database_collection():
    mongo_client = MongoClient(host="mongodb://localhost:27017/")
    test_database = mongo_client.get_database("test_database")
    test_database.create_collection("test_collection")
    test_collection = test_database.get_collection("test_collection")
    collection = test_database[test_collection]
    yield collection
    test_collection.drop()


@pytest.fixture
def single_document_collection(mongo_client):
    test_database = mongo_client.get_database("test_database")
    test_collection = test_database.get_collection("test_collection")
    query = {"first_name": "tae-su", "last_name": "kang"}
    test_collection.insert_one(query)
    yield test_collection
    test_collection.delete_one(query)


@pytest.fixture
def nosql_base_document():
    return NoSQLBaseDocument()