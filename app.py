from fastapi import FastAPI
from pydantic import BaseModel
from src.chatbot import chatbot_response

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "API do Chatbot A.C.E. está rodando!"}

@app.post("/chat")
def chat(question: Question):
    response = chatbot_response(question.question)
    return {"user": question.question, "chatbot": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
