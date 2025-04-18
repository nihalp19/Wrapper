import os
import requests
from fastapi import HTTPException
from app.schemas import AgentCreateRequest
from dotenv import load_dotenv


load_dotenv() 

VAPI_BASE_URL = "https://api.vapi.ai/assistant"
print("VAPI_API_KEY:", os.getenv("VAPI_API_KEY"))

VAPI_API_KEY = os.getenv("VAPI_API_KEY") 

def create_vapi_agent(request: AgentCreateRequest):
    """Create agent using Vapi.ai API"""
    headers = {
        "Authorization": f"Bearer {VAPI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
    "name": request.agent_name,
    "model": request.model,
    "voice": "jennifer-playht", 
    "serverUrl": request.webhook_url
    }
    
    try:
        response = requests.post(
            VAPI_BASE_URL, 
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Vapi API error: {response.text}"
        )
