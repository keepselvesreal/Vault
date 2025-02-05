from src.application.utils.misc import batch
from src.application.preprocessing.dispatchers import ChunkingDispatcher, EmbeddingDispatcher
from src.domain.embedded_chunks import EmbeddedPostChunk, EmbeddedArticleChunk, EmbeddedRepositoryChunk

def test_dispatch(cleaned_documents):
    for document in cleaned_documents:
        chunks = ChunkingDispatcher.dispatch(document)
        print("chunks\n", chunks)
        for batched_chunks in batch(chunks, 10):
            print("batched_chunks\n", batched_chunks)
            batched_embedded_chunks = EmbeddingDispatcher.dispatch(batched_chunks)
            print("batched_embedded_chunks\n", batched_embedded_chunks)
            assert isinstance(batched_embedded_chunks, list)

            expected_embedded_chunk_type = (EmbeddedPostChunk, EmbeddedArticleChunk, EmbeddedRepositoryChunk)
            for batched_embedded_chunk in batched_embedded_chunks:
                assert isinstance(batched_embedded_chunk, expected_embedded_chunk_type)



