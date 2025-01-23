

class TestAcceptance:
    def test_generate_response(query: str) -> str:
        retriever = ContextRetriever()
        documents = retriever.search(query, k=3)
        answer = call_llm_service(query, document)

        return answer


        