import pytest
import uuid
from pydantic import Field

from src.domain.base.nosql import NoSQLBaseDocument
from src.domain.documents import UserDocument, ArticleDocument, PostDocument, RepositoryDocument


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

    def test_model_dump(self):
        class TestDocument(NoSQLBaseDocument):
            first_name : str
            last_name: str

            class Settings:
                name = "test_collection"

        test_document  = TestDocument()
        result = test_document.model_dump()
        assert isinstance(result["id"], str)

    def test_to_mongo(self, nosql_base_document):
        result = nosql_base_document.to_mongo()
        assert "_id" in result.keys()

    def test_save(self, nosql_base_document):
        filter_options = {"first_name": "tae-su", "last_name": "kang"}

        class TestDocument(NoSQLBaseDocument["TestDocument"]):
            first_name: str
            last_name: str

            class Settings:
                name = "test"

        test_document = TestDocument(first_name="tae-su", last_name="kang")
        new_instance = test_document.save(**filter_options)
        assert isinstance(new_instance, test_document)

    def test_bulk_find_no_data(self, nosql_base_document):
        user = UserDocument.get_or_create(first_name="tae-su", last_name="kang")
        user_id = str(user.id)
        results = PostDocument.bulk_find(author_id=user_id)
        assert isinstance(results, list)
        assert results == []

    def test_bulk_find_with_article_document(self):
        user_id = "b6317053-87fa-4e6a-892f-443467a509d1"
        results = ArticleDocument.bulk_find(author_id=user_id)
        assert isinstance(results, list)
        assert len(results) == 1

    def test_bulk_find_with_post_document(self):
        user_id = "835612b3-ea87-4b05-9c5e-969300b50ce5"
        # user_id = "3256258f-b353-47f5-9985-9caf763d99ae"
        results = PostDocument.bulk_find(author_id=user_id)
        assert isinstance(results, list)
        assert len(results) == 1

    def test_bulk_find_with_repository_document(self):
        user_id = "72b34430-afd3-4639-b4ef-e8f9b0661dc1"
        results = RepositoryDocument.bulk_find(author_id=user_id)
        assert isinstance(results, list)
        assert len(results) == 1

    def test_get_or_create_existing_data(self):
        user = UserDocument.get_or_create(first_name="tae-su", last_name="kang")
        assert isinstance(user, UserDocument)
        assert user.first_name == "tae-su"
        assert user.last_name == "kang"
        assert user.Settings.name == "users"

    def test_get_or_create_creating_data(self):
        # user = UserDocument.get_or_create(first_name="jung-su", last_name="kang")
        # user = UserDocument.get_or_create(first_name="eun", last_name="heo")
        user = UserDocument.get_or_create(first_name="eun-a", last_name="gwak")
        assert isinstance(user, UserDocument)
        assert user.first_name == "eun-a"
        assert user.last_name == "gwak"
        assert user.Settings.name == "users"


        


    


