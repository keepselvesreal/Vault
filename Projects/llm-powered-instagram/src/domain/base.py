from abc import ABC
from typing import Generic

from pydantic import BaseModel

from ..infrastructure.db.qdrant import connection


class VectorBaseDocument(BaseModel, Generic[T], ABC):
    pass