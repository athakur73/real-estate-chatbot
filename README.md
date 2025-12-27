🏡 Agent Mira – Backend Service

AI-Powered Real Estate Chatbot (FastAPI + LangGraph + Gemini)

📌 Overview

This backend powers Agent Mira, an AI-driven real estate assistant that enables users to search for properties using natural language queries.

The backend is designed with production principles:

* Deterministic data handling
* Responsible LLM usage
* Explicit agent orchestration
* Clean separation of concerns

The system converts conversational input into structured filters, applies them deterministically to property data, and returns accurate results.

🎯 Core Capabilities

* Natural language property search
* Multi-constraint filtering (location, budget, bedrooms, amenities)
* Session-based conversation handling
* Saved properties persistence (MongoDB)
* LLM-powered intent extraction (Gemini)
* Deterministic property filtering (Python)

)

🧠 Key Design Principle

LLMs interpret intent — application code enforces truth.

The LLM is never used for:

* Filtering logic
* Data mutation
* Business decisions

All critical operations remain deterministic.

🏗️ High-Level Architecture
        Client (React)
        ↓
        FastAPI (/chat, /save)
        ↓
        LangGraph Agent
        ├── Intent Extraction (Gemini)
        ├── Property Filtering (Python)
        └── Response Builder
        ↓
        JSON Response
Saved properties are persisted independently in MongoDB.

🧩 Tech Stack
Backend Framework
    * Python 3.11+
    * FastAPI
    * Uvicorn

AI / Agent Layer

    * LangChain
    * LangGraph
    * Google Gemini API

Data & Storage

    * JSON property datasets
    * MongoDB (saved properties)

📂 Project Structure
    app/
    ├── main.py                  # FastAPI entry point
    ├── api/
    │   ├── chat.py              # /chat endpoint
    │   ├── save.py              # /save endpoint
    │   └── schemas.py           # Request/response models
    ├── agents/
    │   ├── real_estate_agent.py # LangGraph agent
    │   └── nodes.py             # Agent nodes
    ├── services/
    │   ├── query_extractor.py   # LLM intent extraction
    │   ├── property_filter.py   # Deterministic filtering
    │   ├── property_loader.py   # JSON merge logic
    │   └── gemini_llm.py        # Gemini client
    ├── data/
    │   ├── properties_basic.json
    │   ├── property_images.json
    │   └── property_characteristics.json
    └── db/
        └── mongodb.py           # MongoDB integration

🔄 Agent Flow (LangGraph)

Each user query passes through explicit agent states:

1. User Input
    * Receives raw user message

2. Intent Extraction
    * Gemini converts text → structured filters
    * Output validated against schema

3. Filter Execution
    * Python applies filters on merged dataset
    * No AI involvement

4. Response Generation
    * Final reply + matching properties returned

LangGraph ensures:
    * Clear execution order
    * Debuggable state transitions
    * Easy extensibility

📊 Property Data Handling
Property data is distributed across multiple JSON files:

    * Basic details
    * Location & pricing
    * Amenities & metadata

These files are merged at application startup into a single in-memory dataset.
    ✔ Deterministic
    ✔ Fast
    ✔ No runtime LLM dependency

💾 Saved Properties (MongoDB)
Users can save properties via the /save endpoint.

Design Highlights
    * Stateless search
    * Persistent user actions
    * Session-based identification
    * Idempotent saves

This allows future extension to:

    * User accounts
    * Saved searches
    * Recommendations

🚀 Running the Backend Locally
1️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Environment Variables
export GOOGLE_API_KEY=your_api_key
export MONGO_URI=mongodb://localhost:27017

4️⃣ Start Server
uvicorn app.main:app --reload

API will be available at:
http://localhost:8000

🔌 API Endpoints
POST /chat
Processes user queries and returns matching properties.

Request
    {
    "message": "Show me 3-bedroom homes in Dallas under 600K",
    "session_id": "uuid"
    }

Response
    {
    "reply": "Here are some matching properties.",
    "count": 2,
    "properties": [...]
    }

POST /save

Saves a property for the current session.
Request:
{
  "property_id": "prop_123",
  "session_id": "uuid"
}

📈 Scalability & Future Enhancements

    * Redis for session memory
    * Authentication & user profiles
    * RAG for schools & neighborhood data
    * Streaming responses
    * Analytics & personalization
    * Caching for LLM responses

🧠 Key Engineering Takeaways

    * Explicit agent orchestration
    * Responsible LLM usage
    * Deterministic business logic
    * Production-aware error handling
    * Clean separation of AI vs system logic
