
from ollama import Client
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
load_dotenv()

# Ollama embedding model
ollama_embeddings = OllamaEmbeddings(
    model= os.getenv("OLLAMA_EMBEDDING_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL")
)

# Vector db connection on docker
vector_db = QdrantVectorStore.from_existing_collection(
    embedding=ollama_embeddings,
    url="http://localhost:6333/",
    collection_name="learning_rag_ollama",
)

def process_query(query:str):

    print("Searching Chunks : ", query)
    # Relevant chunks from the vector DB

    search_result = vector_db.similarity_search(query=query)

    context = "\n\n\n".join([f"Page Content: {result.page_content}\n Page Number: {result.metadata['page_label']}\nPage location: {result.metadata['source']})" for result in search_result])

    SYSTEM_PROMPT = f"""
        - You are a helpful AI assistand who answer user query on the available context
        retrieved from a PDF file along with page_content and page_number.\n
        - You should only answer the user based on the following context and navigate
        the user to open the right page number to know more.\n
        - You should explain something if user explicitly asks to explain.\n
        - Context: {context}
    """

    # Making llm call
    ollama_client = Client(
        host=os.getenv("OLLAMA_BASE_URL"))

    # Creating message for LLM
    message = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": query
        }
    ]

    # Calling LLM 
    ollama_response = ollama_client.chat(
        model= os.getenv("OLLAMA_LLM_MODEL"),
        messages=message,
    )

    print(ollama_response.message.content)

    return ollama_response.message.content



