from langgraph.graph import StateGraph, END
from app.agents.state import AgentState
from app.agents.nodes import (
    extract_filters_node,
    merge_filters_node,
    filter_properties_node,
    response_node
)

def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("extract_filters", extract_filters_node)
    graph.add_node("merge_filters", merge_filters_node)
    graph.add_node("filter_properties", filter_properties_node)
    graph.add_node("response", response_node)

    graph.set_entry_point("extract_filters")

    graph.add_edge("extract_filters", "merge_filters")
    graph.add_edge("merge_filters", "filter_properties")
    graph.add_edge("filter_properties", "response")
    graph.add_edge("response", END)

    return graph.compile()


def route_intent(state: dict) -> str:
    msg = state["user_message"].lower()

    if "save" in msg:
        return "save_property"
    if "saved" in msg or "favorites" in msg:
        return "show_saved"
    return "search"