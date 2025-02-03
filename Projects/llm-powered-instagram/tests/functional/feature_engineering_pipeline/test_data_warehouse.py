import uuid

from zenml import step, get_step_context

from src.domain.documents import UserDocument
from steps.feature_engineering.query_data_warehouse import fetch_all_data, get_metadata, query_data_warehouse

class TestQueryDataWareHouse:
    def test_fetch_all_data(self):
        user = UserDocument(first_name="tae-su", last_name="kang")
        user.id = uuid.UUID("67d9d100-1371-4997-a161-b69b2e284ef1")
        results = fetch_all_data(user)
        
        expected_keys = ["articles", "posts", "repositories"]
        for expected_key in expected_keys:
            assert expected_key in results, f"{expected_key} 키가 results에 없습니다."
        assert len(results["articles"]) == 1
        assert len(results["posts"]) == 1
        assert len(results["repositories"]) == 1

    def test_get_metadata(self):
        # author_full_names = ["tae-su kang"]
        documents = []
        first_name, last_name =" tae-su", "kang"
        # user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)
        user = UserDocument(first_name=first_name, last_name=last_name)
        user.id = uuid.UUID("67d9d100-1371-4997-a161-b69b2e284ef1")
        results = fetch_all_data(user)

        expected_keys = ["articles", "posts", "repositories"]
        for expected_key in expected_keys:
            assert expected_key in results, f"{expected_key} 키가 results에 없습니다."

        user_documents = [doc for query_result in results.values() for doc in query_result]
        documents.extend(user_documents)

        metadata = get_metadata(documents)

        assert isinstance(metadata, dict)
        assert len(metadata) == 4
        expected_keys = ["num_documents", "articles", "posts", "repositories"]
        for expected_key in expected_keys:
            assert expected_key in metadata, f"{expected_key} 키가 results에 없습니다."
        

    # def test_add_output_metadata(self):
    #     documents = []
    #     first_name, last_name =" tae-su", "kang"
    #     user = UserDocument(first_name=first_name, last_name=last_name)
    #     user.id = uuid.UUID("9992c7b0-6a9e-42fb-8dd3-0c2874a75243")
    #     results = fetch_all_data(user)

    #     expected_keys = ["articles", "posts", "repositories"]
    #     for expected_key in expected_keys:
    #         assert expected_key in results, f"{expected_key} 키가 results에 없습니다."

    #     user_documents = [doc for query_result in results.values() for doc in query_result]
    #     documents.extend(user_documents)

    #     print("documents\n", documents)
    #     print("-"*50)
    #     add_metadata(documents)

    def test_add_output_metadata(self):
        author_full_names = ["tae-su kang"]
        documents = query_data_warehouse(author_full_names)
        
        assert isinstance(documents, list)
        assert len(documents) == 3


@step
def add_metadata(docs):
    print("docs\n", docs)
    step_context = get_step_context()
    metadata = get_metadata(docs)
    step_context.add_output_metadata(
        output_name="raw_documents", 
        metadata=metadata
    )
    return metadata
            






