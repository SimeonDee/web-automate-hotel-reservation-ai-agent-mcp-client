from src.agent import agent
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Query(BaseModel):
    message: str


app = FastAPI()


@app.post("/agents/run")
async def run_agent(query: Query) -> str:
    response = await agent.run(query.message, max_steps=20)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
