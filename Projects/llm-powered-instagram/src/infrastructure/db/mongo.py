from pymongo import MongoClient

from src.settings import Settings# settings

class MongoDatabaseConnector:
    
    def __new__(cls, *args, **kwargs):
        client = MongoClient(host=Settings.DATABASE_LOCAL_HOST)

        return client

        
connection = MongoDatabaseConnector()