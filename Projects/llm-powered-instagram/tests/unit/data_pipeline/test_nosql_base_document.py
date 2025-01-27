import pytest

from src.domain.base.nosql import NoSQLBaseDocument

class TestNoSQLBaseDocument:
    @pytest.mark.usefixtures("nosql_base_document")
    def test_get_collection_name(nosql_base_document):
        class TestDocument(NoSQLBaseDocument["TestDocument"]):

            class Settings:
                name = "test"

        assert TestDocument.get_colleciton_name() == "test"

    def test_from_mongo(nosql_base_document, single_document_collection):
        
        filtered_options = {"first_name":"tae-su", "last_name": "kang"}
        instance = single_document_collection.find_one(filtered_options)
        
        class TestDocument(NoSQLBaseDocument["TestDocument"]):
            first_name: str
            last_name: str

            class Settings:
                name = "test"

        test_instance = TestDocument.from_mongo(instance)

        assert isinstance(test_instance, TestDocument)
        assert test_instance.first_name == "tae-su"
        assert test_instance.last_name == "kang"

        


    


