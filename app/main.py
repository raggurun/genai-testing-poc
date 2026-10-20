from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from pydantic import BaseModel # pyright: ignore[reportMissingImports]

from app.agent import run_agent


app = FastAPI(
    title="GenAI Banking Testing POC",
)


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health():

    return {
        "status": "UP"
    }


@app.post("/api/chat")
def chat(request: ChatRequest):

    return run_agent(
        request.message
    )