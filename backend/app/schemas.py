from pydantic import BaseModel
from typing import Optional, Dict, Any

class AgentCreateRequest(BaseModel):
    provider: str
    agent_name: str

    # Optional fields for Vapi
    description: Optional[str] = None
    model: Optional[str] = None
    webhook_url: Optional[str] = None

    # Retell-specific fields
    voice_id: Optional[str] = None
    response_engine: Optional[Dict[str, Any]] = None
