import pytest
from pymongo import MongoClient


@pytest.fixture
def mongo_client():
    return MongoClient(host="mongodb://localhost:27017/")
