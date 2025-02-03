from abc import ABC
from typing import Optional

from pydantic import UUID4

from.base.vector import VectorBaseDocument
from src.domain.types import DataCategory

class CleanedDocument(VectorBaseDocument, ABC):
    content: str
    platform: str
    author_id: UUID4
    author_full_name: str


class CleanedPostDocument(CleanedDocument):
    image: Optional[str] = None

    class Config:
        name = "cleaned_posts"
        category = DataCategory.POSTS
        use_vector_index = False