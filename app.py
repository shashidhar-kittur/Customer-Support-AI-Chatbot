from fastapi import FastAPI
from pydantic import BaseModel
from database import init_db, get_history, update_history
from llm_utils import generate_response, summarize_conversation

app = FastAPI()


init_db()

# Pydantic model for the incoming query data
class Query(BaseModel):
    session_id: str
    query: str

@app.post("/chat")
def chat(query: Query):
    
    history = get_history(query.session_id)   # Retrieve conversation history
    
  
    response, escalate = generate_response(query.query, history)
    
    new_history = history + f"\nUser: {query.query}\nBot: {response}"
    update_history(query.session_id, new_history)

    if escalate:
        summary = summarize_conversation(new_history)
        return {"response": response, "escalate": True, "summary": summary}
    
  
    return {"response": response, "escalate": False, "summary": "N/A"}