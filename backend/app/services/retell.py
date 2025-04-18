import os
import requests
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()

RETELL_API_KEY = os.getenv("RETELL_API_KEY")
RETELL_API_BASE = "https://api.retellai.com"

HEADERS = {
    "Authorization": f"Bearer {RETELL_API_KEY}",
    "Content-Type": "application/json"
}

def get_voices():
    url = f"{RETELL_API_BASE}/voices"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch voices: {response.text}")
    return response.json()  # Expecting a list of voices with voice_id

def get_llms():
    url = f"{RETELL_API_BASE}/llms"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=f"Failed to fetch LLMs: {response.text}")
    return response.json()  # Expecting a list of llms with llm_id

def create_retell_agent(request: AgentCreateRequest):
    # Fetch voices and llms dynamically if not provided
    voices = get_voices()
    llms = get_llms()

    # Select first voice_id and llm_id as default
    voice_id = voices[0]["voice_id"] if voices else None
    llm_id = llms[0]["llm_id"] if llms else None

    if not voice_id or not llm_id:
        raise HTTPException(status_code=500, detail="No voices or LLMs available in Retell account")

    headers = {
        "Authorization": f"Bearer {RETELL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "agent_name": request.agent_name,
        "voice_id": voice_id,
        "response_engine": {
            "type": "retell-llm",
            "llm_id": llm_id
        }
    }

    try:
        response = requests.post(
            f"{RETELL_API_BASE}/create-agent",
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
