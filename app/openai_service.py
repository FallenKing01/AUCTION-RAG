from dotenv import load_dotenv
from openai import OpenAI
import os


load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

def chat_gpt(prompt : str)-> str:
    
    response = client.chat.completions.create(model="gpt-3.5-turbo",messages=[{"role": "user", "content": prompt}])
    
    if prompt.strip() == "":
        
            raise Exception("Invalid question: prompt is empty")
        
    return response.choices[0].message.content.strip()