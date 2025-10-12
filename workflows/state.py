from typing import TypedDict, Annotated, Dict, List, Any
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages: Annotated[List[str], add_messages]
    toolCall: Dict[str, Any]
    