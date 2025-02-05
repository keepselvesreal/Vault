from steps.feature_engineering.rag import _add_embeddings_metadata

def test_add_embedding_metadata(cleaned_documents, embedded_chunks):
    metadata = {"chunking": {}, "embedding": {}, "num_documents": len(cleaned_documents)}
    result = _add_embeddings_metadata(embedded_chunks, metadata)
    print("result\n", result)
    assert isinstance(result, dict)
