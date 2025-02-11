

from src.model.inference.inference import LLMInferenceSagemakerEndpoint
from src.model.inference.run import InferenceExecutor
from src.settings import settings
# from src.application.rag.retriever import ContextRetriever
# from src.domain.embedded_chunks import EmbeddedChunk

def call_llm_service(query: str, context: str | None) -> str:
    llm = LLMInferenceSagemakerEndpoint(
        endpoint_name=settings.SAGEMAKER_ENDPOINT_INFERENCE, inference_component_name=None
    )
    answer = InferenceExecutor(llm, query, context).execute()

    return answer


def rag(query: str) -> str:
    # retriever = ContextRetriever(mock=False)
    # documents = retriever.search(query, k=3)
    # context = EmbeddedChunk.to_context(documents)
    query = "what is the content of DL paper whose title 'attention is all you need'"
    context = 'Attention Is All You Need" introduces the Transformer model, which relies solely on self-attention mechanisms instead of recurrent or convolutional layers, enabling parallelization and improved training efficiency. The model utilizes multi-head attention to capture different aspects of the input data and employs positional encoding to retain the order of sequences. This architecture significantly enhances performance in various natural language processing tasks, setting a new standard for future models'

    answer = call_llm_service(query, context)

    # opik_context.update_current_trace(
    #     tags=["rag"],
    #     metadata={
    #         "model_id": settings.HF_MODEL_ID,
    #         "embedding_model_id": settings.TEXT_EMBEDDING_MODEL_ID,
    #         "temperature": settings.TEMPERATURE_INFERENCE,
    #         "query_tokens": misc.compute_num_tokens(query),
    #         "context_tokens": misc.compute_num_tokens(context),
    #         "answer_tokens": misc.compute_num_tokens(answer),
    #     },
    # )

    return answer

if __name__ == "__main__":
    print("response\n", rag(query="dummy"))