from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import asyncio, os

from portfolio_ai.crew import PortfolioAi

load_dotenv()  # Load environment variables on Render/local

app = FastAPI(title="Joel Mbaka Chatbot API", version="1.0.0")

crew = PortfolioAi().crew()  # Build crew once at startup

class Query(BaseModel):
    question: str

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat")
async def chat(q: Query):
    try:
        answer = await asyncio.to_thread(crew.kickoff, inputs={"question": q.question})
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

from fastapi.responses import StreamingResponse

@app.post("/chat-stream")
async def chat_stream(q: Query):
    """Server-Sent Events streaming of token chunks."""
    def generator():
        for chunk in crew.kickoff(inputs={"question": q.question}, stream=True):
            if chunk:
                yield f"data: {chunk}\n\n"
        yield "event: end\ndata: [DONE]\n\n"

    return StreamingResponse(generator(), media_type="text/event-stream")
