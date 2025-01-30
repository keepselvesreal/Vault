import uuid
from abc import ABC
from typing import Generic, Type, TypeVar

from loguru import logger
from pydantic import BaseModel, Field, UUID4

from src.infrastructure.db.mongo import connection
from src.settings import settings

_database = connection.get_database(settings.DATABASE_NAME)
T = TypeVar("T", bound="NoSQLBaseDocument")

class NoSQLBaseDocument(BaseModel, Generic[T], ABC):
    id: UUID4 = Field(default_factory=uuid.uuid4)

    @classmethod
    def get_or_create(cls: Type[T], **filter_options) -> T:
        collection = _database[cls.get_collection_name()]
        try:
            instance = collection.find_one(filter_options)
            if instance:
                return cls.from_mongo(instance)
            
            new_instance = cls(**filter_options)
            new_instance = new_instance.save()
            
            return new_instance
        except:
            logger.exception(f"Failed to retrieve document with filter options: {filter_options}")

    @classmethod
    def get_collection_name(cls: Type[T]) -> str:
        if not hasattr(cls, "Settings") or not hasattr(cls.Settings, "name"):
            raise
        # return cls.Settings.name
        return str(cls.Settings.name)

    @classmethod
    def from_mongo(cls: Type[T], data: dict) -> T:
        if not data:
            raise ValueError("Data is empty")

        id = data.pop("_id") # _id는 collection에서 조회된 개별 데이터 객체의 id인 듯
        
        return cls(**data, id=id)

    def to_mongo(self: T, **kwargs) -> dict:
        kwargs = kwargs or {}
        exclude_unset = kwargs.pop("exclude_unset", False)
        by_alias = kwargs.pop("by_alias", True)

        parsed = self.model_dump(exclude_unset=exclude_unset, by_alias=by_alias, **kwargs)

        if "_id" not in parsed and "id" in parsed:
            parsed["_id"] = str(parsed.pop("id"))
        
        return parsed

    def model_dump(self: T, **kwargs) -> dict:
        dict_ = super().model_dump(**kwargs)

        for key, value in dict_.items():
            if isinstance(value, uuid.UUID):
                dict_[key] = str(value)

        return dict_


    def save(self: T, **kwargs) -> T | None:
        collection = _database[self.get_collection_name()]
        try:
            collection.insert_one(self.to_mongo(**kwargs))

            return self
        except:
            logger.exception("Failed to insert document")
            return None

    @classmethod    
    def bulk_find(cls: Type[T], **filter_options) -> list[T]:
        collection = _database[cls.get_collection_name()]
        try:
            instances = collection.find(filter_options)
            return [document for instance in instances if (document:= cls.from_mongo(instance)) is None]
        except:
            logger.error("Failed to retrive documents")
            return []


_database = connection.get_database(settings.DATABASE_NAME)