import sys
sys.path.append('.')

from typing import TypedDict
from langgraph.graph import StateGraph, END
from tools.rag import search
from tools.summarizer import summarize
from tools.extractor import extract

# Define state
class AgentState(TypedDict):
    query: str
    articles: list
    summary: str
    extracted: str
    final_response: str

# Node 1: Search
def search_node(state: AgentState):
    print("\n Agent: Searching articles...")
    results = search(state["query"], top_k=3)
    return {"articles": results}

# Node 2: Summarize
def summarize_node(state: AgentState):
    print("\n Agent: Summarizing...")
    combined = " ".join([r['headline'] + ". " + r['short_description'] for r in state["articles"]])
    summary = summarize(combined)
    return {"summary": summary}

# Node 3: Extract
def extract_node(state: AgentState):
    print("\n Agent: Extracting entities...")
    combined = " ".join([r['headline'] + ". " + r['short_description'] for r in state["articles"]])
    extracted = extract(combined)
    return {"extracted": extracted}

# Node 4: Final response
def final_node(state: AgentState):
    print("\n Agent: Preparing final response...")
    final = f"""
 QUERY: {state['query']}

 SUMMARY:
{state['summary']}

 EXTRACTED INFO:
{state['extracted']}
    """
    return {"final_response": final}

# Build graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("search", search_node)
workflow.add_node("summarize", summarize_node)
workflow.add_node("extract", extract_node)
workflow.add_node("final", final_node)

# Add edges
workflow.set_entry_point("search")
workflow.add_edge("search", "summarize")
workflow.add_edge("summarize", "extract")
workflow.add_edge("extract", "final")
workflow.add_edge("final", END)

# Compile
app = workflow.compile()

# Test
if __name__ == "__main__":
    result = app.invoke({"query": "climate change and environment"})
    print(result["final_response"])