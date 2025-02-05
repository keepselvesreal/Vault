from src.application.preprocessing.dispatchers import ChunkingDispatcher
from src.domain.chunks import PostChunk, ArticleChunk, RepositoryChunk

def test_chunking_dispatcher(cleaned_documents):
    expected_chunk_types = (PostChunk, ArticleChunk, RepositoryChunk)
    for cleaned_document in cleaned_documents:
        chunks = ChunkingDispatcher.dispatch(cleaned_document)
        for chunk in chunks:
            assert isinstance(chunk, expected_chunk_types)

