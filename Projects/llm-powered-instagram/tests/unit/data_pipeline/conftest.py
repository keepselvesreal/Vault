import pytest

from src.domain.base.nosql import NoSQLBaseDocument
from src.domain.documents import UserDocument


@pytest.fixture
def nosql_base_document():
    return NoSQLBaseDocument()


@pytest.fixture(scope="class")
def same_user():
    user = UserDocument(first_name="tae-su", last_name="kang")
    yield user 
    