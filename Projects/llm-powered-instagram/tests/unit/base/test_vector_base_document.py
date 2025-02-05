from src.application.utils import misc
from src.domain.chunks import PostChunk

class TestVectorBaseDocument:
    def test_group_by_class(self, vector_base_document, list_of_vector_base_documents):
        print("list of vector base documents\n", list_of_vector_base_documents)
        print("vector_base_document\n", vector_base_document)
        results = vector_base_document.group_by_class(list_of_vector_base_documents)
        assert isinstance(results, dict)
        expected_key_typs = (dict)
        for key, value in results.items():
            isinstance(key, expected_key_typs)
            isinstance(value, dict)

    def test_create_collection(self, qdrant_database, list_of_document_classes):
        cleaned_article_document, cleaned_posts_document, cleaned_repository_docuemnt = list_of_document_classes
        cleaned_article_document.create_collection()
        cleaned_posts_document.create_collection()
        cleaned_repository_docuemnt.create_collection()
        collections = qdrant_database.get_collections()
        
        expceted_collection_names = ("cleaned_articles, cleaned_posts", "cleaned_repositories")
        for collection_name in expceted_collection_names:
            assert collection_name in collections

    def test_bulk_insert(self, grouped_documents):
        for document_class, documents in grouped_documents.items():
            for documents_batch in misc.batch(documents, size=4):
                document_class.bulk_insert(documents_batch)

    def test_get_category(self):
        category = PostChunk.get_category()
        assert category == "posts"


        

