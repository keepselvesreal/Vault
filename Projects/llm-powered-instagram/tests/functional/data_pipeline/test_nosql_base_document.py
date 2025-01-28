import pytest


class TestNoSQLBaseDocument:
    @pytest.mark.usefixtures("nosql_base_document")
    def test_from_mongo(self, nosql_base_document):
        data = {
            "_id": "kts",
            
        }
        nosql_base_document.from_mongo()