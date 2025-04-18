from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import AgentCreateRequest
from app.services.vapi import create_vapi_agent
from app.services.retell import create_retell_agent
from dotenv import load_dotenv

load_dotenv()  

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    return {"status": "Backend is running"}

@app.post("/create-agent")
async def create_agent(request: AgentCreateRequest):
    if request.provider.lower() == "vapi":
        if not request.model or not request.webhook_url:
            raise HTTPException(status_code=400, detail="model and webhook_url are required for Vapi")
        return create_vapi_agent(request)
    elif request.provider.lower() == "retell":
        return create_retell_agent(request)
    else:
        raise HTTPException(status_code=400, detail="Invalid provider")
