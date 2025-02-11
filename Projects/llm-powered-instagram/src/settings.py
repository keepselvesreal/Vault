import os

from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
# class Settings:
    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    #  MongoDB database
    DATABASE_LOCAL_HOST: str = "mongodb://localhost:27017/"
    DATABASE_HOST: str = "dummy"
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

    # OpenAI API
    OPENAI_MODEL_ID: str = "gpt-4o-mini"
    OPENAI_API_KEY: str | None = None

    # Huggingfae API
    HUGGINGFACE_ACCESS_TOKEN: str | None = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

    # AWS Authentication
    AWS_REGION: str = "ap-northeast-2"
    AWS_ACCESS_KEY: str | None = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY: str | None = os.getenv("AWS_SECRET_KEY")
    AWS_ARN_ROLE: str | None = os.getenv("AWS_ARN_ROLE")
    
    # AWS SageMaker
    HF_MODEL_ID: str = "mlabonne/TwinLlama-3.1-8B-DPO"
    GPU_INSTANCE_TYPE: str = "ml.g5.2xlarge"
    SM_NUM_GPUS: int = 1
    MAX_INPUT_LENGTH: int = 2048
    MAX_TOTAL_TOKENS: int = 4096
    MAX_BATCH_TOTAL_TOKENS: int = 4096

    SAGEMAKER_ENDPOINT_CONFIG_INFERENCE: str = "twin"
    SAGEMAKER_ENDPOINT_INFERENCE: str = "twin"
    TEMPERATURE_INFERENCE: float = 0.01
    TOP_P_INFERENCE: float = 0.9
    MAX_NEW_TOKENS_INFERENCE: int = 150
    COPIES: int = 1
    GPUS: int = 1
    CPUS: int = 2


settings = Settings()

print(settings.AWS_ACCESS_KEY) 
print(settings.AWS_SECRET_KEY) 