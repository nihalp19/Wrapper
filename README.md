# Voice AI Agents Wrapper API

A unified FastAPI service for creating voice AI agents across multiple providers, including Vapi.ai and Retell.ai.

## 📋 Overview

This API provides a streamlined interface to create AI voice agents using different providers through a single, consistent endpoint. Currently supported providers:

- **Vapi.ai** - For creating voice agents with customizable models and webhook integration
- **Retell.ai** - For creating voice agents with predefined voice and response models

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice-ai-wrapper.git
   cd voice-ai-wrapper
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   ```
   Edit the `.env` file and add your API keys:
   ```
   VAPI_API_KEY=your_vapi_api_key
   RETELL_API_KEY=your_retell_api_key
   ```

5. Start the server:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://127.0.0.1:5000`.

## 📚 API Documentation

### Create Agent Endpoint

**URL**: `/create-agent`  
**Method**: `POST`  
**Content-Type**: `application/json`

#### Request Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| provider | string | Yes | The AI provider to use: "vapi" or "retell" |
| agent_name | string | Yes | Name of the agent to create |
| model | string | For Vapi | LLM model to use (e.g., "gpt-4") |
| webhook_url | string | For Vapi | Webhook URL for agent callbacks |

#### Vapi.ai Example

```json
{
  "provider": "vapi",
  "agent_name": "Customer Support Agent",
  "model": "gpt-4",
  "webhook_url": "https://example.com/webhook"
}
```

#### Retell.ai Example

```json
{
  "provider": "retell",
  "agent_name": "Sales Assistant"
}
```

> **Note**: For Retell.ai, the voice_id and response_engine are currently set to static values in the implementation.

#### Response

A successful request returns the response from the provider's API, typically including an agent ID and other provider-specific details.

## 🔧 Configuration

### Environment Variables

| Variable | Description |
|----------|-------------|
| VAPI_API_KEY | Your Vapi.ai API key |
| RETELL_API_KEY | Your Retell.ai API key |

## 📝 Usage Examples

### Using cURL

```bash
# Create a Vapi.ai agent
curl -X POST "http://localhost:8000/create-agent" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "vapi",
    "agent_name": "Customer Support",
    "model": "gpt-4",
    "webhook_url": "https://example.com/webhook"
  }'

# Create a Retell.ai agent
curl -X POST "http://localhost:8000/create-agent" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "retell",
    "agent_name": "Sales Assistant"
  }'
```

### Using Python Requests

```python
import requests

# Create a Vapi.ai agent
response = requests.post(
    "http://localhost:8000/create-agent",
    json={
        "provider": "vapi",
        "agent_name": "Customer Support",
        "model": "gpt-4",
        "webhook_url": "https://example.com/webhook"
    }
)
print(response.json())

# Create a Retell.ai agent
response = requests.post(
    "http://localhost:8000/create-agent",
    json={
        "provider": "retell",
        "agent_name": "Sales Assistant"
    }
)
print(response.json())
```

## 🛠️ Development

### Project Structure

```
project-root/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app instance
│   ├── schemas.py       # Pydantic models
│   └── services/
│       ├── __init__.py
│       ├── vapi.py      # Vapi.ai service
│       └── retell.py    # Retell.ai service
├── requirements.txt
├── .env                 # Environment variables
└── README.md
```

### Adding Additional Providers

To add a new provider:

1. Create a new service file in `app/services/`
2. Update the `schemas.py` file to include any new provider-specific fields
3. Add the provider handling in the `create_agent` endpoint in `main.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋 Support

For support or questions, please open an issue in the GitHub repository or contact the maintainers.
