from app.services.query_extractor import extract_filters
from app.services.property_loader import load_all_properties
from app.services.property_filter import filter_properties
from app.services.filter_merge import merge_filters
from app.agents.state import AgentState


def extract_filters_node(state: AgentState) -> AgentState:
    filters = extract_filters(state["user_message"])
    return {**state, "extracted_filters": filters}


def merge_filters_node(state: AgentState) -> AgentState:
    merged = merge_filters(
        state.get("previous_filters"),
        state["extracted_filters"]
    )
    return {**state, "merged_filters": merged}


def filter_properties_node(state: AgentState) -> AgentState:
    properties = load_all_properties()
    results = filter_properties(properties, state["merged_filters"])

    return {
        **state,
        "properties": properties,
        "results": results
    }


def response_node(state: AgentState) -> AgentState:
    count = len(state["results"])

    if count == 0:
        reply = (
            "I couldn’t find matching properties. "
            "Would you like to adjust budget or location?"
        )
    else:
        reply = (
            f"I found {count} properties. "
            "You can refine further by price, bedrooms, or amenities."
        )

    return {**state, "reply": reply}


from app.repositories.saved_properties_repo import (
    save_property,
    get_saved_properties
)
from app.services.intent_detector import (
    is_save_intent,
    is_show_saved_intent
)

def save_property_node(state: dict) -> dict:
    if not state["results"]:
        return {**state, "reply": "No property to save."}

    # Save first result for simplicity (UI can control this later)
    property_id = state["results"][0]["id"]
    save_property(state["session_id"], property_id)

    return {
        **state,
        "reply": "✅ Property saved to your favorites!"
    }


def show_saved_node(state: dict) -> dict:
    saved = get_saved_properties(state["session_id"])
    return {
        **state,
        "results": saved,
        "reply": f"You have {len(saved)} saved properties."
    }
