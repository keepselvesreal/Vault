from src.domain.cleaned_documents import CleanedDocument
from src.domain.documents import Document


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
