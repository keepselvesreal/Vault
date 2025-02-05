import pytest
import uuid

from src.domain.documents import UserDocument

from steps.feature_engineering.query_data_warehouse import fetch_all_data
from src.application.preprocessing.dispatchers import CleaningDispatcher
from src.application.preprocessing.dispatchers import ChunkingDispatcher
from src.application.utils.misc import batch
from src.application.preprocessing.dispatchers import EmbeddingDispatcher


@pytest.fixture(scope="function")
def cleaned_documents() -> list:
    author_full_names = ["tae-su kang"]
    documents = []
    authors = []
    for author_full_name in author_full_names:
        user = UserDocument(first_name="tae-su", last_name="kang")
        user.id = uuid.UUID("67d9d100-1371-4997-a161-b69b2e284ef1")
        authors.append(user)

        results = fetch_all_data(user)
        user_documents = [doc for query_result in results.values() for doc in query_result]
        documents.extend(user_documents)

    cleaned_documents = []
    for document in documents:
        cleaned_document = CleaningDispatcher.dispatch(document)
        cleaned_documents.append(cleaned_document)

    return cleaned_documents

@pytest.fixture(scope="function")
def embedded_chunks(cleaned_documents):
    embedded_chunks = []
    for document in cleaned_documents:
        chunks = ChunkingDispatcher.dispatch(document)
        for batched_chunks in batch(chunks, 10):
            batched_embedded_chunks = EmbeddingDispatcher.dispatch(batched_chunks)
            embedded_chunks.extend(batched_embedded_chunks)
    yield embedded_chunks
    
    
