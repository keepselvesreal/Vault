from typing import Generic, TypeVar
from abc import ABC

from pydantic import BaseModel

T = TypeVar("T", bound="VectorBaseDocument")

class VectorBaseDocument(BaseModel, Generic[T], ABC):
    pass