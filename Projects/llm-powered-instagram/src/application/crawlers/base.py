from abc import ABC, abstractmethod

from src.domain.base.nosql import NoSQLBaseDocument


class BaseCrawler(ABC):
    model: type[NoSQLBaseDocument]

    @abstractmethod
    def extract(slef, link:str, **kwargs) -> None: ...