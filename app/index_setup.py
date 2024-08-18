from llama_index.core import SummaryIndex,SimpleDirectoryReader, VectorStoreIndex, Settings,StorageContext,load_index_from_storage,ServiceContext,set_global_service_context
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv
from app.constants import DATA,STORAGE_DIR
import os


def initialize_index():
    
    load_dotenv()
    
    embed_model = OpenAIEmbedding(api_key=os.environ.get("OPENAI_API_KEY"))

    if os.path.exists(STORAGE_DIR):
        
        storage_context = StorageContext.from_defaults(persist_dir=STORAGE_DIR)
        index = load_index_from_storage(storage_context)
        
    else :
        
        documents = SimpleDirectoryReader(DATA,recursive=True).load_data()
        index = VectorStoreIndex.from_documents(documents,embed_model=embed_model)
        index.storage_context.persist()
    
    return index

