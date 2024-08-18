from fastapi import FastAPI, HTTPException
from app.index_setup import initialize_index
from utils.valitation import validate_ai_input
from app.openai_service import chat_gpt
from app.chat_engine import chat_engine
from models.expect.chat_engine_expect import question_model
import subprocess


index = initialize_index()
app = FastAPI()
@app.get("/test")
async def test():
    return {"status": "success", "detail": "API is running."}

@app.get("/ask")
async def ask_question(question: str)-> dict:
    
    try:
        
        answer = chat_gpt(question)

        return {"response": answer}

    except Exception as e:

         raise HTTPException(status_code=500, detail=f" {str(e)}")
    
@app.post("/chat_engine")
async def query_on_data(body : question_model):
    
    try:
        
        body = body.dict()     
        
        validate_ai_input(body)
        
        response = chat_engine(body,index)

        return response
    
    except Exception as e:
        
        raise HTTPException(status_code=500, detail=f" {e}")
    
    
@app.post("/reinitialize_vectorstore")
async def reinitialize_vectorstore():
    
    result = subprocess.run(["python", "./app/manage_vectorstore.py"], capture_output=True, text=True)
    
    if result.returncode == 0:
        
        return {"status": "success", "detail": "Vector store initialized successfully."}
    
    else:
        
        return {"status": "failure", "detail": result.stderr}