from abc import ABC, abstractmethod
from typing import Generic, TypeVar


from src.domain.documents import Document, PostDocument, ArticleDocument, RepositoryDocument
from src.domain.cleaned_documents import CleanedDocument, CleanedPostDocument, CleanedArticleDocument, CleanedRepositoryDocument
from .operations.cleaning import clean_text


DocumentT = TypeVar("DocumentT", bound=Document)
CleanedDocumentT = TypeVar("CleanedDocumentT", bound=CleanedDocument)

class CleaningDataHandler(ABC, Generic[DocumentT, CleanedDocumentT]):
    """
    Abstract class for all cleaning data handlers.
    """
    @abstractmethod
    def clean(self, data_model: DocumentT) -> CleanedDocumentT:
        pass


class PostCleaningHandler(CleaningDataHandler):
    def clean(self, data_model: PostDocument) -> CleanedDocumentT:
        return CleanedPostDocument(
            id=data_model.id,
            content=clean_text(" ### ".join(data_model.content.values())),
            platform=data_model.platform,
            author_id=data_model.author_id,
            author_full_name=data_model.author_full_name
        )
    
class ArticleCleaningHandler(CleaningDataHandler):
    def clean(self, data_model: ArticleDocument) -> CleanedArticleDocument:
        valid_content = [content for content in data_model.content.values() if content]

        return CleanedArticleDocument(
            id=data_model.id,
            content=clean_text(" #### ".join(valid_content)),
            platform=data_model.platform,
            link=data_model.link,
            author_id=data_model.author_id,
            author_full_name=data_model.author_full_name,
        )


class RepositoryCleaningHandler(CleaningDataHandler):
    def clean(self, data_model: RepositoryDocument) -> CleanedRepositoryDocument:
        return CleanedRepositoryDocument(
            id=data_model.id,
            content=clean_text(" #### ".join(data_model.content.values())),
            platform=data_model.platform,
            name=data_model.name,
            link=data_model.link,
            author_id=data_model.author_id,
            author_full_name=data_model.author_full_name,
        )