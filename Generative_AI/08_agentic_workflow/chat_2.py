from typing import Optional, Literal
from typing_extensions import TypedDict
from ollama import Client
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model


ollama_client = Client()

class State(TypedDict):
    user_query : str
    llm_output : Optional[str]
    is_good : Optional[bool]


def chatbot(state: State):
    print(f"chatbot Node: {state}")
    response = ollama_client.chat(
        model="qwen3.5:9b-q4_K_M",
        messages = [{"role": "user",
        "content": state.get("user_query")}]
    )

    state["llm_output"] = response.message.content
    return state

def evalauate_output(state: State) -> Literal["chatbot_llama", "endnode"]:
    print(f"Evaluation Node: {state}")
    if True:
        return "endnode"
    return "chatbot_llama"

def chatbot_llama(state: State):
    print(f"chatbot llama Node: {state}")
    response = ollama_client.chat(
        model="llama3.1:8b",
        messages = [{"role": "user",
        "content": state.get("user_query")}]
    )
    state["llm_output"] = response.output_text
    return state

def endnode(state: State):
    return state



graph_builder= StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("evalauate_output",evalauate_output)
graph_builder.add_node("chatbot_llama",chatbot_llama)
graph_builder.add_node("endnode",endnode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evalauate_output)
graph_builder.add_edge("chatbot_llama","endnode")
graph_builder.add_edge("endnode",END)

graph = graph_builder.compile()
updated_state = graph.invoke(State({"user_query": "What is 2+2?"}))

print(f"Update state: {updated_state}")