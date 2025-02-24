from fastapi import FastAPI, Query
from chatbot import ask_question

app = FastAPI()

@app.get("/ask")
def ask(question: str = Query(..., description="Enter your question")):
    response = ask_question(question)
    return {"answer": response}