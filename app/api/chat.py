from fastapi import APIRouter
from app.api.schemas import ChatRequest, ChatResponse
from app.agents.real_estate_agent import build_agent
from app.services.session_memory import (
    get_session_filters,
    save_session_filters
)

router = APIRouter()
agent = build_agent()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    session_id = request.session_id or "default"

    previous_filters = get_session_filters(session_id)

    final_state = agent.invoke({
    "user_message": request.message,
    "session_id": session_id,
    "previous_filters": previous_filters
    })


    # Save merged filters back to memory
    save_session_filters(session_id, final_state["merged_filters"])

    return ChatResponse(
        reply=final_state["reply"],
        count=len(final_state["results"]),
        properties=final_state["results"]
    )
