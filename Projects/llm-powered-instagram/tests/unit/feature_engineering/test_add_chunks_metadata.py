from src.application.preprocessing.dispatchers import ChunkingDispatcher
from steps.feature_engineering.rag import _add_chunks_metadata

def test_add_chunks_metadata(cleaned_documents):
    metadata = {"chunking": {}, "embedding": {}, "num_documents": len(cleaned_documents)}
    
    for cleaned_document in cleaned_documents:
        chunks = ChunkingDispatcher.dispatch(cleaned_document)
        metadata["chunking"] = _add_chunks_metadata(chunks, metadata)

    print("metadata['chunking']\n", metadata["chunking"])
    print("metadata['chunking'].keys()\n", metadata["chunking"].keys())
    assert isinstance(metadata["chunking"], dict)
    # for key in metadata["chunking"].keys():
    #     # assert key in ("articles", "posts", "repositories")
    #     assert "num_chunks" in metadata[key]
    #     assert "authors" in metadata[key]
    #     assert len(metadata[key]["authors"]) == 1

    