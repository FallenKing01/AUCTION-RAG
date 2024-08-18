from llama_index.core import SummaryIndex, SimpleDirectoryReader, VectorStoreIndex, Settings, StorageContext, load_index_from_storage, ServiceContext, set_global_service_context
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv
import os



STORAGE_DIR = "./storage"
DATA = "./data"  

def initialize_index():
    
    load_dotenv()  
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    embed_model = OpenAIEmbedding(api_key=openai_api_key, model="text-embedding-3-small")
    documents = SimpleDirectoryReader(DATA, recursive=True).load_data()
    
    index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)
    index.storage_context.persist(persist_dir=STORAGE_DIR)


if __name__ == "__main__":
    
    initialize_index()
