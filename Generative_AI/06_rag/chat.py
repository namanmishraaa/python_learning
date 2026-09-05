from langchain_openai import OpenAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI
from ollama import Client
from dotenv import load_dotenv
import os

load_dotenv()


# Create vector embeddings
# openai_embeddings = OpenAIEmbeddings(
#     model='text-embedding-3-small',
# )

ollama_embeddings = OllamaEmbeddings(
    model= os.getenv("OLLAMA_EMBEDDING_MODEL"),
    base_url=os.getenv("OLLAMA_BASE_URL")
)



# Load the vector store collection
vector_db = QdrantVectorStore.from_existing_collection(
    embedding=ollama_embeddings,
    url="http://localhost:6333/",
    collection_name="learning_rag_ollama",
)

# Take user input 
user_query = input("Ask something :")

# Relevant chunks from the vector DB
search_result = vector_db.similarity_search(query=user_query)


context = "\n\n\n".join([f"Page Content: {result.page_content}\n Page Number: {result.metadata['page_label']}\nPage location: {result.metadata['source']})" 
for result in search_result])


SYSTEM_PROMPT = f"""
    You are a helpful AI assistand who answer user query on the available context
    retrieved from a PDF file along with page_content and page_number.

    You should only answer the user based on the following context and navigate
    the user to open the right page number to know more.

    You should explain something if user explicitly asks to explain something.

    Context: 
    {context}
"""


# openai_client = OpenAI()
ollama_client = Client(
    host=os.getenv("OLLAMA_BASE_URL")
)

message = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": user_query
    }
]

# openai_response = openai_client.responses.create(
#     model="gpt-5",
#     input=message, 
# )


ollama_response = ollama_client.chat(
    model= os.getenv("OLLAMA_LLM_MODEL"),
    messages=message,
)


# print(f"🤖: {llm_response.output_text} ")
print(ollama_response.message.content)