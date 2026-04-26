from fastapi import FastAPI
from pydantic import BaseModel
import sys
sys.path.append('.')

from agent import app as agent_app

# FastAPI app
app = FastAPI(title="AgentIQ API")

# Request model
class QueryRequest(BaseModel):
    query: str

# Endpoint
@app.post("/analyze")
def analyze(request: QueryRequest):
    result = agent_app.invoke({"query": request.query})
    return {
        "query": request.query,
        "summary": result["summary"],
        "extracted": result["extracted"],
        "final_response": result["final_response"]
    }

# Health check
@app.get("/")
def home():
    return {"status": "AgentIQ is running!"}