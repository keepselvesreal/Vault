import pytest

class TestAcceptance:
    def test_generate_response(query: str) -> str:
        retriever = ContextRetriever(mock=True)
        documents = retriever.search(query, k=3)
        context =  EmbeddedChunk.to_context(documents)

        answer = call_llm_service(query, context)

        return answer


        