from pymongo import MongoClient

from src.settings import settings

class MongoDatabaseConnector:
    
    def __new__(cls, *args, **kwargs):
        client = MongoClient(host=settings.DATABASE_LOCAL_HOST)

        return client

        
connection = MongoDatabaseConnector()