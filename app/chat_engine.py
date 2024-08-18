from llama_index.core import VectorStoreIndex, SimpleDirectoryReader,llms
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

def chat_engine(body, index: VectorStoreIndex):

    items = body["history"]
    history_list = []

    for item in items:
        
        if item["role"] == "user":

            obj = ChatMessage(role=MessageRole.USER, content=item["content"])
            history_list.append(obj)

        else:

            obj = ChatMessage(role=MessageRole.ASSISTANT, content=item["content"])
            history_list.append(obj)

    llm = OpenAI(model="gpt-3.5-turbo", api_key=os.environ.get("OPENAI_API_KEY"))
    chat_engine = index.as_chat_engine(

        verbose=True,
        node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.80)],
    )

    response = chat_engine.chat(body["question"]+"Raspunde-mi in limba romana!", chat_history=history_list)
    

    if not response.source_nodes:
        response.response = "I'm sorry, I don't have information on that topic."

    return response