
from loguru import logger 

from src.domain.types import DataCategory
from src.application.preprocessing.cleaning_data_handlers import CleaningDataHandler
from .cleaning_data_handlers import PostCleaningHandler
from src.domain.base.nosql import NoSQLBaseDocument
from src.domain.base.vector import VectorBaseDocument


class CleaningHandlerFactory:
    @staticmethod
    def create_handler(data_category: DataCategory) -> CleaningDataHandler:
        # if data_category == DataCategory.POSTS:
        if data_category == "posts":
            return PostCleaningHandler()
        elif data_category ==  DataCategory.ARTICLES:
            pass
        elif data_category == DataCategory.REPOSITORIES:
            pass
        else:
            raise ValueError("unsupported data type")


class CleaningDispatcher:
    factory = CleaningHandlerFactory()

    @classmethod
    def dispatch(cls, data_model: NoSQLBaseDocument) -> VectorBaseDocument:
        data_category = data_model.get_collection_name
        data_category = "posts"
        handler = cls.factory.create_handler(data_category)
        clean_model = handler.clean(data_model)

        logger.info(
            "Document cleaned successfully.",
            data_category=data_category,
            cleaned_contente_len=len(clean_model.content)

        )