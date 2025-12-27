from typing import List, Optional
from typing_extensions import TypedDict
from app.services.query_schema import PropertyQuery


class AgentState(TypedDict):
    user_message: str
    session_id: str
    extracted_filters: Optional[object]
    merged_filters: Optional[object]
    results: List[dict]
    reply: str