from pathlib import Path
# from llama_index import download_loader, LLMPredictor, ServiceContext, VectorStoreIndex
from llama_index.core import Settings
from llama_index.core  import VectorStoreIndex, StorageContext # ts 수정
# ts 추가
from llama_index.llms.openai import OpenAI

# from llama_index.vector_stores import MilvusVectorStore
from llama_index.vector_stores.milvus import MilvusVectorStore # ts 수정 from 공식 doc
# from llama_index.readers import PDFReader
from llama_index.readers.file import PDFReader # ts 수정
# from llama_index import StorageContext
# from pymilvus import MilvusClient
from pymilvus import Milvus # ts 수정 from gpt
import os

# Define constants for Milvus configuration
MILVUS_HOST = os.environ.get("MILVUS_HOST", "10.97.151.193")
MILVUS_PORT = os.environ.get("MILVUS_PORT", "19530")
MILVUS_URI = f"http://{MILVUS_HOST}:{MILVUS_PORT}"

# Initialize PDFReader
pdf_reader = PDFReader()

# Load documents from a PDF file
document_path = Path('ingestion/keiichi_tsuchiya.pdf')  #ToDo: load from S3 instead of local
documents = pdf_reader.load_data(file=document_path)

# Create an LLMPredictor with default parameters
# llm_predictor = LLMPredictor(llm=None)
llm_predictor =  OpenAI() # ts 수정

# Create a ServiceContext with LLMPredictor
# service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)
Settings.llm = llm_predictor

# Initialize a MilvusVectorStore with Milvus server configuration
vector_store = MilvusVectorStore(
    uri=MILVUS_URI,
    dim=384,
    use_secure=False
)

# Create a StorageContext with the MilvusVectorStore
storage_context = StorageContext.from_defaults(vector_store=vector_store)


# ts 수정
index = VectorStoreIndex.from_documents(
    documents=documents,
    overwrite=True,  # Set to False if you don't want to overwrite the index
)

# You can now perform queries with the index
# For example:
# result = index.query("What communication protocol is used in Pymilvus for communicating with Milvus?")
# print(result)