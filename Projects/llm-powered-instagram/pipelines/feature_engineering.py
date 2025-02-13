from zenml import pipeline

# from steps import feature_engineering as fe_steps
from steps.feature_engineering.query_data_warehouse import query_data_warehouse
from steps.feature_engineering.clean import clean_documents
from steps.feature_engineering.load_to_vector_db import load_to_vector_db
from steps.feature_engineering.rag import chunk_and_embed


@pipeline
def feature_engineering(author_full_names: list[str], wait_for: str | list[str] | None = None) -> list[str]:
    raw_documents = query_data_warehouse(author_full_names, after=wait_for)

    cleaned_documents = clean_documents(raw_documents)
    # last_step_1 = fe_steps.load_to_vector_db(cleaned_documents)
    last_step_1 = load_to_vector_db(cleaned_documents)

    # embedded_documents = fe_steps.chunk_and_embed(cleaned_documents)
    embedded_documents = chunk_and_embed(cleaned_documents)
    # last_step_2 = fe_steps.load_to_vector_db(embedded_documents)
    last_step_2 = load_to_vector_db(embedded_documents)

    return [last_step_1.invocation_id, last_step_2.invocation_id]
    # return cleaned_documents

if __name__ == "__main__":
    feature_engineering(author_full_names=["Alice Johnson", "Bob Smith", "Charlie Brown"]).run()