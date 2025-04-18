import os
import requests
from fastapi import HTTPException
from app.schemas import AgentCreateRequest
from dotenv import load_dotenv

load_dotenv()

RETELL_BASE_URL = "https://api.retellai.com/create-agent"
RETELL_API_KEY = os.getenv("RETELL_API_KEY")

def create_retell_agent(request: AgentCreateRequest):
    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }

  
    payload = {
        "agent_name": request.agent_name,
        "voice_id": "11labs-Adrian",  
        "response_engine": {
            "type": "retell-llm",
            "llm_id": "llm_1c92ba2ab2538c76c5151f627ec4"  
        }
    }

    try:
        response = requests.post(
            RETELL_BASE_URL,
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Retell API error: {e.response.text}"
        )
