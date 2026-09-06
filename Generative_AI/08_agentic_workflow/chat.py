from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model


llm = init_chat_model(
    model="qwen3.5:9b-q4_K_M",
    model_provider="ollama"
)

class State(TypedDict):
    message: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state.get("message"))
    return {"message":[response]}

def samplenode(state: State):
    # This is a samples node
    print(f"\n\nInside samplenode: {state}")
    return{"message": ["This is a sample node"]}


graph_builder= StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")

graph_builder.add_edge("samplenode", END)


graph = graph_builder.compile()
udpated_state = graph.invoke(State({"message": "Hi, my name in Astra."}))
print("\n\n",udpated_state)


"""

(START) -> chatbot -> samplenode -> (END)

State = {messages: ["hey there"]}
node runs : chatbot(state: ["hey there"] -> ["Hi, this is a message from ChatBot"])
State = {messages: ["hey there", "Hi, this is a message from ChatBot"]}



Example of o/p :-



Inside samplenode: {'message': [HumanMessage(content='Hi, my name in Astra.', additional_kwargs={}, response_metadata={}, id='4476c609-355d-4848-a0ba-3cff63aeeda4'), AIMessage(content="Hi Astra! It's nice to meet you. Is there anything specific I can help you with today?", additional_kwargs={}, response_metadata={'model': 'qwen3.5:9b-q4_K_M', 'created_at': '2026-09-06T16:55:38.179914803Z', 'done': True, 'done_reason': 'stop', 'total_duration': 45390866323, 'load_duration': 31890567254, 'prompt_eval_count': 17, 'prompt_eval_duration': 1032029000, 'eval_count': 427, 'eval_duration': 12397086000, 'logprobs': None, 'model_name': 'qwen3.5:9b-q4_K_M', 'model_provider': 'ollama'}, id='lc_run--01a077a4-ee66-7a83-a92b-e44cfd7dac36-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 17, 'output_tokens': 427, 'total_tokens': 444})]}


 {'message': [HumanMessage(content='Hi, my name in Astra.', additional_kwargs={}, response_metadata={}, id='4476c609-355d-4848-a0ba-3cff63aeeda4'), AIMessage(content="Hi Astra! It's nice to meet you. Is there anything specific I can help you with today?", additional_kwargs={}, response_metadata={'model': 'qwen3.5:9b-q4_K_M', 'created_at': '2026-09-06T16:55:38.179914803Z', 'done': True, 'done_reason': 'stop', 'total_duration': 45390866323, 'load_duration': 31890567254, 'prompt_eval_count': 17, 'prompt_eval_duration': 1032029000, 'eval_count': 427, 'eval_duration': 12397086000, 'logprobs': None, 'model_name': 'qwen3.5:9b-q4_K_M', 'model_provider': 'ollama'}, id='lc_run--01a077a4-ee66-7a83-a92b-e44cfd7dac36-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 17, 'output_tokens': 427, 'total_tokens': 444}), HumanMessage(content='This is a sample node', additional_kwargs={}, response_metadata={}, id='d9e86de6-ec4f-43f8-819c-9ca5e2e5ee82')]}"""