from concurrent.futures import ThreadPoolExecutor, as_completed

from loguru import logger
from zenml import step, get_step_context
from typing_extensions import Annotated
import uuid

from src.domain.base.nosql import NoSQLBaseDocument
from src.domain.documents import UserDocument, Document, ArticleDocument, PostDocument, RepositoryDocument
from src.application import utils


@step
def query_data_warehouse(
    author_full_names: list[str],
) -> Annotated[list, "raw_documents"]:
    documents = []
    authors = []
    for author_full_name in author_full_names:
        logger.info(f"Querying data warehouse for user: {author_full_name}")

        # first_name, last_name = utils.split_user_full_name(author_full_name)
        # logger.info(f"First name: {first_name}, Last name: {last_name}")
        # user = UserDocument.get_or_create(first_name=first_name, last_name=last_name)
        user = UserDocument(first_name="tae-su", last_name="kang")
        user.id = uuid.UUID("9992c7b0-6a9e-42fb-8dd3-0c2874a75243")
        authors.append(user)

        results = fetch_all_data(user)
        user_documents = [doc for query_result in results.values() for doc in query_result]

        documents.extend(user_documents)

    step_context = get_step_context()
    step_context.add_output_metadata(output_name="raw_documents", metadata=get_metadata(documents))

    return documents



def fetch_all_data(user: UserDocument) -> dict[str, list[NoSQLBaseDocument]]:
    user_id = str(user.id)
    with ThreadPoolExecutor() as executor:
        future_to_query = {
            executor.submit(__fetch_articles, user_id): "articles",
            executor.submit(__fetch_posts, user_id):  "posts",
            executor.submit(__fetch_repositoris, user_id): "repositories",
        }

        results = {}
        for future in as_completed(future_to_query):
            query_name = future_to_query[future]
            try:
                results[query_name] = future.result()
            except Exception:
                logger.exception(f"'{query_name}' request failed.")
                
                results[query_name] = []

        return results
    

def __fetch_articles(user_id) -> list[NoSQLBaseDocument]:
    return ArticleDocument.bulk_find(author_id=user_id)


def __fetch_posts(user_id) -> list[NoSQLBaseDocument]:
    return PostDocument.bulk_find(author_id=user_id)


def __fetch_repositoris(user_id) -> list[NoSQLBaseDocument]:
    return RepositoryDocument.bulk_find(author_id=user_id)


def get_metadata(documents: list[Document]) -> dict:
    metadata = {
        "num_documents": len(documents)
    }

    for document in documents:
        collection = document.get_collection_name()
        if collection not in metadata:
            metadata[collection] = {}
        if "authors" not in metadata[collection]:
            metadata[collection]["authors"] = list()

        metadata[collection]["num_documents"] = metadata[collection].get("num_documents", 0) + 1
        metadata[collection]["authors"].append(document.author_full_name)

    for value in metadata.values():
        if isinstance(value, dict) and "authors" in value:
            value["authors"] = list(set(value["authors"]))

    return metadata