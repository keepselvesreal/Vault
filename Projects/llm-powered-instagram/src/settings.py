
from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
class Settings:
    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    #  MongoDB database
    DATABASE_LOCAL_HOST: str = "mongodb://localhost:27017/"
    DATABASE_HOST: str = None
    DATABASE_NAME: str = "twin"

    # Qdrant vector database
    USE_QDRANT_CLOUD: bool = False
    QDRANT_DATABASE_HOST: str = "localhost"
    QDRANT_DATABASE_PORT: int = 6333
    QDRANT_CLOUD_URL: str = "str"
    QDRANT_APIKYE: str | None = None

    # RAG
    TEXT_EMBEDDING_MODEL_ID: str = "sentence-transformers/all-MiniLM-L6-v2"
    RAG_MODEL_DEVICE: str = "cpu"


settings = Settings()

