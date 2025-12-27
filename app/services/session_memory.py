from typing import Dict
from app.services.query_schema import PropertyQuery

# In-memory store (per process)
SESSION_MEMORY: Dict[str, PropertyQuery] = {}


def get_session_filters(session_id: str) -> PropertyQuery | None:
    return SESSION_MEMORY.get(session_id)


def save_session_filters(session_id: str, filters: PropertyQuery):
    SESSION_MEMORY[session_id] = filters
