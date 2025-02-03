import pytest
import uuid
from zenml import get_step_context, step

from src.domain.documents import UserDocument
from steps.feature_engineering.query_data_warehouse import fetch_all_data


@pytest.fixture
def zenml_step_context():
    @step
    def get_step_context():
        return get_step_context()
    return get_step_context()

@pytest.fixture(scope="class")
def documents():
    documents = []
    first_name, last_name =" tae-su", "kang"
    user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)
    user.id = uuid.UUID("9992c7b0-6a9e-42fb-8dd3-0c2874a75243")
    results = fetch_all_data(user)
    user_documents = [doc for query_result in results.values() for doc in query_result]
    documents.extend(user_documents)
    return documents