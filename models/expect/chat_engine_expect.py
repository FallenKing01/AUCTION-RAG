from pydantic import BaseModel, validator
from typing import List


class history_item(BaseModel):
    
    role: str
    content: str
    
    
class question_model(BaseModel):
    
    question: str
    history: List[history_item]
    
    