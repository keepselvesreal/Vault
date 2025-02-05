import pytest
import uuid
from pymongo import MongoClient

from src.domain.base.nosql import NoSQLBaseDocument
from src.infrastructure.db.qdrant import connection
from src.domain.documents import UserDocument
from steps.feature_engineering.query_data_warehouse import fetch_all_data
from src.application.preprocessing.dispatchers import CleaningDispatcher
from src.domain.base.vector import VectorBaseDocument
from src.domain.cleaned_documents import CleanedArticleDocument, CleanedPostDocument, CleanedRepositoryDocument

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


@pytest.fixture(scope="function")
def qdrant_database():
    yield connection


@pytest.fixture(scope="function")
def vector_base_document():
    yield VectorBaseDocument

def test_query_data_warehouse(author_full_names: list[str]) -> list:
    documents = []
    authors = []
    for author_full_name in author_full_names:
        user = UserDocument(first_name="tae-su", last_name="kang")
        user.id = uuid.UUID("67d9d100-1371-4997-a161-b69b2e284ef1")
        authors.append(user)

        results = fetch_all_data(user)
        user_documents = [doc for query_result in results.values() for doc in query_result]
        documents.extend(user_documents)

    return documents

def test_clean_documents(documents: list) -> list:
    cleaned_documents = []
    for document in documents:
        cleaned_document = CleaningDispatcher.dispatch(document)
        cleaned_documents.append(cleaned_document)
    return cleaned_documents


@pytest.fixture(scope="class")
def list_of_vector_base_documents():
    author_full_names = ["tae-su kang"]
    raw_documents = test_query_data_warehouse(author_full_names)
    cleaned_documents = test_clean_documents(raw_documents)
    yield cleaned_documents

@pytest.fixture(scope="function")
def list_of_document_classes():
    yield (CleanedArticleDocument, CleanedPostDocument, CleanedRepositoryDocument)


@pytest.fixture(scope="function")
def grouped_documents(vector_base_document):
    author_full_names = ["tae-su kang"]
    raw_documents = test_query_data_warehouse(author_full_names)
    cleaned_documents = test_clean_documents(raw_documents)
    grouped_documents = vector_base_document.group_by_class(cleaned_documents)
    yield grouped_documents




