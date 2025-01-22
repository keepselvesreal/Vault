

from .base import VectorBaseDocument
from .types import DataCategory


class Query(VectorBaseDocument):
    pass


class EmbeddingQuery(Query):
    embedding: list[float]

    class Config:
        category = DataCategory.QUERIES