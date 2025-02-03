import pytest

from src.domain.base.nosql import NoSQLBaseDocument


@pytest.fixture
def nosql_base_document():
    return NoSQLBaseDocument()