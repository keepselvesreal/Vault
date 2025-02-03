import pytest

class TestMongoDBClient:
    @pytest.mark.usefixtures("mongo_client")
    def test_get_databases(self, mongo_client):
        test_database = mongo_client.get_database("test_db")
        assert test_database.name == "test_db"

    # @pytest.mark.usefixtures("mongo_client")
    # def test_create_collection(self, mongo_client):
    #     test_database = mongo_client["test_db"]
    #     test_database.create_collection("test_collection")
    #     collection = test_database.get_collection("test_collection")
    #     assert "test_collection" in test_database.list_collection_names()

    @pytest.mark.usefixtures("mongo_database_collection")
    def test_create_collection(self, mongo_database_collection):
        assert "test_collection" in  mongo_database_collection.list_collection_names()

    @pytest.mark.usefixtures("mongo_client")
    def test_delete_collection(self, mongo_client):
        test_database = mongo_client["test_db"]
        test_collection_name = "test_collection"
        test_collection = test_database.get_collection(test_collection_name)

        test_collection.insert_one({"key": "value"})  # 임시 데이터 추가로 컬렉션 생성 보장
        assert test_collection_name in test_database.list_collection_names()

        test_collection.drop()
        assert test_collection_name not in test_database.list_collection_names()

    @pytest.mark.usefixtures
    def test_collection_find_one(self, single_document_collection):
        filtered_options = {"first_name":"tae-su", "last_name": "kang"}
        instance = single_document_collection.find_one(filtered_options)
        instance.pop("_id")
        assert instance == filtered_options


    
