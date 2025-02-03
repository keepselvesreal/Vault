from steps.feature_engineering.query_data_warehouse import query_data_warehouse
from steps.feature_engineering.clean import clean_documents
from src.domain.cleaned_documents import CleanedPostDocument, CleanedArticleDocument, CleanedRepositoryDocument
from src.application.preprocessing.dispatchers import CleaningDispatcher

class TestCleanDocuments:
    def test_clean_documents(self):
        author_full_names = ["tae-su kang",]
        # raw_documents = query_data_warehouse(author_full_name)
        # cleaned_documents = clean_documents(documents=raw_documents)

        # cleaned_documents = feature_engineering([author_full_name])

        raw_documents = query_data_warehouse(author_full_names)
        print("raw documents\n", raw_documents)

        cleaned_documents = []
        for document in raw_documents:
            cleaned_document = CleaningDispatcher.dispatch(document)
            cleaned_documents.append(cleaned_document)
        

        assert isinstance(cleaned_documents, list)
        expected_types = (CleanedPostDocument, CleanedArticleDocument, CleanedRepositoryDocument)
        for document in cleaned_documents:
            assert isinstance(document, expected_types), \
            f"Document type {type(document)} is not one of expected types: {expected_types}"
        assert cleaned_documents[0].platform in ("linkedin", "github", "medium")
        assert len(cleaned_documents) == 3

        